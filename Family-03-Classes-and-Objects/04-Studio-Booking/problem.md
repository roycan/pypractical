# Studio Booking

## Story

A recording-studio complex is developing a booking system for its studios.

Another programmer has already written the scheduling algorithm, but the system
cannot work because two important classes are incomplete.

Your job is to complete the **Session** and **Studio** classes.

## Task

Complete the `Session` and `Studio` classes so the scheduling system works.

You do **not** need to write the scheduling algorithm.

## Class Specification

### Session

A `Session` object represents one recording session.

Each session stores:

- start time
- end time
- number of musicians

### Studio

A `Studio` object represents one recording studio.

Each studio should remember:

- when it becomes available
- every session booked into it

Initially, a studio is available at time **0**.

## Required Methods

### Session.__init__(start, end, musicians)

Store the three values as instance variables.

### Studio.__init__()

- Set `available_at` to `0`.
- Create an empty list named `sessions`.

### Studio.can_book(session)

Return `True` if this studio can book the given session, `False` otherwise.

A studio can book a session if:

```text
session.start >= available_at
```

### Studio.book(session)

1. Add the session to the studio's list.
2. Update `available_at` to the session's ending time.

## Constraints

- Number of sessions ≤ 100
- Start time < end time
- Times are positive integers
- Sessions are processed in order of starting time

You do **not** need to write the scheduling algorithm.

## Example

```python
session = Session(5, 8, 2)

studio = Studio()

print(studio.can_book(session))
```

Output

```text
True
```

After booking the session:

```python
studio.book(session)

print(studio.available_at)
```

Output

```text
8
```

The studio now contains one session.

## Explanation

A fresh studio is available at time `0`. The session starts at time `5`, and
`5 >= 0`, so the studio `can_book` it.

After `book`, the studio stores the session and becomes available again at the
session's ending time, `8`.

## Hint

Remember that objects store **state** (their variables) and **behavior** (their
methods).

The scheduling system has already been written for you. If your classes behave
correctly, the scheduler will assign every session to a studio.
