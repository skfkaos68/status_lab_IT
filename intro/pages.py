from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Consent_A(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 5

class Consent_A2(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 5

class Consent_A3(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 5
class Consent_A4(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 5

class Consent_B(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Consent_B2(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10
class Consent_B2(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Consent_B3(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Consent_B4(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Consent_C(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group == 11

# class Consent_CC(Page):
#     def is_displayed(self):
#         player = self.player
#         return player.id_in_group == 11

# class Consent_C2(Page):
#     def is_displayed(self):
#         player = self.player
#         return player.id_in_group == 11

# class Survey(Page):
#     form_model = 'player'
#     form_fields = ['player_id', 'age', 'sex', 'race', 'other_race']

class Instruction_A(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 5

class Instruction_A2(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 5

class Instruction_A3(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >= 1 and player.id_in_group <= 5

class Instruction_A4(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >= 1 and player.id_in_group <= 5

class Instruction_A5(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >= 1 and player.id_in_group <= 5

class Instruction_A6(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >= 1 and player.id_in_group <= 5

class Instruction_A7(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >= 1 and player.id_in_group <= 5

    form_model = 'player'
    form_fields = ['type', 'station_id']

class Instruction_B(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Instruction_B2(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Instruction_B3(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Instruction_B4(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

class Instruction_B5(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group > 5 and player.id_in_group <= 10

    form_model = 'player'
    form_fields = ['type', 'station_id']

class task_will_start(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >= 1 and player.id_in_group <= 10

# class Instruction_C(Page):
#     def is_displayed(self):
#         player = self.player
#         return player.id_in_group == 11
#
#     form_model = 'player'
#     form_fields = ['type']

# class Instruction_C2(Page):
#     def is_displayed(self):
#         player = self.player
#         return player.id_in_group == 11

# class Instruction_C3(Page):
#     def is_displayed(self):
#         player = self.player
#         return player.id_in_group == 11

# class Result_C(Page):
#     def is_displayed(self):
#         player = self.player
#         return player.id_in_group == 11


page_sequence = [Consent_A, Consent_A2, Consent_A3, Consent_A4, Consent_B, Consent_B2, Consent_B3, Consent_B4,
                 Consent_C, Instruction_A, Instruction_A2, Instruction_A3, Instruction_A4, Instruction_A5,
                 Instruction_A6, Instruction_A7, Instruction_B, Instruction_B2, Instruction_B3, Instruction_B4,
                 Instruction_B5, task_will_start
                 ]
            #  Consent_C, Consent_CC, Consent_C2, survey, Instruction_C, Instruction_C2, Instruction_C3, Result_C