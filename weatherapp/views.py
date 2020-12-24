from django.shortcuts import render


# Create your views here.
def weatherview(request):
    return render(request, 'weather.html')


def about(request):
    return render(request, 'about.html')
