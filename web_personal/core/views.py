from django.shortcuts import render, HttpResponse
from django.views.defaults import page_not_found
from django.conf import settings
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

items = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
# path = 'core/base.html'
l = list(range(3))
s = [1,1,1,1]

def home(request):
    return render(request, 'core/index.html', {'v':'Esta es una variable'})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def sample(request):
    return render(request, 'core/sample.html', {'items':items, 'path':"core/base.html", 'text':'aASDFAasdfasdDF', 'list':l, 'list1':s, 'id':3})

def client(request, id):
    return render(request, 'core/client.html', {'id':id})

def error(request, exception):
    return page_not_found(request, exception, 'core/404.html')

def image(request):
    image = open(settings.MEDIA_ROOT + '/projects/elon-quote.jpeg', "rb").read()
    return HttpResponse(image, content_type='image/png')

def pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
