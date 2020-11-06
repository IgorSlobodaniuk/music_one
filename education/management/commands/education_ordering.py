from django.core.management.base import BaseCommand

from education.models.quest_structure import (
    EducationLevel,
    QuestGroup,
    Quest,
)
from education.models.card_ordering import CardOrdering


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for level in EducationLevel.objects.all():
            quest_groups = QuestGroup.objects.filter(level=level).values()
            for group in quest_groups:
                quests = Quest.objects.filter(group=group)
                for quest in quests:
                    quest_obj = CardOrdering.objects.create(card=quest.pk)
                    quest_obj.save()
                group_test_obj = CardOrdering.objects.create(card=group.group.group_test.pk)
                group_test_obj.save()
            level_exam_obj = CardOrdering.objects.create(card=level.level_exam.pk)
            level_exam_obj.save()
