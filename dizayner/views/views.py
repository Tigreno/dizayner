from django.shortcuts import render
from dizayner.models.dizayner import Dizayner


def index(request):
    context = {}

    return render(request, template_name='dizayner\index.html', context=context)


def index_my(request):
    
    dizayner = Dizayner.objects.filter(user=request.user).first()
    context = {'dizayner':dizayner}

    return render(request, template_name='dizayner\index.html', context=context)

# Create your views here.
