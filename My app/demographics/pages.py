from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Information(Page):
    def vars_for_template(self):
        return {
            'paying_round': self.participant.vars['paying_round'],
            'final_payoff': self.participant.vars['final_payoff']
        }


class demographics(Page):
     form_model = models.Player
     form_fields = ['age', 'gender', 'major', 'studyyear', 'experiencegeneral', 'experiencespecific', 'nationality']

page_sequence = [
    demographics,
    Information
]
