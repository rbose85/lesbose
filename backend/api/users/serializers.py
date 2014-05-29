from rest_framework import serializers

from profiles.models import AccountHolder


class UserList(serializers.Serializer):
    """
    set of logged-in User related resources
    """

    url = serializers.HyperlinkedIdentityField(view_name='users-detail')

    class Meta:
        fields = ('url', )


class UserCreate(serializers.Serializer):
    """
    set of *minimal* fields to create a new User
    """

    username = serializers.CharField(required=False)
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        fields = ('username', 'email', 'password')
        write_only_fields = ('password', )


class UserRetrieve(serializers.HyperlinkedModelSerializer):
    """
    complete set of logged-in User related info
    """

    url = serializers.HyperlinkedIdentityField(view_name='users-detail')
    email = serializers.EmailField(source='user.email')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = AccountHolder
        exclude = ('user', )


class UserUpdate(serializers.Serializer):
    """
    set of *minimal* fields to create a new User
    """

    username = serializers.CharField()

    class Meta:
        fields = ('username', )
