from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth.models import User
from datetime import date
from .choices import (
    Gender,
    Education,
    Occupation,
    MaritalStatus,
    SmokingChoices,
    DrinkingChoices,
    DietaryChoices,
    FitnessChoices,
    SocialMediaHabitsChoices,
)


class PrimaryProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="primary_profile"
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\+?[1-9]\d{1,14}$",
                message="Enter a valid phone number, e.g., +1234567890.",
            )
        ],
        help_text="Phone number in international format (e.g., +1234567890).",
    )
    dob = models.DateField(
        help_text="Enter your date of birth.",
        validators=[
            MinValueValidator(
                limit_value=date(1900, 1, 1), message="DOB must be after 1900."
            ),
        ],
    )

    gender = models.CharField(max_length=10, choices=Gender.choices)
    height = models.IntegerField()

    address = models.TextField(blank=True, null=True)

    height = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(50.0),  # Minimum height of 50 cm
            MaxValueValidator(250.0),  # Maximum height of 250 cm
        ],
        help_text="Enter height in centimeters (e.g., 175.5).",
    )

    education = models.CharField(
        max_length=20,
        choices=Education.choices,
        blank=True,
        null=True,
        help_text="Select your highest level of education.",
    )
    occupation = models.CharField(
        max_length=30, blank=True, null=True, help_text="Enter your occupation."
    )
    occupation_sector = models.CharField(
        max_length=20, choices=Occupation.choices, verbose_name="Occupation Sector"
    )
    monthly_income = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000_000),
        ],
        help_text="Enter your monthly income in integer format.",
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Primary Profile"
        verbose_name_plural = "Primary Profiles"
        ordering = ["user__username"]


class Photos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="photos")
    profile_picture = models.ImageField(upload_to="photos/", blank=True, null=True)
    pic1 = models.ImageField(upload_to="photos/", blank=True, null=True)
    pic2 = models.ImageField(upload_to="photos/", blank=True, null=True)
    pic3 = models.ImageField(upload_to="photos/", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Photos"

    class Meta:
        verbose_name = "Photo"
        ordering = ["user__username"]


class SecondaryProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="secondary_profile"
    )
    nationality = models.CharField(
        max_length=100, verbose_name="Nationality", default="Nepali"
    )
    religion = models.CharField(
        max_length=100, verbose_name="Religion", blank=True, null=True
    )
    caste = models.CharField(
        max_length=100, verbose_name="Caste", blank=True, null=True
    )
    mother_tongue = models.CharField(
        max_length=100, verbose_name="Mother Tongue", default="Nepali"
    )
    known_languages = models.TextField(
        max_length=200,
        verbose_name="Known Languages",
        help_text="List all known languages separated by commas",
        default="Nepali",
    )
    marital_status = models.CharField(
        max_length=10,
        choices=MaritalStatus.choices,
        verbose_name="Marital Status",
        default=MaritalStatus.SINGLE,
    )
    is_planning_foreign = models.BooleanField(
        default=False, verbose_name="Planning to Move Abroad"
    )
    planned_foreign_country = models.CharField(
        max_length=100,
        default=None,
        blank=True,
        null=True,
        verbose_name="Planned Country to Move",
        help_text="Leave blank if not planning to move abroad",
    )
    is_living_in_foreign = models.BooleanField(
        default=False, verbose_name="Living in a Foreign Country"
    )
    living_foreign_country = models.CharField(
        max_length=100,
        default=None,
        blank=True,
        null=True,
        verbose_name="Country Living In",
        help_text="Leave blank if not living in a foreign country",
    )

    def __str__(self):
        return f"{self.user.username}'s Secondary Profile"

    class Meta:
        verbose_name = "Secondary Profile"
        verbose_name_plural = "Secondary Profiles!"
        ordering = ["user__username"]


# Lifestyle Model
class Lifestyle(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="lifestyle_profile"
    )
    smoking = models.CharField(
        max_length=20, choices=SmokingChoices.choices, verbose_name="Smoking Habits"
    )
    drinking = models.CharField(
        max_length=20, choices=DrinkingChoices.choices, verbose_name="Drinking Habits"
    )
    dietary_preference = models.CharField(
        max_length=20, choices=DietaryChoices.choices, verbose_name="Dietary Preference"
    )
    fitness_level = models.CharField(
        max_length=20, choices=FitnessChoices.choices, verbose_name="Fitness Level"
    )
    sleep_schedule = models.CharField(
        max_length=100, verbose_name="Sleep Schedule", blank=True, null=True
    )
    hobbies = models.TextField(
        verbose_name="Hobbies", help_text="List hobbies separated by commas", blank=True
    )
    social_media_habits = models.CharField(
        max_length=20,
        choices=SocialMediaHabitsChoices.choices,
        verbose_name="Social Media Habits",
        help_text="Describe your social media usage habits.",
        default=SocialMediaHabitsChoices.USUAL,
    )

    def __str__(self):
        return f"{self.user.username}'s Lifestyle"


