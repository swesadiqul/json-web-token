from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('instructors', InstructorListView.as_view()),
    path('courses', CourseListView.as_view()), 
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'), 
    path('instructors/<int:pk>', InstructorDetailView.as_view(), name='instructor-detail'), 

    # path('auth/login', obtain_auth_token, name='create-token'), 

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]