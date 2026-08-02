class Program:
    """Represents one TV program."""

    def __init__(self, start, end, channel):
        """
        Initialize a TV program.

        Args:
            start (int): Starting time.
            end (int): Ending time.
            channel (int): Channel number.
        """
        # TODO:
        # Save the values into instance variables.
        pass


class Recorder:
    """Represents one TV recorder."""

    def __init__(self):
        """
        Initialize a recorder.

        A recorder starts available at time 0
        and has no assigned programs.
        """
        # TODO:
        # available_at = 0
        # programs = []
        pass

    def can_record(self, program):
        """
        Return True if this recorder can record
        the given program.

        Args:
            program (Program)

        Returns:
            bool
        """
        # TODO
        pass

    def record(self, program):
        """
        Assign a program to this recorder.

        This should

        1. add the program to self.programs
        2. update self.available_at

        Args:
            program (Program)
        """
        # TODO
        pass


def minimum_recorders(program_data):
    """
    The scheduling algorithm.

    Students do NOT modify this function.
    """

    programs = [
        Program(start, end, channel)
        for start, end, channel in program_data
    ]

    programs.sort(key=lambda p: p.start)

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