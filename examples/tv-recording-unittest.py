import unittest


class TestRecorderSystem(unittest.TestCase):

    # ---------- Program ----------

    def test_program_start(self):
        p = Program(1, 4, 2)
        self.assertEqual(p.start, 1)

    def test_program_end(self):
        p = Program(1, 4, 2)
        self.assertEqual(p.end, 4)

    def test_program_channel(self):
        p = Program(1, 4, 2)
        self.assertEqual(p.channel, 2)

    # ---------- Recorder ----------

    def test_recorder_initial_time(self):
        r = Recorder()
        self.assertEqual(r.available_at, 0)

    def test_recorder_initial_programs(self):
        r = Recorder()
        self.assertEqual(len(r.programs), 0)

    def test_can_record_true(self):
        r = Recorder()
        p = Program(5, 8, 1)
        self.assertTrue(r.can_record(p))

    def test_can_record_false(self):
        r = Recorder()
        r.available_at = 6
        p = Program(5, 9, 1)
        self.assertFalse(r.can_record(p))

    def test_record_updates_time(self):
        r = Recorder()
        p = Program(3, 10, 2)

        r.record(p)

        self.assertEqual(r.available_at, 10)

    def test_record_adds_program(self):
        r = Recorder()
        p = Program(3, 10, 2)

        r.record(p)

        self.assertEqual(len(r.programs), 1)
        self.assertIs(r.programs[0], p)

    # ---------- Scheduler ----------

    def test_scheduler_simple(self):
        data = [
            (1, 5, 1),
            (5, 8, 2),
        ]
        self.assertEqual(minimum_recorders(data), 1)

    # ---------- Hidden Tests ----------

    def test_scheduler_overlap(self):
        data = [
            (1, 5, 1),
            (2, 6, 2),
        ]
        self.assertEqual(minimum_recorders(data), 2)

    def test_scheduler_many(self):
        data = [
            (1, 4, 1),
            (2, 5, 2),
            (3, 6, 3),
            (6, 8, 1),
        ]
        self.assertEqual(minimum_recorders(data), 3)

    def test_scheduler_non_overlapping(self):
        data = [
            (1, 2, 1),
            (2, 3, 2),
            (3, 4, 3),
            (4, 5, 1),
        ]
        self.assertEqual(minimum_recorders(data), 1)

    def test_scheduler_complex(self):
        data = [
            (1, 7, 2),
            (3, 5, 3),
            (5, 9, 1),
            (8, 10, 2),
            (10, 12, 3),
        ]
        self.assertEqual(minimum_recorders(data), 2)