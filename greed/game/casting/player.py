from game.casting.actor import Actor

class Player(Actor):
    """ Player class. Inherits all methods and attributes of Actor, adding a score
    Attribute:
        _score (int): The running score for this user.
    """
    def __init__(self):
        super().__init__()
        
        self._score = 0
    def get_score(self):
        """Return the current score for the player. """
        return self._score
    def set_score(self, score):
        """Set the current score for this player."""
        self._score = score
