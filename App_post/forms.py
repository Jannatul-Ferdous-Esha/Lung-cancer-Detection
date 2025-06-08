# import os
# import pandas as pd
# from django import forms
# from django import forms
# from .models import PatientData

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# csv_path = os.path.join(BASE_DIR, "App_post", "data.csv")  # Updated path

# df = pd.read_csv(csv_path)
# input_columns = [col for col in df.columns if col.lower() != 'diagnosis']

# class CancerPredictionForm(forms.Form):
#     for col in input_columns:
#         locals()[col] = forms.FloatField(label=col.replace("_", " ").title(), required=True)


# class CancerPredictionForm(forms.ModelForm):
#     class Meta:
#         model = PatientData
#         fields = "__all__"  # All fields will be included, but optional

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.required = False  # Make all fields optional
#             field.widget.attrs.update({'class': 'form-control'})

# import os
# import pandas as pd
# from django import forms

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# csv_path = os.path.join(BASE_DIR, "App_post", "data.csv")  # Updated path

# df = pd.read_csv(csv_path)
# input_columns = [col for col in df.columns if col.lower() != 'diagnosis']

# class CancerPredictionForm(forms.Form):
#     # Dynamically create form fields based on CSV columns
#     for col in input_columns:
#         locals()[col] = forms.FloatField(label=col.replace("_", " ").title(), required=True)
# import os
# import pandas as pd
# from django import forms

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# csv_path = os.path.join(BASE_DIR, "App_post", "data.csv")

# df = pd.read_csv(csv_path)
# input_columns = [col for col in df.columns if col.lower() != 'diagnosis']

# class CancerPredictionForm(forms.Form):
#     for col in input_columns:
#         locals()[col] = forms.FloatField(label=col.replace("_", " ").title(), required=True)
# import os
# import pandas as pd
# from django import forms

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# csv_path = os.path.join(BASE_DIR, "App_post", "data.csv")

# # Load and clean only the correct features
# df = pd.read_csv(csv_path)
# df.drop(columns=['id', 'Unnamed: 32'], errors='ignore', inplace=True)
# input_columns = [col for col in df.columns if col != 'diagnosis']  

# class CancerPredictionForm(forms.Form):
#     for col in input_columns:
#         locals()[col] = forms.FloatField(
#             label=col.replace("_", " ").title(),
#             required=True
#         )

# from django import forms

# # Gender: Male = 0, Female = 1
# GENDER_CHOICES = [
#     (0, "Male"),
#     (1, "Female"),
# ]

# # All binary yes/no choices: No = 1, Yes = 2
# YES_NO_CHOICES = [
#     (1, "No"),
#     (2, "Yes"),
# ]

# class LungCancerForm(forms.Form):
#     GENDER = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender", widget=forms.Select(attrs={"class": "form-control"}))
#     AGE = forms.IntegerField(label="Age", widget=forms.NumberInput(attrs={"class": "form-control"}))
#     SMOKING = forms.ChoiceField(choices=YES_NO_CHOICES, label="Smoking", widget=forms.Select(attrs={"class": "form-control"}))
#     YELLOW_FINGERS = forms.ChoiceField(choices=YES_NO_CHOICES, label="Yellow Fingers", widget=forms.Select(attrs={"class": "form-control"}))
#     ANXIETY = forms.ChoiceField(choices=YES_NO_CHOICES, label="Anxiety", widget=forms.Select(attrs={"class": "form-control"}))
#     PEER_PRESSURE = forms.ChoiceField(choices=YES_NO_CHOICES, label="Peer Pressure", widget=forms.Select(attrs={"class": "form-control"}))
#     CHRONIC_DISEASE = forms.ChoiceField(choices=YES_NO_CHOICES, label="Chronic Disease", widget=forms.Select(attrs={"class": "form-control"}))
#     FATIGUE = forms.ChoiceField(choices=YES_NO_CHOICES, label="Fatigue", widget=forms.Select(attrs={"class": "form-control"}))
#     ALLERGY = forms.ChoiceField(choices=YES_NO_CHOICES, label="Allergy", widget=forms.Select(attrs={"class": "form-control"}))
#     WHEEZING = forms.ChoiceField(choices=YES_NO_CHOICES, label="Wheezing", widget=forms.Select(attrs={"class": "form-control"}))
#     ALCOHOL_CONSUMING = forms.ChoiceField(choices=YES_NO_CHOICES, label="Alcohol Consuming", widget=forms.Select(attrs={"class": "form-control"}))
#     COUGHING = forms.ChoiceField(choices=YES_NO_CHOICES, label="Coughing", widget=forms.Select(attrs={"class": "form-control"}))
#     SHORTNESS_OF_BREATH = forms.ChoiceField(choices=YES_NO_CHOICES, label="Shortness of Breath", widget=forms.Select(attrs={"class": "form-control"}))
#     SWALLOWING_DIFFICULTY = forms.ChoiceField(choices=YES_NO_CHOICES, label="Swallowing Difficulty", widget=forms.Select(attrs={"class": "form-control"}))
#     CHEST_PAIN = forms.ChoiceField(choices=YES_NO_CHOICES, label="Chest Pain", widget=forms.Select(attrs={"class": "form-control"}))
# from django import forms

