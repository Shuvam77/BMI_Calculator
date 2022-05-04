from urllib import request
from django.shortcuts import render
from .models import Bmi
from django.views.generic import CreateView

# Create your views here.

class indexView(CreateView):
    model = Bmi
    fields = ['height', 'weight']
    template_name = 'bmi/index.html'
    success_url = '/'

    def form_valid(self, form):
        weight=form.instance.weight
        height=form.instance.height
        bmi=round(((weight/(height**2))*100), 3)

        form.instance.user = self.request.user
        form.instance.bmi = bmi
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state = Bmi.objects.all()
        context['track_list'] = state
        return context

