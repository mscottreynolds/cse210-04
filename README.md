# cse210-04
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as there are gems to collect.

## Design


Q. How did you apply inheritance to your program's design?
A. Inheritance was applied to the Greed game by defining a base class, Actor, that has all of the attributes and methods that would be common to the gems, stones, and the player. An artifact class is used for both the gems and stones as they differ in only score values and what message is displayed to the player. The player inherits from the Actor class and implements one extra attribute for the player's score. Other classes use the Actor class directly like the Banner that is displayed to the user for scores and other messages--It is possible that in future implementations of this game the Banner could even move around the screen in the same way that the artifacts and player do, thus the reason for the banner also using all of the attributes and methods of the base Actor class.

The Director encapsulates attributes to keep track of the Player, Artifacts, Terminal, and Video services as well as the original parameters passed to it upon initialization. The Actor class encapsulates the Point class which implements everything about a point on the screen. The Actor class also keeps track of every point the actor has been to in order to make it easier to determine collisions. The point class encapsulates the Color class as every point can potentially have its own color. Each point can even have its own unique display character.
