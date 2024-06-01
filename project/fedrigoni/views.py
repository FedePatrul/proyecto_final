from django.shortcuts import render
from django.http import HttpResponse
from .models import PDF

# Create your views here.
def index(request):
    return render(request, "fedrigoni/index.html")


def list_pdfs(request):
    query = request.GET.get('q')
    if query:
        pdfs = PDF.objects.filter(nombre__icontains=query)
    else:
        pdfs = PDF.objects.all()
    return render(request, 'fedrigoni/list_pdfs.html', {'pdfs': pdfs})

def download_pdf(request, pdf_id):
    pdf = PDF.objects.get(id=pdf_id)
    response = HttpResponse(pdf.archivo, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf.archivo.name}"'
    return response