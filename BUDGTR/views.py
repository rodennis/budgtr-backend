from rest_framework import viewsets
from .serializers import MonthSerializer, BillSerializer
from .models import Month, Bill

# Create your views here.

class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer
    # auth goes here

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    # auth goes here