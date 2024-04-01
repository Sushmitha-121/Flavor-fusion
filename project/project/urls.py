"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from myrecipe.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getdetails/',getdetails),
    path('formsubmit',login,name='login'),
    path('v1/',recipe,name='v_page'),
    path('c1/',recipe1,name = 'c_page'),
    path('e1/',recipe2,name = 'e_page'),
    path('h/', recipe3, name='h_page'),
    path('index/', index, name='home'),
    path('regsubmit/',regsubmit,name='regsubmit'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('h_detail/<str:rname>/', fun, name='h_detail'),
    path('comment/', comment, name='comment'),
    path('add_comment/<str:recipe_name>/', add_comment, name='add_comment'),
    path('recipe/<str:rname>/', recipe_detail, name='recipe_detail'),

    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

