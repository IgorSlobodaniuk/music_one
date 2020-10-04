from django.db import models

from main.models.user_info import MusicOneUser
from education.models.quest_structure import (
    EducationLevel,
    QuestGroup,
    Quest
)


class IGTVMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    level = models.ForeignKey(
        EducationLevel,
        on_delete=models.PROTECT
    )
    value = models.PositiveIntegerField()


class StoryMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    level = models.ForeignKey(
        EducationLevel,
        on_delete=models.PROTECT
    )
    value = models.PositiveIntegerField()


class LevelExamMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    level = models.ForeignKey(
        EducationLevel,
        on_delete=models.PROTECT
    )
    value = models.PositiveIntegerField()


class TestMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    quest_group = models.ForeignKey(
        QuestGroup,
        on_delete=models.PROTECT
    )
    value = models.PositiveIntegerField()


class QuestResult(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    quest = models.ForeignKey(
        Quest,
        on_delete=models.PROTECT
    )
    status_mark = models.BooleanField()
