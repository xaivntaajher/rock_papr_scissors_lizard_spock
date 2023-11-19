import random
from player import Player

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0
        self.name = name
              
    def choose_gestures(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        chosen_gesture_index = random.randint(0, 4)
        chosen_gesture = gesture_list[chosen_gesture_index]
        print(f'{self.name} has picked {chosen_gesture}')
        return chosen_gesture
