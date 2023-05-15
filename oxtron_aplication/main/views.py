from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from api.Oxtronaplication.user import ScopesCalculation
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

@csrf_exempt
@require_POST
def calculate(request):
    data = request.POST
    print(data)
    print(request.text)
   
    allScope=ScopesCalculation()

    result = allScope.callScope(scope1=data.get ('Stationary Combustion'))

    #result = allScope.callScope(scope1=data['Stationary Combustion'],scope12= data["Mobile Combustion"],scope13= data["Refrigerants"],scope2= data["Purchased Electricity"],scope3= data["Transportation"],paramsGrid= data["params"])
    #return JsonResponse({'result': result})

    return JsonResponse({'message': '¡Calculando!'})