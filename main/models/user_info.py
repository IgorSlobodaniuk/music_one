from django.db import models
from django.contrib.auth.models import AbstractUser


class MusicOneUser(AbstractUser):
    pass


class StudentsRating(models.Model):
    student = models.ForeignKey(MusicOneUser, on_delete=models.CASCADE)
    education_level = models.ForeignKey(MusicOneUser, on_delete=models.CASCADE)


class EducationLevels(models.Model):
    name = models.CharField()
