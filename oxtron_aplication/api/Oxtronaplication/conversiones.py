import pandas as pd		

																																					
#Common              Name	Formula	AR4	AR5		2014 IPCC Fifth Assessment							[@EF[Reference KG CO2]]/IF([@[Reference Unit in F7]]=[@[Standardized Unit of fuel]],1,VLOOKUP([@[Reference Unit in F7]]&"_to_"&[@[Standardized Unit]],REF_UnitConversions,REF_UnitConversions_Col,FALSE))																									
CarbonDioxide       	        =  ["CO2",	1,	1,		0]																																
Methane             	        =  ["CH4",	25,	28,		0]																																
NitrousOxide        	        =  ["N2O",	298,	265,		0]																																
NitrogenTrifluoride 	        =  ["NF3",	17200,	16100,		0]		 																														
SulfurHexafluoride  	        =  ["SF6",	22800,	23500,		0]																																
																																						
#         Unit	From Unit	gal (US)  	L	          brl	scf	ft^3	ccf	yd^3	m3	cm^3	t	kg	lb	ton	LT	g	mi	nm	m	km	kWh	MWh	GWh	therm	BTU	MMBTU	MJ	GJ	t-mi	ton-mi	ton-km	t-km	p-mi	MPG	L/km	sq ft	acre	ha
class originalUnit():
	def originalUnit(self):
		listConvertino=["gal (US)","L","brl","scf","ft^3","ccf","yd^3","m3","cm^3","t","kg","lb","ton","LT","g","mi","nm","m","km",
		"kWh","MWh","GWh","therm","BTU","mmBtu","MJ","GJ","t-mi","ton-mi","ton-km","t-km","p-mi","MPG","L/km","sq ft","acre","ha"]
		return listConvertino

