# myApp/urls.py

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('index/', views.index, name="index"),
    path('post/', views.post, name="post"),
    path('dev/', views.dev, name="dev"),
    path('detail/<int:post_id>/', views.detail, name="detail"),
    path('update/<int:post_id>', views.update, name="update"),
    path('delete/<int:post_id>', views.delete, name="delete"),
    path('c_post/<int:post_id>', views.c_post, name="c_post"),
    path('c_post/<int:post_id>/<int:comment_id>', views.c_delete, name="c_delete"),
    path('like', views.like, name='like'),
    path('search', views.search, name='search'),
    path('explore/tags/<str:tag>/', views.search, name='search'),   
    path('explore/tags_2/<str:tag_2>/', views.search, name='search'),   
]