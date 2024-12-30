from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    PrimaryProfile,
    Photos,
    SecondaryProfile,
    Lifestyle,
    Interests,
    PartnerPreferences,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    primary_profile = serializers.HyperlinkedRelatedField(
        view_name="primaryprofile-detail", read_only=True
    )
    secondary_profile = serializers.HyperlinkedRelatedField(
        view_name="secondaryprofile-detail", read_only=True
    )
    photos = serializers.HyperlinkedRelatedField(
        view_name="photos-detail", read_only=True
    )
    lifestyle = serializers.HyperlinkedRelatedField(
        view_name="lifestyle-detail", read_only=True
    )
    interests = serializers.HyperlinkedRelatedField(
        view_name="interests-detail", read_only=True
    )
    partner_preferences = serializers.HyperlinkedRelatedField(
        view_name="partnerpreferences-detail", read_only=True
    )

    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "primary_profile",
            "secondary_profile",
            "photos",
            "lifestyle",
            "interests",
            "partner_preferences",
        ]


class PrimaryProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = PrimaryProfile
        fields = "__all__"


class SecondaryProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = SecondaryProfile
        fields = "__all__"


class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = Photos
        fields = "__all__"


class LifestyleSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = Lifestyle
        fields = "__all__"


class InterestsSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = Interests
        fields = "__all__"


class PartnerPreferencesSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = PartnerPreferences
        fields = "__all__"
