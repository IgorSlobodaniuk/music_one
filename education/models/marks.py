from django.db import models

from education.models.quest_structure import (
    EducationLevel,
    QuestGroup,
    Quest,
)
from main.models.user_info import MusicOneUser

MARK_CHOISES = (
    ('igtv', 'igtv'),
    ('story', 'story'),
    ('exam', 'exam'),
)


class TestMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    quest_group = models.ForeignKey(
        QuestGroup,
        on_delete=models.PROTECT
    )
    value = models.IntegerField(default=0)


class QuestResult(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    quest = models.ForeignKey(
        Quest,
        on_delete=models.PROTECT
    )
    value = models.IntegerField(default=0)


class LevelMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    level = models.ForeignKey(
        EducationLevel,
        on_delete=models.PROTECT
    )
    mark = models.IntegerField(default=0)
    type_mark = models.CharField(
        max_length=5,
        choices=MARK_CHOISES,
    )
