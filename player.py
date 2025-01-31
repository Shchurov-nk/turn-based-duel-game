class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100  # Starting health
        self.shield = 0 # Shield - obtained for 1 turn by defending
        self.action_points = 0 # Total action points per turn. Player gets +4 actions per turn
        self.attack_points = 0 # Use action points to get att/def/skip points
        self.defend_points = 0
        self.skip_points = 0

    def attack(self, attack_points, target):
        attack_points = max(0, attack_points - target.shield) # Defender's shield reduces attack points
        damage = 10 * [0, 1, 2, 3, 5, 8, 13, 21, 34][attack_points]  # Damage: Fibonacci scaled
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {attack_points} points = {damage} damage!")

    def defend(self, defend_points):
        # Defending provides temporary shield
        self.shield += defend_points
        print(f"{self.name} is defending for {defend_points} points this turn!")

    def skip(self, skip_points):
        self.action_points += skip_points
        print(f"{self.name} is skipping for {skip_points} points this turn!")

    def is_alive(self):
        return self.health > 0