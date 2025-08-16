from rest_framework import serializers
from . import models

class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Costumer
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pets
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = '__all__'

class PetKnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetKnowledge
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductDetail
        fields = '__all__'