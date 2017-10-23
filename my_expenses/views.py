from django.shortcuts import render


def hello_world(request):
    # Give response
    return render(request, 'index.html')
