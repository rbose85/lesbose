from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
]
