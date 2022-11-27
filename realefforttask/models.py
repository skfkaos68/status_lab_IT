from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)

from django.db import models as djmodels
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist

from . import ret_functions
from otree.lookup import get_page_lookup
author = ''

doc = """
    multi-round real effort task
"""


class Constants(BaseConstants):
    name_in_url = 'realefforttask'
    players_per_group = 11
    num_rounds = 1
    # this parameter defines how much time a user will stay on a RET page per round (in seconds)
    task_time = 3000
    PRACTICE_TIME_SEC = 60
    WORKING_TIME_SEC = 30

class Subsession(BaseSubsession):
    def creating_session(self):
        # we look for a corresponding Task Generator in our library (ret_functions.py) that contain all task-generating
        # functions. So the name of the generator in 'task_fun' parameter from settings.py should coincide with an
        # actual task-generating class from ret_functions.
        self.session.vars['task_fun'] = getattr(ret_functions, self.session.config['task'])
        # If a task generator gets some parameters (like a level of difficulty, or number of rows in a matrix etc.)
        # these parameters should be set in 'task_params' settings of an app, in a form of dictionary. For instance:
        # 'task_params': {'difficulty': 5}
        self.session.vars['task_params'] = self.session.config.get('task_params', {})

        # for each player we call a function (defined in Player's model) called get_or_create_task
        # this is done so that when a RET page is shown to a player for the first time they would already have a task
        # to work on
        # for p in self.get_players():
        #     p.get_or_create_task()

class Group(BaseGroup):
    ...



