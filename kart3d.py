import os
import numpy as np
import gymnasium as gym
from gymnasium import spaces
import gymize
from paiagym import PAIAGame

def kart_env(file_name: str=None, render_mode: str=None):
    observation_space = spaces.Dict(
        {
            # The RaySensor is composed of the distance to the hit object and hit object
			# The item that Raycast hit, record it will a specific item number.
			# RayHit
			# 0: No hit
			# 1: Wall
			# 2: Car
			# 3: Gas
			# 4: Wheel
			# 5: Nitro
			# 6: Turtle
			# 7: Banana
            'RaySensor': spaces.Dict(
                {
                    'Front': spaces.Dict(
                        {
                            'Distance': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
                            'Hit': spaces.Discrete(8)
                        }
                    ),
                    'FrontRight': spaces.Dict(
                        {
                            'Distance': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
                            'Hit': spaces.Discrete(8)
                        }
                    ),
                    'FrontLeft': spaces.Dict(
                        {
                            'Distance': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
                            'Hit': spaces.Discrete(8)
                        }
                    ),
                    'Left': spaces.Dict(
                        {
                            'Distance': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
                            'Hit': spaces.Discrete(8)
                        }
                    ),
                    'Right': spaces.Dict(
                        {
                            'Distance': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
                            'Hit': spaces.Discrete(8)
                        }
                    ),
                    'Back': spaces.Dict(
                        {
                            'Distance': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
                            'Hit': spaces.Discrete(8)
                        }
                    ),
                    'BackRight': spaces.Dict(
                        {
                            'Distance': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
                            'Hit': spaces.Discrete(8)
                        }
                    ),
                    'BackLeft': spaces.Dict(
                        {
                            'Distance': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
                            'Hit': spaces.Discrete(8)
                        }
                    )
                }
                
            ),
            # The image that camera captures, include front and back:
            'CameraFront': spaces.Box(low=0, high=255, shape=(112, 252, 3), dtype=np.uint8),
            'CameraBack': spaces.Box(low=0, high=255, shape=(112, 252, 3), dtype=np.uint8),
            # A floating point number that shows the current progress:
			'Progress': spaces.Box(low=-1, high=1, shape=(1,), dtype=np.float32),
			# A floating point number that shows how much time has been used:
			'UsedTime': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
			# A floating point number that shows current velocity:
			'Velocity': spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32),
			# The amount of refill remains, refills = (gas, wheels):
			'RefillRemaining': spaces.Box(low=0, high=1, shape=(2,), dtype=np.float32),
			# The number of effect remains, effects = (nitro, banana, turtle):
			'EffectRemaining': spaces.Box(low=0, high=np.iinfo(np.int32).max, shape=(3,), dtype=np.int32)
        }
    )

    action_space = spaces.Dict(
        {
            'Acceleration': spaces.Box(low=0, high=1, dtype=np.bool_),
            'Brake': spaces.Box(low=0, high=1, dtype=np.bool_),
            'Steering': spaces.Box(low=-1, high=1, dtype=np.float32),
        }
    )

    env = gym.make('gymize/Unity-v0', env_name='kart', file_name=file_name, observation_space=observation_space, action_space=action_space, render_mode=render_mode)
    
    return env

class Game(PAIAGame):
    def __init__(self):
        self.name = 'kart3d'

    def env(self, *args, **kwargs):
        return kart_env(*args, **kwargs)
    
    def unity_path(self):
        return super().unity_path(os.path.dirname(__file__))