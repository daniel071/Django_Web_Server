from django.shortcuts import render
# Create your views here.


def republic_view(request):
    return render(request, 'republic.html')
