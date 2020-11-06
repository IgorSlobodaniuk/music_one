from django.db import models
from main.models.user_info import MusicOneUser

from education.models.quest_structure import (
    LEVEL_EXAM,
    GROUP_TEST,
    QUEST,
)

CARD_TYPE_CHOICES = (
    (LEVEL_EXAM, LEVEL_EXAM),
    (GROUP_TEST, GROUP_TEST),
    (QUEST, QUEST),
)


class CardOrdering(models.Model):
    card_id = models.IntegerField()
    card_type = models.CharField(choices=CARD_TYPE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.card_id)
