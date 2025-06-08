# from django.db import models
# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

# # class PatientData(models.Model):
# #     id = models.AutoField(primary_key=True)
# #     radius_mean = models.FloatField()
# #     texture_mean = models.FloatField()
# #     perimeter_mean = models.FloatField()
# #     area_mean = models.FloatField()
# #     smoothness_mean = models.FloatField()
# #     compactness_mean = models.FloatField()
# #     concavity_mean = models.FloatField()
# #     concave_points_mean = models.FloatField()
# #     symmetry_mean = models.FloatField()
# #     fractal_dimension_mean = models.FloatField()
# #     radius_se = models.FloatField()
# #     texture_se = models.FloatField()
# #     perimeter_se = models.FloatField()
# #     area_se = models.FloatField()
# #     smoothness_se = models.FloatField()
# #     compactness_se = models.FloatField()
# #     concavity_se = models.FloatField()
# #     concave_points_se = models.FloatField()
# #     symmetry_se = models.FloatField()
# #     fractal_dimension_se = models.FloatField()
# #     radius_worst = models.FloatField()
# #     texture_worst = models.FloatField()
# #     perimeter_worst = models.FloatField()
# #     area_worst = models.FloatField()
# #     smoothness_worst = models.FloatField()
# #     compactness_worst = models.FloatField()
# #     concavity_worst = models.FloatField()
# #     concave_points_worst = models.FloatField()
# #     symmetry_worst = models.FloatField()
# #     fractal_dimension_worst = models.FloatField()
  
# class PatientData(models.Model):
#     id = models.AutoField(primary_key=True)
#     radius_mean = models.FloatField(null=True, blank=True)
#     texture_mean = models.FloatField(null=True, blank=True)
#     perimeter_mean = models.FloatField(null=True, blank=True)
#     area_mean = models.FloatField(null=True, blank=True)
#     smoothness_mean = models.FloatField(null=True, blank=True)
#     compactness_mean = models.FloatField(null=True, blank=True)
#     concavity_mean = models.FloatField(null=True, blank=True)
#     concave_points_mean = models.FloatField(null=True, blank=True)
#     symmetry_mean = models.FloatField(null=True, blank=True)
#     fractal_dimension_mean = models.FloatField(null=True, blank=True)
#     radius_se = models.FloatField(null=True, blank=True)
#     texture_se = models.FloatField(null=True, blank=True)
#     perimeter_se = models.FloatField(null=True, blank=True)
#     area_se = models.FloatField(null=True, blank=True)
#     smoothness_se = models.FloatField(null=True, blank=True)
#     compactness_se = models.FloatField(null=True, blank=True)
#     concavity_se = models.FloatField(null=True, blank=True)
#     concave_points_se = models.FloatField(null=True, blank=True)
#     symmetry_se = models.FloatField(null=True, blank=True)
#     fractal_dimension_se = models.FloatField(null=True, blank=True)
#     radius_worst = models.FloatField(null=True, blank=True)
#     texture_worst = models.FloatField(null=True, blank=True)
#     perimeter_worst = models.FloatField(null=True, blank=True)
#     area_worst = models.FloatField(null=True, blank=True)
#     smoothness_worst = models.FloatField(null=True, blank=True)
#     compactness_worst = models.FloatField(null=True, blank=True)
#     concavity_worst = models.FloatField(null=True, blank=True)
#     concave_points_worst = models.FloatField(null=True, blank=True)
#     symmetry_worst = models.FloatField(null=True, blank=True)
#     fractal_dimension_worst = models.FloatField(null=True, blank=True)
    
# class Project(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=250)
#     image = models.ImageField(upload_to='portfolio/images/')
#     url = models.URLField(blank=True)

#     def __str__(self):
#         return self.title

# from django.db import models

# class PatientData(models.Model):
#     GENDER_CHOICES = [
#         (0, "Male"),
#         (1, "Female"),
#     ]

#     YES_NO_CHOICES = [
#         (1, "No"),
#         (2, "Yes"),
#     ]

#     id = models.AutoField(primary_key=True)
#     gender = models.IntegerField(choices=GENDER_CHOICES)
#     age = models.IntegerField()
#     smoking = models.IntegerField(choices=YES_NO_CHOICES)
#     yellow_fingers = models.IntegerField(choices=YES_NO_CHOICES)
#     anxiety = models.IntegerField(choices=YES_NO_CHOICES)
#     peer_pressure = models.IntegerField(choices=YES_NO_CHOICES)
#     chronic_disease = models.IntegerField(choices=YES_NO_CHOICES)
#     fatigue = models.IntegerField(choices=YES_NO_CHOICES)
#     allergy = models.IntegerField(choices=YES_NO_CHOICES)
#     wheezing = models.IntegerField(choices=YES_NO_CHOICES)
#     alcohol_consuming = models.IntegerField(choices=YES_NO_CHOICES)
#     coughing = models.IntegerField(choices=YES_NO_CHOICES)
#     shortness_of_breath = models.IntegerField(choices=YES_NO_CHOICES)
#     swallowing_difficulty = models.IntegerField(choices=YES_NO_CHOICES)
#     chest_pain = models.IntegerField(choices=YES_NO_CHOICES)

#     def __str__(self):
#         return f"Patient {self.id} - Age {self.age}"

# class Project(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=250)
#     image = models.ImageField(upload_to='portfolio/images/')
#     url = models.URLField(blank=True)

#     def __str__(self):
#         return self.title
from django.db import models

# class PatientData(models.Model):
#     GENDER_CHOICES = [
#         (0, "Male"),
#         (1, "Female"),
#     ]

#     YES_NO_CHOICES = [
#         (1, "No"),
#         (2, "Yes"),
#     ]

#     id = models.AutoField(primary_key=True)
#     gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
#     age = models.IntegerField(default=30)

#     smoking = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     yellow_fingers = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     anxiety = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     peer_pressure = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     chronic_disease = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     fatigue = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     allergy = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     wheezing = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     alcohol_consuming = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     coughing = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     shortness_of_breath = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     swallowing_difficulty = models.IntegerField(choices=YES_NO_CHOICES, default=1)
#     chest_pain = models.IntegerField(choices=YES_NO_CHOICES, default=1)

#     def __str__(self):
#         return f"Patient {self.id} - Age {self.age}"
from django.db import models


class PatientData(models.Model):
    GENDER_CHOICES = [
        (0, "Male"),
        (1, "Female"),
    ]

    YES_NO_CHOICES = [
        (1, "No"),
        (2, "Yes"),
    ]

    id = models.AutoField(primary_key=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    age = models.IntegerField(default=30)
    chronic_disease = models.IntegerField(choices=YES_NO_CHOICES, default=1)
    wheezing = models.IntegerField(choices=YES_NO_CHOICES, default=1)
    alcohol_consuming = models.IntegerField(choices=YES_NO_CHOICES, default=1)
    chest_pain = models.IntegerField(choices=YES_NO_CHOICES, default=1)
    smoking = models.IntegerField(choices=YES_NO_CHOICES, default=1)
    yellow_fingers = models.IntegerField(choices=YES_NO_CHOICES, default=1)
    coughing = models.IntegerField(choices=YES_NO_CHOICES, default=1)
    shortness_of_breath = models.IntegerField(choices=YES_NO_CHOICES, default=1)

    def __str__(self):
        return f"Patient {self.id} - Age {self.age}"
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
