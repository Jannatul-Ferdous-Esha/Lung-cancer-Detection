# from django.shortcuts import render
# from django.shortcuts import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.shortcuts import render

# import requests

# from App_post.models import Project 
# @login_required
# def new(request):
#     projects = Project.objects.all()
#     return render(request,'App_post/new.html',context={'title': 'Home Page','projects':projects})


# # COLAB_URL = "YOUR_COLAB_ENDPOINT_HERE"  # Replace with your actual Colab URL

# # # @login_required
# # # def input_page(request):
# # #     if request.method == "POST":
# # #         form = CancerPredictionForm(request.POST)
# # #         if form.is_valid():
# # #             input_data = form.cleaned_data
            
# # #             # Send data to your Colab model
# # #             response = requests.post(COLAB_URL, json=input_data)
# # #             prediction = response.json().get("prediction", "Error")

# # #             return render(request, "input_page.html", {"form": form, "prediction": prediction})
# # #     else:
# # #         form = CancerPredictionForm()

    
# # #     return render(request, "App_post/input_page.html", {"form": form})

# # # # def picture(request):
# # # #     projects = Project.objects.all()
# # # #     return render(request, 'App_post/new.html', {'projects':projects})

# # # from django.shortcuts import render, redirect
# # # from django.contrib.auth.decorators import login_required
# # # import numpy as np
# # # import joblib  # For loading the ML model
# # # from .forms import CancerPredictionForm
# # # from django.shortcuts import HttpResponse

# # # # Load the pre-trained ML model
# # # MODEL_PATH = "App_post/model.pkl"
# # # model = joblib.load(MODEL_PATH)

# # # from django.shortcuts import redirect

# # # @login_required
# # # def input_page(request):
# # #     if request.method == "POST":
# # #         form = CancerPredictionForm(request.POST)
# # #         if form.is_valid():
# # #             # Prepare the input data for prediction
# # #             input_data = np.array([
# # #                 form.cleaned_data.get(field) or 0 for field in form.fields
# # #             ]).reshape(1, -1)

# # #             # Make prediction (0 = benign, 1 = malignant)
# # #             pred = model.predict(input_data)[0]
# # #             prediction = "Malignant" if pred == 1 else "Benign"

# # #             # Redirect to the results page with the prediction value
# # #             return redirect('App_post:results_page', prediction=prediction)

# # #     else:
# # #         form = CancerPredictionForm()

# # #     return render(request, "App_post/input_page.html", {"form": form})

# # @login_required
# # def results_page(request, prediction):
# #     return render(request, "App_post/results_page.html", {"prediction": prediction})
# # from django.shortcuts import render, redirect
# # from django.contrib.auth.decorators import login_required
# # import numpy as np
# # import joblib
# # from .forms import CancerPredictionForm
# # import os
# # import pickle
# # import numpy as np
# # from django.conf import settings
# # from django.shortcuts import render
# # from .forms import InputForm  # Create this form
# # from django.http import HttpResponse
# # # # Load once at module level
# # # MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor', 'model')

# # # with open(os.path.join(MODEL_PATH, 'scaler.pkl'), 'rb') as f:
# # #     scaler = pickle.load(f)

# # # with open(os.path.join(MODEL_PATH, 'model.pkl'), 'rb') as f:
# # #     model = pickle.load(f)
# # # MODEL_PATH = "App_post/model.pkl"
# # # SCALER_PATH = "App_post/scaler.pkl"

# # # model = joblib.load(MODEL_PATH)
# # # scaler = joblib.load(SCALER_PATH)



# # # def predict_view(request):
# # #     prediction = None
# # #     if request.method == 'POST':
# # #         form = InputForm(request.POST)
# # #         if form.is_valid():
# # #             input_data = np.array([[form.cleaned_data[field] for field in form.fields]])
# # #             scaled_data = scaler.transform(input_data)
# # #             result = model.predict(scaled_data)[0]
# # #             prediction = "Malignant" if result == 1 else "Benign"
# # #     else:
# # #         form = InputForm()