# GENDER_CHOICES = [
#     (0, "Male"),
#     (1, "Female"),
# ]

# YES_NO_CHOICES = [
#     (1, "No"),
#     (2, "Yes"),
# ]

# class BreastCancerForm(forms.Form):
#     GENDER = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender", widget=forms.Select(attrs={"class": "form-control"}))
#     AGE = forms.IntegerField(label="Age", widget=forms.NumberInput(attrs={"class": "form-control"}))
#     SMOKING = forms.ChoiceField(choices=YES_NO_CHOICES, label="Smoking", widget=forms.Select(attrs={"class": "form-control"}))
#     YELLOW_FINGERS = forms.ChoiceField(choices=YES_NO_CHOICES, label="Yellow Fingers", widget=forms.Select(attrs={"class": "form-control"}))
#     ANXIETY = forms.ChoiceField(choices=YES_NO_CHOICES, label="Anxiety", widget=forms.Select(attrs={"class": "form-control"}))
#     PEER_PRESSURE = forms.ChoiceField(choices=YES_NO_CHOICES, label="Peer Pressure", widget=forms.Select(attrs={"class": "form-control"}))
#     CHRONIC_DISEASE = forms.ChoiceField(choices=YES_NO_CHOICES, label="Chronic Disease", widget=forms.Select(attrs={"class": "form-control"}))
#     FATIGUE = forms.ChoiceField(choices=YES_NO_CHOICES, label="Fatigue", widget=forms.Select(attrs={"class": "form-control"}))
#     ALLERGY = forms.ChoiceField(choices=YES_NO_CHOICES, label="Allergy", widget=forms.Select(attrs={"class": "form-control"}))
#     WHEEZING = forms.ChoiceField(choices=YES_NO_CHOICES, label="Wheezing", widget=forms.Select(attrs={"class": "form-control"}))
#     ALCOHOL_CONSUMING = forms.ChoiceField(choices=YES_NO_CHOICES, label="Alcohol Consuming", widget=forms.Select(attrs={"class": "form-control"}))
#     COUGHING = forms.ChoiceField(choices=YES_NO_CHOICES, label="Coughing", widget=forms.Select(attrs={"class": "form-control"}))
#     SHORTNESS_OF_BREATH = forms.ChoiceField(choices=YES_NO_CHOICES, label="Shortness of Breath", widget=forms.Select(attrs={"class": "form-control"}))
#     SWALLOWING_DIFFICULTY = forms.ChoiceField(choices=YES_NO_CHOICES, label="Swallowing Difficulty", widget=forms.Select(attrs={"class": "form-control"}))
#     CHEST_PAIN = forms.ChoiceField(choices=YES_NO_CHOICES, label="Chest Pain", widget=forms.Select(attrs={"class": "form-control"}))

from django import forms

