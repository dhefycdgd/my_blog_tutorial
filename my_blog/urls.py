"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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



#from django.conf.urls import include
from article import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/', views.home),         #kaiguan
    path('detail/', views.detail),
    #path('test/', views.test),
    path('home/', views.home),
]



"""
urlpatterns = patterns[
	url(r'^admin/',include(admin.site.urls)),
	url(r'^$', article.views.home),
]
"""




"""
#from django.conf.urls import include, url

from django.contrib import admin
urlpatterns = patterns('',
# Examples:
# url(r'^$', 'my_blog.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
url(r'^admin/', include(admin.site.urls)),
url(r'^$', 'article.views.home'), #由于目前只有一个app, 方便起见, 就不设置include了
)
"""
