from django.db import models
from django.contrib.auth.models import AbstractUser


class MusicOneUser(AbstractUser):
    pass


class EducationLevels(models.Model):
    name = models.CharField()


class StudentsRating(models.Model):
    student = models.ForeignKey(MusicOneUser, on_delete=models.CASCADE)
    education_level = models.ForeignKey(EducationLevels, on_delete=models.CASCADE)
