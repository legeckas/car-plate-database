from .models import Plate
from rest_framework import viewsets, permissions
from .serializers import PlateSerializer

class PlateViewSet(viewsets.ModelViewSet):
	queryset = Plate.objects.all()
	permission_classes = [
		permissions.AllowAny
	]

	serializer_class = PlateSerializer