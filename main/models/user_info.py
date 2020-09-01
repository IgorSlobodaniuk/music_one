from django.contrib.auth.models import AbstractUser
from django.db import models

STUDENT = 'student'
TEACHER = 'teacher'


class MusicOneUser(AbstractUser):
    ROLE_CHOICES = [
        (STUDENT, STUDENT),
        (TEACHER, TEACHER),
    ]
    instagram = models.URLField(blank=True, null=True)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=STUDENT,
    )

    class Meta:
        verbose_name = 'Music One User'
        verbose_name_plural = 'Music One Users'


class EducationLevel(models.Model):
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    LEVEL_CHOICES = [
        (IN_PROGRESS, 'in_progress'),
        (COMPLETED, 'completed'),
    ]
    level = models.CharField(
        max_length=10,
        choices=LEVEL_CHOICES,
    )
    user = models.OneToOneField(MusicOneUser, on_delete=models.CASCADE)

# class StudentsRating(models.Model):
#     student = models.ForeignKey(MusicOneUser, on_delete=models.CASCADE)
#     education_level = models.ForeignKey(EducationLevels, on_delete=models.CASCADE)
