from django.http import HttpResponse

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from employees.models import Employee
from employees.serializers import EmployeeSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        emp_serializer = EmployeeSerializer(emp, many=True)
        return JsonResponse(emp_serializer.data, safe=False)


@csrf_exempt
def employee_add(request):

    if request.method == 'POST':
        emp_data = JSONParser().parse(request)
        emp_serializer = EmployeeSerializer(data=emp_data)

        if emp_serializer.is_valid():
            emp_serializer.save()
            return JsonResponse(emp_serializer.data,
                                status=201)
        return JsonResponse(emp_serializer.errors,
                            status=400)