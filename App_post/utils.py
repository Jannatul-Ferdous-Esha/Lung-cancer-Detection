from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import get_template
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html_string = template.render(context_dict)
    pdf = HTML(string=html_string).write_pdf()
    return HttpResponse(pdf, content_type="application/pdf")
