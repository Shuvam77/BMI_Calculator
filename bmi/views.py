from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Bmi
from django.views.generic import CreateView

# Create your views here.

class indexView(CreateView):
    model = Bmi
    fields = ['height', 'weight']
    template_name = 'bmi/index.html'
    success_url = '/'

    # def form_valid(self, form):
    #     weight=form.instance.weight
    #     height=form.instance.height
    #     bmi=round(((weight/(height**2))*100), 3)
    #     form.instance.user = self.request.user
    #     form.instance.bmi = bmi
    #     return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        context={}
        if request.method == "POST":
            weight_metric = request.POST.get("weightMetric")
            weight_imperial = request.POST.get("weightImperial")

            if weight_metric:
                weight = float(request.POST.get("weightMetric"))
                height = float(request.POST.get("heightMetric"))
            elif weight_imperial:
                weight = float(request.POST.get("weightImperial"))*0.45359237
                height = (float(request.POST.get("feet"))*30.48) + (float(request.POST.get("inches"))*2.54)
            bmi=round(((weight/(height**2))*100), 3)
            user = request.user
            Bmi_obj = Bmi.objects.create(
                height=height,
                weight=weight,
                bmi=bmi,
                user=user
            )
            context['bmi']=Bmi_obj
            # return redirect('index-view')
        return render (request, 'bmi/index.html', context)



    # def form_valid(self, form):
        # weight_metric = float(form.cleaned_data.get('weight-metric'))
        # weight_imperial= float(form.cleaned_data.get('weight-imperial'))
        # bmi=round(((weight/(height**2))*100), 3)
        # form.instance.bmi = bmi
        # form.instance.user = self.request.user
        # return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'index'
        state = Bmi.objects.all()
        context['track_list'] = state
        return context

