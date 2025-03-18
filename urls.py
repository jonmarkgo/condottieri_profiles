from django.urls import path, re_path

from condottieri_profiles.views import *

app_name = 'profiles'

urlpatterns = [
	re_path(r'^profile/(?P<username>[\w.@+-]+)$',
		ProfileDetailView.as_view(),
		name='profile_detail'
	),
	path('edit',
		ProfileUpdateView.as_view(),
		name='profile_edit'
	),
	re_path(r'^profile/f/(?P<username>[\w.@+-]+)$',
		ToggleFriendshipView.as_view(),
		name='change_friendship'
	),
]
