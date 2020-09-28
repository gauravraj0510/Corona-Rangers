from django.urls import path
from blog.api.views import(
	ApiBlogListView,
    ApiDonateListView,
)

app_name = 'blog'

urlpatterns = [
	path('blog/', ApiBlogListView.as_view(), name="detail"),
	path('donate/', ApiDonateListView.as_view(), name="create"),
	
]