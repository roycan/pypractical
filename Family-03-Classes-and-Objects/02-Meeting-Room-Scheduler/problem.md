# Meeting Room Scheduler

## Story

A conference center is developing a scheduling system for its meeting rooms.

Another programmer has already written the scheduling algorithm, but the system
cannot work because two important classes are incomplete.

Your job is to complete the **Meeting** and **Room** classes.

## Task

Complete the `Meeting` and `Room` classes so the scheduling system works.

You do **not** need to write the scheduling algorithm.

## Class Specification

### Meeting

A `Meeting` object represents one scheduled meeting.

Each meeting stores:

- start time
- end time
- number of attendees

### Room

A `Room` object represents one meeting room.

Each room should remember:

- when it becomes available
- every meeting assigned to it

Initially, a room is available at time **0**.

## Required Methods

### Meeting.__init__(start, end, attendees)

Store the three values as instance variables.

### Room.__init__()

- Set `available_at` to `0`.
- Create an empty list named `meetings`.

### Room.can_host(meeting)

Return `True` if this room can host the given meeting, `False` otherwise.

A room can host a meeting if:

```text
meeting.start >= available_at
```

### Room.host(meeting)

1. Add the meeting to the room's list.
2. Update `available_at` to the meeting's ending time.

## Constraints

- Number of meetings ≤ 100
- Start time < end time
- Times are positive integers
- Meetings are processed in order of starting time

You do **not** need to write the scheduling algorithm.

## Example

```python
meeting = Meeting(5, 8, 2)

room = Room()

print(room.can_host(meeting))
```

Output

```text
True
```

After hosting the meeting:

```python
room.host(meeting)

print(room.available_at)
```

Output

```text
8
```

The room now contains one meeting.

## Explanation

A fresh room is available at time `0`. The meeting starts at time `5`, and
`5 >= 0`, so the room `can_host` it.

After `host`, the room stores the meeting and becomes available again at the
meeting's ending time, `8`.

## Hint

Remember that objects store **state** (their variables) and **behavior** (their
methods).

The scheduling system has already been written for you. If your classes behave
correctly, the scheduler will assign every meeting to a room.
