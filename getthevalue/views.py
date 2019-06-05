from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'home.html')


def sentvalue(request):
    value1 = request.GET['nameradio']
    return render(request, 'value.html', {'value2': value1, })
