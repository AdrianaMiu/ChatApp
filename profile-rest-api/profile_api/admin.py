from django.contrib import admin

from profile_api import models

# Register your models here.
admin.site.register(models.UserProfile) #inregistarea modelului profilului de util cu admin
admin.site.register(models.ProfileFeedItem)