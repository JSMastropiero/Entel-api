from rest_framework import serializers
from .models import TypeOfUser, Place, TypeOfStatus, Status, StatusChangeLog, Incidence, Franchise, Store
from django.contrib.auth.models import User

class TypeOfUserSerializer(serializers.ModelSerializer):
   
   
    class Meta:
        model = TypeOfUser
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Place
        fields = '__all__'

class TypeOfStatusSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = TypeOfStatus
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    type_of_status = TypeOfStatusSerializer()

    class Meta:
        model = Status
        fields = '__all__'

class StatusChangeLogSerializer(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = StatusChangeLog
        fields = '__all__'

class IncidenceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    place = PlaceSerializer()
    status = StatusSerializer()
    status_changelog = StatusChangeLogSerializer(many=True)

    
    class Meta:
        model = Incidence
        fields = '__all__'

class FranchiseSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Franchise
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    franchise = FranchiseSerializer()


    class Meta:
        model = Store
        fields = '__all__'


