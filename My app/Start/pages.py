from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Information(Page):
    pass



class SessionInstruction(Page):
    pass


page_sequence = [
     Information,
     SessionInstruction
]
