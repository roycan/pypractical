"""Unit tests for TV Recorder Scheduler -- Family 03, Assessment 01."""

import unittest

try:
    from solution import Program, Recorder, minimum_recorders
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestRecorderSystem(unittest.TestCase):

    # --- Program ---

    def test_program_start(self):
        program = Program(1, 4, 2)
        self.assertEqual(program.start, 1)

    def test_program_end(self):
        program = Program(1, 4, 2)
        self.assertEqual(program.end, 4)

    def test_program_channel(self):
        program = Program(1, 4, 2)
        self.assertEqual(program.channel, 2)

    # --- Recorder ---

    def test_recorder_initial_time(self):
        recorder = Recorder()
        self.assertEqual(recorder.available_at, 0)

    def test_recorder_initial_programs(self):
        recorder = Recorder()
        self.assertEqual(len(recorder.programs), 0)

    def test_can_record_true(self):
        recorder = Recorder()
        program = Program(5, 8, 1)
        self.assertTrue(recorder.can_record(program))

    def test_can_record_false(self):
        recorder = Recorder()
        recorder.available_at = 6
        program = Program(5, 9, 1)
        self.assertFalse(recorder.can_record(program))

    def test_record_updates_time(self):
        recorder = Recorder()
        program = Program(3, 10, 2)
        recorder.record(program)
        self.assertEqual(recorder.available_at, 10)

    def test_record_adds_program(self):
        recorder = Recorder()
        program = Program(3, 10, 2)
        recorder.record(program)
        self.assertEqual(len(recorder.programs), 1)
        self.assertIs(recorder.programs[0], program)

    # --- Scheduler (integration) ---

    def test_scheduler_simple(self):
        data = [(1, 5, 1), (5, 8, 2)]
        self.assertEqual(minimum_recorders(data), 1)

    # --- Hidden ---

    def test_scheduler_overlap(self):
        data = [(1, 5, 1), (2, 6, 2)]
        self.assertEqual(minimum_recorders(data), 2)

    def test_scheduler_many(self):
        data = [(1, 4, 1), (2, 5, 2), (3, 6, 3), (6, 8, 1)]
        self.assertEqual(minimum_recorders(data), 3)

    def test_scheduler_non_overlapping(self):
        data = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 1)]
        self.assertEqual(minimum_recorders(data), 1)

    def test_scheduler_complex(self):
        data = [(1, 7, 2), (3, 5, 3), (5, 9, 1), (8, 10, 2), (10, 12, 3)]
        self.assertEqual(minimum_recorders(data), 2)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
