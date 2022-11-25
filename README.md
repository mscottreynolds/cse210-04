# cse210-04
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Design

Color: Class to represent a color.
-----------------------------------------------------------
_r: Red
_g: Green
_b: Blue
-----------------------------------------------------------


Point: Class used to repsent the position, size, and color of the actors.
-----------------------------------------------------------
_display(str): Displayable text representation.
_x: x position on the screen.
_y: y position on the screen.
_size: Size of this point.
_color(Color): Color of this point.
-----------------------------------------------------------


Actor: Base class for Artifact and Player.
-----------------------------------------------------------
_description(str): Current description (or message) of this actor.
_position(Point): Current position of actor on the screen.
_velocity(int): How fast the actor is moving.
_full_path(Point[]): Collection of points representing the path this actor has taken.
_last_path(Point[]): Collection of points representing the most recent movement.
-----------------------------------------------------------
move_actor(dx, dy): Move the actor in the specified directions.
is_intercept(Point): Returns true if the specified point was intercepted by the most recent movement.


Artificat(Actor): Class that represents the gems and rocks.
-----------------------------------------------------------
_value: Number of points for this artificat, 1 for gem, -1 for rock.
-----------------------------------------------------------
move_artifact(dx, dy): Move the artifact in the specified directions.


Player(Actor): Class that represents the player.
-----------------------------------------------------------
_score: The players current score.
-----------------------------------------------------------
move_player(dx, dy): Move the player in the specified directions.


TerminalServices: Class to handle keyboard input.
--------------------------------------------------------------
--------------------------------------------------------------


VideoServices: Class to handle video output.
--------------------------------------------------------------
--------------------------------------------------------------


Director: Class that controls the game play.
-----------------------------------------------------------
_cast(Actor): Collection of all actors.
_banner(Actor): Main banner of messages.
_player(Player): Represents the player
_artifacts(Artificat): Collection of artifacts.
_terminal(TerminalServices): Terminal services.
_video(VideoServices): Video services.
-----------------------------------------------------------
start_game(): Starts the game.
draw_screen(): Draws the current state of the screen.
get_input(): Gets input from the player, players movement or key presses.
do_updates(): Update the positions of the actors


