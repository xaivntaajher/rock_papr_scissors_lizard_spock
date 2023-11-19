from ai import AI
from human import Human

Gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

class Game():
    def __init__(self):
        self.gesture_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.best_of_rounds = 2
        self.P1 = None
        self.P2 = None
        self.P1_current_score = 0
        self.P2_current_score = 0

      
        


    def run_game(self):
        self.game_start()
        self.display_winner()        


    def game_start(self):
        print()
        print("Welcome to another game of ROCK, PAPER, SCISSORS, LIZARD, SPOCK")
        print()
        print("Each match will be best of three games. Use the numerator keys to enter your selection.")
        print()     
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard Poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("paper disproves Spock")
        print("Spock vaporizes Rock")
        print()
        
        self.start = input("How many players? 1, 2, or 3 for a surprise. ")
        if self.start == "1":
            self.P1 = Human('Player1')
            self.P2 = AI('AI')
            self.game_run_player_ai()
        elif self.start == "2":
            self.P1 = Human('Player1')
            self.P2 = Human('Player2')
            self.game_run_player_player()
        elif self.start == "3":
            self.P1 = AI("Player 1")
            self.P2 = AI("Player 2")
            self.game_run_ai_ai()
        else:
            print("Please enter a valid key.")
            self.game_start()
        
       



    def game_run_player_ai(self):
        while self.P1_current_score < 2 and self.P2_current_score < 2:
            p1_choice = input("Player 1, choose your gesture (Rock, Paper, Scissors, Lizard, Spock): ")
            p2_choice = self.P2.choose_gestures()
            if p1_choice == p2_choice:
                print("Tie!")
            elif (p1_choice == "Rock" and (p2_choice == "Scissors" or p2_choice == "Lizard")) or \
                    (p1_choice == "Paper" and (p2_choice == "Rock" or p2_choice == "Spock")) or \
                    (p1_choice == "Scissors" and (p2_choice == "Paper" or p2_choice == "Lizard")) or \
                    (p1_choice == "Lizard" and (p2_choice == "Paper" or p2_choice == "Spock")) or \
                    (p1_choice == "Spock" and (p2_choice == "Rock" or p2_choice == "Scissors")):
                self.P1.score_point()
                self.P1_current_score += 1
                print()
                print("Player 1 wins this round!")
            else:
                self.P2.score_point()
                self.P2_current_score += 1
                print()
                print("Player 2 wins this round!")
        print(f"Score - Player 1: {self.P1.score}, Player 2: {self.P2.score}")
              

    def game_run_player_player(self):
            while self.P1_current_score < 2 and self.P2_current_score < 2:
                p1_choice = input("Player 1, choose your gesture (Rock, Paper, Scissors, Lizard, Spock): ")
                p2_choice = input("Player 2, choose your gesture (Rock, Paper, Scissors, Lizard, Spock): ")
                if p1_choice == p2_choice:
                    print("Tie!")
                elif (p1_choice == "Rock" and (p2_choice == "Scissors" or p2_choice == "Lizard")) or \
                        (p1_choice == "Paper" and (p2_choice == "Rock" or p2_choice == "Spock")) or \
                        (p1_choice == "Scissors" and (p2_choice == "Paper" or p2_choice == "Lizard")) or \
                        (p1_choice == "Lizard" and (p2_choice == "Paper" or p2_choice == "Spock")) or \
                        (p1_choice == "Spock" and (p2_choice == "Rock" or p2_choice == "Scissors")):
                    self.P1.score_point()
                    self.P1_current_score += 1
                    print()
                    print("Player 1 wins this round!")
                else:
                    self.P2.score_point()
                    self.P2_current_score += 1
                    print()
                    print("Player 2 wins this round!")
            print(f"Score - Player 1: {self.P1.score}, Player 2: {self.P2.score}")
            

    def game_run_ai_ai(self):
            while self.P1_current_score < 2 and self.P2_current_score < 2:
                    
                p1_choice = self.P1.choose_gestures()
                p2_choice = self.P2.choose_gestures()
                if p1_choice == p2_choice:
                    print("Tie!")
                elif (p1_choice == "Rock" and (p2_choice == "Scissors" or p2_choice == "Lizard")) or \
                    (p1_choice == "Paper" and (p2_choice == "Rock" or p2_choice == "Spock")) or \
                    (p1_choice == "Scissors" and (p2_choice == "Paper" or p2_choice == "Lizard")) or \
                    (p1_choice == "Lizard" and (p2_choice == "Paper" or p2_choice == "Spock")) or \
                    (p1_choice == "Spock" and (p2_choice == "Rock" or p2_choice == "Scissors")):
                    self.P1.score_point()
                    self.P1_current_score += 1
                    print("Player 1 wins this round!")
            
                else:
                    self.P2.score_point()
                    self.P2_current_score += 1
                    print("Player 2 wins this round!")
                    print(f"Score - Player 1: {self.P1.score}, Player 2: {self.P2.score}")
                    
                if self.P1_current_score == 2:
                    print()
                    print("Player 1 wins the game!")
                    
                elif self.P2_current_score ==2:
                    print()
                    print("Player 2 wins the game!")
                
                
    def display_winner(self):
            if self.P1_current_score > self.P2_current_score:
                print()
                print(f"The winner is {self.P1.name}!")
                new_game = input("Would you like to play again? y/n ")
                if new_game == "y":
                    self.P1_current_score = 0
                    self.P2_current_score = 0
                    self.run_game()
                   
                else:
                    print("Ok Goodbye")
            elif self.P2_current_score > self.P1_current_score:
                print()
                print(f"The winner is {self.P2.name}! ")
                new_game = input("Would you like to play again? y/n ")
                if new_game == "y":
                    self.P1_current_score = 0
                    self.P2_current_score = 0
                    self.run_game()
                   
                else:
                    print("Ok Goodbye")
                

