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

class Results(Page):
    def is_displayed(self):
        player = self.player
        return player.id_in_group >=  1 and player.id_in_group <= 10

page_sequence = [
    WorkPage, Results
]
