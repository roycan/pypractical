"""Interview Scheduler -- Family 03, Assessment 03 (teacher solution)."""


class Interview:
    """Represents one candidate interview."""

    def __init__(self, start, end, panel):
        """Initialize a candidate interview.

        Args:
            start (int): Starting time.
            end (int): Ending time.
            panel (int): Panel size (number of interviewers).
        """
        self.start = start
        self.end = end
        self.panel = panel


class Interviewer:
    """Represents one interviewer."""

    def __init__(self):
        """Initialize an interviewer.

        An interviewer starts available at time 0 and has no assigned interviews.
        """
        self.available_at = 0
        self.interviews = []

    def can_take(self, interview):
        """Return True if this interviewer can take the given interview.

        Args:
            interview (Interview): The interview to check.

        Returns:
            bool: True if the interview can be taken, False otherwise.
        """
        return interview.start >= self.available_at

    def conduct(self, interview):
        """Assign an interview to this interviewer.

        Args:
            interview (Interview): The interview to conduct.
        """
        self.interviews.append(interview)
        self.available_at = interview.end


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


if __name__ == "__main__":
    interview = Interview(5, 8, 2)
    interviewer = Interviewer()

    print(interviewer.can_take(interview))
    interviewer.conduct(interview)
    print(interviewer.available_at)
