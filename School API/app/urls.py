from django.contrib import admin
from django.urls import path
from students.views import StudentCreateListView, StudentRetrieveUpdateDestroyView
from teachers.views import TeacherCreateListView, TeacherRetrieveUpdateDestroy
from courses.views import CourseCreateListView, CourseRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentCreateListView.as_view(), name='student-create-list'),
    path('students/<int:pk>', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail-view'),
    path('teachers/', TeacherCreateListView.as_view(), name='teacher-create-list'),
    path('teachers/<int:pk>', TeacherRetrieveUpdateDestroy.as_view(), name='teacher-detail-view'),
    path('courses/', CourseCreateListView.as_view(), name='course-create-list'),
    path('courses/<int:pk>', CourseRetrieveUpdateDestroy.as_view(), name='course-detail-view'),
]