# # #     return render(request, 'predictor/form.html', {'form': form, 'prediction': prediction})

# # # @login_required
# # # def input_page(request):
# # #     if request.method == "POST":
# # #         form = CancerPredictionForm(request.POST)
# # #         if form.is_valid():
# # #             # Prepare input
# # #             input_data = np.array([
# # #                 form.cleaned_data.get(field) or 0 for field in form.fields
# # #             ]).reshape(1, -1)

# # #             # 🔍 Debug print
# # #             print("Input shape:", input_data.shape)  # Should be (1, 30)

# # #             # Normalize input
# # #             input_scaled = scaler.transform(input_data)

# # #             # Predict
# # #             prediction = model.predict(input_scaled)[0]
# # #             result = "Malignant" if prediction == 1 else "Benign"

# # #             return redirect('App_post:results_page', prediction=result)
# # #     else:
# # #         form = CancerPredictionForm()

# # #     return render(request, "App_post/input_page.html", {"form": form})
# # from django.shortcuts import render, redirect
# # from django.contrib.auth.decorators import login_required
# # import numpy as np
# # import joblib
# # from .forms import CancerPredictionForm

# # # Load the new model and scaler
# # MODEL_PATH = "App_post/new_model.pkl"  # Update with the correct path
# # SCALER_PATH = "App_post/new_scaler.pkl"  # Update with the correct path

# # model = joblib.load(MODEL_PATH)
# # scaler = joblib.load(SCALER_PATH)

# # @login_required
# # def input_page(request):
# #     if request.method == "POST":
# #         form = CancerPredictionForm(request.POST)
# #         if form.is_valid():
# #             # Prepare input
# #             input_data = np.array([
# #                 form.cleaned_data.get(field) or 0 for field in form.fields
# #             ]).reshape(1, -1)

# #             # Normalize input using the new scaler
# #             input_scaled = scaler.transform(input_data)

# #             # Make prediction using the newly trained model
# #             prediction = model.predict(input_scaled)[0]
# #             result = "Malignant" if prediction == 1 else "Benign"

# #             return redirect('App_post:results_page', prediction=result)
# #     else:
# #         form = CancerPredictionForm()

# #     return render(request, "App_post/input_page.html", {"form": form})

# # @login_required
# # def results_page(request, prediction):
# #     return render(request, "App_post/results_page.html", {"prediction": prediction})
# import numpy as np
# import joblib
# from django.shortcuts import render, redirect

# from django.shortcuts import render
# from django.shortcuts import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.shortcuts import render

# import requests

# # # Load the new model and scaler
# # MODEL_PATH = "App_post/new_model.pkl"  # Update with the correct path
# # SCALER_PATH = "App_post/new_scaler.pkl"  # Update with the correct path

# # model = joblib.load(MODEL_PATH)
# # scaler = joblib.load(SCALER_PATH)

# # @login_required
# # def input_page(request):
# #     if request.method == "POST":
# #         form = CancerPredictionForm(request.POST)
# #         if form.is_valid():
# #             # Prepare input data
# #             input_data = np.array([
# #                 form.cleaned_data.get(field) or 0 for field in form.fields
# #             ]).reshape(1, -1)

# #             # Debugging: Print the input data
# #             print("Input Data:", input_data)

# #             # Normalize input using the new scaler
# #             input_scaled = scaler.transform(input_data)

# #             # Debugging: Print the scaled input data
# #             print("Scaled Input Data:", input_scaled)

# #             # Make prediction using the newly trained model
# #             prediction = model.predict(input_scaled)[0]

# #             # Debugging: Print the prediction result
# #             print("Prediction:", prediction)

# #             result = "Malignant" if prediction == 1 else "Benign"

# #             return redirect('App_post:results_page', prediction=result)
# #     else:
# #         form = CancerPredictionForm()

