from django.urls import path
from .views import BlogPostAPIView

urlpatterns = [
    path('blogposts/<int:tenant_id>/', BlogPostAPIView.as_view(), name='blogposts'),
    path('blogposts/', BlogPostAPIView.as_view(), name='create_blogpost'),

]
