from django.shortcuts import get_object_or_404, render
from ..models.dizayner import Dizayner

def detail(request, dizayner_id):
    diz_object = get_object_or_404(Dizayner, pk=dizayner_id)
    #diz_object = Dizayner.objects.first()
    context = {'dizayner':diz_object}

    return render(request, template_name='dizayner\index.html', context=context)

def spisok(request):
    items = Dizayner.objects.all();
    context = {'items':items, 'nameShablon': 'dizayner:dizayner_detail'}    
    return render(request, template_name='dizayner\proizvoditeli_spisok.html', context=context) 
