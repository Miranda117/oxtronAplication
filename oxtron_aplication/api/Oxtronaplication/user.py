from .process import *
import pandas as pd


#GWPdatasetIPCCassessment=["2014 IPCC Fifth Assessment",2,"2007 IPCC Fifth Assessment"]


#		S3 - Transportation	
#	Facility ID	Year	##Custom Emission Factors?##	#Fuel#			##Amount of fuel##	
#scope1=	[[1,2019,		0, 	52,			503100,					20],
#	[1,2019,		0,	53,			251550,					25]]


#Fuel:Dato proporcionado por el usuario

#Amount of fuel: AQUI VA LA KEY DE LA Unidad a convertir
#Custom Emission Factors: La key de el tipo de Emisiones




#		Year		Description		Facility ID		##Activity Type##		Fuel Source		##Vehicle Type##			#Activity Amount#		##Unit of Fuel Amountr##	
						

#scope12=		[[2019,	"Motocicleta para reparto",			1,			0,		"Motor Gasoline",		20,				5465,			1],
#		[2020,		"Motocicleta para reparto",		2,			1,		"Motor Gasoline",		6,				5465,			17	],
#		[2021,		"Motocicleta para reparto",		3,			0,		"Motor Gasoline",		20,				5465,			4]]

#Activity Type: Este parametro se para para saber si que parametro es Fuel Use, Distance Activityy  Custom emission factor.
#Vehicle Type Esta key para saber que emición tedremos  
#Activity Amount: este valo sera el proporcionado por el usuario
#Unit of Fuel Amountr: campo proporcionado por el usuario
##Unit of Fuel Amountr##



#	Year	Facility ID	Type of Air Conditioning and Refrigeration Equipment			Refrigerant Used	Refrigerant inventory 	(in storage, not equipment) at the beginning of the Year	Refrigerant inventory (in storage, not equipment) at the end of the Year	Refrigerant purchased from producers/ distributors	Refrigerant returned by equipment users	Refrigerant returned after off-site recycling or reclamation	"Refrigerant charged into equipment* 	Refrigerant delivered to equipment users in containers	Refrigerant returned to refrigerant producers	Refrigerant sent off-site for recycling or reclamation	Refrigerant sent off-site for destructio	Nameplate Capacity of Partially Charged Equipment		Density or Pressure** of partical charge	Density or Pressure** of full charge
				



'''scope13=[[2019,	1,		"Enfriador Horizontal con Circulación Forzada de Aire (Modelo CFX-SL HC)",		7,		242.00,		0.05,							0.05,								0.05,							0.00,										0.05,				5.00,						5.00,						53.00,					4.00,				2.00,								1.00,				2.0],
	[2019,	2,		"Enfriador Horizontal con Circulación Forzada de Aire (Modelo CLH-38 2P HC)",		7,		452.00,		0.11,							0.11,								0.11,							0.00,										0.11,				1.00,						1.00,						1.00,					1.00,	 			5.00,								6.00,				8.0,]]
'''

#Refrigerant Used: Aqui dede de ir la key para saber que emision se usara.
#Los demás campos seran para calculos aritmeticos 

#		Year		#Facility ID#		#Amount of Electricity Consumption#	##Units##		Calculation Approach		##Type of Emission Factor##

'''scope2=[
		[2019,			1,			560000,			25,				0,			0],
		[2020,			2,			560000,			23,				2,			2],
		[2021,			3,			560000,			25,				2,			1]]
'''
#Facility ID: es la referencia para tomar las los grid estabelcidos en params 
#Amount of Electricity Consumption: Monto proporcionado por el usuario
#Units: Key para las conversiones

#Type of Emission Factor: key para el tipo de calculo


#	Year		Description		Category			Emission Factor Dataset	Mode of Transport		Activity Type	##Vehicle Type##	##Amount of Activity Type#	##Units of Measurement##

