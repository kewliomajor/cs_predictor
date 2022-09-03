class CsMap:

    def __init__(self, name, times_played, win_percentage):
        self.name = name
        self.times_played = times_played
        self.win_percentage = win_percentage
        self.rounds_lost_in_wins = 0
        self.rounds_won_in_losses = 0

    def get_name(self):
        return self.name

    def set_rounds_lost_in_wins(self, count):
        self.rounds_lost_in_wins = count

    def set_rounds_won_in_losses(self, count):
        self.rounds_won_in_losses = count
