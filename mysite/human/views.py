from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .forms import *
from time import timezone


def home(request):
    return render(request, 'human/home.html')


def index(request):
    human = Person.objects.order_by('-pub_date')
    return render(request, 'human/index.html', {'human': human})


class DetailPerson(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'human/detail.html'


class CreatePerson(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'human/create.html'
    success_url = reverse_lazy('index')


class DeletePerson(DeleteView):
    model = Person
    template_name = 'human/delete.html'
    success_url = reverse_lazy('index')


class UpdatePerson(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'human/update.html'
