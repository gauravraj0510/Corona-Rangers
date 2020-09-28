from rest_framework import serializers
#from rest_framework.renders import JSONRenderer
from blog.models import Post,Donation


# class PostSerializer(serializers.Serializers):
#     id= serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length = 100)
#     content = serializers.TextField()
#     date_posted = serializers.DateTimeField(default=timezone.now)
#     author = serializers.ForeignKey(User, on_delete=models.CASCADE)
#     category = serializers.CharField(max_length = 100, default='ventilator')



class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [ 'title', 'content',  'date_posted', 'author','category']


class DonationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Donation
		fields = [ 'receiver', 'donor',  'quantity', 'category','date_posted']		