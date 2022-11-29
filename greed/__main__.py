import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.player import Player
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 800
MAX_Y = 800
CELL_SIZE = 40
FONT_SIZE = 40
COLS = 20
ROWS = 20
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 20


def main():
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banner", banner)
    
    # create the player
    player = Player()
    player.set_score(0)

    x = int(MAX_X / 2)
    position = Point(x, MAX_Y)
    position = position.scale(CELL_SIZE)
    player.set_position(position)
    player.set_color(WHITE)
    player.set_text("#")
    player.set_size(FONT_SIZE)
    cast.add_actor("player", player)

    # Load in silly messages for gems and stones.
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    # Keep track of previously used positions so gems and stones won't be created
    # on top of each other.
    positions = set()

    # Create the artificats. Half gems, half stones.
    for n in range(DEFAULT_ARTIFACTS):
        if n % 2 == 0:
            text = "*"      # gem
        else:
            text = "O"      # stone
        message = messages[n]       # A silly message to display to the user.

        artifact = _create_artifact(text, CELL_SIZE, message, positions)
        cast.add_actor("artifacts", artifact)

    # Setup input and output.    
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE, False)

    # start the game
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


def _create_artifact(text, size, message, positions = set()):
    """
    Create an artifact.
    text: Displayable text for this artifact.
    size: Size of this artifact.
    message: Silly message assigned to this artifact.
    positions: (Optional) A set of previously defined positions. New artifacts will avoid being created with a position already defined in the set.
    
    Returns: New artifact.
    """

    # Create color.
    r = 0
    g = 0
    b = 0
    while r == 0 and g == 0 and b == 0:
        # Repeat until something other than black is selected.
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

    color = Color(r, g, b)
    
    # Create the initial position.
    position = None
    while position == None:
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(size)
        
        # Make sure position isn't already used.
        if position in positions:
            position = None
        else:
            positions.add(position)

    artifact = Artifact()
    artifact.set_text(text)
    artifact.set_size(size)
    artifact.set_color(color)
    artifact.set_position(position)
    artifact.set_description(message)

    return artifact


if __name__ == "__main__":
    main()