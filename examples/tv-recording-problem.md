# TV Recorder Scheduler

A software company is developing a scheduling system for digital TV recorders.

Another programmer has already written the scheduling algorithm, but the system cannot work because two important classes are incomplete.

Your job is to complete the **Program** and **Recorder** classes.

---

## Program Class

A `Program` object represents one television program.

Each program stores:

- start time
- end time
- channel number

---

## Recorder Class

A `Recorder` object represents one TV recorder.

Each recorder should remember:

- when it becomes available
- every program assigned to it

Initially, a recorder is available at time **0**.

---

## Required Methods

### Program

```python
Program(start, end, channel)
```

The constructor should store the three values as instance variables.

---

### Recorder

```python
Recorder()
```

The constructor should

- set `available_at` to `0`
- create an empty list named `programs`

---

```python
can_record(program)
```

Returns

- `True` if the recorder can record the given program
- `False` otherwise

A recorder can record a program if

```text
program.start >= available_at
```

---

```python
record(program)
```

This method should

1. add the program to the recorder's list
2. update `available_at` to the program's ending time

---

## Example

```python
p = Program(5, 8, 2)

r = Recorder()

print(r.can_record(p))
```

Output

```
True
```

After recording

```python
r.record(p)

print(r.available_at)
```

Output

```
8
```

The recorder now contains one program.

---

## Hint

Remember that objects store **state** (their variables) and **behavior** (their methods).

The scheduling system has already been written for you.

If your classes behave correctly, the scheduler will automatically assign every TV program to a recorder.

---

## Constraints

- Number of programs ≤ 100
- Start time < End time
- Times are positive integers
- Programs are processed in order of starting time

You do **not** need to write the scheduling algorithm.