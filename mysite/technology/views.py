from django.shortcuts import render
# Create your views here.

def technology_view(request):
    return render(request, 'technology.html')
