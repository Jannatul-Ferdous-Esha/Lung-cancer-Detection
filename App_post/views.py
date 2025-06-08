# import os
# import numpy as np
# import joblib
# from datetime import datetime
# from django.conf import settings
# from django.http import HttpResponse, FileResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.template.loader import get_template
# from weasyprint import HTML

# from .forms import BreastCancerForm
# from .models import PatientData, Project
# from .utils import render_to_pdf

# PIPELINE_PATH = "App_post/pipeline.pkl"
# pipeline = joblib.load(PIPELINE_PATH)

# @login_required
# def input_page(request):
#     if request.method == "POST":
#         form = BreastCancerForm(request.POST)
#         if form.is_valid():
#             field_order = ['age', 'chronic_disease', 'wheezing', 'alcohol_consuming', 'chest_pain',
#                            'smoking', 'yellow_fingers', 'coughing', 'shortness_of_breath', 'gender']
#             input_dict = {field: form.cleaned_data.get(field, 1) for field in field_order}

#             request.session["input_data"] = input_dict
#             input_array = [input_dict[field] for field in field_order]
#             result = pipeline.predict([input_array])[0]
#             prediction = "Lung Cancer Detected" if result == 2 else "No Lung Cancer"

#             return redirect("App_post:results_page", prediction=prediction)
#     else:
#         form = BreastCancerForm()

#     return render(request, "App_post/input_page.html", {"form": form})

# @login_required
# def results_page(request, prediction):
#     return render(request, "App_post/results_page.html", {"prediction": prediction})

# @login_required
# def new(request):
#     projects = Project.objects.all()
#     return render(request, 'App_post/new.html', context={'title': 'Home Page', 'projects': projects})

# @login_required
# def download_pdf(request, prediction):
#     input_data = request.session.get("input_data")
#     if not input_data:
#         return HttpResponse("No input data found in session.", status=400)

#     context = {
#         "user": request.user,
#         "input_data": input_data,
#         "prediction": prediction
#     }

#     return render_to_pdf("App_post/pdf_template.html", context)

# @login_required
# def down_pdf(request, prediction):
#     input_data = request.session.get("input_data")
#     if not input_data:
#         return HttpResponse("No input data found in session.", status=400)

#     context = {
#         "user": request.user,
#         "input_data": input_data,
#         "prediction": prediction
#     }

#     template = get_template("App_post/pdf_template.html")
#     html_string = template.render(context)
#     html = HTML(string=html_string)
#     pdf_file = html.write_pdf()

#     filename = f"Lung_Cancer_Result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
#     save_path = os.path.join(settings.MEDIA_ROOT, filename)

#     with open(save_path, "wb") as f:
#         f.write(pdf_file)

#     return FileResponse(open(save_path, "rb"), as_attachment=True, filename=filename)

# model = joblib.load("App_post/pipeline.pkl")

# @login_required
# def predict_view(request):
#     if request.method == "POST":
#         input_fields = ['chronic_disease', 'wheezing', 'alcohol_consuming', 'chest_pain',
#                         'shortness_of_breath', 'smoking', 'yellow_fingers', 'coughing', 'age', 'gender']
#         input_data = {field: int(request.POST.get(field, 1)) for field in input_fields}

#         request.session["input_data"] = input_data

#         features = np.array([[input_data[field] for field in input_fields]])
#         result = model.predict(features)[0]
#         prediction = "Lung Cancer Detected" if result == 2 else "No Lung Cancer"

#         return redirect("download_pdf", prediction=prediction)
import os
import numpy as np
import joblib
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from weasyprint import HTML

from .forms import BreastCancerForm
from .models import PatientData, Project
from .utils import render_to_pdf

PIPELINE_PATH = "App_post/pipeline.pkl"
pipeline = joblib.load(PIPELINE_PATH)

# These are the 5 features your model expects
MODEL_FEATURES = ['age', 'chronic_disease', 'wheezing', 'alcohol_consuming', 'chest_pain']

@login_required
def input_page(request):
    if request.method == "POST":
        form = BreastCancerForm(request.POST)
        if form.is_valid():
            all_fields = form.cleaned_data
            request.session["input_data"] = all_fields

            # Select only the 5 model features in the correct order
            model_input = [all_fields.get(field, 0) for field in ['age', 'chronic_disease', 'wheezing', 'alcohol_consuming', 'chest_pain']]
            prediction_result = pipeline.predict([model_input])[0]
            prediction = "Lung Cancer Detected" if prediction_result == 2 else "No Lung Cancer"

            return redirect("App_post:results_page", prediction=prediction)
    else:
        form = BreastCancerForm()

    return render(request, "App_post/input_page.html", {"form": form})

@login_required
def results_page(request, prediction):
    return render(request, "App_post/results_page.html", {"prediction": prediction})

@login_required
def new(request):
    projects = Project.objects.all()
    return render(request, 'App_post/new.html', context={'title': 'Home Page', 'projects': projects})

@login_required
def download_pdf(request, prediction):
    input_data = request.session.get("input_data")
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

    template = get_template("App_post/pdf_template.html")
    html_string = template.render(context)
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()

    filename = f"Lung_Cancer_Result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    save_path = os.path.join(settings.MEDIA_ROOT, filename)

    with open(save_path, "wb") as f:
        f.write(pdf_file)

    return FileResponse(open(save_path, "rb"), as_attachment=True, filename=filename)


