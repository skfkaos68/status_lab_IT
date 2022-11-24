from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class WorkPage(Page):
    live_method = 'live_ret'
    title = 'Performance Period - Stage 1'

    def vars_for_template(self):
        self.player.get_or_create_task()
        return dict()

    def get_timeout_seconds(self):
        return self.session.config.get('working_time_sec', Constants.WORKING_TIME_SEC)

    def before_next_page(self):
        self.player._num_tasks_correct = self.player.num_tasks_correct(page_name='WorkPage')
        self.player._num_tasks_total = self.player.num_tasks_total(page_name='WorkPage')
        self.player.set_payoff()

class Type_attention(Page):
  form_model = 'player'
  form_fields = ['type']

class Second_stageA(Page):
    def is_displayed(self):
        player = self.player
        return player.type ==0

class Second_stageB(Page):
    def is_displayed(self):
        player = self.player
        return player.type==1
class Post_Survey(Page):
    pass
    # def is_displayed(self):
    #     player = self.player
    #     return player.id_in_group >=  1 and player.id_in_group <= 10

    form_model = 'player'
    form_fields = ['agree_statement', 'agree_statement2', 'agree_statement3', 'agree_statement4']

class Post_Survey2(Page):
    pass
    # def is_displayed(self):
    #     player = self.player
    #     return player.id_in_group >=  1 and player.id_in_group <= 10

    form_model = 'player'
    form_fields = ['Video_frequency', 'Video_frequency2', 'Video_frequency3']

class Post_Survey3(Page):
    pass
    # def is_displayed(self):
    #     player = self.player
    #     return player.id_in_group >=  1 and player.id_in_group <= 10

    form_model = 'player'
    form_fields = ['Video_opinion', 'Video_opinion2', 'Video_opinion3']

class Post_Survey4(Page):
    pass
    # def is_displayed(self):
    #     player = self.player
    #     return player.id_in_group >=  1 and player.id_in_group <= 10

    form_model = 'player'
    form_fields = ['open_question', 'open_question2', 'open_question3', 'open_question4']

# class Wait_others(WaitPage):
#     def is_displayed(self):
#         player = self.player
#         return player.type==1 and player.type==0

class Results(Page):
    pass
    # def is_displayed(self):
    #     player = self.player
    #     return player.id_in_group >=  1 and player.id_in_group <= 10

page_sequence = [
    WorkPage, Type_attention, Second_stageA, Second_stageB,
    Post_Survey, Post_Survey2, Post_Survey3, Post_Survey4, Results
]
