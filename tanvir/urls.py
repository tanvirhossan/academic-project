"""tanvir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from tourism.views import travel
from tourism.views import Dhaka
from tourism.views import Barisal
from tourism.views import Rajshahi
from tourism.views import Rangpur
from tourism.views import Khulna
from tourism.views import Sylhet

from tourism.views import Chittagong
from tourism.views import dynamicshow
from tourism.views import showitem
from tourism.views import searchItem

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^travel/', travel, name='travel'),
	url(r'^Dhaka/', Dhaka, name='Dhaka'),
	url(r'^dynamicshow/', dynamicshow, name='dynamicshow'),
	url(r'^showitem/', showitem, name='showitem'),
	url(r'^searchItem/', searchItem, name='searchItem'),
	url(r'^Chittagong/',Chittagong , name='Chittagong'),
	url(r'^Barisal/', Barisal, name='Barisal'),
	url(r'^Rajshahi/',Rajshahi , name='Rajshahi'),
	url(r'^Rangpur/', Rangpur, name='Rangpur'),
	url(r'^Khulna/',Khulna , name='Khulna'),
	url(r'^Sylhet/', Sylhet, name='Sylhet'),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)