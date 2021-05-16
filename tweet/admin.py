from django.contrib import admin
# from .models import Tweet, TweetLike, User
# from .models import User
from .models import ImageUpload
# Register your models here.


# class TweetLikeAdmin(admin.TabularInline):
#     model = TweetLike


# class TweetAdmin(admin.ModelAdmin):
#     inlines = [TweetLikeAdmin]
#     list_display = ['__str__', 'user']
#     search_fields = ['user__username', 'user__email']

#     class Meta:
#         model = Tweet
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'password']

#     class Meta:
#         model = User
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'image_name',
        'object_name',
        'x_min',
        'x_max',
        'y_min',
        'y_max',
        'image_path',
        'xml_path',
        'timestamp',
    ]

    class Meta:
        model = ImageUpload


# admin.site.register(Tweet, TweetAdmin)
# admin.site.register(User, UserAdmin)
admin.site.register(ImageUpload, ImageAdmin)
