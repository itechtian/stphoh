from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Patient, Result

def admin_view(request):
    context = {'Patient':Patient.objects.all()}
    return render(request, "adminbase.html", context)

def hiv_test(request):
    if request.method == "POST":
        first = request.POST.get("first")
        last = request.POST.get("last")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        phone = request.POST.get("phone")
        state = request.POST.get("state")
        result = Result()

        form = Patient(first=first, last=last, state=state, age=age, sex=sex, phone=phone, instance=result)
        form.save()
        return render(request, "hivtest.html") 

    return render(request, "hivtest.html")

def add_result(request, patient_id, first, last):
    patient = Patient.objects.get(pk=patient_id, first=first, last=last)
    if request.method == 'POST':
        hepatitis_B_test = request.POST.get('hepatitisBtest')
        hiv_aid_test = request.POST.get('hivaidtest')
        form = Result(hepatitis_B_test=hepatitis_B_test, hiv_aid_test=hiv_aid_test)
        form.save()
        return HttpResponseRedirect(reverse("adminview"))
    return render(request, "add_result.html",{'patient':patient})


def patientinfo(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    result = patient.result
    return render(request, "patientinfo.html",{'patient':patient, 'result':result})


def delete(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    if request.method == "POST":
        obj = Patient.objects.get(id=patient_id).delete()
        return HttpResponseRedirect(reverse("adminview"))
    return render(request, "delete.html")
