from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnnouncementViewSet, announcement_detail

router = DefaultRouter()
router.register(r'announcements', AnnouncementViewSet, basename='announcement-list')

urlpatterns = [
    path('announcements/<int:pk>/', announcement_detail, name='announcement_detail'),
    path('', include(router.urls)),
]