# #     return render(request, "App_post/input_page.html", {"form": form})

# # @login_required
# # def results_page(request, prediction):
# #     return render(request, "App_post/results_page.html", {"prediction": prediction})
# import numpy as np
# import joblib
# from django.shortcuts import render, redirect

# from django.conf import settings

# # # Load the new model and scaler
# # MODEL_PATH = "App_post/final_model.pkl"
# # SCALER_PATH = "App_post/final_scaler.pkl"

# # model = joblib.load(MODEL_PATH)
# # scaler = joblib.load(SCALER_PATH)

# # @login_required
# # def input_page(request):
# #     if request.method == "POST":
# #         form = CancerPredictionForm(request.POST)
# #         if form.is_valid():
# #             # Prepare input
# #             input_data = np.array([
# #                 form.cleaned_data.get(field) or 0 for field in form.fields
# #             ]).reshape(1, -1)

# #             # Normalize input using the new scaler
# #             input_scaled = scaler.transform(input_data)

# #             # Make prediction using the newly trained model
# #             prediction = model.predict(input_scaled)[0]
# #             result = "Malignant" if prediction == 1 else "Benign"

# #             return redirect('App_post:results_page', prediction=result)
# #     else:
# #         form = CancerPredictionForm()

# #     return render(request, "App_post/input_page.html", {"form": form})
# # import numpy as np
# # import joblib
# # from django.shortcuts import render, redirect
# # from .forms import CancerPredictionForm
# # from django.contrib.auth.decorators import login_required
# # from tensorflow.keras.models import Sequential
# # from tensorflow.keras.layers import Conv1D, Dropout, BatchNormalization, Flatten, Dense

# # # Load model and scaler once
# # MODEL_PATH = "App_post/final_model.pkl"
# # SCALER_PATH = "App_post/final_scaler.pkl"

# # model = joblib.load(MODEL_PATH)
# # scaler = joblib.load(SCALER_PATH)

# # # CNN feature extractor (same architecture as in training)
# # def create_cnn_feature_extractor(input_shape=(30, 1)):
# #     return Sequential([
# #         Conv1D(128, 3, activation='relu', input_shape=input_shape),
# #         BatchNormalization(), Dropout(0.5),
# #         Conv1D(64, 3, activation='relu'),
# #         BatchNormalization(), Dropout(0.5),
# #         Conv1D(32, 3, activation='relu'),
# #         BatchNormalization(), Dropout(0.5),
# #         Flatten(),
# #         Dense(128, activation='relu'),
# #         BatchNormalization(), Dropout(0.5),
# #         Dense(64, activation='relu'),
# #         Dropout(0.5)
# #     ])

# # feature_extractor = create_cnn_feature_extractor()

# # @login_required
# # def input_page(request):
# #     if request.method == "POST":
# #         form = CancerPredictionForm(request.POST)
# #         if form.is_valid():
# #             # Step 1: Extract raw form data
# #             input_data = np.array([form.cleaned_data[field] or 0 for field in form.fields]).reshape(1, -1)  # (1, 30)

# #             # Step 2: Scale the input
# #             input_scaled = scaler.transform(input_data)  # (1, 30)

# #             # Step 3: Reshape for CNN
# #             input_reshaped = input_scaled.reshape((1, 30, 1))  # (1, 30, 1)

# #             # Step 4: Extract CNN features
# #             extracted_features = feature_extractor.predict(input_reshaped)  # (1, 64)

# #             # Step 5: Predict
# #             prediction = model.predict(extracted_features)[0]
# #             result = "Malignant" if prediction == 1 else "Benign"

# #             return redirect('App_post:results_page', prediction=result)
# #     else:
# #         form = CancerPredictionForm()

# #     return render(request, "App_post/input_page.html", {"form": form})
# # @login_required
# # def results_page(request, prediction):
# #     return render(request, "App_post/results_page.html", {"prediction": prediction})
# # @login_required
# # def new(request):
# #     projects = Project.objects.all()
# #     return render(request,'App_post/new.html',context={'title': 'Home Page','projects':projects})

