"""Person ID -- Family 09, Assessment 06 (teacher solution)."""


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
        """Initialize a person with no ID card."""
        self.name = name
        self.id_card = None

    def set_id_card(self, card):
        """Store the person's ID card."""
        self.id_card = card

    def get_id_card(self):
        """Return the stored ID card, or None."""
        return self.id_card

    def get_id_number(self):
        """Return the ID number, or "No ID"."""
        if self.id_card is None:
            return "No ID"
        return self.id_card.get_number()


if __name__ == "__main__":
    person = Person("Ada")
    print(person.get_id_number())

    person.set_id_card(IDCard("A-1001"))
    print(person.get_id_number())
    print(person.get_id_card().get_number())