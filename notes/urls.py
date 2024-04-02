from django.urls import path, include
from rest_framework import routers
from notes import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteView, 'notes')

urlpatterns = [
    path("notes/", include(router.urls))
]