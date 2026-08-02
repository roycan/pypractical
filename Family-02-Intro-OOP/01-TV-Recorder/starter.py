"""TV Recorder Scheduler -- Family 02, Assessment 01 (starter).

Complete the Program and Recorder classes. Do NOT modify minimum_recorders.
"""


class Program:
    """Represents one TV program."""

    def __init__(self, start, end, channel):
        """Initialize a TV program.

        Args:
            start (int): Starting time.
            end (int): Ending time.
            channel (int): Channel number.
        """

        # TODO: Write your solution here.

        return


class Recorder:
    """Represents one TV recorder."""

    def __init__(self):
        """Initialize a recorder.

        A recorder starts available at time 0 and has no assigned programs.
        """

        # TODO: Write your solution here.

        return

    def can_record(self, program):
        """Return True if this recorder can record the given program.

        Args:
            program (Program): The program to check.

        Returns:
            bool: True if the program can be recorded, False otherwise.
        """

        # TODO: Write your solution here.

        return False

    def record(self, program):
        """Assign a program to this recorder.

        Args:
            program (Program): The program to record.
        """

        # TODO: Write your solution here.

        return


def minimum_recorders(program_data):
    """The scheduling algorithm. Students do NOT modify this function."""
    # Programs are processed in order of starting time.
    ordered_data = sorted(program_data)

    programs = []
    for start, end, channel in ordered_data:
        programs.append(Program(start, end, channel))

    recorders = []

    for program in programs:
        assigned = False

        for recorder in recorders:
            if recorder.can_record(program):
                recorder.record(program)
                assigned = True
                break

        if not assigned:
            recorder = Recorder()
            recorder.record(program)
            recorders.append(recorder)

    return len(recorders)
