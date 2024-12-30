from django.db import models


class Gender(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
    OTHER = "other", "Other"


class Education(models.TextChoices):
    TENTH = "10th", "10th"
    TWELFTH = "12th", "12th"
    GRADUATION = "graduation", "Graduation"
    POST_GRADUATION = "post graduation", "Post Graduation"
    DOCTORATE = "doctorate", "Doctorate"


class Occupation(models.TextChoices):
    GOVERNMENT = "government", "Government"
    PRIVATE = "private", "Private"
    BUSINESS = "business", "Business"
    OTHER = "other", "Other"
    NONE = "None", "None"


class MaritalStatus(models.TextChoices):
    MARRIED = "married", "Married"
    SINGLE = "single", "Single"
    DIVORCED = "divorced", "Divorced"
    WIDOWED = "widowed", "Widowed"


class SmokingChoices(models.TextChoices):
    NEVER = "never", "Never"
    OCCASIONALLY = "occasionally", "Occasionally"
    REGULARLY = "regularly", "Regularly"


class DrinkingChoices(models.TextChoices):
    NEVER = "never", "Never"
    SOCIALLY = "socially", "Socially"
    REGULARLY = "regularly", "Regularly"


class DietaryChoices(models.TextChoices):
    VEGETARIAN = "vegetarian", "Vegetarian"
    NON_VEGETARIAN = "non_vegetarian", "Non-Vegetarian"
    VEGAN = "vegan", "Vegan"
    OTHER = "other", "Other"


class FitnessChoices(models.TextChoices):
    NOT_ACTIVE = "not_active", "Not Active"
    MODERATELY_ACTIVE = "moderately_active", "Moderately Active"
    VERY_ACTIVE = "very_active", "Very Active"


class SocialMediaHabitsChoices(models.TextChoices):
    USUAL = "usual", "Usual"
    ADDICTED = "addicted", "Addicted"
    AVOIDANT = "avoidant", "Avoidant"
    NONE = "none", "None"
