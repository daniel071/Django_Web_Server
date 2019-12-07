from django.shortcuts import render
# Create your views here.


def army_view(request):
    return render(request, 'army.html')
