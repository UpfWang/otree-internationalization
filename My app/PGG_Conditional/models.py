from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
This is a one-period public goods game with 3 players.
"""


class Constants(BaseConstants):
    name_in_url = 'PGG_Conditional'
    players_per_group = 3
    num_rounds = 1

    instructions_template = 'PGG_Conditional/Instructions.html'

    # """Amount allocated to each player"""
    endowment = c(30)
    multiplier = 2
    contribution_increment = c(3)
    contribute_choices = currency_range(0, endowment, contribution_increment)

class Subsession(BaseSubsession):
    def creating_session(self):
         self.get_group_matrix()


def make_field(amount):
        return models.CurrencyField(min=0,max=Constants.endowment,
            doc="""contribution""",
            label='How much would you contribute if your two teammates on average contributed {}?'.format(c(amount))
        )

class Group(BaseGroup):
    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()


    def set_payoffs(self):
        self.total_contribution = sum([p.actual_contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group
        for p in self.get_players():
            p.payoff = (Constants.endowment - p.actual_contribution) + self.individual_share

class Player(BasePlayer):
    teammates_average_contribution = models.CurrencyField()

    actual_contribution = models.CurrencyField()

    # for strategy method, see the make_field function above

    response_0 = make_field(0)
    response_3 = make_field(3)
    response_6 = make_field(6)
    response_9 = make_field(9)
    response_12 = make_field(12)
    response_15 = make_field(15)
    response_18 = make_field(18)
    response_21 = make_field(21)
    response_24 = make_field(24)
    response_27 = make_field(27)
    response_30 = make_field(30)


    def method(self):
        for p in self.get_players():
            p.teammates_average_contribution = sum(
                [self.participant.vars['PGG_Contribution'] for p in self.get_others_in_group()]) / 2
            p.actual_contribution = getattr(self, 'response_{}'.format(
                int(self.teammates_average_contribution)))