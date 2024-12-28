from django.contrib import admin
from .models import (
    PrimaryProfile,
    Photos,
    SecondaryProfile,
    Lifestyle,
    Interests,
    PartnerPreference,
)


# Registering Primary Profile model
@admin.register(PrimaryProfile)
class PrimaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number",
        "dob",
        "gender",
        "height",
        "education",
        "occupation",
        "occupation_sector",
        "monthly_income",
    )
    search_fields = (
        "user__username",
        "phone_number",
        "gender",
        "occupation",
        "occupation_sector",
    )
    list_filter = ("gender", "occupation_sector")


# Registering Photos model
@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ("user", "profile_picture", "pic1", "pic2", "pic3")
    search_fields = ("user__username",)


# Registering Secondary Profile model
@admin.register(SecondaryProfile)
class SecondaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "nationality",
        "religion",
        "caste",
        "mother_tongue",
        "known_languages",
        "marital_status",
    )
    search_fields = ("user__username", "nationality", "religion", "caste")
    list_filter = ("marital_status",)


# Registering Lifestyle model
@admin.register(Lifestyle)
class LifestyleAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "smoking",
        "drinking",
        "dietary_preference",
        "fitness_level",
        "sleep_schedule",
        "social_media_habits",
    )
    search_fields = ("user__username", "smoking", "drinking")
    list_filter = ("smoking", "drinking", "dietary_preference")


# Registering Interests model
@admin.register(Interests)
class InterestsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "favorite_music_genres",
        "favorite_movies",
        "favorite_books",
        "sports",
        "travel_destinations",
    )
    search_fields = ("user__username", "favorite_music_genres", "favorite_movies")
    list_filter = ("sports",)


# Registering Partner Preference model
@admin.register(PartnerPreference)
class PartnerPreferenceAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "age_range",
        "height_range",
        "occupation",
        "occupation_sector",
        "monthly_income_range",
        "nationality_preference",
        "religion_preference",
        "caste_preference",
        "smoking_preference",
        "drinking_preference",
        "dietary_preference",
        "social_media_habits",
    )
    search_fields = ("user__username", "age_range", "nationality_preference")
    list_filter = ("smoking_preference", "drinking_preference", "dietary_preference")
