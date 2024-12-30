from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth.models import User
from .models import (
    PrimaryProfile,
    Photos,
    SecondaryProfile,
    Lifestyle,
    Interests,
    PartnerPreferences,
)
from .serializers import (
    UserSerializer,
    PrimaryProfileSerializer,
    SecondaryProfileSerializer,
    PhotosSerializer,
    LifestyleSerializer,
    InterestsSerializer,
    PartnerPreferencesSerializer,
)


class UserViewset(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# permission not given for now
class PrimaryProfileViewSet(ModelViewSet):
    queryset = PrimaryProfile.objects.all()
    serializer_class = PrimaryProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SecondaryProfileViewSet(ModelViewSet):
    queryset = SecondaryProfile.objects.all()
    serializer_class = SecondaryProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotosViewSet(ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LifestyleViewSet(ModelViewSet):
    queryset = Lifestyle.objects.all()
    serializer_class = LifestyleSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InterestsViewSet(ModelViewSet):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PartnerPreferencesViewSet(ModelViewSet):
    queryset = PartnerPreferences.objects.all()
    serializer_class = PartnerPreferencesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
