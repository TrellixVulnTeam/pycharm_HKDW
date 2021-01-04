#this folder allows us to add stuff to the admin page
from django.contrib import admin
from .models import Question, Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)