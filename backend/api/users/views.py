from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response

from profiles.models import AccountHolder
from . import serializers


class UserListCreate(generics.ListCreateAPIView):
    """
    An api representation of a `User` instance.
    """

    def get_queryset(self):
        user = self.request.user
        return AccountHolder.objects.filter(user=user)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.UserList
        return serializers.UserCreate

    def post(self, request, *args, **kwargs):
        # todo: need to create a new auth User obj, and accountHolder obj
        return super(UserListCreate, self).post(request, *args, **kwargs)


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Amend or suspend the logged-in `User`, mostly relating to authentication.
    """

    def get_queryset(self):
        user = self.request.user
        return AccountHolder.objects.filter(user=user)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.UserRetrieve
        return serializers.UserUpdate

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.UserRetrieve(queryset,
                                              context={'request': request})
        return Response(serializer.data)

        # todo: think about the update, partial update, and destroy actions
