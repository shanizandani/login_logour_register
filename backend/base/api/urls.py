# from django.urls import path
# from . import views
# from .views import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )


# urlpatterns = [
#     path('', views.getRoutes),
#     path('notes/', views.getNotes),

#     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]





from django.urls import path, include
from . import views
from.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from .views import ForgotPasswordView


urlpatterns = [
    path('', views.getRoutes),
    # path('notes/' , views.getNotes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register_user, name='register'),
    # ----------------------------------
    path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.jwt')),

    path('reset-password/', ForgotPasswordView.as_view(), name='reset-password'),
   
    
]





