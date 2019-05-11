from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

# Create your views here.
from photos.models import Photo


def latest_photos(request):
    photos = Photo.objects.all().order_by('-modification_date')

    context = {'latest_photos': photos[:5]}

    html = render(request, 'photos/latest.html', context)

    return HttpResponse(html)


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    context = {'photo': photo}

    html = render(request, 'photos/detail.html', context)

    return HttpResponse(html)
