"""
The control actions action contains the class and functions that get the direction of 
the actor and also will close the game if the escape key is pressed
"""
from arcade import key as arcade_key
from data.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def __init__(self):
        """The class constructor.
        """
        pass

    def execute(self, game, cast, key):
        """Executes the action using the given actors.

        Args:
            game (arcade.Window): The game (only used to close if the escape key is pressed)
            cast (dict): The game actors {key: tag, value: list}.
            key (arcade.key): The current key that has been pressed
        """

        for player in cast["players"]:
            direction = self._get_direction(game, player, key)
            if not player.is_dead():

                # checks if a direction was returned since it will return None if invalid key
                if direction:
                    player_velocity = player.get_velocity()
                    
                    # direction_angle = direction.get_angle()

                    if not ((player_velocity[0] != 0 and direction[0] != 0) or (player_velocity[1] != 0 and direction[1] != 0)):
                        player.set_velocity(direction)
                        player.get_trail().add_point(player.get_position())
                        # player.get_sprite().angle = direction_angle
        
    def _get_direction(self, game, player, key):
        """Gets the selected direction for the given player.

        Returns:
            tuple: The selected direction.
            None: If there was an invalid key inputted
        """

        if key == 65307:
            game.window.close()
        
        # if key == arcade_key.X:
        #     player.set_movement_speed(player.get_movement_speed() * 2)
        
        player_keys = player.get_keys()
        if key in player_keys:
            direction = player_keys[key]
            return direction