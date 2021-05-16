
from django.contrib import admin
from django.urls import path
# from .views import home_view, tweet_view, tweet_delete_view, tweet_list_view, tweet_detail_view, tweet_create_view, tweet_action_view
from .views import *

urlpatterns = [
    path('imageupload/', AugmentImageView.as_view(), name='upload_image'),
    # path('action/', tweet_action_view),  # Dynamic Routing
    # path('create/', tweet_create_view),  # Dynamic Routing
    # path('<int:tweet_id>/', tweet_detail_view),  # Dynamic Routing
    # path('<int:tweet_id>/delete/',
    #      tweet_delete_view),  # Dynamic Routing
]
