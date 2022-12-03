# Greed

Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as there are gems to collect.

## Getting Started

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 greed
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure

The project files and folders are organized as follows:
```
root                            (project root folder)
+-- greed                       (source code for game)
  +-- game                      (specific game classes)
    +-- casting                 
        +-- actor.py            (root class for artifact and player)
        +-- artifact.py         (artifact - gem or stone)
        +-- cast.py             (collection of all of the cast, actors)
        +-- player.py           (player)
    +-- directing
        +-- directory.py        (director controls gameplay)
    +-- services
        +-- keyboard_service.py (services for interacting with the keyboard)
        +-- video_service.py    (services for drawing to the screen)
    +-- shared
        +-- color.py            (color object)
        +-- point.py            (point object)
  +-- __main__.py               (entry point for program)
+-- README.md                   (general info)
```

## Required Technologies

* Python 3.8.0
* Raylib Python CFFI 3.7

## Design

```
class Color {
    _r: Red
    _g: Green
    _b: Blue
}

class Point {
    _x: x position on the screen.
    _y: y position on the screen.
}

class Actor {
    _text: Displayable text representation.
    _font_size: Size of this actor.
    _color: Color of the actor.
    _position: Current position of actor on the screen.
    _velocity: How fast the actor is moving.

    move_actor(dx, dy): Move the actor in the specified directions.
}

class Artifact {
    _value: Number of points for this Artifact, 1 for gem, -1 for rock.

    is_intercept(Point): Returns true if the specified point was intercepted by the most recent movement.
}

Actor <|-- Artifact 

class Player {
    _score: Players score.
}

Actor <|-- Artifact

class Cast {
    add_actor(self, group, actor): Adds an actor to the given group.
    get_actors(self, group): Gets the actors in the given group.
    get_all_actors(self): Gets all of the actors in the cast.
    get_first_actor(self, group): Gets the first actor in the given group.
    remove_actor(self, group, actor): Removes an actor from the given group.
}

class TerminalServices

class VideoServices

class Director {
    _cast: Collection of all actors.
    _keyboard: Keyboard services.
    _video: Video services.

    start_game(): Starts the game.
    _draw_screen(): Draws the current state of the screen.
    _get_input(): Gets input from the player, players movement or key presses.
    _do_updates(): Update the positions of the actors
}
```

## FAQ

Q. How did you apply inheritance to your program's design?
A. Inheritance was applied to the Greed game by defining a base class, Actor, that has all of the attributes and methods that would be common to the gems, stones, and the player. An artifact class is used for both the gems and stones as they differ in only score values and what message is displayed to the player. The player inherits from the Actor class and implements one extra attribute for the player's score. Other classes use the Actor class directly like the Banner that is displayed to the user for scores and other messages--It is possible that in future implementations of this game the Banner could even move around the screen in the same way that the artifacts and player do, thus the reason for the banner also using all of the attributes and methods of the base Actor class.

The Director encapsulates attributes to keep track of the Player, Artifacts, Terminal, and Video services as well as the original parameters passed to it upon initialization. The Actor class encapsulates the Point class which implements everything about a point on the screen. The Actor class also keeps track of every point the actor has been to in order to make it easier to determine collisions. The point class encapsulates the Color class as every point can potentially have its own color. Each point can even have its own unique display character.

## Authors

* M. Scott Reynolds rey22006@byui.edu
