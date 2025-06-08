from django.urls import path
from App_post import views

app_name = "App_post"

urlpatterns = [
    path('new/', views.new, name='new'),
    path("input/", views.input_page, name="input_page"),
    path("results/<str:prediction>/", views.results_page, name="results_page"),
    path('results/', views.results_page, name='results_page'),
    path("input/", views.input_page, name="input_page"),
    path("results/<str:prediction>/", views.results_page, name="results_page"),
    path("pdf/<str:prediction>/", views.download_pdf, name="download_pdf"),
    path('generate-pdf/', views.render_to_pdf, name='generate_pdf'),
    path("data/pdf/<str:prediction>/", views.download_pdf, name="download_pdf"),
    path('download/<str:prediction>/', views.down_pdf, name='down_pdf'),


    
]
