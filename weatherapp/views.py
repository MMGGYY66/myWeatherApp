from django.shortcuts import render


# Create your views here.
def weatherview(request):
    """
    docstring
    """
    return render(request, 'weather.html')
