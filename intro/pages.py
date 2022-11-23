from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Consent_A(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 5

class Consent_B(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Consent_C(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group == 11

class Consent_A2(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 5

class Consent_B2(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Consent_C2(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group == 11

class Survey(Page):
    form_model = 'player'
    form_fields = ['player_id', 'age', 'sex', 'race', 'other_race']

class Instruction_A(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 5

    # form_model = 'player'
    # form_fields = ['type']

class Instruction_B(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

    # form_model = 'player'
    # form_fields = ['type']

class Instruction_C(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group == 11

    # form_model = 'player'
    # form_fields = ['type']

class Instruction_C2(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group == 11

class Instruction_C3(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group == 11

class Result_C(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group == 11

class Results(Page):
    pass

page_sequence = [Consent_A, Consent_B, Consent_C, Consent_A2, Consent_B2, Consent_C2, Survey,
                 Instruction_A, Instruction_B, Instruction_C, Instruction_C2, Instruction_C3,
                 Result_C]