class Player(BasePlayer):
    type = models.IntegerField(choices=[
        [0, 'A'],
        [1, 'B'],
    ], widget=widgets.RadioSelect, label="Che tipo di giocatore sei?")

    age = models.IntegerField(label="Qual è la tua età?")
    gender = models.IntegerField(label="Qual è il tuo genere?", choices=[
        [0, 'Uomo'],
        [1, 'Donna'],
    ], widget=widgets.RadioSelect)
    race = models.IntegerField(label="Qual è la tua etnia?", choices=[
        [0, 'Bianco'],
        [1, 'Nero'],
        [2, 'Ispanico'],
        [3, 'Asiatico'],
        [4, 'Altri']
    ], widget=widgets.RadioSelect)
    other_race = models.StringField(blank=True, label="Se hai scelto 'altri' nella domanda precedente, scrivi la tua risposta")
    salient_gender_men = models.IntegerField(label = "Ricordi quanti uomini stavano aspettando insieme a te all'inizio dell'esperimento?", choices=[1,2,3,4,5,6,7,8])
    salient_gender_women = models.IntegerField(label = "Ricordi quante donne stavano aspettando insieme a te all'inizio dell'esperimento?", choices=[1,2,3,4,5,6,7,8])
    others_performance = models.LongStringField(label = "Rispetto a te, come ti aspetti che gli altri partecipanti abbiano svolto il compito e perché?")
    which_group_better = models.IntegerField(label="Quale gruppo pensi abbia svolto  meglio il compito?", choices=[
        [0, 'Uomini'],
        [1, 'Donne']
    ], widget=widgets.RadioSelect)

    participate_less = models.IntegerField(choices=[
        [0, 'Fortemente in disaccordo'],
        [1, 'In disaccordo'],
        [2, 'Abbastanza in disaccordo'],
        [3, 'Né in accordo né in disaccordo'],
        [4, 'Abbastanza in accordo'],
        [5, 'In accordo'],
        [6, 'Fortemente in accordo']
    ], widget=widgets.RadioSelect, label="Guardando la mia esperienza, partecipo e contribuisco meno a un gruppo durante le videoconferenze rispetto all'interazione faccia a faccia.")

    evaluative_threat = models.IntegerField(choices=[
        [0, 'Fortemente in disaccordo'],
        [1, 'In disaccordo'],
        [2, 'Abbastanza in disaccordo'],
        [3, 'Né in accordo né in disaccordo'],
        [4, 'Abbastanza in accordo'],
        [5, 'In accordo'],
        [6, 'Fortemente in accordo']
    ], widget=widgets.RadioSelect, label="Rispetto all'interazione faccia a faccia, in videoconferenze tendo a non condividere un'idea o un'opinione perché sono preoccupato di cosa ne penserebbero gli altri.")

    evaluative_threat2 = models.IntegerField(choices=[
        [0, 'Fortemente in disaccordo'],
        [1, 'In disaccordo'],
        [2, 'Abbastanza in disaccordo'],
        [3, 'Né in accordo né in disaccordo'],
        [4, 'Abbastanza in accordo'],
        [5, 'In accordo'],
        [6, 'Fortemente in accordo']
    ], widget=widgets.RadioSelect, label="Mi sento più osservato o giudicato dagli altri in videoconferenza rispetto all'interazione faccia a faccia.")

    verbal_dominance_for_women = models.IntegerField(choices=[
        [0, 'Fortemente in disaccordo'],
        [1, 'In disaccordo'],
        [2, 'Abbastanza in disaccordo'],
        [3, 'Né in accordo né in disaccordo'],
        [4, 'Abbastanza in accordo'],
        [5, 'In accordo'],
        [6, 'Fortemente in accordo']
    ], widget=widgets.RadioSelect, label="Rispetto all'interazione faccia a faccia, gli uomini tendono a dominare la conversazione più delle donne in videoconferenze.")

    verbal_dominance_for_men = models.IntegerField(choices=[
        [0, 'Fortemente in disaccordo'],
        [1, 'In disaccordo'],
        [2, 'Abbastanza in disaccordo'],
        [3, 'Né in accordo né in disaccordo'],
        [4, 'Abbastanza in accordo'],
        [5, 'In accordo'],
        [6, 'Fortemente in accordo']
    ], widget=widgets.RadioSelect, label="Rispetto all'interazione faccia a faccia, le donne tendono a dominare la conversazione più degli uomini in videoconferenze.")

    open_comment = models.LongStringField(label= "Se vuoi, puoi lasciare un commento qui sotto.")

    _num_tasks_correct = models.IntegerField(default=0)
    _num_tasks_total = models.IntegerField(default=0)
    def set_payoff(self):
        self.payoff = self.num_tasks_correct(page_name='WorkPage') * self.session.config.get('stage1_fee', 0)
        self.participant.vars['stage1payoff'] = self.payoff

    def live_ret(self, data):
        answer = data.get('answer')
        if answer:
            old_task = self.get_or_create_task()
            old_task.answer = answer
            old_task.save()
            new_task = self.get_or_create_task()
            resp = {'task_body': new_task.html_body,
                    'num_tasks_correct': self.num_tasks_correct(),
                    'num_tasks_total': self.num_tasks_total(),
                    'correct_answer': new_task.correct_answer
                    }

            return {self.id_in_group: resp}

    def get_current_page_name(self):
        
        lookup = get_page_lookup(self.participant._session_code, self.participant._index_in_pages)
        return lookup.page_class.__name__

    def get_tasks_by_page(self, page_name=None):
        page_name = page_name or self.get_current_page_name()
        return self.tasks.filter(page_name=page_name)


    def num_tasks_correct(self, page_name=None):
        """returns total number of tasks to which a player provided a correct answer"""
        page_name = page_name or self.get_current_page_name()
        return self.get_tasks_by_page(page_name=page_name).filter(correct_answer=F('answer')).count()


    def num_tasks_total(self, page_name=None):
        """returns total number of tasks to which a player provided an answer"""
        page_name = page_name or self.get_current_page_name()
        return self.get_tasks_by_page(page_name=page_name).filter(answer__isnull=False, ).count()

    def get_or_create_task(self):
        """
            checks if there are any unfinished (with no answer) tasks. If yes, we return the unfinished
            task. If there are no uncompleted tasks we create a new one using a task-generating function from session settings
        """

        page_name = self.get_current_page_name()
        app_name = self._meta.app_label
        try:
            last_one = self.tasks.filter(page_name=page_name).latest()

            nlast = last_one.in_player_counter
        except ObjectDoesNotExist:
            nlast = 0

        try:
            task = self.tasks.get(answer__isnull=True, page_name=page_name)
        except ObjectDoesNotExist:
            fallback_fun = getattr(ret_functions, self.session.config['task'])
            fallback_params = { 'task_params': {'difficulty': 5},}
            params = self.session.vars.get('task_params', fallback_params)
            params['seed'] = app_name + page_name + str(self.round_number) +str(nlast)
            fun = self.session.vars.get('task_fun', fallback_fun)
            proto_task = fun(**params)

            task = self.tasks.create(player=self,
                                     body=proto_task.body,
                                     html_body=proto_task.html_body,
                                     correct_answer=proto_task.correct_answer,
                                     task_name=proto_task.name,
                                     in_player_counter=nlast + 1,
                                     app_name=app_name,
                                     page_name=page_name)

        return task

# This is a custom model that contains information about individual tasks. In each round, each player can have as many
# tasks as they tried to solve (we can call for the set of all tasks solved by a player by calling for instance
# player.tasks.all()
# Each task has a body field, html_body - actual html code shown at each page, correct answer and an answer provided by
# a player. In addition there are two automatically updated/created fields that track time of creation and of an update
# These fields can be used to track how long each player works on each task
class Task(djmodels.Model):
    class Meta:
        ordering = ['-created_at']
        get_latest_by = 'in_player_counter'

    player = djmodels.ForeignKey(to=Player, related_name='tasks', on_delete=djmodels.CASCADE)
    body = models.LongStringField()
    html_body = models.LongStringField()
    correct_answer = models.StringField()
    answer = models.StringField(null=True)
    page_name = models.StringField()
    app_name = models.StringField()
    created_at = djmodels.DateTimeField(auto_now_add=True)
    updated_at = djmodels.DateTimeField(auto_now=True)
    task_name = models.StringField()
    in_player_counter = models.IntegerField(default=0)

    # the following method creates a new task, and requires as an input a task-generating function and (if any) some
    # parameters fed into task-generating function.
    @classmethod
    def create(cls, player, fun, **params):
        proto_task = fun(**params)
        task = cls(player=player,
                   body=proto_task.body,
                   html_body=proto_task.html_body,
                   correct_answer=proto_task.correct_answer,
                   task_name = proto_task.name)
        return task
