from django.conf.urls import include, url

urlpatterns = [

    url(r'^v1/', include('api.urls')),

    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
]
