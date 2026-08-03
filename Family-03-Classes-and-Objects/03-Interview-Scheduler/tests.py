"""Unit tests for Interview Scheduler -- Family 03, Assessment 03."""

import unittest

try:
    from solution import Interview, Interviewer, minimum_interviewers
except ModuleNotFoundError:
    # Serverless runner injects student code into this namespace, so the
    # imported names are already defined; local unittest still imports solution.py.
    pass


class TestInterviewSchedulerSystem(unittest.TestCase):

    # --- Interview ---

    def test_interview_start(self):
        interview = Interview(1, 4, 2)
        self.assertEqual(interview.start, 1)

    def test_interview_end(self):
        interview = Interview(1, 4, 2)
        self.assertEqual(interview.end, 4)

    def test_interview_panel(self):
        interview = Interview(1, 4, 2)
        self.assertEqual(interview.panel, 2)

    # --- Interviewer ---

    def test_interviewer_initial_time(self):
        interviewer = Interviewer()
        self.assertEqual(interviewer.available_at, 0)

    def test_interviewer_initial_interviews(self):
        interviewer = Interviewer()
        self.assertEqual(len(interviewer.interviews), 0)

    def test_can_take_true(self):
        interviewer = Interviewer()
        interview = Interview(5, 8, 1)
        self.assertTrue(interviewer.can_take(interview))

    def test_can_take_false(self):
        interviewer = Interviewer()
        interviewer.available_at = 6
        interview = Interview(5, 9, 1)
        self.assertFalse(interviewer.can_take(interview))

    def test_conduct_updates_time(self):
        interviewer = Interviewer()
        interview = Interview(3, 10, 2)
        interviewer.conduct(interview)
        self.assertEqual(interviewer.available_at, 10)

    def test_conduct_adds_interview(self):
        interviewer = Interviewer()
        interview = Interview(3, 10, 2)
        interviewer.conduct(interview)
        self.assertEqual(len(interviewer.interviews), 1)
        self.assertIs(interviewer.interviews[0], interview)

    # --- Scheduler (integration) ---

    def test_scheduler_simple(self):
        data = [(1, 5, 1), (5, 8, 2)]
        self.assertEqual(minimum_interviewers(data), 1)

    # --- Hidden ---

    def test_scheduler_overlap(self):
        data = [(1, 5, 1), (2, 6, 2)]
        self.assertEqual(minimum_interviewers(data), 2)

    def test_scheduler_many(self):
        data = [(1, 4, 1), (2, 5, 2), (3, 6, 3), (6, 8, 1)]
        self.assertEqual(minimum_interviewers(data), 3)

    def test_scheduler_non_overlapping(self):
        data = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 1)]
        self.assertEqual(minimum_interviewers(data), 1)

    def test_scheduler_complex(self):
        data = [(1, 7, 2), (3, 5, 3), (5, 9, 1), (8, 10, 2), (10, 12, 3)]
        self.assertEqual(minimum_interviewers(data), 2)

# Run locally with:  python3 -m unittest tests
# if __name__ == "__main__":
#     unittest.main()
