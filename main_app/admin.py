from django.contrib import admin
from .models import *
from main_app.views import *
from newsApp.views import *
# Register your models here.
admin.site.register(News)
admin.site.register(Full_news)
