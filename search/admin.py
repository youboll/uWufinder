from django.contrib import admin
from search.models import user
# Register your models here.
class user_admin(admin.ModelAdmin):
	pass
admin.site.register(user,user_admin)