# TV Recorder Scheduler

## Story

A software company is developing a scheduling system for digital TV recorders.

Another programmer has already written the scheduling algorithm, but the system
cannot work because two important classes are incomplete.

Your job is to complete the **Program** and **Recorder** classes.

## Task

Complete the `Program` and `Recorder` classes so the scheduling system works.

You do **not** need to write the scheduling algorithm.

## Class Specification

### Program

A `Program` object represents one television program.

Each program stores:

- start time
- end time
- channel number

### Recorder

A `Recorder` object represents one TV recorder.

Each recorder should remember:

- when it becomes available
- every program assigned to it

Initially, a recorder is available at time **0**.

## Required Methods

### Program.__init__(start, end, channel)

Store the three values as instance variables.

### Recorder.__init__()

- Set `available_at` to `0`.
- Create an empty list named `programs`.

### Recorder.can_record(program)

Return `True` if this recorder can record the given program, `False` otherwise.

A recorder can record a program if:

```text
program.start >= available_at
```

### Recorder.record(program)

1. Add the program to the recorder's list.
2. Update `available_at` to the program's ending time.

## Constraints

- Number of programs ≤ 100
- Start time < end time
- Times are positive integers
- Programs are processed in order of starting time

You do **not** need to write the scheduling algorithm.

## Example

```python
program = Program(5, 8, 2)

recorder = Recorder()

print(recorder.can_record(program))
```

Output

```text
True
```

After recording the program:

```python
recorder.record(program)

print(recorder.available_at)
```

Output

```text
8
```

The recorder now contains one program.

## Explanation

A fresh recorder is available at time `0`. The program starts at time `5`, and
`5 >= 0`, so the recorder `can_record` it.

After `record`, the recorder stores the program and becomes available again at the
program's ending time, `8`.

## Hint

Remember that objects store **state** (their variables) and **behavior** (their
methods).

The scheduling system has already been written for you. If your classes behave
correctly, the scheduler will assign every TV program to a recorder.
