# from rest_framework import serializers
# from .models import Address, AppUser, CustomerRelationship, OptimizedAppUser, OptimizedCustomerRelationship


# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = '__all__'


# class CustomerRelationshipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerRelationship
#         fields = '__all__'


# class AppUserSerializer(serializers.ModelSerializer):
#     address = AddressSerializer(read_only=True)
#     customerrelationship = serializers.SerializerMethodField()

#     class Meta:
#         model = AppUser
#         fields = '__all__'

#     def get_customerrelationship(self, obj):
#         rel = obj.customerrelationship.first() if hasattr(obj, 'customerrelationship') else None
#         return CustomerRelationshipSerializer(rel).data if rel else None


# class OptimizedAppUserSerializer(serializers.ModelSerializer):
#     address_city = serializers.SerializerMethodField()
#     address_country = serializers.SerializerMethodField()
#     points = serializers.SerializerMethodField()

#     class Meta:
#         model = OptimizedAppUser
#         fields = [
#             'id', 'customer_id', 'first_name', 'last_name',
#             'gender', 'birthday', 'phone_number',
#             'address_city', 'address_country', 'points'
#         ]

#     def get_address_city(self, obj):
#         return getattr(obj.address, 'city', None)

#     def get_address_country(self, obj):
#         return getattr(obj.address, 'country', None)

#     def get_points(self, obj):
#         rel = obj.customerrelationship.first() if hasattr(obj, 'customerrelationship') else None
#         return rel.points if rel else None


from rest_framework import serializers
from .models import Address, AppUser, CustomerRelationship, OptimizedAppUser


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomerRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRelationship
        fields = '__all__'


class AppUserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    customerrelationships = serializers.SerializerMethodField()

    class Meta:
        model = AppUser
        fields = '__all__'

    def get_customerrelationships(self, obj):
        rel = obj.customerrelationships.first() if hasattr(obj, 'customerrelationships') else None
        return CustomerRelationshipSerializer(rel).data if rel else None


class OptimizedAppUserSerializer(serializers.ModelSerializer):
    address_city = serializers.SerializerMethodField()
    address_country = serializers.SerializerMethodField()
    points = serializers.IntegerField()

    class Meta:
        model = OptimizedAppUser
        fields = [
            'id', 'customer_id', 'first_name', 'last_name',
            'gender', 'birthday', 'phone_number',
            'address_city', 'address_country', 'points'
        ]

    def get_address_city(self, obj):
        return getattr(obj.address, 'city', None)

    def get_address_country(self, obj):
        return getattr(obj.address, 'country', None)
