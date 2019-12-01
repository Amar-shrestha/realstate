from rest_framework import serializers
from listings.models import Listing
from realtors.models import Realtor



class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('realtor', 'title', 'address', 'city', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size',
                  'photo_main')
        # def validate_rating(self, value):
        # 	if value in range(1, 1000):
        # 		return value
        # 	raise serializers.ValidationError('error detected')



class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = ('name', 'photo', 'description', 'phone', 'email', 'is_mvp', 'hire_date')






        