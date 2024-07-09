from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('search_profile',views.search_profile, name='search_profile'),
    path('profile',views.profile, name='profile'),
    #path('newlineremove',views.newlineremove, name='newlineremove'),
    #path('spaceremove',views.spaceremove, name='spaceremove'),
    #path('charcount',views.charcount, name='charcount'),
]
