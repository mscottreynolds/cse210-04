from game.casting.actor import Actor
"""
Artifact class implements Actor and adds attributes and methods for dealing with the path the artifact has taken, its point value, description, and for checking interecepted positions.
"""
class Artifact(Actor):
    """ Artifact class. Inherits all methods and attributes of Actor, adding a message attribute, that doesn't exist in Actor.
    Attribute:
        _message (string): Unique message for this artificat.
    """
    def __init__(self):
        """Initialize with blank message."""
        self._description = ""  # silly description or message
        self._value = 0         # point value
        self._full_path = []    # Full path that this artifact has traveled.
        self._recent_path = []  # The path artifact took with recent move.

    def get_description(self):
        """Return message for this artifact. """
        return self._message

    def set_description(self, message):
        """Set the message for this artifcat."""
        self._message = message

    def get_value(self):
        """Get this artifacts point value."""
        return self._value

    def set_value(self, value):
        """Set this artifacts point value. """
        self._value = value

    def is_intercept(self, position):
        """Check the supplied position (Point) and see if it was intercepted with the most recent move/path."""
        return False