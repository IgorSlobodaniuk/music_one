from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from education.models.semester import Semester, IN_PROGRESS
from main.models.user_info import MusicOneUser, STUDENT
from core.services.registry import ServiceRegistry

from education.models.card_ordering import CardOrdering

from education.models.quest_structure import (
    LEVEL_EXAM,
    GROUP_TEST,
    QUEST,
)


from education.models.user_education_status import UserEducationStatus
from education.models.quest_structure import (
    LevelExam,
    GroupTest,
    Quest,
)


CARD_OBJ = {
    LEVEL_EXAM: LevelExam,
    GROUP_TEST: GroupTest,
    QUEST: Quest
}

CARD_OBJ_SERIALIZER = {
    LEVEL_EXAM: LevelExam,
    GROUP_TEST: GroupTest,
    QUEST: Quest
}

from education.api.serializers.mark_serializer import (
    QuestMarkSerializer,
    TestMarkSerializer,
    LevelExamMarkSerializer,
)

MARK_SERIALIZERS = {
    LEVEL_EXAM: LevelExamMarkSerializer,
    GROUP_TEST: TestMarkSerializer,
    QUEST: QuestMarkSerializer
}


class CardPermissionMixin(permissions.BasePermission):
    def has_permission(self, request, view):
        is_allow = True
        user = request.user
        if user.role != STUDENT or user.is_active:
            is_allow = False
        if self.check_started_semester() is False:
            is_allow = False
        return is_allow

    @staticmethod
    def check_started_semester():
        try:
            return Semester.objects.get(status=IN_PROGRESS).exists()
        except Semester.DoesNotExist:
            return False


class UserCardView(APIView, CardPermissionMixin):
    permission_classes = (CardPermissionMixin,)
    service = ServiceRegistry.education_service()

    def get(self, request, *args, **kwargs):
        current_card_id = self.service.get_current_card_id(user=request.user)
        current_card_type = CardOrdering.objects.get(card_id=current_card_id).card_type
        card_data = self.service.get_all_questions_by_card(current_card_id, current_card_type)
        return Response(card_data)

    def post(self, request, *args, **kwargs):
        data = request.data
        card_object_data = self.service.test_checker(data=data, user=request.user)
        serializer = MARK_SERIALIZERS[data['type']](data=card_object_data)
        serializer.is_valid()
        serializer.save()
