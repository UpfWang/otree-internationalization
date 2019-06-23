from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group =None
    num_rounds = 1

    instructions_template = 'demographics/Instructions.html'




class Subsession(BaseSubsession):
   pass

class Group(BaseGroup):
   pass

class Player(BasePlayer):
    age = models.IntegerField()
    gender = models.StringField(
        choices=['Masculino','Femenino'],
        widget=widgets.RadioSelect
    )
    major=models.StringField(
        choices=[
            'Ciencias de la salud y de la vida',
            'Ciencias políticas y sociales',
            'Comunicación',
            'Derecho',
            'Economía y empresa',
            'Humanidades',
            'Ingenierías',
            'Traducción y ciencias del lenguaje',
            'Interdisciplinarios',
            'Grados simultáneos',
            'Grados de centros adscritos',
            'Grado Abierto UPF',
            'Ninguno de los anteriores'
        ]
    )
    studyyear=models.IntegerField()
    experiencegeneral=models.IntegerField()
    experiencespecific = models.IntegerField()
    nationality = models.StringField(
        choices=['España', 'Otro pais'],
        widget=widgets.RadioSelect
    )

