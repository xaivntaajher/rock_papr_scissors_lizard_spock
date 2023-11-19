


class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name
        self.gesture_options = []
        

    def choose_gestures(self):
        self.gesture_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def score_point(self):
        self.score += 1