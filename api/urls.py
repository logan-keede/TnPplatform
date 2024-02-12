'''from django.urls import include, path
from rest_framework import routers
from .views import JSON2pdfViewSet


router = routers.DefaultRouter()
router.register(r'pdfs', JSON2pdfViewSet)

urlpatterns = [
    path('', include(router.urls)),
]'''

from django.urls import path
from .views import JSON2pdfView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('json2pdf/', JSON2pdfView.as_view(), name='json2pdf'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

for static_url in settings.STATICFILES_DIRS:
    urlpatterns += static(static_url, document_root=settings.STATIC_ROOT)