# import numpy as np
# import joblib
# from django.shortcuts import render, redirect
# from .forms import LungCancerForm
# from .models import Project
# from django.contrib.auth.decorators import login_required

# # Load model and scaler
# MODEL_PATH = "App_post/final_model.pkl"
# SCALER_PATH = "App_post/final_scaler.pkl"

# model = joblib.load(MODEL_PATH)
# scaler = joblib.load(SCALER_PATH)

# @login_required
# def input_page(request):
#     if request.method == "POST":
#         form = LungCancerForm(request.POST)
#         if form.is_valid():
#             # Extract input features in the correct order
#             input_data = np.array([
#                 form.cleaned_data[field] for field in form.fields
#             ]).reshape(1, -1)  # shape: (1, n_features)

#             # Scale input
#             input_scaled = scaler.transform(input_data)

#             # Predict using model
#             prediction = model.predict(input_scaled)[0]
#             result = "Lung Cancer Detected" if prediction == 2 else "No Lung Cancer"

#             return redirect('App_post:results_page', prediction=result)
#     else:
#         form = LungCancerForm()

#     return render(request, "App_post/input_page.html", {"form": form})

# @login_required
# def results_page(request, prediction):
#     return render(request, "App_post/results_page.html", {"prediction": prediction})

# @login_required
# def new(request):
#     projects = Project.objects.all()
#     return render(request, 'App_post/new.html', context={'title': 'Home Page', 'projects': projects})
import numpy as np
import joblib
from django.shortcuts import render, redirect
from .forms import BreastCancerForm
from .models import PatientData, Project
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from weasyprint import HTML
from django.http import HttpResponse

import os
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Load model and scaler
# Load the pipeline once (globally)
PIPELINE_PATH = "App_post/pipeline.pkl"
pipeline = joblib.load(PIPELINE_PATH)

# @login_required
# def input_page(request):
#     if request.method == "POST":
#         form = BreastCancerForm(request.POST)
#         if form.is_valid():
#             field_order = ['AGE', 'CHRONIC_DISEASE', 'WHEEZING', 'ALCOHOL_CONSUMING', 'CHEST_PAIN']
#             input_data = [form.cleaned_data[field] for field in field_order]
#             input_scaled = pipeline.predict([input_data])[0]

#             result = "Breast Cancer Detected" if input_scaled == 2 else "No Breast Cancer"

#             PatientData.objects.create(
#                 age=form.cleaned_data["AGE"],
#                 chronic_disease=form.cleaned_data["CHRONIC_DISEASE"],
#                 wheezing=form.cleaned_data["WHEEZING"],
#                 alcohol_consuming=form.cleaned_data["ALCOHOL_CONSUMING"],
#                 chest_pain=form.cleaned_data["CHEST_PAIN"]
#             )

#             return redirect('App_post:results_page', prediction=result)
#     else:
#         form = BreastCancerForm()

#     return render(request, "App_post/input_page.html", {"form": form})
@login_required
@login_required
def input_page(request):
    if request.method == "POST":
        form = BreastCancerForm(request.POST)
        if form.is_valid():
            field_order = ['AGE', 'CHRONIC_DISEASE', 'WHEEZING', 'ALCOHOL_CONSUMING', 'CHEST_PAIN']
            input_dict = {field: form.cleaned_data[field] for field in field_order}

            # Save to session
            request.session["input_data"] = input_dict
            

            # Predict
            input_array = [input_dict[field] for field in field_order]
            result = pipeline.predict([input_array])[0]
            prediction = "Lung Cancer Detected" if result == 2 else "No Lung Cancer"

            return redirect("App_post:results_page", prediction=prediction)
    else:
        form = BreastCancerForm()

    return render(request, "App_post/input_page.html", {"form": form})
