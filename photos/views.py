from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from photos.models import Photo


def latest_photos(request):
    photos = Photo.objects.all().order_by('-modification_date')

    context = {'latest_photos': photos}

    html = render(request, 'photos/latest.html', context)

    return HttpResponse(html)

def photo_detail(request, pk):
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return HttpResponseNotFound()

    context = {'photo': photo}

    html = render(request, 'photos/detail.html', context)

    return HttpResponse(html)
