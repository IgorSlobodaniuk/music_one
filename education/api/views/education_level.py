from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.user_info import MusicOneUser
from education.models import UserEducation


class LevelView(APIView):

    def get(self, request, *args, **kwargs):

        user = request.user
        if user.role != 'student':
            raise Exception

        queryset = UserEducation.objects.get(user=request.user).values('current_level', 'test_mark')
        return Response(
            data=queryset,
            status=status.HTTP_200_OK
        )
