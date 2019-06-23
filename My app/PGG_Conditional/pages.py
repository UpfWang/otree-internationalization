from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    pass


class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.contribute_choices]

    def before_next_page(self):
        self.player.method()

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Waiting for other participants to make decisions."

class Results(Page):
   pass


page_sequence = [
    Introduction,
    Contribute,
    ResultsWaitPage,
    Results,
]
