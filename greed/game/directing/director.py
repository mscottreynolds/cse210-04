from game.casting.cast import Cast
from game.casting.artifact import Artifact
from game.casting.player import Player
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

class Director:
    """A person who directs the game. The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service: KeyboardService, video_service: VideoService):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard = keyboard_service
        self._video = video_service

        
    def start_game(self, cast: Cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._cast = cast

        self._video.open_window()
        while self._video.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)

        self._video.close_window()


    def _get_inputs(self, cast: Cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        velocity = self._keyboard.get_direction()
        player = cast.get_first_actor("player")
        player.set_velocity(velocity)        

    def _do_updates(self, cast: Cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banner")
        player = cast.get_first_actor("player")
        artifacts = cast.get_actors("artifacts")

        # banner.set_text("")
        max_x = self._video.get_width()
        max_y = self._video.get_height()
        player.move_next(max_x, max_y)
        score = player.get_score()
        
        for artifact in artifacts:
            if player.get_position().equals(artifact.get_position()):
                score += artifact.get_value()
                player.set_score(score)

                # Remove the artifact from the cast.
                cast.remove_actor("artifacts", artifact)
                # message = artifact.get_description()
                # self._player.set_text(message)

                # Add new artifact?
                # ...
            else:
                # Move artifact to next position.
                artifact.move_next(max_x, max_y)
        
        banner.set_text(f"Score: {score}")


    def _do_outputs(self, cast: Cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        video = self._video
        video.clear_buffer()
        actors = cast.get_all_actors()
        video.draw_actors(actors)
        video.flush_buffer()

        