from blog.api import urls as api_url
from django.urls import path, include
from .views import (PostListView, PostDetailView, PostCreateView,PostUpdateView, PostDeleteView, CategoryView)
from . import views

urlpatterns = [
    
    path('', views.mainhome, name='main-home'),
    path('blogs/', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('category/<str:cats>/', CategoryView, name='category'),
    # path('donate/', views.DonateView, name='donate'),
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('api/', include(api_url)),
]