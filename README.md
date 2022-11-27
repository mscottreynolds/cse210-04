# cse210-04
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Design

```
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
_position(Point): Current position of actor on the screen.
_velocity(int): How fast the actor is moving.
_full_path(Point[]): Collection of points representing the path this actor has taken.
_last_path(Point[]): Collection of points representing the most recent movement.
-----------------------------------------------------------
move_actor(dx, dy): Move the actor in the specified directions.
is_intercept(Point): Returns true if the specified point was intercepted by the most recent movement.


Artificat(Actor): Class that represents the gems and rocks.
-----------------------------------------------------------
_description(str): Current description (or message) of this actor.
_value: Number of points for this artificat, 1 for gem, -1 for rock.
-----------------------------------------------------------


Player(Actor): Class that represents the player.
-----------------------------------------------------------
_score: The players current score.
-----------------------------------------------------------


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
_draw_screen(): Draws the current state of the screen.
_get_input(): Gets input from the player, players movement or key presses.
_do_updates(): Update the positions of the actors
```


Q. How did you apply inheritance to your program's design?
A. Inheritance was applied to the Greed game by defining a base class, Actor, that has all of the attributes and methods that would be common to the gems, stones, and the player. An artifact class is used for both the gems and stones as they differ in only score values and what message is displayed to the player. The player inherits from the Actor class and implements one extra attribute for the player's score. Other classes use the Actor class directly like the Banner that is displayed to the user for scores and other messages--It is possible that in future implementations of this game the Banner could even move around the screen in the same way that the artifacts and player do, thus the reason for the banner also using all of the attributes and methods of the base Actor class.

The Director encapsulates attributes to keep track of the Player, Artifacts, Terminal, and Video services as well as the original parameters passed to it upon initialization. The Actor class encapsulates the Point class which implements everything about a point on the screen. The Actor class also keeps track of every point the actor has been to in order to make it easier to determine collisions. The point class encapsulates the Color class as every point can potentially have its own color. Each point can even have its own unique display character.
