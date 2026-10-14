# Interview Scheduler

## Story

A job fair is developing a scheduling system for candidate interviews.

Another programmer has already written the scheduling algorithm, but the system
cannot work because two important classes are incomplete.

Your job is to complete the **Interview** and **Interviewer** classes.

## Task

Complete the `Interview` and `Interviewer` classes so the scheduling system
works.

You do **not** need to write the scheduling algorithm.

## Class Specification

### Interview

An `Interview` object represents one candidate interview.

Each interview stores:

- start time
- end time
- panel size

### Interviewer

An `Interviewer` object represents one interviewer.

Each interviewer should remember:

- when they become available
- every interview assigned to them

Initially, an interviewer is available at time **0**.

## Required Methods

### Interview.__init__(start, end, panel)

Store the three values as instance variables.

### Interviewer.__init__()

- Set `available_at` to `0`.
- Create an empty list named `interviews`.

### Interviewer.can_take(interview)

Return `True` if this interviewer can take the given interview, `False`
otherwise.

An interviewer can take an interview if:

```text
interview.start >= available_at
```

### Interviewer.conduct(interview)

1. Add the interview to the interviewer's list.
2. Update `available_at` to the interview's ending time.

## Constraints

- Number of interviews ≤ 100
- Start time < end time
- Times are positive integers
- Interviews are processed in order of starting time

You do **not** need to write the scheduling algorithm.

## Example

```python
interview = Interview(5, 8, 2)

interviewer = Interviewer()

print(interviewer.can_take(interview))
```

Output

```text
True
```

After conducting the interview:

```python
interviewer.conduct(interview)

print(interviewer.available_at)
```

Output

```text
8
```

The interviewer now contains one interview.

## Explanation

A fresh interviewer is available at time `0`. The interview starts at time `5`,
and `5 >= 0`, so the interviewer `can_take` it.

After `conduct`, the interviewer stores the interview and becomes available
again at the interview's ending time, `8`.

## Hint

Remember that objects store **state** (their variables) and **behavior** (their
methods).

The scheduling system has already been written for you. If your classes behave
correctly, the scheduler will assign every interview to an interviewer.
