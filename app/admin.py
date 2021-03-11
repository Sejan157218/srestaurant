from django.contrib import admin
from app.models import Addess
from app.models import Slider
from app.models import Recipes
from app.models import About
from app.models import Blog
from app.models import Blocktitle
from app.models import Client
from app.models import Contact
from app.models import Newsletter
# Register your models here.


class Addessadmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'addess', 'date')


class Slideradmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'desc', 'date')


class Recipesadmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date')


class Aboutadmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'desc1', 'desc2', 'date')


class Blogadmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'date')


class Blocktitleadmin(admin.ModelAdmin):
    list_display = ('blocktitle', 'blockdesc', 'date')


class Clientadmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'desc', 'date')


class Contactadmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'date')


class Newsletteradmin(admin.ModelAdmin):
    list_display = ('newsletteremail',)


admin.site.register(Slider, Slideradmin)
admin.site.register(Addess, Addessadmin)
admin.site.register(Recipes, Recipesadmin)
admin.site.register(About, Aboutadmin)
admin.site.register(Blog, Blogadmin)
admin.site.register(Blocktitle, Blocktitleadmin)
admin.site.register(Client, Clientadmin)
admin.site.register(Contact, Contactadmin)
admin.site.register(Newsletter, Newsletteradmin)