# def input_page(request):
#     if request.method == "POST":
#         form = BreastCancerForm(request.POST)
#         if form.is_valid():
#             field_order = ['AGE', 'CHRONIC_DISEASE', 'WHEEZING', 'ALCOHOL_CONSUMING', 'CHEST_PAIN']
#             input_data = {field: form.cleaned_data[field] for field in field_order}
#             request.session['input_data'] = input_data
            
#             # Make prediction
#             input_scaled = pipeline.predict([input_data])[0]
#             result = "Breast Cancer Detected" if input_scaled == 2 else "No Breast Cancer"

#             # Optionally save the patient input data to the database
#             PatientData.objects.create(
#                 age=form.cleaned_data["AGE"],
#                 chronic_disease=form.cleaned_data["CHRONIC_DISEASE"],
#                 wheezing=form.cleaned_data["WHEEZING"],
#                 alcohol_consuming=form.cleaned_data["ALCOHOL_CONSUMING"],
#                 chest_pain=form.cleaned_data["CHEST_PAIN"]
#             )

#             return redirect('App_post:results_page', prediction=result)
#     else:
#         form = BreastCancerForm()

#     return render(request, "App_post/input_page.html", {"form": form})

# def input_page(request):
#     if request.method == "POST":
#         form = BreastCancerForm(request.POST)
#         if form.is_valid():
#             # Maintain input order
#             field_order = [
#                 'GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE',
#                 'CHRONIC_DISEASE', 'FATIGUE', 'ALLERGY', 'WHEEZING', 'ALCOHOL_CONSUMING',
#                 'COUGHING', 'SHORTNESS_OF_BREATH', 'SWALLOWING_DIFFICULTY', 'CHEST_PAIN'
#             ]

#             input_data = np.array([form.cleaned_data[field] for field in field_order]).reshape(1, -1)
#             input_scaled = scaler.transform(input_data)
#             prediction = model.predict(input_scaled)[0]
#             result = "Breast Cancer Detected" if prediction == 2 else "No Breast Cancer"

#             # Optionally save patient input
#             PatientData.objects.create(
#                 gender=form.cleaned_data["GENDER"],
#                 age=form.cleaned_data["AGE"],
#                 smoking=form.cleaned_data["SMOKING"],
#                 yellow_fingers=form.cleaned_data["YELLOW_FINGERS"],
#                 anxiety=form.cleaned_data["ANXIETY"],
#                 peer_pressure=form.cleaned_data["PEER_PRESSURE"],
#                 chronic_disease=form.cleaned_data["CHRONIC_DISEASE"],
#                 fatigue=form.cleaned_data["FATIGUE"],
#                 allergy=form.cleaned_data["ALLERGY"],
#                 wheezing=form.cleaned_data["WHEEZING"],
#                 alcohol_consuming=form.cleaned_data["ALCOHOL_CONSUMING"],
#                 coughing=form.cleaned_data["COUGHING"],
#                 shortness_of_breath=form.cleaned_data["SHORTNESS_OF_BREATH"],
#                 swallowing_difficulty=form.cleaned_data["SWALLOWING_DIFFICULTY"],
#                 chest_pain=form.cleaned_data["CHEST_PAIN"]
#             )

#             return redirect('App_post:results_page', prediction=result)
#     else:
#         form = BreastCancerForm()

#     return render(request, "App_post/input_page.html", {"form": form})

@login_required
def results_page(request, prediction):
    return render(request, "App_post/results_page.html", {"prediction": prediction})

@login_required
def new(request):
    projects = Project.objects.all()
    return render(request, 'App_post/new.html', context={'title': 'Home Page', 'projects': projects})
from django.http import HttpResponse
from .utils import render_to_pdf

from django.http import HttpResponse
from .utils import render_to_pdf


# def download_pdf(request, prediction):
#     user = request.user
#     input_data = request.session.get("input_data", {})  # dictionary of input values

