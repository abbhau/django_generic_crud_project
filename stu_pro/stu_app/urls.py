from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('students/',views.StudentList.as_view(),name='student_url'),
    path('students/create/', views.StudentCreate.as_view(), name='student_create_url'),
    path('students/update/<int:pk>/', views.StudentUpdate.as_view(), name='student_update_url'),
    path('students/delete/<int:pk>/', views.StudentDelete.as_view(), name='student_delete_url'),
    path('login/',LoginView.as_view( template_name = 'stu_app/student_form.html',next_page= '/p1/students/'),name="login"),
    path('logout/',LogoutView.as_view(next_page = '/p1/login/'),name='logout'),
    path('signup/',views.StudentRegister.as_view(),name='signup')
]