# Interests Model
class Interests(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="interests_profile"
    )
    favorite_music_genres = models.TextField(
        verbose_name="Favorite Music Genres",
        help_text="List genres separated by commas",
        blank=True,
        null=True,
    )
    favorite_movies = models.TextField(
        verbose_name="Favorite Movies", blank=True, null=True
    )
    favorite_books_genres = models.TextField(
        verbose_name="Favorite Books Generes", blank=True, null=True
    )
    favorite_books = models.TextField(
        verbose_name="Favorite Books", blank=True, null=True
    )
    sports = models.TextField(
        verbose_name="Sports Interested In", blank=True, null=True
    )
    travel_destinations = models.TextField(
        verbose_name="Dream Travel Destinations", blank=True, null=True
    )
    social_activities = models.TextField(
        verbose_name="Social Activities Enjoyed", blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username}'s Interests"


# Partner Preference Model
class PartnerPreferences(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="partner_preference"
    )
    age_range = models.CharField(
        max_length=6, verbose_name="Preferred Age Range", help_text="E.g., 25-35"
    )
    height_range = models.CharField(
        max_length=20,
        verbose_name="Preferred Height Range",
        help_text="E.g., 5'2\"-6'0\"",
    )
    occupation = models.CharField(
        max_length=30,
        default="Any",
        help_text="what occupation should your pather have?",
    )
    occupation_sector = models.CharField(
        max_length=20,
        choices=Occupation.choices,
        verbose_name="Occupation Sector Preference",
        default=Occupation.OTHER,
    )
    monthly_income_range = models.CharField(
        max_length=20,
        verbose_name="Preferred Monthly Income Range",
        help_text="E.g., 50,000-1,00,000",
        blank=True,
        null=True,
    )

    nationality_preference = models.CharField(
        max_length=100, verbose_name="Preferred Nationality", default="Nepali"
    )
    religion_preference = models.CharField(
        max_length=100, verbose_name="Preferred Religion", default="Any"
    )
    caste_preference = models.CharField(
        max_length=100, verbose_name="Preferred Caste", default="Any"
    )

    smoking_preference = models.CharField(
        max_length=20,
        choices=SmokingChoices.choices,
        verbose_name="Smoking Habits Preference",
    )
    drinking_preference = models.CharField(
        max_length=20,
        choices=DrinkingChoices.choices,
        verbose_name="Drinking Habits Preference",
    )
    dietary_preference = models.CharField(
        max_length=20, choices=DietaryChoices.choices, verbose_name="Dietary Preference"
    )
    fitness_level_preference = models.CharField(
        max_length=20,
        choices=FitnessChoices.choices,
        verbose_name="Fitness Level Preference",
    )
    interests_overlap = models.BooleanField(
        default=False, verbose_name="Similar Interests Required?"
    )
    location_preference = models.CharField(
        max_length=100, verbose_name="Preferred Patner Location", blank=True, null=True
    )

    is_planning_foreign = models.BooleanField(
        default=False, verbose_name="Planning to Move Abroad"
    )
    planned_foreign_country = models.CharField(
        max_length=100,
        default=None,
        blank=True,
        null=True,
        verbose_name="Planned Country to Move",
        help_text="Leave blank if if not seeking patner who is moving abroad",
    )

    is_living_in_foreign = models.BooleanField(
        default=False, verbose_name="Living in a Foreign Country"
    )
    living_foreign_country = models.CharField(
        max_length=100,
        default=None,
        blank=True,
        null=True,
        verbose_name="Country Living In",
        help_text="Leave blank if not seeking  foreign living partner",
    )
    social_media_habits = models.CharField(
        max_length=20,
        choices=SocialMediaHabitsChoices.choices,
        verbose_name="Social Media Habits",
        help_text="Describe your social media usage habits.",
        default=SocialMediaHabitsChoices.USUAL,
    )

    def __str__(self):
        return f"{self.user.username}'s Partner Preferences"
