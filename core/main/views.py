from . import serializers, models
from rest_framework import generics

class CategoryList(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CostumerList(generics.ListAPIView):
    queryset = models.Costumer.objects.all()
    serializer_class = serializers.CostumerSerializer

class ProductList(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductDetailRetrieve(generics.RetrieveAPIView):
    queryset = models.ProductDetail.objects.all()
    serializer_class = serializers.ProductDetailSerializer

class ProductDetailList(generics.ListAPIView):
    queryset = models.ProductDetail.objects.all()
    serializer_class = serializers.ProductDetailSerializer

class PetsList(generics.ListAPIView):
    queryset = models.Pets.objects.all()
    serializer_class = serializers.PetsSerializer

class PetKnowledgeList(generics.ListAPIView):
    queryset = models.PetKnowledge.objects.all()
    serializer_class = serializers.PetKnowledgeSerializer

class SellerList(generics.ListAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer