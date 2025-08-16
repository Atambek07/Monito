from django.urls import path
from . import views
from .views import CategoryList, CostumerList
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('category/', CategoryList.as_view(), name='category'),
    path('costumer/', CostumerList.as_view(), name='costumer'),
    path('product/', views.ProductList.as_view(), name='product'),
    path('detail-product/', views.ProductDetailList.as_view(), name='detail-product'),
    path('detail-product/<int:pk>/', views.ProductDetailRetrieve.as_view(), name='detail-product'),
    path('pets/', views.PetsList.as_view(), name='pets'),
    path('sellers/', views.SellerList.as_view(), name='sellers'),
    path('pet-knowledge/', views.PetKnowledgeList.as_view(), name='pet-knowledge'),
]