from django.conf.urls import include, url
from django.contrib import admin
from core import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'simplemooc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
