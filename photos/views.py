from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

# Create your views here.
from photos.forms import PhotoForm
from photos.models import Photo


def latest_photos(request):
    photos = Photo.objects.filter(visibility=Photo.PUBLIC).order_by('-modification_date')

    context = {'latest_photos': photos[:5]}

    html = render(request, 'photos/latest.html', context)

    return HttpResponse(html)


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk, visibility=Photo.PUBLIC)

    context = {'photo': photo}

    html = render(request, 'photos/detail.html', context)

    return HttpResponse(html)

@login_required
def new_photo(request):
    if request.method == 'POST':
        photo = Photo()
        photo.owner = request.user
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            new_photo = form.save()
            messages.success(request, 'Foto creada correctamente con ID {0}'.format(new_photo.pk))

    else:
        form = PhotoForm()

    context = {'form': form}
    return render(request, 'photos/new.html', context)
