
from django.shortcuts import render

from dizayner.models.proizvoditeli import Proizvoditeli


def spisok(request):

    items = Proizvoditeli.objects.all();
    context = {'items':items, 'nameShablon': 'dizayner:proizvoditeli_detail'}    
    return render(request, template_name='dizayner\proizvoditeli_spisok.html', context=context) 

def detail(request, proizvoditel_id):

    context = {}
    return render(request, template_name='dizayner\proizvoditeli_spisok.html', context=context) 