class BreastCancerForm(forms.Form):
    age = forms.IntegerField(label="Age")
    gender = forms.ChoiceField(choices=[(1, "Male"), (2, "Female")], widget=forms.RadioSelect)
    chronic_disease = forms.ChoiceField(choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect)
    wheezing = forms.ChoiceField(choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect)
    alcohol_consuming = forms.ChoiceField(choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect)
    chest_pain = forms.ChoiceField(choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect)
    smoking = forms.ChoiceField(choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect)
    yellow_fingers = forms.ChoiceField(choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect)
    coughing = forms.ChoiceField(choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect)
    shortness_of_breath = forms.ChoiceField(choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect)

from django import forms

GENDER_CHOICES = [
    (0, "Male"),
    (1, "Female"),
]

YES_NO_CHOICES = [
    (1, "No"),
    (2, "Yes"),
]

class BreastCancerForm(forms.Form):
    GENDER = forms.ChoiceField(
        choices=GENDER_CHOICES, 
        label="Gender", 
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
    AGE = forms.IntegerField(
        label="Age", 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    SMOKING = forms.ChoiceField(
        choices=YES_NO_CHOICES, 
        label="Smoking", 
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
    YELLOW_FINGERS = forms.ChoiceField(
        choices=YES_NO_CHOICES, 
        label="Yellow Fingers", 
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
#     ANXIETY = forms.ChoiceField(
#         choices=YES_NO_CHOICES, 
#         label="Anxiety", 
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"})
#     )
#     PEER_PRESSURE = forms.ChoiceField(
#         choices=YES_NO_CHOICES, 
#         label="Peer Pressure", 
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"})
#     )
    CHRONIC_DISEASE = forms.ChoiceField(
        choices=YES_NO_CHOICES, 
        label="Chronic Disease", 
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
#     FATIGUE = forms.ChoiceField(
#         choices=YES_NO_CHOICES, 
#         label="Fatigue", 
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"})
#     )
#     ALLERGY = forms.ChoiceField(
#         choices=YES_NO_CHOICES, 
#         label="Allergy", 
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"})
#     )
    WHEEZING = forms.ChoiceField(
        choices=YES_NO_CHOICES, 
        label="Wheezing", 
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
    ALCOHOL_CONSUMING = forms.ChoiceField(
        choices=YES_NO_CHOICES, 
        label="Alcohol Consuming", 
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
    COUGHING = forms.ChoiceField(
        choices=YES_NO_CHOICES, 
        label="Coughing", 
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
    SHORTNESS_OF_BREATH = forms.ChoiceField(
        choices=YES_NO_CHOICES, 
        label="Shortness of Breath", 
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
#     SWALLOWING_DIFFICULTY = forms.ChoiceField(
#         choices=YES_NO_CHOICES, 
#         label="Swallowing Difficulty", 
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"})
#     )
    CHEST_PAIN = forms.ChoiceField(
        choices=YES_NO_CHOICES, 
        label="Chest Pain", 
        widget=forms.RadioSelect(attrs={"class": "form-check-input"})
    )
# from django import forms

# GENDER_CHOICES = [
#     (0, "Male"),
#     (1, "Female"),
# ]

# YES_NO_CHOICES = [
#     (1, "No"),
#     (2, "Yes"),
# ]

# class BreastCancerForm(forms.Form):
#     AGE = forms.IntegerField(
#         label="Age", 
#         widget=forms.NumberInput(attrs={"class": "form-control"})
#     )
#     CHRONIC_DISEASE = forms.ChoiceField(
#         choices=YES_NO_CHOICES, 
#         label="Chronic Disease", 
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"})
#     )
#     WHEEZING = forms.ChoiceField(
#         choices=YES_NO_CHOICES, 
#         label="Wheezing", 
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"})
#     )
#     ALCOHOL_CONSUMING = forms.ChoiceField(
#         choices=YES_NO_CHOICES, 
#         label="Alcohol Consuming", 
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"})
#     )
#     CHEST_PAIN = forms.ChoiceField(
#         choices=YES_NO_CHOICES, 
#         label="Chest Pain", 
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"})
#     )
