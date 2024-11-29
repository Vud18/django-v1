from django.shortcuts import render

from services.models import SliderImage


def home(request):
    images = SliderImage.objects.all()
    return render(request, 'services/index.html', {'images': images})
