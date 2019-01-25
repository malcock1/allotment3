from django.shortcuts import render
from django.http import HttpResponse

from .models import Design, Bed

# Create your views here.
def index(request):
    designs = Design.objects.all()
    context = {
            'designs': designs,
            }

    return render(request, "designs/index.html", context)

def detail(request, design_id):
    design = Design.objects.get(id=design_id)
    context = {
            'design': design,
            }

    return render(request, "designs/detail.html", context)

def designer(request):
    context = {}
    return render(request, "designs/designer.html", context)

# Most add validation
def add(request):
    if request.method == "POST" and request.POST.get("svg"):
        design = Design(
                name = "Test",
                description = "This is a test",
                width = 800,
                height = 1200,
                svg = request.POST.get("svg"),
                )
        design.save()
    return HttpResponse(status=201)

def edit(request, design_id):
    design = Design.objects.get(id=design_id)
    return HttpResponse(design.svg, content_type="text/plain")
