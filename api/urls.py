from django.urls import path, include


from .views import (
    UserViewset,
    PrimaryProfileViewSet,
    SecondaryProfileViewSet,
    PhotosViewSet,
    LifestyleViewSet,
    InterestsViewSet,
    PartnerPreferencesViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", UserViewset, basename="user")
router.register("primaryprofile", PrimaryProfileViewSet, basename="primaryprofile")
router.register(
    "secondaryprofile", SecondaryProfileViewSet, basename="secondaryprofile"
)
router.register("photos", PhotosViewSet, basename="photos")
router.register("lifestyle", LifestyleViewSet, basename="lifestyle")
router.register("interests", InterestsViewSet, basename="interests")
router.register(
    "partnerpreferences", PartnerPreferencesViewSet, basename="partnerpreferences"
)

urlpatterns = [path("router/", include(router.urls))]
