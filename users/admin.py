from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

#allow admin to set/alter our profile db