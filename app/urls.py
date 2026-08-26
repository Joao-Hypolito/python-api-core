from django.contrib import admin
from django.urls import path
from students.views import StudentCreateListView, StudentRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentCreateListView.as_view(), name='student-create-list'),
    path('students/<int:pk>', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail-view'),
]