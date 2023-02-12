from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.getUser.as_view(), name="User"),
    # path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', views.RegisterView.as_view(), name='auth_register'),
]