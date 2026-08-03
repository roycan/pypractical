#!/usr/bin/env python3
"""
Objective brand-color / palette analysis for every PNG in `pics/`.

Brand identity = WARM palette:
    terracotta #C96A4A, amber, warm paper/cream, sage green, dusty blue.
    Must NOT be dominated by cool blue / green / teal "tech" colors.

For each PNG the script:
  1. Opens the image, composites transparency onto white (in memory only),
     converts to RGB, downscales to ~120 px on the long edge.
  2. Quantizes colors (4 bits / channel -> 16 levels each) and counts pixels.
  3. For every quantized color computes HSV, then classifies it into a
     "family" and assigns a weight:
         - neutral (low saturation)        -> weight = count           (full)
         - any chromatic family (by hue)   -> weight = count * sat     (vivid
           colors dominate; muted/dusty/sage colors count little, so a
           saturated tech blue registers far more than a muted dusty blue).
     This is the requested "weighting pixel counts by HSV hue/saturation":
     hue selects the family, saturation scales the weight.
  4. Prints, per image: filename, top-3 families by weighted share (%),
     the single most-common quantized color as a hex code, and a verdict.

Verdict rule (objective, documented thresholds):
    warm    = red/warm + orange/terracotta + amber/yellow
    neutral = neutral share
    cool    = teal/cyan + blue          (saturation-weighted -> only vivid
                                          cool colors count much; dusty blue
                                          barely registers -> stays on-brand)
    green   = green share               (sage = low sat -> low weight -> OK)

    OFF-BRAND : cool is the dominant block (cool >= 40% AND cool beats
                warm+neutral+green)  -> dominated by cool tech blue/teal.
    ON-BRAND  : warm + neutral >= 60%
              OR (warm + neutral + green >= 55% AND cool < 25%)
    MIXED     : everything in between.

No image files are read into or written from disk; nothing is modified.
"""

from __future__ import annotations

import colorsys
import os
from collections import Counter

from PIL import Image

PICS_DIR = "pics"
TARGET_SIZE = 120          # long edge after downscale
QUANT_BITS = 4             # bits kept per channel (16 levels)
QUANT_STEP = 1 << QUANT_BITS          # 16
QUANT_MASK = (1 << QUANT_BITS) - 1    # low nibble mask, for rounding
# Keep the high bits and round to the middle of each quantized bucket so the
# reported hex looks like a representative color (e.g. 0xC0 instead of 0xF0).
HALF_STEP = QUANT_STEP // 2

NEUTRAL_SAT = 0.22         # saturation below this => neutral (paper/cream/ink)

# Hue family boundaries (degrees). Order matters; first match wins.
# (low_deg, high_deg, family_name)
HUE_BANDS = [
    (345, 361, "red/warm"),
    (0,   15,  "red/warm"),
    (15,  40,  "orange/terracotta"),
    (40,  70,  "amber/yellow"),
    (70,  165, "green"),
    (165, 195, "teal/cyan"),
    (195, 255, "blue"),
    (255, 300, "purple"),
    (300, 345, "pink/magenta"),
]

ALL_FAMILIES = [
    "red/warm", "orange/terracotta", "amber/yellow", "green",
    "teal/cyan", "blue", "purple", "pink/magenta", "neutral",
]


def family_of(h_deg: float, s: float) -> str:
    """Map an HSV color to a family name."""
    if s < NEUTRAL_SAT:
        return "neutral"
    for lo, hi, name in HUE_BANDS:
        if lo <= h_deg < hi:
            return name
    return "neutral"  # fallback (shouldn't happen)


def quantize_value(v: int) -> int:
    """Round a 0-255 channel to its 4-bit bucket midpoint."""
    q = v & ~QUANT_MASK  # drop low nibble
    return min(255, q + HALF_STEP)


