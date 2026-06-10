from django.shortcuts import render

def song(request):
    return render(request, 'sing/song.html')
