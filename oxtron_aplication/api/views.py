from django.shortcuts import render

# Create your vie ws here.
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from Oxtronaplication.user import ScopesCalculation
from django.views.decorators.csrf import csrf_exempt
import json as js



def welcome(request):
    return JsonResponse({'message': '¡Bienvenido a la API de mi aplicación!'})

@csrf_exempt
@require_POST
def calculateScopeOne(request):
    data = request.body
    data=js.loads(data)
    print(data)
    #print(request.text)
   
    allScope=ScopesCalculation()
    allScope=ScopesCalculation()



    result = allScope.callScope(scope1=data['Stationary Combustion'],scope12= data["Mobile Combustion"],scope13= data["Refrigerants"])
    return JsonResponse({'result': result})






@csrf_exempt
@require_POST
def calculateRefrigerantsPurchased(request):
    data = request.body
    data=js.loads(data)
    print(data)
    #print(request.text)
   
    allScope=ScopesCalculation()

    #result = allScope.callScope(scope1=data ['Stationary Combustion'])

    result = allScope.callScope(scope2= data["Purchased Electricity"],paramsGrid= data["params"])
    return JsonResponse({'result': result})




@csrf_exempt
@require_POST
def calculateTransportation(request):
    data = request.body
    data=js.loads(data)
    print(data)
    #print(request.text)
   
    allScope=ScopesCalculation()

    #result = allScope.callScope(scope1=data ['Stationary Combustion'])

    result = allScope.callScope(scope3= data["Transportation"])
    return JsonResponse({'result': result})

