# Teacher Notes — Internet Cafe Daily Report

> Family 01 · Minimum Cost · Assessment 02 · Difficulty 1/5 · ~15 minutes

## Learning Objective

Students use a loop and a conditional to choose the cheaper of two pricing
options for every item in a list, while accumulating a running total.

## Concepts Reinforced

- Variables and assignment
- Integer arithmetic
- `for` loops over a list
- `if` / `else` conditionals
- The accumulator pattern

## Common Student Mistakes

- Forgetting to initialize `total = 0` before the loop.
- Charging the day pass for every customer instead of the cheaper option.
- Returning inside the loop, which stops after the first customer.
- Confusing the order of the arguments when calling the function.

## Suggested Teaching Strategy

1. Build the worked example table from `problem.md` on the board together.
2. Ask: "For one customer, how do we decide which plan to charge?"
3. Then ask: "How do we repeat that decision for every customer?"
4. Have students trace the loop by hand for the example before they code.
5. Encourage students to run the manual check in the `if __name__ == "__main__"`
   block of `solution.py`.

## Automatic Assessment

`tests.py` runs 12 equal-weight behavior tests (basic, boundary, typical, mixed,
and hidden). A student's score is the percentage of passing tests. Hidden tests
check only behavior already described in the problem — they add no new
requirements.
