from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('classbaseview/', views.class_base_view.as_view()),
    path('game/', views.Game.as_view()),
    path('blog/<int:pk>', views.Blog_view.as_view()),
    path('blog_add_view/', views.Blog_add_view.as_view()),
    path('blog_update/<int:pk>', views.BlogUpdateView.as_view()),
    path('blog_delete/<int:pk>', views.BlogUpdateView.as_view()),
    path('check_token', views.CheckToken.as_view()),
    path('login', obtain_auth_token),
    path('', views.hello),
]