class TablaConvertions():
	def __init__(self):
		self.galUS  	 =        ["US Gallon", 	          1,	          3.78541178,	0.0238095238,	0.133680556,	0.133680556,	0,	0.004951,  	0.00378541178,	3785.41178,	0,                  0,                  0,                  0,                  0,                  0,                          	0,        	0,        	0,	0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																				
		self.L		=	["litre",      	          0.264172052,	1,	          0.00628981077,	0.0353146667,	0.0353146667,	0,	0.001308,  	0.001,		0,		0,                  0,                  0,                  0,                  0,                  0,                          	0,        	0,        	0,	0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																									
		self.brl	     	=        	["Barrel",    	          42,	          158.987295,	1,        	5.61458333,	5.61458333,	0,	0,                  0.158987295,        0,		0,                  0,                  0,                  0,                  0,                  0,                          	0,        	0,        	0,	0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																											
		self.scf	     	=        	["Standard Cubic Foot",	7.48051948,	28.3168466,	0.178107607,	1,         	1,		0,	0,                  0.0283168466,	0,		0,                  0,                  0,                  0,                  0,                  0,                          	0,        	0,        	0,	0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.ft3	     	=        	["Cubic Foot",	          7.48051948,	28.3168466,	0.178107607,	1,         	1,         	0,	0.037037,           0.0283168466,	0,		0,                  0,                  0,                  0,                  0,                  0,                          	0,        	0,        	0,	0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.ccf	     	=        	["Hundred Cubic Feet",	748.051948,	2831.68466,	17.8107607,	100,       	100,                1,	3.7037,    	2.83168466,	0,		0,                  0,                  0,                  0,                  0,                  0,                          	0,        	0,        	0,	0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.yd3	     	=        	["Cubic Yard",	          201.974,            764.5549,		0,                  0,                  27,        	0,        1,         	0.764555,           764554.9,		0,                  0,                  0,                  0,                  0,                  0,                          	0,        	0,        	0,	0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.m3		=        	["Cubic Meter",	          264.172052,	1000,               6.28981077,	35.3146667,	35.3146667,	0,	1.3079511,          1,                  1000000,		0,                  0,                  0,                  0,                  0,                  0,                          	0,        	0,        	0,	0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.cm3	     	=        	["Cubic Centimeter",	0.000264172,	0,		0,		0,        	0,                  0,        1.31E-06,  	0.000001,           1,		0,                  0,                  0,                  0,                  0,                  0,                          	0,        	0,        	0,	0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.t		=        	["Metric Ton",		0,                  0,                  0,                  0,                  0,                  0,         0,                  0,                 0,		1,                  1000,      	2204.62262,	1.10231131,	0.984206528,	1000000,			0,		0,		0,	0,	0,	          0,	          0,	          0,                  0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]
		self.kg		=        	["Kilogram",		0,                  0,                  0,                  0,                  0,                  0,         0,                  0,                 0,		0.001,     	1,        	2.20462262,	0.00110231131,	0.000984206528,	1000,			0,		0,		0,	0,	0,	          0,	          0,	          0,                  0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]
		self.lb		=        	["Pound",			0,                  0,                  0,                  0,                  0,                  0,         0,                  0,                 0,		0.00045359237,	0.45359237,	1,        	0.0005,   	0.000446428571,	453.59237,		0,		0,		0,	0,	0,	          0,	          0,	          0,                  0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]
		self.ton	     	=        	["Short Ton",		0,                  0,                  0,                  0,                  0,                  0,         0,                  0,                 0,		0.90718474,	907.18474, 	2000,     	1,        	0.892857143,	907184.74,		0,		0,		0,	0,	0,	          0,	          0,	          0,                  0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]
		self.LT		=        	["Long Ton",		0,                  0,                  0,                  0,                  0,                  0,         0,                  0,                 0,		1.01604691,	1016.04691,	2240,     	1.12,     	1,	          1016046.91,		0,		0,		0,	0,	0,	          0,	          0,	          0,                  0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]	
		self.g		=        	["Gram",			0,                  0,                  0,                  0,                  0,                  0,         0,                  0,                 0,	          0.000001,   	0.001,     	453.59237,          0,        	0,		1,			0,		0,		0,	0,	0,	          0,	          0,	          0,                  0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]	
		self.mi		=        	["Mile",			0,		0,		0,		0,                  0,                  0,         0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	1,                   0.868976, 	1609.344, 1.609344,	0,	          0,	          0,	          0,		0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]			
		self.nm		=        	["Nautical Mile",		0,		0,		0,		0,                	0,                  0,         0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	1.150779,            1,        	1852,     1.852,	0,	          0,	          0,	          0,		0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]			
		self.m		=        	["Meter",			0, 		0,		0,		0,                 	0,                  0,         0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	0.000621,            0.00054,  	1,        0.001,	0,	          0,	          0,	          0,		0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]			
		self.km		=        	["Kilometer",		0,  		0,		0,		0,               	0,                  0,         0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	0.621371192,         0.539957, 	1000,     1,	0,	          0,	          0,	          0,		0,	          0,        	0,	          0,        	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]			
		self.kWh	     	=        	["Kilowatt-hour",		0,		0,		0,		0,                	0,                  0,         0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,       	1,	          0.001,	          0.000001,	          0.0341214163,	3412.14163,	0.00341214163,	3.6,	          0.0036,		0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]		
		self.MWh	     	=        	["Megawatt-hour",		0,          	0,		0,		0,         	0,                  0,         0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        1000,	          1,	          0.001,	          34.1214163,	3412141.63,	3.41214163,	3600,	          3.6,		0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]		
		self.GWh	     	=        	["Gigawatt-hour",		0,          	0,		0,		0,         	0,                  0,         0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        1000000,	          1000,	          1,	          34121.4163,	3412141630,	3412.14163,	3600000,	          3600,		0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]		
		self.therm	=        	["Therm",			0,              	0,		0,		0,     		0,                  0,	 0,                  0,                 0,        	0,                  0,                 0,		0,		0,		0,                          	0,		0,                  0,        0,        29.307107,          0.029307107,	0.000029307107,	1,	          100000,   	0.1,      	105.505585,	0.105505585,	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]			
		self.BTU	     	=        	["BTU",			0,              	0,		0,		0,     		0,                  0,         0,                  0,                 0,         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,        0,        0.00029307107,	0.00000029307107,	0.00000000029307107,0.00001,  	1,        	0.000001, 	0.00105505585,	0.00000105505585,	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]			
		self.MMBTU	=        	["MMBTU",			0,              	0,		0,		0,     		0,                  0,         0,                  0,                 0,         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        293.07107,          0.29307107,	0.00029307107,	10,       	1000000,  	1,        	1055.05585,	1.05505585,	0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]			
		self.MJ		=        	["Megajoule",		0,          	0,		0,		0,        	0,                  0,         0,                  0,                 0,         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,       	0,        0.277777778,	0.000277777778,	0.000000277777778,	0.0094781712,	947.81712,	0.00094781712,	1,        	0.001,		0,	          0,        	0,        	0,	          0,        0,                  0,                  0,                  0,                 	0]		
		self.GJ		=        	["Gigajoule",		0,          	0,		0,		0,        	0,                  0,         0,                  0,                 0,         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,       	0,        277.777778,	0.277777778,	0.000277777778,	9.4781712,	947817.12,	0.94781712,	1000,     	1,		0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                  0]								
		self.tmi	     	=        	["Tonne Mile",		0,      		0,		0,		0,            	0,                  0,	 0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        0,		0,		0,		0,		0,                  0,                  0,                  0,	          1,        	1.10231131,	1.77399809,	1.609344,           0,        0,                  0,                  0,                  0,                  0]
		self.tonmi	=        	["Short Ton Mile",		0,      		0,		0,		0,            	0,                  0,	 0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        0,		0,		0,		0,		0,                  0,                  0,                  0,	          0.9071847408,	1,        	1.609344001,	1.459972319,        0,        0,                  0,                  0,                  0,                  0]	          	
		self.tonkm	=        	["Short Ton Kilometer",	0,  		0,		0,		0,		0,                  0,         0,                  0,                 0,         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        0,		0,		0,		0,		0,                  0,                  0,                  0,		0.5636984637,	0.621371192,	1,        	0.90718474,         0,        0,                  0,                  0,                  0,                  0]
		self.tkm	     	=        	["Tonne Kilometer",		0,      		0,		0,		0,            	0,                  0,         0,                  0,                 0,         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        0,		0,		0,		0,		0,                  0,                  0,                  0,		0.621371192,	0.6849444926,	1.10231131,	1,                  0,        0,                  0,                  0,                  0,                  0]
		self.pmi	     	=        	["Passenger Mile",		0,      		0,		0,		0,            	0,                  0,         0,                  0,                 0,         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        0,		0,		0,		0,		0,                  0,                  0,                  0,		0,		0,	          0,                  0,                  1,        0,                  0,                  0,                  0,                  0]
		self.MPG	     	=        	["Miles per Gallon",	0,      		0,		0,		0,            	0,                  0,         0,                  0,                 0,         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        0,		0,		0,		0,		0,                  0,                  0,                  0,		0,		0,		0,	          0,                  0,        1,	          2.35214583,	0,		0,                  0]
		self.Lkm	     	=        	["Liters per Kilometer",	0,  		0,		0,		0,                	0,                  0,	 0,                  0,                 0,	         	0,                  0,                 0,		0,		0,		0,                  	0,		0,                  0,	0,        0,		0,		0,		0,		0,                  0,                  0,                  0,		0,		0,		0,	          0,                  0,	2.35214583,	1,		0,        	0,                  0]
		self.sqFt	     	=        	["Square Foot",		0,                  0,                  0,                  0,                  0,                  0,         0,                  0,                 0,		0,		0,		0,                  0,                  0,                  0,                 	       	0,	        	0,		0,	0,	0,		0,                  0,                  0,                  0,		0,		0,		0,	          0,                  0,	        	0,         	0,		0,	0,		0,                 	1,        	0.00002295684114,	0.000009290304]
		self.acre	     	=        	["Acre",			0,                  0,                  0,                  0,                  0,                  0,         0,                  0,                 0,		0,		0,		0,                  0,                  0,                  0,                 	       	0,	        	0,		0,	0,	0,		0,                  0,                  0,                  0,		0,		0,		0,	          0,                  0,	        	0,                  0,		0,	0,		0,                  43560,     	1,         	0.4046863]
		self.ha		=        	["Hectare",		0,                  0,                  0,                  0,                  0,                  0,         0,                  0,                 0,		0,		0,		0,                  0,                  0,                  0,                 	       	0,	        	0,		0,	0,	0,		0,                  0,                  0,                  0,		0,		0,		0,	          0,                  0,	        	0,              	0,		0,	0,		0,                  107639.1042,	2.471044,  	1]
	
	def makeDataFrame(self):
		listTableConvertion=[self.galUS  ,self.L		,self.brl ,self.scf ,self.ft3 ,self.ccf ,self.yd3 ,self.m3,self.cm3,self.t,self.kg	 ,self.lb	 ,self.ton ,self.LT	 ,self.g	
		        ,self.mi	 ,self.nm	 ,self.m	 ,self.km	 ,self.kWh ,self.MWh ,self.GWh ,self.therm ,self.BTU ,self.MMBTU ,self.MJ	 ,self.GJ	 ,self.tmi ,self.tonmi ,self.tonkm ,self.tkm 
				,self.pmi ,self.MPG ,self.Lkm ,self.sqFt ,self.acre ,self.ha]
		dFFuelMont=pd.DataFrame(listTableConvertion)

		return dFFuelMont																																						
	#2. Standard unit conversions - Mass, Volume, Energy, Distance, Other																																					
	#	Unit Conversions																																				
	#	2	3	4	5																																	
	#Mass																																					
	#Lookup name	Convert From 	Convert To	Multiply By	Units	


class fuelMount():
	def __init__(self) -> None:
		self.galUS	     =        ["US Gallon", 	          1,	          3.78541178,	0.0238095238,	0.133680556,	0.133680556,	0,	0.004951,  	0.00378541178,	3785.41178,	0,                  0,                  0,                  0,                  0,                  0,                  0,         0,       0,        0,        0,        0,        0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																				
		self.L		     =        ["litre",      	          0.264172052,	1,	          0.00628981077,	0.0353146667,	0.0353146667,	0,	0.001308,  	0.001,		0,		0,                  0,                  0,                  0,                  0,                  0,                  0,         0,       0,        0,        0,        0,        0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																									
		self.brl	     =        ["Barrel",    	          42,	          158.987295,	1,        	5.61458333,	5.61458333,	0,	0,                  0.158987295,        0,		0,                  0,                  0,                  0,                  0,                  0,                  0,         0,       0,        0,        0,        0,        0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																											
		self.scf	     =        ["Standard Cubic Foot",	7.48051948,	28.3168466,	0.178107607,	1,         	1,		0,	0,                  0.0283168466,	0,		0,                  0,                  0,                  0,                  0,                  0,                  0,         0,       0,        0,        0,        0,        0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.ft3	     =        ["Cubic Foot",	          7.48051948,	28.3168466,	0.178107607,	1,         	1,         	0,	0.037037,           0.0283168466,	0,		0,                  0,                  0,                  0,                  0,                  0,                  0,         0,       0,        0,        0,        0,        0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.ccf	     =        ["Hundred Cubic Feet",	748.051948,	2831.68466,	17.8107607,	100,       	100,                1,	3.7037,    	2.83168466,	0,		0,                  0,                  0,                  0,                  0,                  0,                  0,         0,       0,        0,        0,        0,        0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.yd3	     =        ["Cubic Yard",	          201.974,            764.5549,		0,                  0,                  27,        	0,        1,         	0.764555,           764554.9,		0,                  0,                  0,                  0,                  0,                  0,                  0,         0,       0,        0,        0,        0,        0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
		self.m3		     =        ["Cubic Meter",	          264.172052,	1000,               6.28981077,	35.3146667,	35.3146667,	0,	1.3079511,          1,                  1000000,		0,                  0,                  0,                  0,                  0,                  0,                  0,         0,       0,        0,        0,        0,        0,        0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,                  0,        0,                  0,                  0,                  0,                         0]																										
	
	
	def makeDataFrame(self):

		listFuelMont=[self.galUS,self.L	,self.brl,self.scf,self.ft3,self.ccf,self.yd3,self.m3	]
		dFFuelMont=pd.DataFrame(listFuelMont)

		return dFFuelMont



class Masa():
	def __init__(self) -> None:
																																	
		self.lbyToG		=         ["lb",	         "g",                 453.59237, 	"gram per pound"]
		self.lbyToKg			=["lb",	         "kg",      	0.45359237,	"kilogram per pound"]
		self.lbyToMetricTon		=         ["lb",	         "metric ton",	0.00045359237,	"metric ton / pound"]
		self.kgyToLb	   	=         ["kg",	         "lb",      	2.20462262,	"pound per kilogram"]
		self.kgyToMetricTon		=         ["kg",	         "metric ton",	0.001,     	"kilogram per metric ton"]
		self.shortTonToLb		=         ["shortTon",       "lb",      	2000,      	"lb / short ton"]
		self.shortTonToKg		=         ["shortTon",       "kg",      	907.18474, 	"kg / short ton"]
		self.metricTonToLb		=         ["metricTon",      "lb",      	2204.62262,	"lb / metric ton"]
		self.metricTonToKg		=         ["metricTon",      "kg",      	1000,      	"kg / metric ton"]
		self.metricTonToShortTon	=         ["metricTon",      "shortTon",          1.10231131,	"short ton / metric ton"]

	def makeDataFrame(self):
		listMasa=[self.lbyToG	,self.lbyToKg	,self.lbyToMetricTon	,self.kgyToLb	   ,self.kgyToMetricTon	,self.shortTonToLb	,self.shortTonToKg	,self.metricTonToLb	,self.metricTonToKg	,self.metricTonToShortTon]
		dFVolumen=pd.DataFrame(listMasa)

		return dFVolumen



	#Volume																																					
#Lookup name	Convert From 	Convert To	Multiply By	Units

class volumen():
	def __init__(self) -> None:
																																		

		self.scfToGalUS			=	["scf",	"galUS",	7.48051948,	"US gallon per standard cubic foot"]
		self.scfToBbl  			=	["scf",	"bbl",	0.178107607,	"barrel per standard cubic foot"]
		self.scfToL    			=	["scf",	"L",	28.3168466,	"liter per standard cubic foot"]
		self.scf_tom3  			=	["scf",	"m3",	0.0283168466,	"cubic meter per standard cubic foot"]
		self.galUS_to_bbl		=	["galUS",	"bbl",	0.0238,	          "barrel per US gallon"]
		self.galUS_to_L			=	["galUS",	"L",	3.78541178,	"liter per US gallon"]
		self.galUS_to_m3		=	["galUS",	"m3",	0.00378541178,	"cubic meter per US gallon"]
		self.bbl_to_galUS		=	["bbl",	"galUS",	42,	          "US gallon per barrel"]
		self.bbl_to_L			=	["bbl",	"L",	158.987295,	"liter per barrel"]
		self.bbl_to_m3			=	["bbl",	"m3",	0.158987295,	"cubic meter per barrel"]
		self.L_to_m3			=	["L",	"m3",	0.001,	          "cubic meter per liter"]
		self.L_to_galUS			=	["L",	"galUS",	0.264172052,	"US gallon per liter"]
		self.m3_to_bbl        	=   ["m3",	"bbl",	6.28981077,	"barrel per cubic meter"]
		self.m3_to_galUS		=	["m3",	"galUS",	264.172052,	"US gallon per cubic meter"]
		self.m3_to_L             =  ["m3",     "L",	1000,     	"liter per cubic meter"]
		self.galUS_to_galUS      =	["galUS",	"gal US",	1,                  ""]																																		
		self.m3_to_m3            =	["m3",	"m3",	1,                  ""]																																		
		self.L_to_L              =	["L",	"L",	1,                  ""]
		self.galUS_to_scf        =	["galUS",	"scf",	0.1336805556,                 ""]
		self.L_to_scf            =	["L",	"scf",	0.03531466671,                ""]
		self.ccf_to_scf          =	["ccf",	"scf",	100,                ""]
		self.m3_to_scf           =        	["m3",	"scf",	35.31466671,                  ""]
	
	def makeDataFrame(self):
		dataframeList=[self.scfToGalUS,self.scfToBbl  	,self.scfToL    	,self.scf_tom3  	,self.galUS_to_bbl	,self.galUS_to_L	
		,self.galUS_to_m3	,self.bbl_to_galUS	,self.bbl_to_L	,self.bbl_to_m3	,self.L_to_m3	,self.L_to_galUS	,self.m3_to_bbl	,self.m3_to_galUS	,self.m3_to_L       ,self.galUS_to_galUS,self.m3_to_m3      ,self.L_to_L        ,self.galUS_to_scf  ,self.L_to_scf      ,self.ccf_to_scf    ,self.m3_to_scf  ]
		dataVolume=pd.DataFrame(dataframeList)
		
		return dataVolume
class Energy():
	def __init__(self) -> None:
		pass
																																						
#	Energy																																					
#                   Lookup name	Convert From 	Convert To	Multiply By	Units																																	
		self.kWh_to_Btu	=         ["kWh",	"Btu",	3412.14163,	"Btu / kWh"]
		self.kWh_to_KJ	          =         ["kWh",	"KJ",	3600      ,	"KJ / kWh"]
		self.MJ_to_GJ            =         ["MJ",	"GJ",	0.001     ,	"GJ / MJ"]
		self.MJ_to_mmBtu	=         ["MJ",	"mmBtu",	0.00094781712,	"mmBtu / MJ"]
		self.GJ_to_mmBtu	=         ["GJ",	"mmBtu",	0.94781712,	"mmBtu / GJ"]
		self.kWh_to_mmBtu	=         ["kWh",	"mmBtu",	0.00341214163,	"mmBtu / kWh"]
		self.MWh_to_mmBtu	=         ["MWh",	"mmBtu",	3.41214163,	"mmBtu / MWh"]
		self.Btu_to_mmBtu	=         ["Btu",	"mmBtu",	0.000001  ,	"mmBtu / Btu"]
		self.MJ_to_kWh 	=         ["MJ",	"kWh",	0.277777778,	"kWh / MJ"]
		self.GJ_to_kWh 	=         ["GJ",	"kWh",	277.777778,	"kWh / GJ"]
		self.mmBtu_to_GJ	=         ["mmBtu",	"GJ",	1.05505585,	"GJ / mmBtu"]
		self.mmBtu_to_kWh	=         ["mmBtu",	"kWh",	293.07107 ,	"kWh / mmBtu"]
		self.MWh_to_kWh	=         ["MWh",	"kWh",	1000      ,	"kWh / MWh"]
		self.therm_to_Btu	=         ["therm",	"Btu",	100000    ,	"Btu / therm"]
		self.therm_to_GJ	=         ["therm",	"GJ",	0.105505585,	"GJ / therm"]
		self.therm_to_kWh	=         ["therm",	"kWh",	29.307107 ,	"kWh / therm"]
		self.kWh_to_MWh	=         ["kWh",	"MWh",	0.001     ,	"MWh / kWh"]
		self.MWh_to_MWh	=         ["MWh",	"MWh",	1         ,	"MWh / MWh"]
		self.BTU_to_MWh	=         ["BTU",	"MWh",	0.00000029307107,	"MWh / BTU"]
		self.BTU_to_kWh	=         ["BTU",	"kWh",	0.00029307107,	"kWh / BTU"]
		self.MMBTU_to_MWh	=         ["MMBTU",	"MWh",	0.29307107,	"MWh / MMBTU"]
		self.GJ_to_MWh 	=         ["GJ",	"MWh",	0.277777778,	"MWh / GJ"]
		self.therm_to_MWh	=         ["therm",	"MWh",	0.029307107,	"MWh / therm"]
		self.kWh_to_therm	=         ["kWh",	"therm",	0.03412141635,	"therm / kWh"]
		self.MWh_to_therm	=         ["MWh",	"therm",	34.12141635,	"therm / MWh"]
		self.BTU_to_therm	=         ["BTU",	"therm",	0.00001   ,	"therm / BTU"]
		self.mmBtu_to_therm	=         ["mmBtu",	"therm",	10        ,	"therm / mmBtu"]
		self.MJ_to_therm	=         ["MJ",	"therm",	0.0094781712,	"therm / MJ"]
		self.GJ_to_therm	=         ["GJ",	"therm",	9.4781712,          "therm / GJ"]
		self.therm_to_therm	=         ["therm",	"therm",	1         ,	"therm / therm"]
		self.mmBtu_to_mmBtu	=         ["mmBtu",	"mmBtu",	1         ,	"mmBtu / mmBtu"]
		self.kWh_to_kWh	=         ["kWh",	"kWh",	1         ,	"kWh / kWh"]
		self.GJ_to_GJ  	=         ["GJ",	"GJ",	1         ,	"GJ / GJ"]
		self.MJ_to_MJ  	=         ["MJ",	"MJ",	1         ,	"MJ / MJ"]
		self.mmBtu_to_Btu	=         ["mmBtu",	"Btu",	1000000   ,	"Btu / mmBtu"]

	def makeDataFranme(self):
		listEnergy=[self.kWh_to_Btu	,self.kWh_to_KJ	,self.MJ_to_GJ       ,self.MJ_to_mmBtu	,self.GJ_to_mmBtu	,self.kWh_to_mmBtu	,self.MWh_to_mmBtu	,self.Btu_to_mmBtu	,self.MJ_to_kWh 	,self.GJ_to_kWh 	,self.mmBtu_to_GJ	,self.mmBtu_to_kWh	,self.MWh_to_kWh	,self.therm_to_Btu	,self.therm_to_GJ	,self.therm_to_kWh	,self.kWh_to_MWh	,self.MWh_to_MWh	,self.BTU_to_MWh	,self.BTU_to_kWh	,self.MMBTU_to_MWh	,self.GJ_to_MWh 	,self.therm_to_MWh	,self.kWh_to_therm	,self.MWh_to_therm	,self.BTU_to_therm	,self.mmBtu_to_therm	,self.MJ_to_therm	,self.GJ_to_therm	,self.therm_to_therm	,self.mmBtu_to_mmBtu	,self.kWh_to_kWh	,self.GJ_to_GJ  	,self.MJ_to_MJ  	,self.mmBtu_to_Btu	]
		dFEnergy=pd.DataFrame(listEnergy)
		return dFEnergy 


kWh_to_Btu		=         ["kWh",	"Btu",	3412.14163,	"Btu / kWh"]
kWh_to_KJ	    =         ["kWh",	"KJ",	3600      ,	"KJ / kWh"]
MJ_to_GJ        =         ["MJ",	"GJ",	0.001     ,	"GJ / MJ"]
MJ_to_mmBtu		=         ["MJ",	"mmBtu",	0.00094781712,	"mmBtu / MJ"]
GJ_to_mmBtu		=         ["GJ",	"mmBtu",	0.94781712,	"mmBtu / GJ"]
kWh_to_mmBtu	=         ["kWh",	"mmBtu",	0.00341214163,	"mmBtu / kWh"]
MWh_to_mmBtu	=         ["MWh",	"mmBtu",	3.41214163,	"mmBtu / MWh"]
Btu_to_mmBtu	=         ["Btu",	"mmBtu",	0.000001  ,	"mmBtu / Btu"]
MJ_to_kWh 		=         ["MJ",	"kWh",	0.277777778,	"kWh / MJ"]
GJ_to_kWh 		=         ["GJ",	"kWh",	277.777778,	"kWh / GJ"]
mmBtu_to_GJ		=         ["mmBtu",	"GJ",	1.05505585,	"GJ / mmBtu"]
mmBtu_to_kWh	=         ["mmBtu",	"kWh",	293.07107 ,	"kWh / mmBtu"]
MWh_to_kWh		=         ["MWh",	"kWh",	1000      ,	"kWh / MWh"]
therm_to_Btu	=         ["therm",	"Btu",	100000    ,	"Btu / therm"]
therm_to_GJ		=         ["therm",	"GJ",	0.105505585,	"GJ / therm"]
therm_to_kWh	=         ["therm",	"kWh",	29.307107 ,	"kWh / therm"]
kWh_to_MWh		=         ["kWh",	"MWh",	0.001     ,	"MWh / kWh"]
MWh_to_MWh		=         ["MWh",	"MWh",	1         ,	"MWh / MWh"]
BTU_to_MWh		=         ["BTU",	"MWh",	0.00000029307107,	"MWh / BTU"]
BTU_to_kWh		=         ["BTU",	"kWh",	0.00029307107,	"kWh / BTU"]
MMBTU_to_MWh	=         ["MMBTU",	"MWh",	0.29307107,	"MWh / MMBTU"]
GJ_to_MWh 		=         ["GJ",	"MWh",	0.277777778,	"MWh / GJ"]
therm_to_MWh	=         ["therm",	"MWh",	0.029307107,	"MWh / therm"]
kWh_to_therm	=         ["kWh",	"therm",	0.03412141635,	"therm / kWh"]
MWh_to_therm	=         ["MWh",	"therm",	34.12141635,	"therm / MWh"]
BTU_to_therm	=         ["BTU",	"therm",	0.00001   ,	"therm / BTU"]
mmBtu_to_therm	=         ["mmBtu",	"therm",	10        ,	"therm / mmBtu"]
MJ_to_therm		=         ["MJ",	"therm",	0.0094781712,	"therm / MJ"]
GJ_to_therm		=         ["GJ",	"therm",	9.4781712,          "therm / GJ"]
therm_to_therm	=         ["therm",	"therm",	1         ,	"therm / therm"]
mmBtu_to_mmBtu	=         ["mmBtu",	"mmBtu",	1         ,	"mmBtu / mmBtu"]
kWh_to_kWh		=         ["kWh",	"kWh",	1         ,	"kWh / kWh"]
GJ_to_GJ  		=         ["GJ",	"GJ",	1         ,	"GJ / GJ"]
MJ_to_MJ  		=         ["MJ",	"MJ",	1         ,	"MJ / MJ"]
mmBtu_to_Btu	=         ["mmBtu",	"Btu",	1000000   ,	"Btu / mmBtu"]

		

	#Distance																																					


#Lookup name	Convert From 	Convert To	Multiply By	Units																																	
class Disctance():
	def __init__(self):
		self.mile_to_km                              =         ["mile",            "km",	          1.609344,	          "km / mile+"]
		self.nauticalmile_to_mile                   	=         ["nm",              "mile",	          1.150779,	          "mile / nautical mile+"]
		self.km_to_mile                    		=         ["km",              "mile",	          0.621371192,	"mile / km+"]
		self.mile_to_passengermile                   =         ["mile",            "passenger-mile",	1,        	"passenger-mile / mile+"]
		self.km_to_passengerMile           		=	["km",              "passenger-mile",	0.621371192,        "passenger-mile / km+"]
		self.mile_to_vehicleMile           			=         ["mile",            "vehicle-mile",	1,        	"vehicle-mile / mile+"]
		self.km_to_vehicle_mile    	        		  =         ["km ",             "vehicle-mile",	0.621371192,       	"vehicle-mile / km+"]
		self.passenger_km_to_passenger_mile			=         ["passenger-km",	"passenger-mile",	0.621371192,	"vehicle-mile / km+"]
		self.vehicle_km_to_vehicle_mile    			=         ["vehicle-km",	"vehicle-mile",	0.621371192,	"vehicle-mile / km+"]
		self.passenger_mile_to_passenger_km			=         ["passenger-mile",	"passenger-km",	1.609344,  	"vehicle-km / mile+"]
		self.vehicleMile_to_vehicle_km      		   	=         ["vehicle-mile",	"vehicle-km",	1.609344,  	"vehicle-km / mile+"]
		self.passenger_mile_to_mile        			=    ["passenger-mile",	"mile",      	1,         	"mile / passenger-mile+"]
		self.passenger_km_to_mile          			=    ["passenger-km",	"mile",	          0.621371192,	"mile / passenger-km+"]
		self.mile_to_vehicle_km            			=    ["mile",	          "vehicle-km",	1.609344,  	"vehicle-km / mile+"]
		self.passenger_mile_to_km          			=    ["passenger-mile",	"km",        	1.609344,  	"km / passenger-mile+"]
		self.ton_mile_to_tonne_km          			=    ["ton-mile",        "tonne-km",  	1.459972,  	"tonne-km / ton-mile+"]
		self.tonne_km_to_ton_mile          			=    ["tonne-km",        "ton-mile",  	0.6849446428,	"tonne-km / ton-mile+"]
		self.galUS_to_ccf                            =	["galUS", 	"ccf",    	0.001336805556,     ""]
		self.scf_to_ccf                              =	["scf",	          "ccf",    	0.01,	          ""]
		self.kWh_to_MJ                               =	["kWh",	          "MJ",     	3.6,	"MJ / kWh"]
		self.kWh_to_GJ                               =	["kWh",	          "GJ",     	0.0036,	"GJ / kWh" ]
		self.lbCO2eMWh_to_kgCO2ekWh                  =	["lbCO2e/MWh",	"kgCO2e/kWh",	0.00045359237,       ""]
		self.mmBtu_to_MJ                             =	["mmBtu", 	"MJ",     	1000,	"MJ / mmBtu"]
		self.Btu_to_mmBtu                            =	["Btu",   	"mmBtu",  	0.000001,	"mmBtu / Btu"]
		self.therm_to_mmBtu                          =	["therm",	          "mmBtu",  	0.1,	"mmBtu / therm"]
		self.passenger_mile_to_vehicle_mile          =	["passenger-mile",	"-vehicle-mile",	1,	          "vehicle-mile / passenger-mile"]
		self.vehicle_mile_to_passenger_mile          =	["vehicle-mile",	"passenger-mile",	1,	          "passenger-mile / vehicle-mile"]
		self.passenger_km_to_vehicle_km              =	["passenger-k-m",	"vehicle-km",	1,	          "vehicle-km / passenger-km"]
		self.vehicle_km_to_passenger_km              =	["vehicle-km",	"-passenger-km",	1,	          "passenger-km / vehicle-km"]
		self.passenger_mile_to_vehicle_km            =	["passenger-mile",	"vehicle-km",	1.609344,	          "vehicle-km / passenger-mile"]
		self.vehicle_mile_to_passenger_km            =	["vehicle-mile",	"passenger-km",	1.609344,	          "passenger-km / vehicle-mile"]
		self.passenger_km_to_vehicle_mile            =	["passenger-km",	"vehicle-mile",	0.621371192,	"vehicle-mile / passenger-km"]
		self.vehicle_km_to_passenger_mile            =	["vehicle-km",	"passenger-mile",	0.621371192,	"passenger-mile / vehicle-km"]
		self.vehicleMile_to_vehicleMile		=["vehicle-mile",            "vehicle-mile",	1,        	"vehicle-mile / mile+"]


	def makeList(self):

		listDistance=[self.mile_to_km,self.nauticalmile_to_mile          ,self.km_to_mile                    ,self.mile_to_passengermile         ,self.km_to_passengerMile           ,self.mile_to_vehicleMile           ,self.km_to_vehicle_mile    	       ,self.passenger_km_to_passenger_mile,self.vehicle_km_to_vehicle_mile    ,self.passenger_mile_to_passenger_km,self.vehicleMile_to_vehicle_km     ,self.passenger_mile_to_mile        ,self.passenger_km_to_mile          ,self.mile_to_vehicle_km            ,self.passenger_mile_to_km          ,self.ton_mile_to_tonne_km          ,self.tonne_km_to_ton_mile          ,self.galUS_to_ccf                  ,self.scf_to_ccf                    ,self.kWh_to_MJ                     ,self.kWh_to_GJ                     ,self.lbCO2eMWh_to_kgCO2ekWh        ,self.mmBtu_to_MJ                   ,self.Btu_to_mmBtu
		,self.therm_to_mmBtu                ,self.passenger_mile_to_vehicle_mile,self.vehicle_mile_to_passenger_mile,self.passenger_km_to_vehicle_km    ,self.vehicle_km_to_passenger_km    ,self.passenger_mile_to_vehicle_km  ,self.vehicle_mile_to_passenger_km  ,self.passenger_km_to_vehicle_mile  ,self.vehicle_km_to_passenger_mile,self.vehicleMile_to_vehicleMile ]
		dfEnergy=pd.DataFrame(listDistance)
		return dfEnergy
	
'''dfConvertion=Disctance().makeList()


originalUnitE= dfConvertion.loc[:,0] == 'mile'
dfConvertion = dfConvertion.loc[originalUnitE]


UnitConvert=dfConvertion.loc[:,1]=="vehicle-mile"
newUnit=dfConvertion.loc[UnitConvert]
print(int(newUnit[2]))'''