from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils import timezone

# from django.utils.text import slugify

# Create your models here.


class Artist(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_year = models.IntegerField(
        validators=[MaxValueValidator(timezone.now().year)], null=True)
    fav_technique = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Martial artists"


class Embodyment(models.Model):
    feature_name = models.CharField(max_length=50, blank=True, null=True)
    event_name = models.CharField(max_length=50, blank=True, null=True)
    cultural_practice_name = models.CharField(
        max_length=50, blank=True, null=True)
    tradition_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.feature_name}"


class Motherland(models.Model):
    name = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    continent = models.CharField(max_length=50, blank=True, null=True)
    official_language = models.CharField(max_length=50, blank=True, null=True)

    embodyment = models.OneToOneField(
        Embodyment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"


class MartialArt(models.Model):
    # id = models.AutoField(primary_key=True) # generates automatically
    name = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    country_of_origin = models.ForeignKey(
        Motherland, on_delete=models.CASCADE, null=True, related_name="martial_arts")
    joint_locks_allowed = models.BooleanField(default=False)

    techniques = models.ManyToManyField('Technique', null=True, blank=True) # originating_martial_art's related name used
                                                     # to avoid NameError because of models' order

    # slugging: Jiu Jitsu --> jiu-jitsu
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("martial-art-detail", args=[self.slug])

    # creating this was for auto creating slug
    # based on "name" but since i moved to django admin
    # administration i set prepopulated_fields= {"slug": ("name", )}
    # which automatically creates slug,
    # it's more efficient and django provides basic validation
    # also considering my validators such as in rating declaration

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name
        # return f"ID:{self.id} {self.name} - {self.rating}*, CO: {self.country_of_origin}"


class Technique(models.Model):

    CLOSE, MIDDLE, LONG = 'close', 'middle', 'long'
    BEGINNER, INTERMEDIATE, ADVANCED, PRO = "Beginner", "Intermediate", "Advanced", "Professional"
    EFFECTIVE_RANGE_CHOICES = [
        (CLOSE, 'Close'), (MIDDLE, 'Middle'), (LONG, 'Long')]
    SKILL_LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'), (INTERMEDIATE, 'Intermediate'), (ADVANCED, 'Advanced'), (PRO, 'Professional')]

    name = models.CharField(max_length=50)
    power_generation = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=20, 
                                   choices=SKILL_LEVEL_CHOICES, default=INTERMEDIATE)
    effective_range = models.CharField(max_length=10, 
                                       choices=EFFECTIVE_RANGE_CHOICES, default=MIDDLE)
    originating_martial_art = models.ForeignKey(
        MartialArt, on_delete=models.CASCADE, null=True, related_name="Technique")

    def __str__(self):
        return f"{self.name}, {self.effective_range}, {self.originating_martial_art}"
