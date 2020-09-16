from django.urls import path
from .views import admin_view, hiv_test, add_result, delete, patientinfo
    

urlpatterns = [
    path('admin_view', admin_view, name="adminview"),
    path('delete/<int:patient_id>', delete, name="delete"),
    path('hiv_test', hiv_test, name="hiv_test"),
    path('<int:patient_id>/patientinfo', patientinfo, name="patientinfo"),
    path("add_result/<int:patient_id>/<str:first>-<str:last>", add_result, name="addresult"),

]