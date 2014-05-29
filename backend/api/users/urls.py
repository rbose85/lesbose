from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^users/$', view=views.UserListCreate.as_view(), name='users-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        view=views.UserRetrieveUpdateDestroy.as_view(), name='users-detail'),
]
