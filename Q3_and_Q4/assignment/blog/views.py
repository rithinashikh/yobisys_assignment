from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import status

class BlogPostAPIView(APIView):
    # Apply throttling
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        posts = BlogPost.objects.all()
        if not posts:
            return Response({"message": "No posts available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogPostSerializer(posts, many=True)
        return Response({
            "message": "Blog posts fetched successfully",
            "posts": serializer.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)