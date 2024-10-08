
from django.shortcuts import render

def ensenas_view(request):
    return render(request, 'start.html')