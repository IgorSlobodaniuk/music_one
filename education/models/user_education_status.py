from django.db import models
from main.models.user_info import MusicOneUser
from education.models.card_ordering import CardOrdering


class UserEducationStatus(models.Model):
    user = models.ForeignKey(MusicOneUser, on_delete=models.PROTECT)
    current_card = models.ForeignKey(CardOrdering, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.current_card)
