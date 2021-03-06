from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vision_api import views

urlpatterns = [
    path('user/exists', views.VisionUserExists.as_view()),
    path('user/<slug:usr>', views.VisionUsers.as_view()),
    path('users', views.AllVisionUsers.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)