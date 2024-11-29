from django.shortcuts import render

from services.models import SliderImage


def home(request):
    images = SliderImage.objects.all()
    return render(request, 'services/index.html', {'images': images})


def test(request):
    images = SliderImage.objects.all()
    return render(request, 'services/test.html', {'images': images})
