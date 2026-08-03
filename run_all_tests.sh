#!/usr/bin/env bash
# Run every PyPractical test suite and print a summary.
# Usage:  ./run_all_tests.sh
set -u
cd "$(dirname "$0")"

total=0
pass=0
fail=0
fails=""

for d in Family-*/0*/; do
  if [ -f "${d}tests.py" ]; then
    out=$(cd "$d" && python3 -m unittest tests 2>&1)
    ran=$(printf '%s\n' "$out" | grep -oE 'Ran [0-9]+ tests' | grep -oE '[0-9]+')
    if printf '%s\n' "$out" | grep -qE '^OK'; then
      status="OK"; pass=$((pass + 1))
    else
      status="FAIL"; fail=$((fail + 1)); fails="${fails} ${d}"
    fi
    total=$((total + ${ran:-0}))
    printf '%-55s %s (%s tests)\n' "$d" "$status" "${ran:-?}"
  fi
done

echo "------------------------------------------------------------"
echo "Folders OK: ${pass} | FAILED: ${fail} | total: $((pass + fail)) | tests: ${total}"
if [ -n "$fails" ]; then
  echo "FAILED:${fails}"
  exit 1
fi
