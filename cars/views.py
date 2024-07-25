from typing import Any
from cars.models import Car
from cars.forms import CarForm, CarModelForm

from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if (search := self.request.GET.get('search')):
            cars = Car.objects.filter(brand__name__icontains=search).order_by('model')

        return cars

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')        
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch') 
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    # success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required(login_url='login'), name='dispatch') 
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'


# def cars_view(request): 
#     # print(request.GET)
#     brand_search = request.GET.get('search')
    
#     ## Documentation: Django ORM
#     cars_list = Car.objects.all().order_by('model')
    
#     if brand_search:
#         cars_list = Car.objects.filter(brand__name__icontains=brand_search).order_by('model')

#     return render(
#         request, 
#         'cars.html', 
#         {'cars' : cars_list }
#     )


# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#     else:
#         new_car_form = CarModelForm()

#     return render(
#         request,
#         'new_car.html',
#         { "new_car_form" : new_car_form }      
#     )

# class NewCarView(View):
#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(request, 'new_car.html', { "new_car_form" : new_car_form } )

#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(request, 'new_car.html', { "new_car_form" : new_car_form } )


