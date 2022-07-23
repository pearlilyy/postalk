from django.shortcuts import render


def hello_postalk(request):
    return render(request, 'postalk/hello_postalk.html', {})
