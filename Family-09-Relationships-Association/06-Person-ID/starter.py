"""Person ID -- Family 09, Assessment 06 (starter).

The IDCard class is provided and complete. Complete the Person class.
"""


# Provided class. Do NOT modify it.
class IDCard:
    """Represents one identification card."""

    def __init__(self, id_number):
        self.id_number = id_number

    def get_number(self):
        """Return the card's id number."""
        return self.id_number


class Person:
    """Represents a person who carries exactly one ID card."""

    def __init__(self, name):
        """Initialize a person with no ID card.

        Args:
            name (str): The person's name.
        """

        # TODO: Write your solution here.

        return

    def set_id_card(self, card):
        """Store the person's ID card.

        Args:
            card (IDCard): The ID card to store.
        """

        # TODO: Write your solution here.

        return

    def get_id_card(self):
        """Return the stored ID card, or None.

        Returns:
            IDCard or None: The stored card, or None if there is none.
        """

        # TODO: Write your solution here.

        return None

    def get_id_number(self):
        """Return the ID number, or "No ID".

        Returns:
            str: The ID number, or "No ID" if there is none.
        """

        # TODO: Write your solution here.

        return ""