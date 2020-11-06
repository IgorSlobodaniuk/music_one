from django.db import models

IN_PROGRESS = 'in_progress'
FINISHED = 'finished'
NOT_STARTED = 'not_started'

SEMESTER_STATUS = (
    (IN_PROGRESS, IN_PROGRESS),
    (FINISHED, FINISHED),
    (NOT_STARTED, NOT_STARTED),
)


class Semester(models.Model):
    status = models.CharField(choices=SEMESTER_STATUS, max_length=11)
    year = models.IntegerField(max_length=4)
    number = models.IntegerField(
        max_length=2,
        choices=((1, 1), (2, 2))
    )
    start = models.DateField()
    finish = models.DateField()
