import worldbrain.cortex.urls

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'api/', include(worldbrain.cortex.urls, namespace='worldbrain')),
    url(r'^admin/', admin.site.urls),
]
