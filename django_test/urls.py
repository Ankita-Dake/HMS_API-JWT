from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientRecordViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'patient-records', PatientRecordViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]