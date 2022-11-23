from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        # if subsession.round_number == 1:
        #     for player in subsession.get_players():
        #         player.participant.id_in_group = player.id_in_group

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    def role(player):
        if player.id_in_group >=  1 and player.id_in_group <= 5:
            player.role = 'A'
        elif player.id_in_group > 5 and player.id_in_group <= 10:
            player.role = 'B'
        elif player.id_in_group == 11:
            player.role = 'C'

    player_id = models.IntegerField(label="What is your station id?")
    age = models.IntegerField(label="What is your age?")
    sex = models.IntegerField(choices=[
        [0, 'man'],
        [1, 'woman'],
    ], widget=widgets.RadioSelect)
    race = models.IntegerField(choices=[
        [0, 'White'],
        [1, 'Black'],
        [2, 'Hispanic'],
        [3, 'Asian'],
        [4, 'Other']
    ], widget=widgets.RadioSelect)
    other_race = models.StringField(blank=True, label="If you chose other in the previous question, "
                                                      "please write down your answer")
    type = models.IntegerField(choices=[
        [0, 'A'],
        [1, 'B'],
        [2, 'C'],
    ], widget=widgets.RadioSelect, label="What is your player type?")

    # number_of_AB = models.IntegerField(
    #     widget=widgets.RadioSelect,
    #     choices=[1, 2, 3, 4, 5], label="How many participants did you meet?")

    # consent_accepted = models.BooleanField()


