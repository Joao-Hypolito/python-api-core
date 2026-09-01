from django.contrib import admin
from django.urls import path
from students.views import StudentCreateListView, StudentRetrieveUpdateDestroy
from teachers.views import TeacherCreateListView, TeacherRetrieveUpdateDestroy
from courses.views import CourseCreateListView, CourseRetrieveUpdateDestroy
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentCreateListView.as_view(), name='student-create-list'),
    path('students/<int:pk>', StudentRetrieveUpdateDestroy.as_view(), name='student-detail-view'),
    path('teachers/', TeacherCreateListView.as_view(), name='teacher-create-list'),
    path('teachers/<int:pk>', TeacherRetrieveUpdateDestroy.as_view(), name='teacher-detail-view'),
    path('courses/', CourseCreateListView.as_view(), name='course-create-list'),
    path('courses/<int:pk>', CourseRetrieveUpdateDestroy.as_view(), name='course-details-view'),
    path('authentication/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]