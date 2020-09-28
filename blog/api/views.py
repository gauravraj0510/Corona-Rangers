from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


from blog.models import Post,Category, Donation
from blog.api.serializers import PostSerializer, DonationSerializer


class ApiBlogListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthenticated,)
	
	
class ApiDonateListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthenticated,)

	




	

