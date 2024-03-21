from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import math

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'word_encryption_trial_TP'
    players_per_group = None
    num_rounds = 1
    timeout_seconds = 120


class Subsession(BaseSubsession):
    # carry on treatment and color assignment from previous app
     def creating_session(self):
        for p in self.get_players():
            p.treatment = p.participant.vars['treatment']
            #p.color=p.participant.vars['color']


class Group(BaseGroup):
   pass


class Player(BasePlayer):
    treatment = models.StringField()
    #color = models.StringField()

    solved_trial = models.IntegerField()
    notSolved_trial = models.IntegerField()
