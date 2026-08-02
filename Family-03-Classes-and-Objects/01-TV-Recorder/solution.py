"""TV Recorder Scheduler -- Family 03, Assessment 01 (teacher solution)."""


class Program:
    """Represents one TV program."""

    def __init__(self, start, end, channel):
        """Initialize a TV program.

        Args:
            start (int): Starting time.
            end (int): Ending time.
            channel (int): Channel number.
        """
        self.start = start
        self.end = end
        self.channel = channel


class Recorder:
    """Represents one TV recorder."""

    def __init__(self):
        """Initialize a recorder.

        A recorder starts available at time 0 and has no assigned programs.
        """
        self.available_at = 0
        self.programs = []

    def can_record(self, program):
        """Return True if this recorder can record the given program.

        Args:
            program (Program): The program to check.

        Returns:
            bool: True if the program can be recorded, False otherwise.
        """
        return program.start >= self.available_at

    def record(self, program):
        """Assign a program to this recorder.

        Args:
            program (Program): The program to record.
        """
        self.programs.append(program)
        self.available_at = program.end


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


if __name__ == "__main__":
    program = Program(5, 8, 2)
    recorder = Recorder()

    print(recorder.can_record(program))
    recorder.record(program)
    print(recorder.available_at)
