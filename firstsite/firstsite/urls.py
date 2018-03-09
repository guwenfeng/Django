from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles


urlpatterns = [
    url(r'', include("learn.urls")),
    url(r'', include("sale.urls")),

]
urlpatterns += staticfiles_urlpatterns()