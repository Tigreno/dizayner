from django.urls import path

from .views import views, dizayner, portfolio, proizvoditeli


app_name = 'dizayner'
urlpatterns = [
    path('dizayner/', dizayner.spisok, name='dizayner_spisok'),
    path('my/', views.index_my, name='index_my'),
    path('dizayner/<int:dizayner_id>/', dizayner.detail, name='dizayner_detail'),
    path('dizayner/<int:dizayner_id>/p<int:portfolio_id>/', portfolio.detail, name='portfolio_detail'),
    path('dizayner/<int:dizayner_id>/p_create', portfolio.Portfolio_CreaterView.as_view(), name='portfolio_create'),
    path('proiz/', proizvoditeli.spisok, name ='proizvoditeli_spisok'),
    path('proiz/<int:proizvoditel_id>/', proizvoditeli.detail, name ='proizvoditeli_detail'),
]