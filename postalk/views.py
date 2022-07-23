from django.shortcuts import render

def hello_world(request):
    return render(request, 'postalk/hello_world.html', {})