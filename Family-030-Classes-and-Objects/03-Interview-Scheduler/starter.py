"""Interview Scheduler -- Family 03, Assessment 03 (starter).

Complete the Interview and Interviewer classes. Do NOT modify minimum_interviewers.
"""


class Interview:
    """Represents one candidate interview."""

    def __init__(self, start, end, panel):
        """Initialize a candidate interview.

        Args:
            start (int): Starting time.
            end (int): Ending time.
            panel (int): Panel size (number of interviewers).
        """

        # TODO: Write your solution here.

        return


class Interviewer:
    """Represents one interviewer."""

    def __init__(self):
        """Initialize an interviewer.

        An interviewer starts available at time 0 and has no assigned interviews.
        """

        # TODO: Write your solution here.

        return

    def can_take(self, interview):
        """Return True if this interviewer can take the given interview.

        Args:
            interview (Interview): The interview to check.

        Returns:
            bool: True if the interview can be taken, False otherwise.
        """

        # TODO: Write your solution here.

        return False

    def conduct(self, interview):
        """Assign an interview to this interviewer.

        Args:
            interview (Interview): The interview to conduct.
        """

        # TODO: Write your solution here.

        return


def minimum_interviewers(interview_data):
    """The scheduling algorithm. Students do NOT modify this function."""
    # Interviews are processed in order of starting time.
    ordered_data = sorted(interview_data)

    interviews = []
    for start, end, panel in ordered_data:
        interviews.append(Interview(start, end, panel))

    interviewers = []

    for interview in interviews:
        assigned = False

        for interviewer in interviewers:
            if interviewer.can_take(interview):
                interviewer.conduct(interview)
                assigned = True
                break

        if not assigned:
            interviewer = Interviewer()
            interviewer.conduct(interview)
            interviewers.append(interviewer)

    return len(interviewers)
