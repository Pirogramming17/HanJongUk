import re
from django.shortcuts import render

# Create your views here.
def main(request):
    context={

    }
    return render(request, template_name="sites/main.html", context=context)