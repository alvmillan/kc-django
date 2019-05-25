from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View

from photos.forms import PhotoForm
from photos.models import Photo

class LatestPhotosView(View):

    def get(self, request):
        photos = Photo.objects.filter(visibility=Photo.PUBLIC).order_by('-modification_date').select_related('owner')

        context = {'latest_photos': photos[:5]}

        html = render(request, 'photos/latest.html', context)

        return HttpResponse(html)

class PhotoDetailView(View):
    def get(self, request, pk):
        photo = get_object_or_404(Photo.objects.select_related('owner'), pk=pk, visibility=Photo.PUBLIC)

        context = {'photo': photo}

        html = render(request, 'photos/detail.html', context)

        return HttpResponse(html)


class NewPhotoView(LoginRequiredMixin, View):

    def get(self, request):
        form = PhotoForm()
        context = {'form': form}
        return render(request, 'photos/new.html', context)

    def post(self, request):
        photo = Photo()
        photo.owner = request.user
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            new_photo = form.save()
            messages.success(request, 'Foto creada correctamente con ID {0}'.format(new_photo.pk))
            form = PhotoForm
        context = {'form': form}
        return render(request, 'photos/new.html', context)
