# coding: utf-8
from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.views.generic.edit import FormView
from app.models import Doctor, Reception
from app.forms import ReceptionForm
from django.http import JsonResponse
from django.template import RequestContext

class DoctorList(ListView):
    model = Doctor
    template_name='start.html'
    context_object_name = 'doctors'

class ReceptionView(FormView):
    form_class = ReceptionForm
    template_name = 'reception.html'

    def form_valid(self, form):
        fcd = form.cleaned_data
        curr_doctor=Doctor.objects.get(id= self.kwargs['doctor_id'])
        response_dict={"form":form,
                       "doctor":curr_doctor,
                       "curr_date":fcd['date'],
                       "curr_time":fcd['time']}
        # условие для предотвращения записи на один и тот же деь у данного врача
        if Reception.objects.filter(date=fcd['date'],time=fcd['time'],doctor=curr_doctor).count()==0:
            Reception.objects.create(date=fcd['date'],time=fcd['time'],
                                     patient_name=fcd['patient_name'],
                                     patient_info=fcd['patient_info'],
                                     doctor=curr_doctor)
            return render_to_response('reception.html',response_dict,
                                      context_instance=RequestContext(self.request))
        else:
            response_dict["message"]="Вы уже зарегистрированны на это время"
            return render_to_response('reception.html',response_dict,
                          context_instance=RequestContext(self.request))

    def get_context_data(self, **kwargs):
        context = super(ReceptionView, self).get_context_data(**kwargs)
        context['doctor']=Doctor.objects.get(id= self.kwargs['doctor_id'])
        return context


def date_from_ajax (request):
    if request.method == "POST" and request.is_ajax():
        doctor=Doctor.objects.get(id= request.POST.get("doctor_id"))
        reception_set=doctor.reception_set.filter(date=request.POST.get("date_from_ajax"))
        time_list=[]
        for reception in reception_set:
            time_list.append(reception.time)
        return JsonResponse({'time_list':time_list})
