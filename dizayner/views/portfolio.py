from django.shortcuts import get_object_or_404, render
from django.core.files.storage import FileSystemStorage
from extra_views import CreateWithInlinesView, InlineFormSetFactory
from ..models.portfolio import Portfolio, Portfolio_photo

def detail(request, dizayner_id, portfolio_id):

    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        for file in request.FILES :
            fs = FileSystemStorage()
            # сохраняем на файловой системе
            filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        return render(request, 'home_page.html', {
            'file_url': file_url
        })

    port_object = get_object_or_404(Portfolio, pk=portfolio_id)
    #diz_object = Dizayner.objects.first()
    context = {'portfolio':port_object}

    return render(request, template_name='dizayner\portfolio_detail.html', context=context)

class Portfolio_photoInline(InlineFormSetFactory):
    model = Portfolio_photo
    fields = ['description', 'image']

class Portfolio_CreaterView(CreateWithInlinesView):
    model = Portfolio
    inlines = [Portfolio_photoInline]
    fields = '__all__'
    template_name = 'dizayner\portfolio_create.html'
   