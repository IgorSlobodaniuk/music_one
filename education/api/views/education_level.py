from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from education.models import EducationLevel


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
