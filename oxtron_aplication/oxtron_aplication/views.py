from django.http import JsonResponse
from django.views.decorators.http import require_POST
from api.Oxtronaplication.user import ScopesCalculation
from django.views.decorators.csrf import csrf_exempt
import json as js

def welcome(request):
    return JsonResponse({'message': '¡Bienvenido a la API de mi aplicación!'})

@csrf_exempt
@require_POST
def calculateScopeOneStationary(request):
    data = request.body
    data=js.loads(data)
    print(data)
    #print(request.text)
   
    allScope=ScopesCalculation()
    allScope=ScopesCalculation()



    result = allScope.callScopeOneOne(scope1=data["stationaryCombustion"])
    return JsonResponse({'result': result})


@csrf_exempt
@require_POST
def calculateScopeOneMobile(request):
    data = request.body
    data=js.loads(data)
    print(data)
    #print(request.text)
   
    allScope=ScopesCalculation()
    allScope=ScopesCalculation()



    result = allScope.callScopeOneTwo(scope12= data["mobileCombustion"])
    return JsonResponse({'result': result})


@csrf_exempt
@require_POST
def calculateScopeOneRefrigerants(request):
    data = request.body
    data=js.loads(data)
    print(data)
    #print(request.text)
   
    allScope=ScopesCalculation()
    allScope=ScopesCalculation()



    result = allScope.callScopeOneThree(scope13= data["refrigerants"])
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

    result = allScope.callScopeTwo(scope2= data["purchasedElectricity"])
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

    result = allScope.callScopeThree(scope3= data["transportation"])
    return JsonResponse({'result': result})

