from django.shortcuts import render
# Create your views here.


def bibliography_view(request):
    return render(request, 'bibliography.html')
