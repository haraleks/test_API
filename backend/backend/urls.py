from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .tokens import ObtainTokenPair


urlpatterns = [
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),  name='token_refresh'),
    path('log_in/', ObtainTokenPair.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('programs.urls')),
              ]
