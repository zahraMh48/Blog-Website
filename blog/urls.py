from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(), name='blog_list'), #as_view -> create a view from class and become a function (becuase we need a func)
    path('<int:pk>/',views.PostDetailView.as_view(), name='post_detail'),   # the number(int) name is primary key
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]