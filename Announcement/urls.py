from django.urls import path
from .views import AnnouncementViewSet

urlpatterns = [
    path('', AnnouncementViewSet.as_view(), name='announcement-list'),
    path('/<int:pk>/', AnnouncementViewSet.as_view(), name='announcement-detail'),
]