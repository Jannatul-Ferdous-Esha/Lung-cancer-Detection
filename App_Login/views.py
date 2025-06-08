from django.shortcuts import render, HttpResponseRedirect
from App_Login.forms import CreateNewUser, EditProfile
from django.contrib.auth import authenticate, login, logout  
from django.urls import reverse, reverse_lazy
from App_Login.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            #login(request, user)  # Log in the user after signup
            return HttpResponseRedirect(reverse('App_Login:login' ))  # Redirect to a relevant page

    return render(request, 'App_Login/signup.html', context={'title': 'Signup Form Here', 'form': form})  

def login_page(request):
    form = AuthenticationForm()
    if request. method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user =authenticate(username=username, password=password)
            if user is not None:
              login(request,user) 
              return HttpResponseRedirect(reverse('App_Login:index'))
    
    return render(request,'App_Login/login.html',context={'title' :'Login Page', 'form' : form})       
            
@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance = current_user)
    return render(request, 'App_Login/profile.html',context = {'title':'Edit Profile Page','form': form})    
    

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))

@login_required
def index(request):
    return render(request, 'portfolio/index.html') 

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def generate_pdf(request):
    # Example: Extract data from POST or session
    user_data = {
        'name': request.POST.get('name'),
        'age': request.POST.get('age'),
        'result': request.POST.get('result'),
    }

    # Render PDF
    response = render_to_pdf('portfolio/pdf_template.html', user_data)
    if response:
        response['Content-Disposition'] = 'attachment; filename="lung_report.pdf"'
    return response
