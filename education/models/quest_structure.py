from django.db import models

from main.models.user_info import MusicOneUser


LEVEL_STATUS_CHOISES = (
    ('passed', 'passed'),
    ('current', 'current')
)

QUEST_CHOISES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)




class EducationLevel(models.Model):
    name = models.PositiveIntegerField(
        unique=True
    )
    theory = models.TextField()

    def __str__(self):
        return self.name


class LevelExam(models.Model):
    name = models.CharField(max_length=500)
    level = models.OneToOneField(
        EducationLevel,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class LevelExamVariant(models.Model):
    name = models.CharField(max_length=500)
    level = models.OneToOneField(
        LevelExam,
        on_delete=models.PROTECT
    )

    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name


class QuestGroup(models.Model):
    name = models.PositiveIntegerField()
    level = models.OneToOneField(
        EducationLevel,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class Quest(models.Model):
    name = models.PositiveIntegerField()
    number = models.CharField(max_length=500)
    group = models.OneToOneField(
        QuestGroup,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class GroupTest(models.Model):
    name = models.PositiveIntegerField()
    group = models.OneToOneField(
        QuestGroup,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class GroupTestVariant(models.Model):
    name = models.CharField(max_length=500)
    group = models.OneToOneField(
        GroupTest,
        on_delete=models.PROTECT
    )
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name


class QuestItem(models.Model):
    name = models.CharField(max_length=500)
    quest = models.OneToOneField(
        Quest,
        on_delete=models.PROTECT
    )
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name
