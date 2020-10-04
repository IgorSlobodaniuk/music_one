from django.urls import path


from education.api.views.education_level import LevelView

urlpatterns = [
    path('current_level/', LevelView.as_view(), name='user'),
]