'''scope3=[
	[2019,		"Toño",			"Employee Commute",			"US EPA",			"Car",		"Vehicle Distance",		2,		563,		"vehicle-mile"],
	[2019,		"Seve",			"Employee Commute",			"UK DEFRA",		"Bus",		"Vehicle Distance",		6,		563,		"vehicle-km"],
	[2019,		"Luis Antonio",		"Employee Commute",			"UK DEFRA",		"Car",		"Passenger Distance",	1,		563,		"passenger-mile"],
	[2019,		"Daniel",			"Employee Commute",			"UK DEFRA",		"Bus",		"Vehicle Distance",		20,		536,		"vehicle-mile"]]
'''
#Vehicle Type:	key para saber que emision es

#Amount of Activity Type: Monto proporcionado por el usuiario

# Units of Measurement:  uNIDADES A CONVERTIR



class ScopesCalculation():
	def callScopeOneOne(self,scope1=0,scope12=0,scope13=0):

		scope11=StationaryCombustion(scope1)
		dFScope1,resumenSumary11=scope11.operaciones()
		


		jsScope1	 = dFScope1.to_json(orient = 'columns')

		jsResumenSumary11 = resumenSumary11.to_json(orient = 'columns')

		

		scopeDisct={"SCOPE11":[jsScope1]}
		jsResume={"SCOPE11":[jsResumenSumary11]}
		JsonResponse={"scopes11":scopeDisct, "resultSumary":jsResume}
		return JsonResponse

	def callScopeOneTwo(self,scope1=0,scope12=0,scope13=0):
			scope12=MobileCombustion(scope12)
			dFScope12,resumenSumary12=scope12.operaciones()
			jsScope12	 = dFScope12.to_json(orient = 'columns')
			
			jsResumenSumary12 = resumenSumary12.to_json(orient = 'columns')

			scopeDisct={"SCOPE12":[jsScope12]}
			jsResume={"SCOPE12":[jsResumenSumary12]}
			JsonResponse={"scope12":scopeDisct, "resultSumary":jsResume}
			return JsonResponse

	def callScopeOneThree(self,scope1=0,scope12=0,scope13=0):


			scope13=Refrigerantes(userSuppliedData=scope13)
			dFScope13,resumenSumary13=scope13.operaciones()
			
			jsScope13	 = dFScope13.to_json(orient = 'columns')

			jsResumenSumary13 = resumenSumary13.to_json(orient = 'columns')
			

			

			scopeDisct={"SCOPE13":[jsScope13]}
			jsResume={"SCOPE13":[jsResumenSumary13]}
			JsonResponse={"scopes13":scopeDisct, "resultSumary":jsResume}
			return JsonResponse






		
	def callScopeTwo(self,scope1=0,scope12=0,scope13=0,scope2=0,scope3=0,paramsGrid=0):	
		scope2=PurchasedElectricity(userSuppliedData=scope2,gridRegion=paramsGrid)
		dFScope2,resumenSumary2=scope2.operaciones()

		jsScope2	 = dFScope2.to_json(orient = 'columns')


		jsResumenSumary2 = resumenSumary2.to_json(orient = 'columns')
		scopeDisct={"SCOPE2":[jsScope2]}
		jsResume={"SCOPE2":[jsResumenSumary2]  }
		JsonResponse={"scopes":scopeDisct, "resultSumary":jsResume}
		return JsonResponse
	

	

	def callScopeThree(self,scope1=0,scope12=0,scope13=0,scope2=0,scope3=0,paramsGrid=0):
    		

		scope3=Transportation(scope3)
		dFScope3,resumenSumary3=scope3.operaciones()
		

		jsScope3	 = dFScope3.to_json(orient = 'columns')	

		jsResumenSumary3 = resumenSumary3.to_json(orient = 'columns')
		scopeDisct={"SCOPE3":[jsScope3]}
		jsResume={"SCOPE3":[jsResumenSumary3] }
		JsonResponse={"scopes":scopeDisct, "resultSumary":jsResume}
		return JsonResponse
			