def analyze(path: str) -> dict:
    img = Image.open(path)

    # Composite any transparency onto white (brand paper is #FFF). In-memory
    # only; the source file is never modified.
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGBA")
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(bg, img)

    img = img.convert("RGB")

    # Downscale to ~TARGET_SIZE on the long edge (keeps aspect ratio).
    w, h = img.size
    scale = TARGET_SIZE / float(max(w, h))
    if scale < 1.0:
        img = img.resize((max(1, round(w * scale)), max(1, round(h * scale))))

    # Quantize each pixel and count.
    pixels = img.getdata()
    counter: Counter = Counter()
    for r, g, b in pixels:
        qr, qg, qb = quantize_value(r), quantize_value(g), quantize_value(b)
        counter[(qr, qg, qb)] += 1

    total_pixels = sum(counter.values())

    # Most-common quantized color -> hex.
    top_color, top_count = counter.most_common(1)[0]
    top_hex = "#{:02X}{:02X}{:02X}".format(*top_color)

    # Weighted family aggregation.
    weights = {f: 0.0 for f in ALL_FAMILIES}
    total_weight = 0.0
    for (r, g, b), count in counter.items():
        h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        fam = family_of(h * 360.0, s)
        weight = float(count) if fam == "neutral" else float(count) * s
        weights[fam] += weight
        total_weight += weight

    shares = {f: (100.0 * w / total_weight) for f, w in weights.items()}
    ranked = sorted(shares.items(), key=lambda kv: kv[1], reverse=True)

    warm = shares["red/warm"] + shares["orange/terracotta"] + shares["amber/yellow"]
    neutral = shares["neutral"]
    cool = shares["teal/cyan"] + shares["blue"]
    green = shares["green"]

    if cool >= 40.0 and cool > (warm + neutral + green):
        verdict = "OFF-BRAND"
    elif (warm + neutral) >= 60.0:
        verdict = "ON-BRAND"
    elif (warm + neutral + green) >= 55.0 and cool < 25.0:
        verdict = "ON-BRAND"
    else:
        verdict = "MIXED"

    return {
        "path": path,
        "name": os.path.basename(path),
        "size": img.size,
        "pixels": total_pixels,
        "top_hex": top_hex,
        "top_hex_share": 100.0 * top_count / total_pixels,
        "ranked": ranked,
        "verdict": verdict,
        "warm": warm,
        "neutral": neutral,
        "cool": cool,
        "green": green,
    }


def fmt_share(rank_item) -> str:
    fam, pct = rank_item
    return "{} {:.1f}%".format(fam, pct)


def main() -> None:
    files = []
    for name in sorted(os.listdir(PICS_DIR)):
        if not name.lower().endswith(".png"):
            continue
        if ":Zone.Identifier" in name:
            continue
        files.append(os.path.join(PICS_DIR, name))

    if not files:
        print("No PNG files found in", PICS_DIR)
        return

    print("=" * 92)
    print("BRAND PALETTE ANALYSIS  -  {} PNG files in '{}'".format(len(files), PICS_DIR))
    print("Warm brand = terracotta/amber/paper/sage; OFF-BRAND = dominated by cool blue/green/teal")
    print("=" * 92)

    results = []
    for f in files:
        try:
            res = analyze(f)
        except Exception as exc:  # noqa: BLE001 - report and continue
            print("\n[ERROR] {}: {}".format(f, exc))
            continue
        results.append(res)

        top3 = res["ranked"][:3]
        print("\n{}  ({}px, {:,} px)".format(res["name"], "x".join(map(str, res["size"])), res["pixels"]))
        print("  Top families : {}".format("  |  ".join(fmt_share(x) for x in top3)))
        print("  Most-common color : {}  ({:.1f}% of pixels)".format(res["top_hex"], res["top_hex_share"]))
        print("  >> VERDICT: {}".format(res["verdict"]))

    # ---- Compact summary table ------------------------------------------------
    print("\n" + "=" * 92)
    print("SUMMARY TABLE")
    print("=" * 92)
    header = "{:<34} {:<10} {:<22} {:<10}".format("FILE", "VERDICT", "TOP COLOR (hex)", "TOP-3 FAMILIES")
    print(header)
    print("-" * 92)
    for res in results:
        t1, t2, t3 = res["ranked"][:3]
        fams = "{}/{}/{}".format(
            t1[0].split("/")[0], t2[0].split("/")[0], t3[0].split("/")[0]
        )
        row = "{:<34} {:<10} {:<22} {:<10}".format(
            res["name"][:33],
            res["verdict"],
            "{} ({:.0f}%)".format(res["top_hex"], res["top_hex_share"]),
            fams,
        )
        print(row)

    # ---- Roll-up --------------------------------------------------------------
    counts = Counter(r["verdict"] for r in results)
    print("\nROLL-UP: " + ", ".join("{}={}".format(k, counts.get(k, 0))
                                    for k in ("ON-BRAND", "MIXED", "OFF-BRAND")))
    if results:
        print("        warm(avg)={:.0f}%  neutral(avg)={:.0f}%  cool-tech(avg)={:.0f}%  green(avg)={:.0f}%".format(
            sum(r["warm"] for r in results) / len(results),
            sum(r["neutral"] for r in results) / len(results),
            sum(r["cool"] for r in results) / len(results),
            sum(r["green"] for r in results) / len(results),
        ))


if __name__ == "__main__":
    main()
