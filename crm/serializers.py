from rest_framework import serializers
from .models import Address, AppUser, CustomerRelationship

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
    
class CustomerRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
    
    def get_customerrelationship(self, obj):
        try:
            rel = CustomerRelationship.objects.get(appuser=obj)
            return CustomerRelationshipSerializer(rel).data
        except CustomerRelationship.DoesNotExist:
            return None