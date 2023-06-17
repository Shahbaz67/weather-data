from django.urls import path, include
from weather_info.views import SummaryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'summary', SummaryViewSet)

urlpatterns = [
    path('', include(router.urls))
]