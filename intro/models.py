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
    players_per_group = 11
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
        # elif player.id_in_group == 11:
        #     player.role = 'C'

    station_id = models.IntegerField(label="Qual è l'id della postazione (station ID)?")
    type = models.IntegerField(choices=[
        [0, 'A'],
        [1, 'B'],
    ], widget=widgets.RadioSelect, label="Che tipo di giocatore sei?")

    # number_of_AB = models.IntegerField(
    #     widget=widgets.RadioSelect,
    #     choices=[1, 2, 3, 4, 5], label="How many participants did you meet?")

    # consent_accepted = models.BooleanField()


