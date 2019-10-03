from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'home'),
    path('blogs/', views.blogs, name = 'blogs'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('blogs/<int:blog_id>/', views.detail, name = 'detail'),
    path('blog/project_detail1/', views.project_detail1, name = 'project_detail1'),
    path('blog/project_detail2/', views.project_detail2, name = 'project_detail2'),
    path('blog/project_detail3/', views.project_detail3, name = 'project_detail3'),
]
