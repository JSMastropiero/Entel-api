from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.models import User

class TypeOfUserViewSet(viewsets.ModelViewSet):
    queryset = TypeOfUser.objects.all()
    serializer_class = TypeOfUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class TypeOfStatusViewSet(viewsets.ModelViewSet):
    queryset = TypeOfStatus.objects.all()
    serializer_class = TypeOfStatusSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusChangeLogViewSet(viewsets.ModelViewSet):
    queryset = StatusChangeLog.objects.all()
    serializer_class = StatusChangeLogSerializer

class IncidenceViewSet(viewsets.ModelViewSet):
    queryset = Incidence.objects.all()
    serializer_class = IncidenceSerializer

class FranchiseViewSet(viewsets.ModelViewSet):
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer