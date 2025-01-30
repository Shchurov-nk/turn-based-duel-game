from player import Player

class Game:
    def __init__(self):
        self.player1 = Player(name="Bob")
        self.player2 = Player(name="Alice")
        self.current_player = self.player1

    def start(self):
        while self.player1.health > 0 and self.player2.health > 0:
            self.display_status()
            self.take_turn()
        self.display_winner()

    def display_status(self):
        print('\n-----')
        print(f"{self.player1.name} Health: {self.player1.health}")
        print(f"{self.player2.name} Health: {self.player2.health}")
        print(f"{self.current_player.name}'s turn!")

    def take_turn(self):
        attack_points, defend_points, skip_points = 0, 0, 0
        self.current_player.action_points += 4
        print(f"{self.current_player.name} has {self.current_player.action_points} action points!")
        while self.current_player.action_points > 0:
            action = input("Choose action (attack/defend/skip - a/d/s): ").strip().lower()
            if action == "a":
                self.current_player.action_points -= 1
                attack_points += 1
            elif action == "d":
                self.current_player.action_points -= 1
                defend_points += 1
            elif action == "s":
                self.current_player.action_points -= 1
                skip_points += 1
            else:
                print("Invalid action. Please choose 'attack' or 'defend'.")

        target = self.player2 if self.current_player == self.player1 else self.player1
        self.current_player.attack(attack_points, target)
        self.current_player.defend(defend_points)
        self.current_player.skip(skip_points)

        # Switch turns
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def display_winner(self):
        if self.player1.health <= 0:
            print(f"{self.player2.name} wins!")
        else:
            print(f"{self.player1.name} wins!")