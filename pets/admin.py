from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Pet)
admin.site.register(Post)
admin.site.register(Message)