#     context = {
#         "username": user.get_full_name() or user.username,
#         "prediction": prediction,
#         "input_data": input_data
#     }

#     pdf = render_to_pdf("App_post/pdf_template.html", context)
#     if pdf:
#         response = HttpResponse(pdf, content_type="application/pdf")
#         filename = "Lung_Cancer_Prediction_Result.pdf"
#         response["Content-Disposition"] = f'inline; filename="{filename}"'
#         return response
#     return HttpResponse("Error generating PDF", status=500)

# @login_required
# def download_pdf(request, prediction):
#     user_name = request.user.username
#     input_data = {
#         "CHRONIC_DISEASE": request.GET.get("CHRONIC_DISEASE"),
#         "WHEEZING": request.GET.get("WHEEZING"),
#         "ALCOHOL_CONSUMING": request.GET.get("ALCOHOL_CONSUMING"),
#         "CHEST_PAIN": request.GET.get("CHEST_PAIN"),
#         "SHORTNESS_OF_BREATH": request.GET.get("SHORTNESS_OF_BREATH"),
#     }

#     context = {
#         "user_name": user_name,
#         "input_data": input_data,
#         "prediction": prediction,
#     }

#     return render_to_pdf("App_post/pdf_template.html", context)

@login_required
def download_pdf(request, prediction):
    input_data = request.session.get("input_data")
    print("Session input_data:", input_data)


    if not input_data:
        return HttpResponse("No input data found in session.", status=400)

    context = {
        "user": request.user,
        "input_data": input_data,
        "prediction": prediction
    }

    return render_to_pdf("App_post/pdf_template.html", context)

@login_required
def down_pdf(request, prediction):
    input_data = request.session.get("input_data")
    
    if not input_data:
        return HttpResponse("No input data found in session.", status=400)

    context = {
        "user": request.user,
        "input_data": input_data,
        "prediction": prediction
    }

    # Render HTML string from template
    template = get_template("App_post/pdf_template.html")
    html_string = template.render(context)

    # Generate PDF from HTML
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()

    # Define file name and path
    filename = f"Lung_Cancer_Result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    save_path = os.path.join(settings.MEDIA_ROOT, filename)

    # Save PDF to disk
    with open(save_path, "wb") as f:
        f.write(pdf_file)

    # Serve file as a downloadable response
    return FileResponse(open(save_path, "rb"), as_attachment=True, filename=filename)
    
model = joblib.load("App_post/pipeline.pkl")
def predict_view(request):
    if request.method == "POST":
        # Get inputs
        chronic_disease = int(request.POST.get("CHRONIC_DISEASE"))
        wheezing = int(request.POST.get("WHEEZING"))
        alcohol_consuming = int(request.POST.get("ALCOHOL_CONSUMING"))
        chest_pain = int(request.POST.get("CHEST_PAIN"))
        shortness_of_breath = int(request.POST.get("SHORTNESS_OF_BREATH"))

        # Save to session
        request.session["input_data"] = {
            "CHRONIC_DISEASE": chronic_disease,
            "WHEEZING": wheezing,
            "ALCOHOL_CONSUMING": alcohol_consuming,
            "CHEST_PAIN": chest_pain,
            "SHORTNESS_OF_BREATH": shortness_of_breath
        }

        # Prepare data for prediction
        features = np.array([[chronic_disease, wheezing, alcohol_consuming, chest_pain, shortness_of_breath]])

        # Make prediction
        result = model.predict(features)[0]

        prediction = "Lung Cancer" if result == 1 else "No Lung Cancer"

        return redirect("download_pdf", prediction=prediction)

from django.template.loader import get_template
from weasyprint import HTML
from django.http import HttpResponse

# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     html_string = template.render(context_dict)
#     html = HTML(string=html_string)
#     pdf_file = html.write_pdf()

#     return HttpResponse(pdf_file, content_type='application/pdf')
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html_string = template.render(context_dict)
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()
    return HttpResponse(pdf_file, content_type='application/pdf')


