from django.shortcuts import render
# Create your views here.


def spartacus_view(request):
    return render(request, 'spartacus.html')
