from rest_framework import viewsets, permissions
from .models import PatientRecord, Department
from .serializers import PatientRecordSerializer, DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class PatientRecordViewSet(viewsets.ModelViewSet):
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Doctors').exists():
            return PatientRecord.objects.filter(department__doctor = user)
        return PatientRecord.objects.filter(patient=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.groups.filter(name='Doctors').exists():
            serializer.save()
        else:
            serializer.save(patient=user)




