from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from .views import FoodTypeApiView,CompositionApiView,FoodApiView,CommentApiView

urlpatterns = [

    path('api/v1/foods/',FoodApiView.as_view({'get':'list','post':'create'})),
    path('api/v1/food/<int:pk>/',FoodApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('api/v1/food-types/',FoodTypeApiView.as_view({'get':'list','post':'create'})),
    path('api/v1/food-type/<int:pk>/',FoodTypeApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('api/v1/compositions/',CompositionApiView.as_view({'get':'list','post':'create'})),
    path('api/v1/composition/<int:pk>/',CompositionApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('api/v1/comments/',CommentApiView.as_view({'get':'list','post':'create'})),
    path('api/v1/comment/<int:pk>/',CommentApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('api-auth/', include('rest_framework.urls')),


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('auth/', include('djoser.urls')),
    path('auth/token', include('djoser.urls.authtoken')),

]