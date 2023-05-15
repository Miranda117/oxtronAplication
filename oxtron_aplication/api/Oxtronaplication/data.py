import pandas as pd

class    StationaryCombustion():
        def __init__(self) -> None:
                  
                    # mmBtu per short ton [0], kg CO2 per mmBtu [1], g CH4 per mmBtu[2], g N2O per mmBtu [3]
                    # kg CO2 per short ton [4], g CH4 per short ton [5], g N2O per short ton [6]
                    #                   [0]    [1]    [2] [3]   [4]   [5] [6]
                    self.anthraciteCoal=   [25.09, 103.69, 11, 1.6, 2602, 276, 40] 
                    self.bituminousCoal=   [24.93, 93.28,  11, 1.6, 2325, 274, 40] 
                    self.subBituminousCoal=[17.25, 97.17,  11, 1.6, 1676, 190, 28] 
                    self.ligniteCoal=      [14.21, 97.72,  11, 1.6, 1389, 156, 23] 
                    self.mixedCS=	   [21.39, 94.27,  11, 1.6, 2016, 235, 34]#(Commercial Sector)	
                    self.mixedEPS=	   [19.73, 95.52,  11, 1.6, 1885, 217, 32]#(Electric Power Sector)	
                    self.mixedIC=          [26.28, 93.90,  11, 1.6, 2468, 289, 42]#(Industrial Coking)	
                    self.mixedIS=          [22.35, 94.67,  11, 1.6, 2116, 246, 36]#(Industrial Sector)	
                    self.coalCoke=         [24.80, 113.67, 11, 1.6, 2819, 273, 40]


                    #Other Fuels - Solid							
                    # mmBtu per short ton [0], kg CO2 per mmBtu [1], g CH4 per mmBtu[2], g N2O per mmBtu [3]
                    # kg CO2 per short ton [4], g CH4 per short ton [5], g N2O per short ton [6]
                    #                       [0]       [1]    [2]    [3]     [4]   [5]     [6]
                    self.municipalSolidWaste=   [9.95,    90.70 ,  32 ,  4.2 ,  902 ,  318  ,   42]
                    self.petroleumCokeSolid=    [30.00,   102.41,  32 ,  4.2 ,  3072 , 960  ,  126]
                    self.plastics	=       [38.00,   75.00 ,  32 ,  4.2 ,  2850 , 1216 ,  160]
                    self.tires	    =           [28.00,   85.97 ,  32 ,  4.2 ,  2407 , 896  ,  118]



                    # Biomass Fuels - Solid			
                    # mmBtu per short ton [0], kg CO2 per mmBtu [1], g CH4 per mmBtu[2], g N2O per mmBtu [3]
                    # kg CO2 per short ton [4], g CH4 per short ton [5], g N2O per short ton [6]				
                    #                             [0]       [1]       [2]       [3]         [4]      [5]    [6]

                    self.agriculturalByproducts    =   [8.25 ,   118.17,    32,     4.2, 	 975,     264,   35 ]
                    self.peat              	=         [8.00 ,   111.84,    32,     4.2, 	 895,     256,   34 ]
                    self.solidByproducts	      =   [10.39,	105.51,    32 ,    4.2, 	 1096,    332,   44 ]
                    self.woodAWoodResiduals	=         [17.48, 	93.80,     7.2,    3.6,        1640,    126,   63 ]

                    # Natural Gas	
                    #	mmBtu per scf[0],	kg CO2 per mmBtu[1],g CH4 per mmBtu[2], g N2O per mmBtu[3]
                    # 	kg CO2 per scf[4],g CH4 per scf [5] y g N2O per scf [6]
                                                            
                    #                             [0]	[1]    [2]     [3]     [4]       [5]        [6]
                    self.naturalGas	    = [0.001026,  53.06 , 1.0  ,  0.10,  0.05444,  0.00103 ,  0.00010 ]


                    #otherFuelsGaseous 
                    #	mmBtu per scf[0],	kg CO2 per mmBtu[1],g CH4 per mmBtu[2], g N2O per mmBtu[3]
                    # 	kg CO2 per scf[4],g CH4 per scf [5] y g N2O per scf [6]
                                                            
                    #                           [0]	       [1]	  [2]     [3]     [4]       [5]        [6]							
                    self.blastFurnaceGas       =[0.000092,  274.32, 0.022,  0.10,  0.02524,  0.000002,  0.000009 ]
                    self.cokeOvenGas          = [0.000599,  46.85 , 0.48 ,  0.10,  0.02806,  0.000288,  0.000060 ]
                    self.fuelGas	    =   [0.001388,  59.00 , 3.0  ,  0.60,  0.08189,  0.004164,  0.000833 ]
                    self.propaneGa        =  [0.002516,  61.46 , 3.0  ,  0.60,  0.15463,  0.007548,  0.001510 ]

                    #biomassFuelsGaseous
                    #	mmBtu per scf[0],	kg CO2 per mmBtu[1],g CH4 per mmBtu[2], g N2O per mmBtu[3]
                    # 	kg CO2 per scf[4],g CH4 per scf [5] y g N2O per scf [6]
                                                            
                    #                                   [0]	[1]	  [2]     [3]     [4]       [5]        [6]							
                                                                                
                    self.landfillGas 	        = [0.000485,  52.07,  3.2,   0.63,  0.025254,  0.001552,  0.000306 ]
                    self.otherBiomassGases	= [0.000655,  52.07,  3.2,   0.63,  0.034106,  0.002096,  0.000413 ]

                    #Petroleum Products 							
                    #mmBtu per gallon[0]	kg CO2 per mmBtu[1]	g CH4 per mmBtu[2]	g N2O per mmBtu[3]	kg CO2 per gallon[4]
                    # 	g CH4 per gallon[5]	g N2O per gallon[6]
                                                            
                    #                             [0]	   [1]	  [2]         [3]      [4]       [5]        [6]							

                    self.asphaltandRoadOil	   =    [ 0.158 ,	  75.36 ,	  3.0 ,	  0.60 ,	  11.91 ,	  0.47 ,	  0.09] 
                    self.aviationGasoline	   =    [ 0.120 ,	  69.25 ,	  3.0 ,	  0.60 ,	  8.31 	,  0.36 	,  0.07 ]
                    self.butane	                =       [ 0.103 ,	  64.77 ,	  3.0 ,	  0.60 ,	  6.67 	,  0.31 	,  0.06 ]
                    self.butylene	         =      [ 0.105 ,	  68.72 ,	  3.0 ,	  0.60 ,	  7.22 	,  0.32 	,  0.06 ]
                    self.crudeOil	             =  [ 0.138 ,	  74.54 ,	  3.0 ,	  0.60 ,	  10.29 ,	  0.41 ,	  0.08] 
                    self.distillateFuelOil1         =   [0.139  ,        73.25 ,        3.0 ,	  0.60, 	  10.18 	,  0.42 	,  0.08 ]
                    self.distillateFuelOil2          =  [ 0.138 ,	  73.96 ,	  3.0 ,	  0.60 ,	  10.21 ,	  0.41 ,	  0.08] 
                    self.distillateFuelOil4      =      [ 0.146 ,	  75.04 ,	  3.0 ,	  0.60 ,	  10.96 ,	  0.44 ,	  0.09] 
                    self.ethane	               =         [ 0.068 ,	  59.60 ,	  3.0 ,	  0.60 ,	  4.05 	,  0.20 	,  0.04 ]
                    self.ethylene	              =   [ 0.058 ,	  65.96 ,	  3.0 ,	  0.60 ,	  3.83 	,  0.17 	,  0.03 ]
                    self.heavyGasOils	        =     [ 0.148 ,	  74.92 ,	  3.0 ,	  0.60 ,	  11.09 ,	  0.44 ,	  0.09] 
                    self.isobutane	        =         [ 0.099 ,	  64.94 ,	  3.0 ,	  0.60 ,	  6.43 	,  0.30 	,  0.06 ]
                    self.isobutylene	        =       [ 0.103 ,	  68.86 ,	  3.0 ,	  0.60 ,	  7.09 	,  0.31 	,  0.06 ]
                    self.kerosene	        =         [ 0.135 ,	  75.20 ,	  3.0 ,	  0.60 ,	  10.15 ,	  0.41 ,	  0.08] 
                    self.keroseneTypeJetFuel     =      [ 0.135 ,	  72.22 ,	  3.0 ,	  0.60 ,	  9.75 	,  0.41 	,  0.08 ]
                    self.liquefiedPetleumGas     =      [ 0.092 ,	  61.71 ,	  3.0 ,	  0.60 ,	  5.68 	,  0.28 	,  0.06 ] #(LPG)
                    self.lubricants              =      [ 0.144 ,	  74.27 ,	  3.0 ,	  0.60 ,	  10.69 ,	  0.43 ,	  0.09] 
                    self.motorGasoline	        =     [ 0.125 ,	  70.22 ,	  3.0 ,	  0.60 ,	  8.78 	,  0.38 	,  0.08 ]
                    self.naphtha     	        =     [0.125, 	  68.02, 	  3.0, 	  0.60, 	  8.50 ,	  0.38 ,	  0.08]   #(<401 deg F)
                    self.naturalGasoline	  =     [0.110, 	  66.88, 	  3.0, 	  0.60, 	  7.36 ,	  0.33 ,	  0.07] 
                    self.otherOil 	        =         [0.139 ,	  76.22, 	  3.0 ,	  0.60 ,	  10.59 ,	  0.42, 	  0.08 ] #(>401 deg F)	
                    self.pentanesPlus	        =     [0.110 ,	  70.02 ,	  3.0 ,	  0.60 ,	  7.70 ,	  0.33 ,	  0.07 ]
                    self.petrocheFeedstocks     =       [0.125 ,	  71.02 ,	  3.0 ,	  0.60 ,	  8.88 ,	  0.38 ,	  0.08 ]   #PetrochemicalFeedstocks	
                    self.petroleumCoke	         =     [0.143 ,	  102.41,   3.0 ,	  0.60 ,	  14.64 ,	  0.43 ,	  0.09 ]
                    self.propane	          =       [0.091 ,	  62.87 ,	  3.0 ,	  0.60 ,	  5.72 ,	  0.27 ,	  0.05 ]
                    self.propylene	        =         [0.091 ,	  67.77 ,	  3.0 ,	  0.60 ,	  6.17 ,	  0.27 ,	  0.05 ]
                    self.residualFuelOil5	  =     [0.140 ,	  72.93 ,	  3.0 ,	  0.60 ,	  10.21 ,	  0.42 ,	  0.08 ]
                    self.residualFuelOil6	  =     [0.150 ,	  75.10 ,	  3.0 ,	  0.60 ,	  11.27 ,	  0.45 ,	  0.09 ]
                    self.specialNaphtha	        =     [0.125 ,	  72.34 ,	  3.0 ,	  0.60 ,	  9.04 ,	  0.38 ,	  0.08 ]
                    self.unfinishedOils	        =     [0.139 ,	  74.54 ,	  3.0 ,	  0.60 ,	  10.36 ,	  0.42 ,	  0.08 ]
                    self.usedOil	        =         [0.138, 	  74.00 ,	  3.0, 	  0.60 ,	  10.21, 	  0.41 ,	  0.08] 


                    # Biomss Fuels - Liquid
                    #mmBtu per gallon[0]	kg CO2 per mmBtu[1]	g CH4 per mmBtu[2]	g N2O per mmBtu[3]	kg CO2 per gallon[4]
                    # 	g CH4 per gallon[5]	g N2O per gallon[6]
                    #                                    [0]	[1]	  [2]         [3]     [4]       [5]        [6]							

                    self.biodieel100	          =  [0.128,        73.84, 	  1.1, 	  0.11, 	  9.45, 	  0.14, 	  0.01 ]# (100%)
                    self.ethanol100	          =  [0.084,        68.44, 	  1.1, 	  0.11, 	  5.75, 	  0.09, 	  0.01 ]# (100%)
                    self.renderedAnimalFat	=  [0.125,        71.06, 	  1.1, 	  0.11, 	  8.88, 	  0.14, 	  0.01 ]
                    self.vegetableOil	          =  [0.120,        81.55, 	  1.1, 	  0.11, 	  9.79, 	  0.13, 	  0.01 ]
                    # Biomass Fuels - 
                    #kraftPulpingLiquor, by Wood Furnish "	
                    #kg CO2 per mmBtu[0]	g CH4 per mmBtu[1]	g N2O per mmBtu[2]	
                    #                             [0]	   [1]        [2]
                    self.northAmericanSoftwood   =        [94.4, 	  1.9, 	  0.42 ]
                    self.northAmericanHardwood   =	  [93.7, 	  1.9, 	  0.42 ]
                    self.bagasse		 =        [95.5, 	  1.9, 	  0.42 ]
                    self.bamboo		         =        [93.7, 	  1.9, 	  0.42 ]
                    self.straw		         =        [95.1, 	  1.9, 	  0.42 ]
       
       
        def __call_back (self):
                dataTotal=[self.anthraciteCoal,  self.bituminousCoal,   self.subBituminousCoal,
                        self.ligniteCoal, self.mixedCS,  self.mixedEPS,	 self.mixedIC,   self.mixedIS, self.coalCoke, self.municipalSolidWaste,
                        self.petroleumCokeSolid,  self.plastics, self.tires,self.agriculturalByproducts,
                        self.peat, self.solidByproducts, self.woodAWoodResiduals, self.naturalGas, self.blastFurnaceGas,
                        self.cokeOvenGas, self.fuelGas,	self.propaneGa, self.landfillGas, self.otherBiomassGases,self.asphaltandRoadOil,
                        self.aviationGasoline, self.butane,self.butylene, self.crudeOil, self.distillateFuelOil1 , self.distillateFuelOil2 ,
                        self.distillateFuelOil4 , self.ethane, self.ethylene, self.heavyGasOils, self.isobutane,  self.isobutylene, self.kerosene, 
                        self.keroseneTypeJetFuel, self.liquefiedPetleumGas, self.lubricants,self.motorGasoline,
                        self.naphtha, self.naturalGasoline, self.otherOil,self.pentanesPlus, self.petrocheFeedstocks, self.petroleumCoke,   
                        self.propane, self.propylene, self.residualFuelOil5, self.residualFuelOil6,self.specialNaphtha, self.unfinishedOils,self.usedOil,
                        self.biodieel100, self.ethanol100, self.renderedAnimalFat, self.vegetableOil,self.northAmericanSoftwood,
                        self.northAmericanHardwood, self.bagasse,self.bamboo, self.straw]	   
                return dataTotal    

class combustiblesGaseousFuels():
        def __init__(self) -> None:
                    #Unit[0]	kg CO2e[1]	kg CO2[2]	kg CH4[3]	kg N2O[4]
                    #                                        [0]                  [1]              [2]                 [3]

                    self.CNGTonnes                          =  [   2542.04,	  2537.36,	  3.34,	            1.34    ]
                    self.CNGTonnesLitres	             =[   0.44486,	  0.44404,	  0.00058,	  0.00023]
                    self.CNGTonnesKWhNetCV	             =[   0.20428,	  0.20390,	  0.00027,	  0.00011 ]          #(Net CV)
                    self.CNGTonnesKWh 	                    =   [   0.18385,	  0.18351,	  0.00024,	  0.00010 ]          #(Gross CV)
                    self.LNGTonnes	                     =  [   2550.04,	  2545.37,	  3.34,	            1.34]
                    self.LNGTonnesLitres	             =[   1.15387,	  1.15175,	  0.00151,	  0.00060]
                    self.LNGTonnesKWhNetCV	             =[   0.20492,	  0.20455,	  0.00027,	  0.00011]
                    self.LNGTonnesKWhGrossCV	           =  [   0.18443,	  0.18409,	  0.00024,	  0.00010]
                    self.LPGTonnes	                     =  [   2936.86,	  2933.01,	  1.94,	            1.91]
                    self.LPGLitres	                       =[   1.52260,	  1.52060,	  0.00101,	  0.00099]
                    self.LPGKWh 	                     =  [   0.23029,	  0.22999,	  0.00015,	  0.00015 ]          #(Net CV)
                    self.LPGKWhGrossCV                    =     [   0.21447,	  0.21419,	  0.00014,	  0.00014 ]          #Gross CV)
                    self.NaturalGasTonnes	           =  [   2542.04,	  2537.36,	  3.34,	            1.34]
                    self.NaturalGascubicMetres            =     [   2.03053,	  2.02680,	  0.00267,	  0.00107]
                    self.NaturalGaskWhNetCV	             =[   0.20428,	  0.20390,	  0.00027,	  0.00011 ]                     #(Net CV)
                    self.NaturalGaskWhGrossCV	          =   [   0.18385,	  0.18351,	  0.00024,	  0.00010 ]          #(Gross CV)
                    self.Naturalgas100MineBleTonnes        =    [   2550.04,      2545.37,	  3.34,	            1.34    ]           #(100% mineral blend)
                    self.Naturalgas100MineBleCubicMetre   =     [   2.03693,	  2.03320,	  0.00267,            0.00107]
                    self.Naturalgas100MineBleKWhNetCV	   =[  0.20492,       0.20455,	  0.00027,            0.00011 ]                    #(Net CV)
                    self.Naturalgas100MineBleKWhGrossCV   =     [  0.18443,	  0.18409,	  0.00024,            0.00010 ]          #(Gross CV)
                    self.OtherPetroGasTonnes	             =[  2610.26,       2607.71,	  1.17,	            1.39]
                    self.OtherPetroGasLitres	             =[  0.95614,	  0.95521,	  0.00043,            0.00051]
                    self.OtherPetroGasKWhNetCV	         =    [  0.20164,	  0.20145,	  0.00009,            0.00011]
                    self.OtherPetroGasKWhGrossCV          =     [  0.18551,       0.18533,	  0.00008,            0.00010]


        def makeList(self):
                dataTola=[self.CNGTonnes, self.CNGTonnesLitres, self.CNGTonnesKWhNetCV, self.CNGTonnesKWh, self.LNGTonnes, self.LNGTonnesLitres,        
                        self.LNGTonnesKWhNetCV, self.LNGTonnesKWhGrossCV, self.LPGTonnes, self.LPGLitres,self.LPGKWh, self.LPGKWhGrossCV, self.NaturalGasTonnes, self.NaturalGascubicMetres ,
                        self.NaturalGaskWhNetCV	, self.NaturalGaskWhGrossCV,  self.Naturalgas100MineBleTonnes, self.Naturalgas100MineBleCubicMetre,
                        self.Naturalgas100MineBleKWhNetCV, self.Naturalgas100MineBleKWhGrossCV, self.OtherPetroGasTonnes,self.OtherPetroGasLitres, self.OtherPetroGasKWhNetCV, self.OtherPetroGasKWhGrossCV]
                return dataTola
class LiquidFuels ():
        def __init__(self) -> None:

                    #                                                 Unit[0]	kg CO2e[1]	kg CO2[2]	kg CH4[3]	kg N2O[4]
                    #                                                   [0]                  [1]              [2]                 [3]

                    self.aviationSpiritTonnes	              =      [3218.92,	  3127.67,	  61.46,	            29.80]
                    self.aviationSpiritLitres	              =      [2.29105,	  2.22610,	  0.04374,	  0.02121]
                    self.aviationSpiritKWhNetCV	              =      [0.25742,	  0.25013,	  0.00491,	  0.00238] #(Net CV)	
                    self.aviationSpiritKWhGrossCV	              =      [0.24455,	  0.23762,	  0.00467,	  0.00226] #(Gross CV)	
                    self.aviationTurbineFuelTonnes	              =      [3181.37,	  3149.67,	  1.91,	            29.80]
                    self.aviationTurbineFuelLitres	              =      [2.54306,	  2.51772,	  0.00152,	  0.02382]
                    self.aviationTurbineFuelKWhNetCV	             =       [0.26080,	  0.25820,	  0.00016,	  0.00244] #(Net CV)	
                    self.aviationTurbineFuelKWhGrossCV	              =      [0.24776,	  0.24529,	  0.00015,	  0.00232] #(Gross CV)	
                    self.burningOilTonnes	                        =      [3165.36,	  3149.67,	  7.85,	            7.84]
                    self.burningOilLitres	                       =       [2.54042,	  2.52782,	  0.00630,	  0.00630]
                    self.burningOilKWhNetCV	                       =       [0.25974,	  0.25845,	  0.00064,	  0.00064] #(Net CV)	
                    self.burningOilKWhGrossCV                         =     [0.24675,	  0.24553,	  0.00061,	  0.00061] #(Gross CV)
                    self.dieselAverageBiofuelBlendTonnes	     =     [3088.23,	  3047.00,            0.36,	            40.86]
                    self.dieselAverageBiofuelBlendlitres	     =     [2.59411,	  2.55956,            0.00030,	  0.03425]
                    self.dieselAverageBiofuelBlendKWhNetCV	     =     [0.26023,	  0.25677,	  0.00003,	  0.00343]          #](Net CV)	
                    self.dieselAverageBiofuelBlendKWhGrossCV	     =     [0.24462,	  0.24137,	  0.00003,	  0.00322]          #](Gross CV)
                    self.diesel100MineralDieselTonnes	               =     [3205.55,	  3164.33,            0.36,	            40.86 ]           # (100% mineral diesel)	Tonnes
                    self.diesel100MineralDiesellitres	              =      [2.68697,	  2.65242,	  0.00030,	  0.03425]
                    self.diesel100MineralDieselkWhNetCV	               =     [0.26880,	  0.26534,	  0.00003,	  0.00343 ]#(Net CV)	
                    self.diesel100MineralDieselKWhGrossCV	     =     [0.25267,	  0.24942,	  0.00003,	  0.00322 ]#( Gross CV)	
                    self.fuelOilTonnes	                                =      [3217.82,	  3205.85,            4.16,	            7.81]
                    self.fuelOilLitres	                                =      [3.17966,	  3.16784,	  0.00411,	  0.00771]
                    self.fuelOilKWhNetCV	                         =     [0.28492,	  0.28386,	  0.00037,	  0.00069 ] #(Net CV)	 
                    self.fuelOilKWhGrossCV	                         =     [0.26782,	  0.26683,	  0.00035,	  0.00065 ] #(Gross CV)
                    self.gasOilTonnes	                                =     [3229.86,	  3190.00,	  3.43,	            36.43]
                    self.gasOilTonnesLitres	                         =     [2.75821,	  2.72417,	  0.00293,	  0.03111]
                    self.gasOilTonnesKWhNetCV	                        =     [0.27315,	  0.26978,	  0.00029,	  0.00308  ]  #(Net CV)
                    self.gasOilTonnesKWhGrossCV	                        =     [0.25676,	  0.25359,	  0.00027,	  0.00290  ]  #(Gross CV)
                    self.lubricantsTonnes	                        =      [3181.89,	  3171.09,	  3.19,	            7.61]
                    #self.lubricantsLitres			=	[],
                    self.lubricantsKWhNetCV	                         =     [0.26909,	  0.26818,	  0.00027,	  0.00064  ]  #(Net CV)
                    self.lubricantsKWhGrossCV	                        =      [0.25294,	  0.25208,	  0.00025,	  0.00061  ]  #(Gross CV)
                    self.naphthaTonnes	                                =      [3142.87,	  3131.33,	  3.41,	            8.13]
                    #self.naphthalitres				[],
                    self.naphthakWhNetCV	                     =         [0.24894,	  0.24803,	  0.00027,	  0.00064  ]  #(Net CV)
                    self.naphthakWhGrossCV	                          =    [0.23650,	  0.23563,	  0.00026,	  0.00061  ]  #(Gross CV)
                    self.petrolAverageBiofuelBlendTonnes	      =    [2997.50,	  2979.53,	  9.37,	            8.60]
                    self.petrolAverageBiofuelBlendLitres	      =    [2.20904,	  2.19585,	  0.00688,	  0.00631]
                    self.petrolAverageBiofuelBlendKWhNetCV	      =    [0.24603,	  0.24458,	  0.00075,	  0.00069]    #(Net CV)
                    self.petrolAverageBiofuelBlendKWhGrossCV	      =    [0.23373,	  0.23235,	  0.00072,	  0.00066 ]   #(Gross CV)
                    self.petrol100MineralPetrolTonnes	               =     [3152.96,	  3135.00,	  9.37,	            8.60]
                    self.petrol100MineralPetrollitres	           =         [2.31495,	  2.30176,	  0.00688,	  0.00631]
                    self.petrol100MineralPetrolKWhNetCV	                =    [0.25367,	  0.25223,	  0.00075,	  0.00069]    #(Net CV)
                    self.petrol100MineralPetrolKWhGrossCV	     =     [0.24099,	  0.23961,	  0.00072,	  0.00066]    #(Gross CV)
                    self.processedFuelOilsResidualOilTonnes	     =     [        3217.82,	  3205.85,	  4.16,	            7.81]
                    self.processedFuelOilsResidualOillitres	        =   [3.17966,	  3.16784,	  0.00411,	  0.00771]
                    self.processedFuelOilsResidualOilkWhNetCV	       =   [0.28492,	  0.28386,	  0.00037,	  0.00069]     #(Net CV)
                    self.processedFuelOilsResidualOilkWhGrossCV	       =   [0.26782,            0.26683,	  0.00035,	  0.00065   ]  #(Gross CV)
                    self.processedFuelOilsDistillateOilTonnes	       =   [3229.86,	  3190.00,	  3.43,	            36.43]
                    self.processedFuelOilsDistillateOilLitres	       =   [2.75821,	  2.72417,	  0.00293,	  0.03111]
                    self.processedFuelOilsDistillateOilKWhNetCV	          =[0.27315,	  0.26978,	  0.00029,	  0.00308]      #(Net CV)
                    self.processedFuelOilsDistillateOilKWhGrossCV	=          [0.25676,	  0.25359,	  0.00027,	  0.00290   ]   #(Gross CV)
                    self.refineryMiscellaneousTonnes	                =   [2944.82,	  2933.33,	  3.39,	            8.09]
                    #self.efineryMiscellaneousLitres			=[	,
                    self.refineryMiscellaneousKWhNetCV	                =       [0.25966,	  0.25864,	  0.00030,	  0.00071]       #(Net CV)
                    self.refineryMiscellaneousKWhGrossCV	      =    [0.24667,	  0.24571,	  0.00028,	  0.00068   ]    #(Gross CV)
                    self.wasteOilsTonnes	                            =   [3225.02,	  3171.09,	  3.19,	            50.74]
                    #self.wasteOilsLitres	=			[
                    self.wasteOilsKWhNetCV	                          =    [0.28556,	  0.28078,	  0.00028,	  0.00449]        #(Net CV)
                    self.wasteOilsKWhGrossCV	                          =    [0.26842,	  0.26393,	  0.00027,	  0.00422 ]       #(Gross CV)
                    self.marineGasOilTonnes	                          =    [3250.08,	  3205.99,	  0.82,	            43.27]
                    self.marineGasOillitres	                          =    [2.77547,	  2.73782,	  0.00070,	  0.03695]
                    self.marineGasOilKWhNetCV	                        = [0.27486,	  0.27113,	  0.00007,	  0.00366 ]      #(Net CV)
                    self.marineGasOilKWhGrossCV	                        = [0.25836,	  0.25486,	  0.00007,	  0.00344  ]     #(Gross CV)
                    self.marineFuelOilTonnes	                        =  [3159.55,	  3113.99,	  1.28,	            44.29]
                    self.marineFuelOilLitres	                             = [3.12209,	  3.07707,	  0.00126,	  0.04376]
                    self.marineFuelOilKWhNetCV	                        =     [0.27976,	  0.27573,	  0.00011,	  0.00392 ]      #(Net CV)
                    self.marineFuelOilKWhGrossCV	               =     [0.26298,	  0.25918,	  0.00011,	  0.00369  ]     #(Gross CV)

        def makeList(self):
                dataTola=[self.aviationSpiritTonnes, self.aviationSpiritLitres, self.aviationSpiritKWhNetCV, self.aviationSpiritKWhGrossCV,
                self.aviationTurbineFuelTonnes, self.aviationTurbineFuelLitres,	self.aviationTurbineFuelKWhNetCV, self.aviationTurbineFuelKWhGrossCV,self.burningOilTonnes,
                self.burningOilLitres, self.burningOilKWhNetCV	               ,self.burningOilKWhGrossCV                  ,self.dieselAverageBiofuelBlendTonnes,self.dieselAverageBiofuelBlendlitres,self.dieselAverageBiofuelBlendKWhNetCV,
                self.dieselAverageBiofuelBlendKWhGrossCV,self.diesel100MineralDieselTonnes	       ,self.diesel100MineralDiesellitres	       ,self.diesel100MineralDieselkWhNetCV	       ,self.diesel100MineralDieselKWhGrossCV,self.fuelOilTonnes	                       ,self.fuelOilLitres, 
                self.fuelOilKWhNetCV	               ,self.fuelOilKWhGrossCV	               ,self.gasOilTonnes	                       ,self.gasOilTonnesLitres	               ,self.gasOilTonnesKWhNetCV	               ,self.gasOilTonnesKWhGrossCV	               ,self.lubricantsTonnes	        ,self.lubricantsKWhNetCV	     
                ,self.lubricantsKWhGrossCV	               ,self.naphthaTonnes	                       				,self.naphthakWhNetCV	               ,self.naphthakWhGrossCV	               ,self.petrolAverageBiofuelBlendTonnes,self.petrolAverageBiofuelBlendLitres,self.petrolAverageBiofuelBlendKWhNetCV,self.petrolAverageBiofuelBlendKWhGrossCV,self.petrol100MineralPetrolTonnes	       ,self.petrol100MineralPetrollitres	       ,self.petrol100MineralPetrolKWhNetCV	       ,self.petrol100MineralPetrolKWhGrossCV,self.processedFuelOilsResidualOilTonnes,self.processedFuelOilsResidualOillitres,self.processedFuelOilsResidualOilkWhNetCV,self.processedFuelOilsResidualOilkWhGrossCV,self.processedFuelOilsDistillateOilTonnes,self.processedFuelOilsDistillateOilLitres,self.processedFuelOilsDistillateOilKWhNetCV,self.processedFuelOilsDistillateOilKWhGross,self.refineryMiscellaneousTonnes	       ,self.refineryMiscellaneousKWhNetCV	       ,self.refineryMiscellaneousKWhGrossCV,self.wasteOilsTonnes,
                self.wasteOilsKWhNetCV,  self.wasteOilsKWhGrossCV,self.marineGasOilTonnes, self.marineGasOillitres,  self.marineGasOilKWhNetCV, self.marineGasOilKWhGrossCV, self.marineFuelOilTonnes,	 self.marineFuelOilLitres,     self.marineFuelOilKWhNetCV, self.marineFuelOilKWhGrossCV]        
                return dataTola

class CombustiblesSolidos():
        def __init__(self) -> None:
#                                                                         kg CO2e[0]	kg CO2[1]	kg CH4[2]	kg N2O[3]
#                                                                                       [0]          [1]           [2]              [3]                       
                    self.solidFuelscoalIndustrialTonnes	                       =      [2464.95,	  2439.07,	  6.89,   	  18.99]
                    self.solidFuelscoalIndustrialKWhNC                         =      [0.34930,	  0.34563,	  0.00098,	  0.00269] #(Net CV)
                    self.solidFuelscoalIndustrialKWhGsC     	               =      [0.33183,	  0.32835,	  0.00093,	  0.00256] #(Gross CV
                    self.solidFuelscoalElectricityGenerationTonnes	       =      [2264.93,	  2251.00,	  0.63,	            13.29]
                    self.solidFuelscoalElectricityGenerationKWhNetCV	       =      [0.32170,	  0.31972,	  0.00009,	  0.00189] #(Net CV)
                    self.solidFuelscoalElectricityGenerationKWhGroCV	       =      [0.30561,	  0.30373,	  0.00009,	  0.00179] #(Gross CV
                    self.solidFuelscoalDomesticTonnes	                       =      [2744.72,	  2505.61,	  204.22,	    34.89]
                    self.solidFuelscoalDomesticKWhNetCV	                       =      [0.36288,	  0.33127,	  0.02700,	  0.00461] #(Net CV)
                    self.solidFuelscoalDomesticKWhGrossCV	               =      [0.34473,	  0.31470,	  0.02565,	  0.00438] #(Gross CV
                    self.solidFuelscokingCoalTonnes	                       =      [3094.60,	  3073.83,	  7.45,	            13.32]
                    self.solidFuelscokingCoalKWhNetCV     	               =      [0.36841,	  0.36593,	  0.00089,	  0.00159]  #(Net CV)
                    self.solidFuelscokingCoalKWhGrossCV	                       =      [0.34998,	  0.34764,	  0.00084,	  0.00151]  #(Gross CV
                    self.solidFuelspetroleumCokeTonnes 	                       =      [3393.76,	  3384.12,	  3.02,	            6.62]
                    self.solidFuelspetroleumCokeKWhNetCV	               =      [0.35964,	  0.35861,	  0.00032,	  0.00070]   #(Net CV)
                    self.solidFuelspetroleumCokeKWhGrossCV	               =      [0.34165,	  0.34068,	  0.00030,	  0.00067]   #(Gross CV
                    self.solidFuelscoalEGeneHPCOTonnes	                       =      [2264.93,	  2251.00,	  0.63,	            13.29]  #(electricity generation - home produced coal only)
                    self.solidFuelscoalEGeneHPCOKWhNetCV	               =      [0.33853,	  0.33645,	  0.00009,	  0.00199]  #(Net CV)
                    self.solidFuelscoalEGeneHPCOKWhGrossCV	               =      [0.32161,	  0.31963,	  0.00009,	  0.00189]  #(Gross CV

        def makeList(self):
                dataTotal=[self.solidFuelscoalIndustrialTonnes, self.solidFuelscoalIndustrialKWhNC               ,                self.solidFuelscoalIndustrialKWhGsC     	     ,                self.solidFuelscoalElectricityGenerationTonnes,                self.solidFuelscoalElectricityGenerationKWhNetCV,        
                        self.solidFuelscoalElectricityGenerationKWhGroCV,                self.solidFuelscoalDomesticTonnes	             ,                self.solidFuelscoalDomesticKWhNetCV	             ,                self.solidFuelscoalDomesticKWhGrossCV	     ,                self.solidFuelscokingCoalTonnes	             ,                self.solidFuelscokingCoalKWhNetCV   ,
                        self.solidFuelscokingCoalKWhGrossCV	             ,                self.solidFuelspetroleumCokeTonnes 	             ,                self.solidFuelspetroleumCokeKWhNetCV	     ,                self.solidFuelspetroleumCokeKWhGrossCV	     ,                self.solidFuelscoalEGeneHPCOTonnes	             ,                self.solidFuelscoalEGeneHPCOKWhNetCV	     ,                self.solidFuelscoalEGeneHPCOKWhGrossCV
                  ]
                return dataTotal
class Biofuel():
        def __init__(self) -> None:


#                                                             kg CO2e
                    self.bioethanolLitres               =        [ 0.00855]
                    self.bioethanolGJ	                =        [ 0.40148]
                    self.bioethanolKg	                =        [ 0.01076]
                    self.biodieselLitre                 =        [ 0.03178]
                    self.biodieselGJ	                =        [ 0.96015]
                    self.biodieselKg	                =        [ 0.03572]
                    #self.biomethane[Litres	=]
                    self.biomethaneGJ	                 =       [ 0.10433]
                    self.biomethaneKg	                 =       [ 0.00511]
                    self.biodieselUsedCookingOilLitres	 =        [0.03178	]
                    self.biodieselGJ	                 =       [ 0.96015]
                    self.biodieselkg	                 =       [ 0.03572]
                    self.biodieselTallowLitres	         =       [ 0.03178]
                    self.biodieselGJ	                 =       [ 0.96015]
                    self.biodieselKg	                 =       [ 0.03572]
        def makeList(self):
                dataTola=[self.bioethanolLitres,
                self.bioethanolGJ	            ,self.bioethanolKg	            ,self.biodieselLitre             ,self.biodieselGJ	            ,self.biodieselKg	        
                ,self.biomethaneGJ	            ,self.biomethaneKg	            ,self.biodieselUsedCookingOilLitres,self.biodieselGJ	            ,self.biodieselkg	            ,self.biodieselTallowLitres	    ,self.biodieselGJ	            ,self.biodieselKg
                ]
                return dataTola
class Biomasa ():
        def __init__(self) -> None:
#                                                 kg CO2e
                    self.woodLogsTonnes	        =          [63.84683]
                    self.woodLogskWh	        =          [ 0.01563]
                    self.woodChipstonnes	=          [59.02902]
                    self.woodChipskWh	        =          [ 0.01563]
                    self.woodPelletsTonnes	=          [73.13523]
                    self.woodPelletskWh 	=          [ 0.01563]
                    self.grassStrawTonnes	=          [33.06449]
                    self.grassStrawKWh  	=          [ 0.00909]

                    

        def makeList(self):
                dataTola=[self.woodLogsTonnes,  
                self.woodLogskWh,self.woodChipstonnes,self.woodChipskWh,self.woodPelletsTonnes,self.woodPelletskWh ,self.grassStrawTonnes,self.grassStrawKWh]
                return dataTola

class Biogas ():
        def __init__(self) -> None:
#                                                    kg CO2e
                    self.biogasTonnes   	=  [1.14837]
                    self.biogasTWhq	        =  [0.00021]
                    self.landfillGasTonnes	=  [0.69343]
                    self.landfillKWh	        =  [0.00020]
        
        def makeList(self):
                dataTola=[self.biogasTonnes, self.biogasTWhq, self.landfillGasTonnes,self.landfillKWh	   ]
                return dataTola


class SubregionEGrid():
        def __init__(self) -> None:

#eGRID subregion acronym	eGRID subregion name	Total output emission rates										13	14	15
#		lb/MWh												
#		                                        CO2	          CH4	N2O	CO2e	AnnualNOx	OzoneSeasonNOx  SO2		kgCO2/kWh	          kgCH4/kWh 	kgN2O/kWh
                    self.AKGDASCCAlaskaGrid	          =         [1039.635,	0.082,	0.011,	1044.989,	5.47,	5.419,	1.1,		0.4715705036,	0.00003719457434,	0.00000498951607]
                    self.AKMSASCCMiscellaneous  	  =         [525.083,	0.024,	0.004,	526.963,	7.712,	7.844,	0.677,		0.2381736424,	0.00001088621688,	0.00000181436948]
                    self.AZNMWECCSouthwest	          =         [1022.355,	0.077,	0.011,	1027.548,	0.73,	0.719,	0.263,		0.4637324274,	0.00003492661249,	0.00000498951607]
                    self.CAMXWECCCalifornia	          =         [496.536,	0.034,	0.004,	498.686,	0.463,	0.414,	0.047,		0.225224941,	0.00001542214058,	0.00000181436948]
                    self.ERCTERCOTAll   	          =         [931.672,	0.066,	0.009,	936.082,	0.545,	0.554,	0.829,		0.4225993105,	0.00002993709642,	0.00000408233133]
                    self.FRCCFRCCAll    	          =         [931.842,	0.066,	0.009,	936.145,	0.356,	0.365,	0.278,		0.4226764212,	0.00002993709642,	0.00000408233133]
                    self.HIMSHICCMiscellaneous            =         [1110.689,	0.118,	0.018,	1119.077,	7.638,	7.582,	3.969,		0.5038000558,	0.00005352389966,	0.00000816466266]
                    self.HIOAHICCOahu   	          =         [1669.943,	0.18,	0.027,	1682.596,	3.515,	3.773,	7.997,		0.7574734031,	0.0000816466266,	0.00001224699399]
                    self.MROEMROEast    	          =         [1678.016,	0.169,	0.025,	1689.651,	0.88,	0.887,	0.891,		0.7611352543,	0.00007665711053,	0.00001133980925]
                    self.MROWMROWest    	          =         [1239.848,	0.138,	0.02,	1249.201,	0.977,	1.009,	1.351,		0.5623855928,	0.00006259574706,	0.0000090718474]
                    self.NEWENPCCNewEngland	          =         [522.312,	0.082,	0.011,	527.564,	0.387,	0.35,	0.136,		0.236916738,	0.00003719457434,	0.00000498951607]
                    self.NWPPWECCNorthwest	          =         [639.037, 	0.064,	0.009,	643.363,	0.58,	0.577,	0.377,		0.2898623073,	0.00002902991168,	0.00000408233133]
                    self.NYCWNPCCNYCWestchester 	  =         [596.414, 	0.022,	0.003,	597.762,	0.251,	0.249,	0.026,		0.2705288398,	0.00000997903214,	0.00000136077711]
                    self.NYLINPCCLongIsland	          =         [1184.241,  0.139,	0.018,	1193.091,	0.86,	0.828,	0.234,		0.5371626818,	0.00006304933943,	0.00000816466266]
                    self.NYUPNPCCUpstateNY	          =         [253.112, 	0.018,	0.002,	253.889,	0.136,	0.136,	0.092,		0.114809672,	0.00000816466266,	0.00000090718474]
                    self.RFCERFCEast    	          =         [715.966, 	0.061,	0.008,	719.979,	0.333,	0.288,	0.48,		0.3247567148,	0.00002766913457,	0.00000362873896]
                    self.RFCMRFCMichigan	          =         [1312.56, 	0.129,	0.018,	1321.185,	0.798,	0.792,	1.296,		0.5953672012,	0.00005851341573,	0.00000816466266]
                    self.RFCWRFCWest    	          =         [1166.096,	0.117,	0.017,	1174.029,	0.825,	0.652,	0.925,		0.5289322483,	0.00005307030729,	0.00000771107029]
                    self.RMPAWECCRockies	          =         [1273.615,	0.123,	0.018,	1281.944,	0.673,	0.689,	0.418,		0.5777020463,	0.00005579186151,	0.00000816466266]
                    self.SPNOSPPNorth   	          =         [1163.187,	0.124,	0.018,	1171.606,	0.642,	0.72,	0.333,		0.5276127481,	0.00005624545388,	0.00000816466266]
                    self.SPSOSPPSouth   	          =         [1166.582,	0.091,	0.013,	1172.755,	0.832,	0.882,	1.242,		0.5291526942,	0.00004127690567,	0.00000589670081]
                    self.SRMVSERCMississippiValley 	  =         [854.645, 	0.055,	0.008,	858.369,	0.614,	0.671,	0.96,		0.3876604511,	0.00002494758035,	0.00000362873896]
                    self.SRMWSERCMidwest	          =         [1664.15, 	0.185,	0.027,	1676.782,	1.06,	0.791,	2.488,		0.7548457425,	0.00008391458845,	0.00001224699399]
                    self.SRSOSERCSouth  	          =         [1027.928,	0.081,	0.012,	1033.471,	0.496,	0.433,	0.297,		0.4662602977,	0.00003674098197,	0.00000544310844]
                    self.SRTVSERCTennesseeValley	  =         [1031.537,	0.097,	0.014,	1038.127,	0.551,	0.504,	0.619,		0.4678973126,	0.00004399845989,	0.00000635029318]
                    self.SRVCSERCVirginiaCarolina	  =         [743.328, 	0.067,	0.009,	747.513,	0.437,	0.426,	0.263,		0.3371679092,	0.00003039068879,	0.00000408233133]
                    self.US                	          =         [947.182,	0.085,	0.012,	952.877,	0.619,	0.58,	0.675,		0.4296345282,	0.00003855535145,	0.00000544310844]

#                   self.                                      kgCO2/kWh        kgCH4/kWh     kgN2O/kWh

                    self.NewSouthWalesACT		=	[0.81,    	0,        	0]
                    self.Victoria			=	[1.02,    	0,        	0]
                    self.Queensland     		=	[0.81,    	0,        	0]
                    self.SouthAustralia 		=	[0.44,    	0,        	0]
                    self.SWISWesternAustralia   	=	[0.69,    	0,        	0]
                    self.Tasmania			=	[0.15,    	0,        	0]
                    self.NorthernTerritory		=	[0.63,    	0,        	0]

        def makeList(self):
          dataTola=[self.AKGDASCCAlaskaGrid,self.AKMSASCCMiscellaneous  ,self.AZNMWECCSouthwest	  ,self.CAMXWECCCalifornia	  ,self.ERCTERCOTAll   	  ,self.FRCCFRCCAll    	  ,self.HIMSHICCMiscellaneous    ,self.HIOAHICCOahu   	  ,self.MROEMROEast    	  ,self.MROWMROWest    	  ,self.NEWENPCCNewEngland	  ,self.NWPPWECCNorthwest	  ,self.NYCWNPCCNYCWestchester ,self.NYLINPCCLongIsland	  ,self.NYUPNPCCUpstateNY	  ,self.RFCERFCEast    	  ,self.RFCMRFCMichigan	  ,self.RFCWRFCWest    	  ,self.RMPAWECCRockies	  ,self.SPNOSPPNorth   	  ,self.SPSOSPPSouth   	  ,self.SRMVSERCMississippiValley,self.SRMWSERCMidwest	  ,self.SRSOSERCSouth  	 
                     ,self.SRTVSERCTennesseeValley,self.SRVCSERCVirginiaCarolina, self.US,self.NewSouthWalesACT,	self.Victoria		, self.Queensland     	, self.SouthAustralia 	, self.SWISWesternAustralia   , self.Tasmania,self.NorthernTerritory]
#                   
class TipoImpactoRegion():
        def __init__(self) -> None:
#                  #                                                                                             CO2    	CH4     	N2O     	        CO2e	Annual NOx	Ozone Season NOx	SO2				kgCO2/kWh	kgCH4/kWh	kgN2O/kWh
                    self.cACO2Intensity                                    =					[140	,	140,       	130					                 ]   #(g CO2 / kWh) 
                    self.cACH4ntensity                                     =					[0.01	,	0,	          0,					                 ]   #(g CH4 / kWh) 
                    self.cAN2OIntensity                                    =					[0.003	,	0,	          0,			130,	0,	0               ]    #(g N2O / kWh)
                    self.cAGenerationIntensity                             =					[140	,	140,	          130,			0.13,	0,	0                  ] #(g CO2 eq / kWh)
                    self.nLCO2Intensity                                    =					[37	,	37,	          40,					                 ]   #(g CO2 / kWh) 
                    self.nLCH4Intensity                                    =					[0.0006	,	0.0006,	          0.0006,					                 ]   #(g CH4 / kWh) 
                    self.nLN2OIntensity                                    =					[0.001	,	0.001,	          0.001,		40,	0.0006, 	0.001           ]    #(g N2O / kWh)
                    self.newfoundlandLabradorGenerationIntensity           =					[37	,	37,	          40,			0.04,	0.0000006,	0.000001           ] #(g CO2 eq / kWh)
                    self.pECO2Intensity                                    =					[25	,	7,	          14,					                 ]   #(g CO2 / kWh) 
                    self.pECH4Intensity                                    =					[0.0005	,	0.0002,	          0.0005		          	        ]   #(g CH4 / kWh) 
                    self.pEN2OIntensity                                    =					[0.0005	,	0.0001,	          0.0002,		14,	0.0005, 	0.0002          ]    #(g N2O / kWh)
                    self.princeEdwardIslandGenerationIntensity             =					[25	,	7,	          14,			0.014,	0.0000005,	0.0000002          ] #(g CO2 eq / kWh)
                    self.nSCO2Intensity                                    =					[670	,	700,	          670,					                 ]   #(g CO2 / kWh) 
                    self.nSCH4Intensity                                    =					[0.02	,	0.03,	          0.03,					                 ]   #(g CH4 / kWh) 
                    self.nSN2OIntensity                                    =					[0.01	,	0.01,	          0.01,			670,	0.03,   	0.01            ]    #(g N2O / kWh)
                    self.novaScotiaGenerationIntensity                     =					[680	,	670,	          670,			0.67,	0.00003,	0.00001            ] #(g CO2 eq / kWh)
                    self.nBCO2Intensity                                    =					[330	,	320,	          310,					                 ]   #(g CO2 / kWh) 
                    self.nBCH4Intensity                                    =					[0.02	,	0.02,	          0.02,					                 ]   #(g CH4 / kWh) 
                    self.nBN2OIntensity                                    =					[0.005	,	0.005,	          0.004,		310,	0.02,   	0.004           ]    #(g N2O / kWh)
                    self.newBrunswickGenerationIntensity                   =					[340	,	320,	          310,			0.31,	0.00002,	0.000004           ] #(g CO2 eq / kWh)
                    self.qCO2Intensity                                     =					[1.2	,	1.2,	          1.2,				                 ]   #(g CO2 / kWh) 
                    self.qCH4Intensity                                     =					[0	,	0,	          0,					                 ]   #(g CH4 / kWh) 
                    self.qN2OIntensity                                     =					[0.0001	,	0.0001,	          0.0001,		1.2,	0,      	0.0001          ]    #(g N2O / kWh)
                    self.quebecGenerationIntensity                         =					[1.3	,	1.3,	          1.3,			0.0012,	0,      	0.0000001          ] #(g CO2 eq / kWh)
                    self.oCO2Intensity                                     =					[35	,	36,	          17,					                 ]   #(g CO2 / kWh) 
                    self.oCH4Intensity                                     =					[0.01	,	0.01,	          0,				           ]   #(g CH4 / kWh) 
                    self.oN2OIntensity                                     =					[0.001	,	0.001,	          0.001,		17,	0,	        0.001           ]    #(g N2O / kWh)
                    self.ontarioGenerationIntensity                        =					[36	,	37,	          17,			0.017,	0,	        0.000001           ] #(g CO2 eq / kWh)
                    self.mCO2Intensity                                     =					[1.9	,	1.9,	          1.9,					                 ]   #(g CO2 / kWh) 
                    self.mCH4Intensity                                     =					[0.0001	,	0.0001,	          0.0001,					                 ]   #(g CH4 / kWh) 
                    self.mN2OIntensity                                     =					[0.0001	,	0.0001,	          0.0001,		1.9,	0.0001,	        0.0001          ]    #(g N2O / kWh)
                    self.manitobaGenerationIntensity                       =					[1.9	,	1.9,	          1.9,			0.0019,	0.0000001,	0.0000001          ] #(g CO2 eq / kWh)
                    self.sCO2Intensity                                     =					[650	,	650,	          650,					                 ]   #(g CO2 / kWh) 
                    self.sCH4Intensity                                     =					[0.05	,	0.05,	          0.05,					                 ]   #(g CH4 / kWh) 
                    self.sN2OItensity                                      =					[0.02	,	0.02,	          0.02,			650,	0.05,	        0.02            ]    #(g N2O / kWh)
                    self.saskatchewanGenerationIntensity                   =					[660	,	660,	          660,			0.65,	0.00005,	0.00002            ] #(g CO2 eq / kWh)
                    self.aCO2Intensity                                     =					[760	,	740,	          750,					                 ]   #(g CO2 / kWh) 
                    self.aCH4Intensity                                     =					[0.04	,	0.04,	          0.04,					                 ]   #(g CH4 / kWh) 
                    self.aN2OIntensity                                     =					[0.01	,	0.01,	          0.01,			750,	0.04,	        0.01            ]    #(g N2O / kWh)
                    self.albertaGenerationIntensity                       =					[760	,	750,	          750,			0.75,	0.00004,	0.00001            ] #(g CO2 eq / kWh)
                    self.bCCO2Intensity                                    =					[10.8	,	11.2,	          9,					                 ]   #(g CO2 / kWh) 
                    self.bCCH4Intensity                                    =					[0.003	,	0.003,	          0.003,				                 ]   #(g CH4 / kWh) 
                    self.bCN2OIntensity                                    =					[0.0008	,	0.0008,	          0.0007,		9,	0.003,	        0.0007          ]    #(g N2O / kWh)
                    self.britishColumbiaGenerationIntensity                =					[11.1	,	11,	          9.3,			0.009,	0.000003,	0.0000007          ] #(g CO2 eq / kWh)
                    self.yCO2Intensity                                     =					[43	,	43,	          48,					                 ]   #(g CO2 / kWh) 
                    self.yCH4Intensity                                     =					[0.003	,	0.003,	          0.004,					                 ]   #(g CH4 / kWh) 
                    self.yN2OIntensity                                     =					[0.01	,	0.01,	          0.01,			48,	0.004,	        0.01            ]    #(g N2O / kWh)
                    self.yukonGenerationIntensity                          =					[45	,	45,	          50,			0.048,	0.000004,	0.00001            ] #(g CO2 eq / kWh)
                    self.nTNCO2Intensity                                   =					[190	,	190,	          170,					                 ]   #(g CO2 / kWh) 
                    self.nTNCH4Intensity                                   =					[0.01	,	0.01,	          0.01,					                 ]   #(g CH4 / kWh) 
                    self.nTNN2OIntensity                                   =					[0.03	,	0.03,	          0.02,			170,	0.01,	        0.02            ]    #(g N2O / kWh)
                    self.northwestTerritoriesNunavutGenerationIntensity    =					[200	,	200,	          180,			0.17,	0.00001,	0.00002            ] #(g CO2 eq / kWh)
#                                                                                                           13  	14	15
                    self.northChinaGrid		        		           =				[0.968,	        0,	0]
                    self.chinaNortheastGrid	        			   =				[1.1082,	0,	0]
                    self.eastChinaGrid        	        			=				[0.8046,	0,	0]
                    self.centralChinaGrid	        			=				[0.9014,	0,	0]
                    self.chinaNorthwestGrid	        			=				[0.9155,	0,	0]
                    self.chinaSouthernGrid	        			=				[0.8367,	0,	0]
                    self.hainanProvinceChinaPowerGrid    			=				[0,	        0,	0]
        
        
        def makeList(self):
                dataTola=[self.cACO2Intensity                         ,self.cACH4ntensity                          ,self.cAN2OIntensity                         ,self.cAGenerationIntensity                  ,self.nLCO2Intensity                         ,self.nLCH4Intensity                         ,self.nLN2OIntensity                         ,self.newfoundlandLabradorGenerationIntensity,self.pECO2Intensity      
                        ,self.pECH4Intensity                         ,self.pEN2OIntensity                         ,self.princeEdwardIslandGenerationIntensity  ,self.nSCO2Intensity                         ,self.nSCH4Intensity                         ,self.nSN2OIntensity                         ,self.novaScotiaGenerationIntensity          ,self.nBCO2Intensity                         ,self.nBCH4Intensity                         ,self.nBN2OIntensity                         ,self.newBrunswickGenerationIntensity        ,self.qCO2Intensity                          ,self.qCH4Intensity                          ,self.qN2OIntensity                          ,self.quebecGenerationIntensity              ,self.oCO2Intensity                          ,self.oCH4Intensity                          ,self.oN2OIntensity                          ,self.ontarioGenerationIntensity             ,self.mCO2Intensity                          ,self.mCH4Intensity                          ,self.mN2OIntensity   
                        ,self.manitobaGenerationIntensity            ,self.sCO2Intensity                          ,self.sCH4Intensity                          ,self.sN2OItensity                           ,self.saskatchewanGenerationIntensity        ,self.aCO2Intensity                          ,self.aCH4Intensity                          ,self.aN2OIntensity                          ,self.albertaGenerationIntensity             ,self.bCCO2Intensity                         ,self.bCCH4Intensity                         ,self.bCN2OIntensity                         ,self.britishColumbiaGenerationIntensity     ,self.yCO2Intensity                          ,self.yCH4Intensity                          ,self.yN2OIntensity                          ,self.yukonGenerationIntensity               ,self.nTNCO2Intensity                        ,self.nTNCH4Intensity                        ,self.nTNN2OIntensity 
                        ,self.northwestTerritoriesNunavutGenerationIntensity                      ,self.northChinaGrid		  ,self.chinaNortheastGrid	  ,self.eastChinaGrid        	  ,self.centralChinaGrid	  ,self.chinaNorthwestGrid	  ,self.chinaSouthernGrid	  ,self.hainanProvinceChinaPowerGrid ]
                return dataTola

class    MobileCombustionCO2():
        def __init__(self) -> None:

#                   Fuel Type	                    kg CO2 per unit	          Unit
                    self.aviationGasoline	          =  8.31 	            #        gallon
                    self.biodiesel100	          =  9.45 	            #        gallon
                    self.compressedNaturalGasCNG	=  0.05444 	         # scf
                    self.dieselFuel	                =  10.21 	           #         gallon
                    self.ethanol100	                =  5.75 	            #        gallon
                    self.keroseneTypeJetFuel	          =  9.75     	        #  gallon
                    self.liquefiedNaturalGasLNG	=  4.50     	        #  gallon
                    self.liquefiedPetroleumGasesLPG	=  5.68     	        #  gallon
                    self.motorGasoline       	=  8.78 	            #        gallon
                    self.residualFuelOil	          =  11.27 	           #         gallon


        def makeList(self):
                dataTola=[self.aviationGasoline	      ,self.biodiesel100	      ,self.compressedNaturalGasCNG	,self.dieselFuel	              ,self.ethanol100	              ,self.keroseneTypeJetFuel	      
                          ,self.liquefiedNaturalGasLNG	,self.liquefiedPetroleumGasesLPG,self.motorGasoline       	,self.residualFuelOil	      ]
                
                return dataTola


class    MobileCombustionCH4N2OOnRoadGasolineVehicles():
        def __init__(self) -> None:
          
#                    Vehicle Typ        Year                          	CH4 Factor          N2O Factor 

                    self.GasolinePassengerCars1973_74  	               =          [0.1696, 	          0.0197]
                    self.GasolinePassengerCars1975	                   =          [0.1423, 	          0.0443]
                    self.GasolinePassengerCars1976_77	               =          [0.1406, 	          0.0458]
                    self.GasolinePassengerCars1978_79	               =          [0.1389, 	          0.0473]
                    self.GasolinePassengerCars1980	                   =          [0.1326, 	          0.0499]
                    self.GasolinePassengerCars1981	                   =          [0.0802, 	          0.0626]
                    self.GasolinePassengerCars1982	                   =          [0.0795, 	          0.0627]
                    self.GasolinePassengerCars1983	                   =          [0.0782, 	          0.0630]
                    self.GasolinePassengerCars1984_93	               =          [0.0704, 	          0.0647]
                    self.GasolinePassengerCars1994	                   =          [0.0531, 	          0.0560]
                    self.GasolinePassengerCars1995	                   =          [0.0358, 	          0.0473]
                    self.GasolinePassengerCars1996	                   =          [0.0272, 	          0.0426]
                    self.GasolinePassengerCars1997	                   =          [0.0268, 	          0.0422]
                    self.GasolinePassengerCars1998	                   =          [0.0241, 	          0.0379]
                    self.GasolinePassengerCars1999	                   =          [0.0216, 	          0.0337]
                    self.GasolinePassengerCars2000	                   =          [0.0178, 	          0.0273]
                    self.GasolinePassengerCars2001	                   =          [0.0110, 	          0.0158]
                    self.GasolinePassengerCars2002	                   =          [0.0107, 	          0.0153]
                    self.GasolinePassengerCars2003	                   =          [0.0115, 	          0.0133]
                    self.GasolinePassengerCars2004	                   =          [0.0157, 	          0.0063]
                    self.GasolinePassengerCars2005	                   =          [0.0164, 	          0.0051]
                    self.GasolinePassengerCars2006	                   =          [0.0161, 	          0.0057]
                    self.GasolinePassengerCars2007	                   =          [0.0170, 	          0.0041]
                    self.GasolinePassengerCars2008	                   =          [0.0172, 	          0.0038]
                    self.GasolinePassengerCars20082009_present	         =          [0.0173, 	          0.0036]

                    
                    self.gasolineLightDutyTrucks1973_74         	=  [0.1908, 	  0.0218] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1975	          =  [0.1634, 	  0.0513] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1976	          =  [0.1594, 	  0.0555] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1977_78        	  =  [0.1614, 	  0.0534] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1979_80        	  =  [0.1594, 	  0.0555] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1981	          =  [0.1479, 	  0.0660] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1982	          =  [0.1442, 	  0.0681] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1983	          =  [0.1368, 	  0.0722] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1984	          =  [0.1294, 	  0.0764] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1985	          =  [0.1220, 	  0.0806] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1986	          =  [0.1146, 	  0.0848] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1987_93 	  =  [0.0813, 	  0.1035] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1994	          =  [0.0646, 	  0.0982] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1995	          =  [0.0517, 	  0.0908] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1996	          =  [0.0452, 	  0.0871] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1997	          =  [0.0452, 	  0.0871] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1998	          =  [0.0412, 	  0.0778] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks1999	          =  [0.0333, 	  0.0593] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks2000	          =  [0.0340, 	  0.0607] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks2001	          =  [0.0221, 	  0.0328] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks2002	          =  [0.0242, 	  0.0378] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks2003	          =  [0.0225, 	  0.0330] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks2004	          =  [0.0162, 	  0.0098] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks2005	          =  [0.0160, 	  0.0081] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks2006	          =  [0.0159, 	  0.0088] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineLightDutyTrucks2007	          =  [0.0161, 	  0.0079] #(Vans, Pickup Trucks, SUVs)

                    self.gasolineLightDutyTrucks2008_Present	   = [0.0163, 	  0.0066] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineHeavyDutyVehicles1981	           =  [0.4604, 	  0.0497] #(Vans, Pickup Trucks, SUVs)
                    self.gasolineHeavyDutyVehicles19811982_84	   = [0.4492, 	  0.0538] 
                    self.gasolineHeavyDutyVehicles19811985_86	   = [0.4090, 	  0.0515] 
                    self.gasolineHeavyDutyVehicles19811987        =  [0.3675, 	  0.0849] 
                    self.gasolineHeavyDutyVehicles19811988_1989	  =  [0.3492, 	  0.0933] 
                    self.gasolineHeavyDutyVehicles19811990_1995	  =  [0.3246, 	  0.1142] 
                    self.gasolineHeavyDutyVehicles19811996        =  [0.1278, 	  0.1680] 
                    self.gasolineHeavyDutyVehicles19811997        =  [0.0924, 	  0.1726] 
                    self.gasolineHeavyDutyVehicles19811998        =  [0.0655, 	  0.1750] 
                    self.gasolineHeavyDutyVehicles19811999        =  [0.0648, 	  0.1721] 
                    self.gasolineHeavyDutyVehicles19812000        =  [0.0630, 	  0.1650] 
                    self.gasolineHeavyDutyVehicles19812001        =  [0.0578, 	  0.1435] 
                    self.gasolineHeavyDutyVehicles19812002        =  [0.0634, 	  0.1664] 
                    self.gasolineHeavyDutyVehicles19812003        =  [0.0603, 	  0.1534] 
                    self.gasolineHeavyDutyVehicles19812004        =  [0.0323, 	  0.0195] 
                    self.gasolineHeavyDutyVehicles19812005        =  [0.0329, 	  0.0162] 
                    self.gasolineHeavyDutyVehicles19812006        =  [0.0318, 	  0.0227] 
                    self.gasolineHeavyDutyVehicles19812007        =  [0.0333, 	  0.0134] 
                    self.gasolineHeavyDutyVehicles19812008_present= [0.0333, 	  0.0134 ]
                    
                    
                    self.gasolineMotorcycles1960_1995  	=   [0.0899, 	  0.0087]
                    self.gasolineMotorcycles1996_present	=   [0.0672, 	  0.0069]

        def makeList(self):
                dataTola=[self.GasolinePassengerCars1973_74  ,self.GasolinePassengerCars1975,self.GasolinePassengerCars1976_77,self.GasolinePassengerCars1978_79
                        ,self.GasolinePassengerCars1980,self.GasolinePassengerCars1981,self.GasolinePassengerCars1982,self.GasolinePassengerCars1983,self.GasolinePassengerCars1984_93,
                        self.GasolinePassengerCars1994,self.GasolinePassengerCars1995,self.GasolinePassengerCars1996,self.GasolinePassengerCars1997,self.GasolinePassengerCars1998,self.GasolinePassengerCars1999,self.GasolinePassengerCars2000,
                        self.GasolinePassengerCars2001,self.GasolinePassengerCars2002,self.GasolinePassengerCars2003,self.GasolinePassengerCars2004,self.GasolinePassengerCars2005,self.GasolinePassengerCars2006,self.GasolinePassengerCars2007,
                        self.GasolinePassengerCars2008,self.GasolinePassengerCars20082009_present,self.gasolineLightDutyTrucks1973_74,self.gasolineLightDutyTrucks1975	,self.gasolineLightDutyTrucks1976	,self.gasolineLightDutyTrucks1977_78,
                        self.gasolineLightDutyTrucks1979_80,self.gasolineLightDutyTrucks1981	,self.gasolineLightDutyTrucks1982	,self.gasolineLightDutyTrucks1983	,self.gasolineLightDutyTrucks1984	,self.gasolineLightDutyTrucks1985
                        ,self.gasolineLightDutyTrucks1986	,self.gasolineLightDutyTrucks1987_93,self.gasolineLightDutyTrucks1994	,self.gasolineLightDutyTrucks1995	,self.gasolineLightDutyTrucks1996	,self.gasolineLightDutyTrucks1997
                        ,self.gasolineLightDutyTrucks1998	,self.gasolineLightDutyTrucks1999	,self.gasolineLightDutyTrucks2000	,self.gasolineLightDutyTrucks2001	,self.gasolineLightDutyTrucks2002	,self.gasolineLightDutyTrucks2003
                	,self.gasolineLightDutyTrucks2004	,self.gasolineLightDutyTrucks2005	,self.gasolineLightDutyTrucks2006	,self.gasolineLightDutyTrucks2007,self.gasolineLightDutyTrucks2008_Present,self.gasolineHeavyDutyVehicles1981	       ,self.gasolineHeavyDutyVehicles19811982_84,
                        self.gasolineHeavyDutyVehicles19811985_86,self.gasolineHeavyDutyVehicles19811987     ,self.gasolineHeavyDutyVehicles19811988_1989,self.gasolineHeavyDutyVehicles19811990_1995,self.gasolineHeavyDutyVehicles19811996     ,self.gasolineHeavyDutyVehicles19811997    
                        ,self.gasolineHeavyDutyVehicles19811998     ,self.gasolineHeavyDutyVehicles19811999     ,self.gasolineHeavyDutyVehicles19812000     ,self.gasolineHeavyDutyVehicles19812001     ,self.gasolineHeavyDutyVehicles19812002     ,self.gasolineHeavyDutyVehicles19812003     
                        ,self.gasolineHeavyDutyVehicles19812004     ,self.gasolineHeavyDutyVehicles19812005     ,self.gasolineHeavyDutyVehicles19812006     ,self.gasolineHeavyDutyVehicles19812007     ,self.gasolineHeavyDutyVehicles19812008_present
                        ,self.gasolineMotorcycles1960_1995  ,self.gasolineMotorcycles1996_present]
                return dataTola

class     MobileCombustionCH4N2OOnRoadDieselAlternativeFuelVehicles():
        def __init__(self) -> None:
        #Vehicle Type	Vehicle Year	
        # "CH4 Factor (g / mile)[0]"	"N2O Factor (g / mile)"[1]
        #                                                              [0]              [1]
                self.dieselPassengerCars1960_1982            	=  [0.0006 ,          0.0012 ]
                self.dieselPassengerCars1983_1995            	=  [0.0005 ,          0.0010 ]
                self.dieselPassengerCars1996_present         	=  [0.0005 ,          0.0010 ]
                self.dieselLightDutyTrucks1960_1982	        =  [0.0011,           0.0017 ]
                self.dieselLightDutyTrucks1983_1995          	=  [0.0009 ,          0.0014 ]
                self.dieselLightDutyTrucks1996_present       	=  [0.0010 ,          0.0015 ]
                self.dieselMediumHeavyDutyVehicles1960_present	=  [0.0051 ,          0.0048 ]
                self.cNGLight_DutyVehicles               		=  [0.737,      	  0.050 ]
                self.cNGMediumHeavyDutyVehicles          		=  [1.966,      	  0.175 ]
                self.cNGBuses                            		=  [1.966,      	  0.175 ]
                self.lPGLightDutyVehicles                		=  [0.037,        	  0.067 ]
                self.lPGMediumHeavyDutyVehicles          		=  [0.066,        	  0.175 ]
                self.lNGMediumHeavyDutyVehicles          		=  [1.966,        	  0.175 ]
                self.ethanolLightDutyVehicles            		=  [0.055,        	  0.067 ]
                self.ethanolMediumHeavyDutyVehicles      		=  [0.197,        	  0.175 ]
                self.ethanolBuses                        		=  [0.197,        	  0.175 ]
                self.biodieselLightDutyVehicles		          =  [0.0005,         	  0.001 ]
                self.biodieselMediumHeavyDutyVehicles    		=  [0.005,      	  0.005 ]
                self.biodieselBuses                      		=  [0.005,        	  0.005 ]

        def makeList(self):
                dataTola=[
                        self.dieselPassengerCars1960_1982      ,self.dieselPassengerCars1983_1995      ,self.dieselPassengerCars1996_present   ,self.dieselLightDutyTrucks1960_1982,
                        self.dieselLightDutyTrucks1983_1995    ,self.dieselLightDutyTrucks1996_present ,self.dieselMediumHeavyDutyVehicles1960_present,self.cNGLight_DutyVehicles
                        ,self.cNGMediumHeavyDutyVehicles     ,self.cNGBuses                       ,self.lPGLightDutyVehicles           ,self.lPGMediumHeavyDutyVehicles     ,self.lNGMediumHeavyDutyVehicles     ,self.ethanolLightDutyVehicles       ,self.ethanolMediumHeavyDutyVehicles ,self.ethanolBuses                   ,self.biodieselLightDutyVehicles	,self.biodieselMediumHeavyDutyVehicle,self.biodieselBuses                      	
                ]
                return dataTola

class MobileCombustionCH4N2ONonRoadVehicles():
        def __init__(self) -> None:
                
        #VehicleType =	CH4 Factor 	N2O Factor 
        #Vehicle Type	"CH4 Factor (g / gallon) [0]"	"N2O Factor (g / gallon) " [1]

        #                                                [0]    [1]
                self.residualFuelOilShipsBoats	        =   [0.11 ,    0.57]
                self.GasolineShipsBoats	                =   [0.64 ,	  0.22]
                self.DieselShipsBoats	                =   [0.06 ,	  0.45]
                self.DieselLocomotives	                =   [0.80 ,	  0.26]
                self.GasolineAgriculturalEquip	        =   [1.26 ,	  0.22]
                self.DieselAgriculturalEquip	        =   [1.44 ,	  0.26]
                self.GasolineConstructionEquip	        =   [0.50 ,	  0.22]
                self.DieselConstructionEquip            =   [0.57 ,	  0.26]
                self.JetFuelAircraft	                =   [0.00 ,	  0.30]
                self.AviationGasolineAircraft	        =   [7.06 ,	  0.11]
                self.OtherGasolinineNonRoadVehicle      =   [0.50 ,	  0.22]
                self.OtherDieselNonRoadVehicles	        =   [0.57 ,	  0.26]
                self.LPGNonRoadVehicles	                =   [0.50 ,	  0.22]
                self.BiodieselNonRoadVehicles	        =   [0.57 ,	  0.26]

        def makeList(self):
                dataTola=[self.residualFuelOilShipsBoats	,self.GasolineShipsBoats	        ,self.DieselShipsBoats	        ,self.DieselLocomotives	        ,self.GasolineAgriculturalEquip	,self.DieselAgriculturalEquip	,self.GasolineConstructionEquip	
                        ,self.DieselConstructionEquip    ,self.JetFuelAircraft	        ,self.AviationGasolineAircraft	,self.OtherGasolinineNonRoadVehic,self.OtherDieselNonRoadVehicles	,self.LPGNonRoadVehicles	        ,self.BiodieselNonRoadVehicles]

                return dataTola


class BusinessTravelEmployeeCommuting ():
        def __init__(self) -> None:
        #Vehicle Type	Vehicle Year	
        #                 "CH4 Factor (g / mile)"[0]	"N2O Factor (g / mile)"[1]             
        #                                                       [0]         [1]
                self.passengerCarA                               =	  [0.343, 	  0.019 ,	  0.011 	]#vehicle-mile
                self.lightDutyTruckB              	            =     [0.472, 	  0.019 ,	  0.018 	]#vehicle-mile
                self.motorcycle          	                    =     [0.189, 	  0.070 ,	  0.007 	]#vehicle-mile
                self.intercityRailIeAmtrakC                      =     [0.140, 	  0.0087, 	  0.0031] 	#passenger-mile
                self.commuterRailD           	                =     [0.161, 	  0.0081, 	  0.0032] 	#passenger-mile
                self.transitRailIeSubwayTramE                    =     [0.119, 	  0.0025, 	  0.0017] 	#passenger-mile
                self.bus         	                            =     [0.056, 	  0.0013, 	  0.0009] 	#passenger-mile
                self.airTravelShortHaul300miles                  =     [0.225, 	  0.0039, 	  0.0072] 	#passenger-mile (< 300 miles) 
                self.airTravelMediumHaul300milesLESS2300miles    =     [0.136, 	  0.0006, 	  0.0043]    #passenger-mile
                self.airTravelLongHaul2300Miles                  =	  [0.166, 	  0.0006, 	  0.0053] 	#passenger-mile

        def makeList(self):
                datoTotal=[self.passengerCarA                         ,self.lightDutyTruckB              	   ,self.motorcycle          	           ,self.intercityRailIeAmtrakC                ,self.commuterRailD           	           ,self.transitRailIeSubwayTramE              ,self.bus         	
                                              ,self.airTravelShortHaul300miles            ,self.airTravelMediumHaul300milesLESS2300miles,self.airTravelLongHaul2300Miles              ]
                return datoTotal
        

class    UpstreamTransportationDistributionDownstreamTransportationDistribution():
        def __init__(self)-> None:

      #  Vehicle Type	"CO2 Factor (kg / unit)"[0]	"CH4 Factor (g / unit)"[1]	"N2O Factor (g / unit)"	Units[2]
          #                                     [0]         [1]         [2]
              self.MediumHeavyDutyTruck    =  [1.467, 	  0.014, 	  0.010 ]	#vehicle-mile
              self.PassengerCarA           =  [0.343, 	  0.019, 	  0.011 ]	#vehicle-mile
              self.LightDutyTruckB         =  [0.472, 	  0.019, 	  0.018 ]	#vehicle-mile
              self.MediumHeavyDutyTruckC   =  [0.202, 	  0.0020, 	  0.0015 ]	#ton-mile
              self.Rail                    =  [0.023, 	  0.0018, 	  0.0006 ]	#ton-mile
              self.WaterborneCraft         =  [0.059, 	  0.0005, 	  0.0040 ]	#ton-mile
              self.Aircraft                =  [1.308, 	  0.0000, 	  0.0402 ]	#ton-mile

        def makeList(self):
                dataTola=[ self.MediumHeavyDutyTruck ,self.PassengerCarA        ,self.LightDutyTruckB      ,self.MediumHeavyDutyTruckC
                          ,self.Rail                 ,self.WaterborneCraft      ,self.Aircraft]
                return dataTola

class ImpactoTiposCoches():
#Activity	Type	Unit	Diesel [kg CO2e	kg CO2	kg CH4 kg N2O][0]  Petrol	[kg CO2e	kg CO2	kg CH4	kg N2O][1]
# Unknown	[kg CO2e	kg CO2	kg CH4	kg N2O] [1]	Plug-in Hybrid Electric Vehicle[kg CO2e	kg CO2	kg CH4	kg N2O] [2] Battery Electric Vehicle [kg CO2e	kg CO2	kg CH4	kg N2O][3]
# 
        def __init__(self) -> None:
        #                                                                  [0]         [1]            [2]      [3]         [4]         [5]         [6]         [7]         [8]         [9]         [10]        [11]        [12]        [13]        [14]        [15]      [16]      [17]        [18]           [19]
                self.carsByMarketSegmentMiniKm                  	=  [0.11009, 	  0.10825, 	  0.000004,	  0.00184, 	  0.13975, 	  0.13905, 	  0.00032, 	  0.00038, 	  0.13958, 	  0.13887, 	  0.00032, 	  0.00039, 		0.0,			0.0,  0.0,         0.0   ,    0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentMinimiles                   	=  [0.17719, 	  0.17421, 	  0.00001 ,	  0.00297, 	  0.2249 , 	  0.22378, 	  0.00051, 	  0.00061, 	  0.22463, 	  0.22349, 	  0.00051, 	  0.00063, 		0.0,			0.0,  0.0     ,   0.0    ,    0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentsuperminiKm             	=  [0.13449, 	  0.13265, 	  0.000004,	  0.00184, 	  0.15538, 	  0.15468, 	  0.00032, 	  0.00038, 	  0.15241, 	  0.15155, 	  0.00027, 	  0.00059, 	  0.02935, 	  0.02918, 	  0.00009, 	  0.00008, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentSuperminimiles                  =  [0.21647, 	  0.21349, 	  0.00001 ,	  0.00297, 	  0.25006, 	  0.24894, 	  0.00051, 	  0.00061, 	  0.24528, 	  0.24389, 	  0.00044, 	  0.00095, 	  0.04723, 	  0.04696, 	  0.00014, 	  0.00013, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentLowerMediumKm           	=  [0.14691, 	  0.14507, 	  0.000004,	  0.00184, 	  0.18008, 	  0.17938, 	  0.00032, 	  0.00038, 	  0.16362, 	  0.16235, 	  0.00016, 	  0.00111, 	  0.064  , 	  0.06362, 	  0.0002 , 	  0.00018, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentLowerMediummiles                =  [0.23644, 	  0.23346, 	  0.00001 ,	  0.00297, 	  0.2898 , 	  0.28868, 	  0.00051, 	  0.00061, 	  0.26332, 	  0.26128, 	  0.00026, 	  0.00178, 	  0.10299, 	  0.10238, 	  0.00032, 	  0.00029, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentUpperMediumKm           	=  [0.16533, 	  0.16349, 	  0.000004,	  0.00184, 	  0.20792, 	  0.20722, 	  0.00032, 	  0.00038, 	  0.17537, 	  0.17379, 	  0.00008, 	  0.0015 , 	  0.07429, 	  0.07383, 	  0.00022, 	  0.00024, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentUpperMediumMiles                =  [0.2661 , 	  0.26312, 	  0.00001 ,	  0.00297, 	  0.33461, 	  0.33349, 	  0.00051, 	  0.00061, 	  0.28223, 	  0.27969, 	  0.00013, 	  0.00241, 	  0.11955, 	  0.11882, 	  0.00035, 	  0.00038, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentExecutiveKm             	=  [0.17525, 	  0.17341, 	  0.000004,	  0.00184, 	  0.23659, 	  0.23589, 	  0.00032, 	  0.00038, 	  0.18909, 	  0.1875 , 	  0.00008, 	  0.00151, 	  0.07546, 	  0.07502, 	  0.00023, 	  0.00021, 	  0.0,     	  0.0,    	  0.0,     	  0.0]		
                self.carsByMarketSegmentExecutiveMiles              	=  [0.28206, 	  0.27908, 	  0.00001 ,	  0.00297, 	  0.38075, 	  0.37963, 	  0.00051, 	  0.00061, 	  0.30432, 	  0.30176, 	  0.00012, 	  0.00244, 	  0.12144, 	  0.12073, 	  0.00037, 	  0.00034, 	  0.0,     	  0.0,    	  0.0,     	  0.0]		
                self.carsByMarketSegmentLuxuryKm                	=  [0.21286, 	  0.21102, 	  0.000004,	  0.00184, 	  0.33566, 	  0.33496, 	  0.00032, 	  0.00038, 	  0.26919, 	  0.26787, 	  0.00015, 	  0.00117, 	  0.09634, 	  0.09577, 	  0.0003 , 	  0.00027, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentLuxuryMiles                 	=  [0.34258, 	  0.3396 , 	  0.00001 ,	  0.00297, 	  0.54019, 	  0.53907, 	  0.00051, 	  0.00061, 	  0.43322, 	  0.43109, 	  0.00024, 	  0.00189, 	  0.15504, 	  0.15413, 	  0.00047, 	  0.00044, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentSportsKm                	=  [0.17332, 	  0.17148, 	  0.000004,	  0.00184, 	  0.246  , 	  0.2453 , 	  0.00032, 	  0.00038, 	  0.23441, 	  0.23353, 	  0.00027, 	  0.00061, 	  0.07981, 	  0.07935, 	  0.00024, 	  0.00022, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentSportsMiles                 	=  [0.27895, 	  0.27597, 	  0.00001 ,	  0.00297, 	  0.3959 , 	  0.39478, 	  0.00051, 	  0.00061, 	  0.37724, 	  0.37582, 	  0.00043, 	  0.00099, 	  0.12845, 	  0.1277 , 	  0.00039, 	  0.00036, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentDualpurposeKm           	=  [0.20257, 	  0.20073, 	  0.000004,	  0.00184, 	  0.23663, 	  0.23593, 	  0.00032, 	  0.00038, 	  0.20925, 	  0.20762, 	  0.00007, 	  0.00156, 	  0.07626, 	  0.07581, 	  0.00023, 	  0.00022, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentDualpurposeMiles            	=  [0.32602, 	  0.32304, 	  0.00001 ,	  0.00297, 	  0.38081, 	  0.37969, 	  0.00051, 	  0.00061, 	  0.33675, 	  0.33413, 	  0.00011, 	  0.00251, 	  0.12273, 	  0.122  , 	  0.00037, 	  0.00036, 	  0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentMPVkm                   	=  [0.18101, 	  0.17917, 	  0.000004,	  0.00184, 	  0.1994 , 	  0.1987 , 	  0.00032, 	  0.00038, 	  0.1861 , 	  0.18457, 	  0.00009, 	  0.00144, 		0.0,	    0.0  ,  0.0      ,   0.0     ,    0.0,     	  0.0,    	  0.0,     	  0.0]     
                self.carsByMarketSegmentMPVMiles                   	=  [0.29133, 	  0.28835, 	  0.00001 ,	  0.00297, 	  0.32089, 	  0.31977, 	  0.00051, 	  0.00061, 	  0.29951, 	  0.29704, 	  0.00015, 	  0.00232, 		0.0,	    0.0  ,  0.0      ,   0.0     ,    0.0,     	  0.0,    	  0.0,     	  0.0]   

        def makeList(self):
                dataTola=[self.carsByMarketSegmentMiniKm, self.carsByMarketSegmentMinimiles       ,self.carsByMarketSegmentsuperminiKm     ,self.carsByMarketSegmentSuperminimiles  ,self.carsByMarketSegmentLowerMediumKm   ,self.carsByMarketSegmentLowerMediummiles
                        ,self.carsByMarketSegmentUpperMediumKm   ,self.carsByMarketSegmentUpperMediumMiles,self.carsByMarketSegmentExecutiveKm     ,self.carsByMarketSegmentExecutiveMiles  ,self.carsByMarketSegmentLuxuryKm        ,self.carsByMarketSegmentLuxuryMiles     ,self.carsByMarketSegmentSportsKm        ,self.carsByMarketSegmentSportsMiles     ,self.carsByMarketSegmentDualpurposeKm   ,self.carsByMarketSegmentDualpurposeMiles,self.carsByMarketSegmentMPVkm           ,self.carsByMarketSegmentMPVMiles]
                return dataTola
        

class ImpactoTamanosCoches():
        def __init__(self) -> None:
    
# Activity	Type	Unit	Diesel[kg CO2e	kg CO2	kg CH4	kg N2O][0]	Petrol [kg CO2e	kg CO2	kg CH4	kg N2O][1]	Hybrid[kg CO2e	kg CO2	kg CH4	kg N2O][2]	CNG[kg CO2e	kg CO2	kg CH4	kg N2O][3]	LPG[kg CO2e	kg CO2	kg CH4	kg N2O][4] Unknown	[kg CO2e	kg CO2	kg CH4	kg N2O][5]
# 	Plug-in Hybrid Electric Vehicle [kg CO2e	kg CO2	kg CH4	kg N2O][6] Battery Electric Vehicle	[kg CO2e	kg CO2	kg CH4	kg N2O][7]
#                                                       [0]         [1]         [2]         [3]         [4]         [5]         [6]         [7]
            self.carsSmallCarkm 	     =   [0.14208, 	  0.14024, 	  0.000004,	  0.00184, 	  0.15371, 	  0.15301, 	  0.00032, 	  0.00038, 	  0.1052 , 	  0.10409, 	  0.00021, 	  0.0009 , 									                                                                0.14958,	0.14847,	0.00021,	0.00090,	0.02935,	0.02918,	0.00009,	0.00008,	  0.0,     	  0.0,     	  0.0,     	  0.0]     
            self.carsSmallCarMiles	     =   [0.22868, 	  0.2257 , 	  0.00001 ,	  0.00297, 	  0.24736, 	  0.24624, 	  0.00051, 	  0.00061, 	  0.1693 , 	  0.16752, 	  0.00033, 	  0.00145, 									                                                                0.24072,	0.23894,	0.00033,	0.00145,	0.04723,	0.04696,	0.00014,	0.00013,	  0.0,     	  0.0,     	  0.0,     	  0.0]     
            self.carsMediumCarKm	     =   [0.17061, 	  0.16877, 	  0.000004,	  0.00184, 	  0.19228, 	  0.19158, 	  0.00032, 	  0.00038, 	  0.10895, 	  0.10764, 	  0.00015, 	  0.00116, 	  0.16176,	  0.15972,	  0.00159,	  0.00045,	0.18066,	0.18016,	0.00005,	0.00045,	0.18071,	0.17940,	0.00015,	0.00116,	0.07083,	0.07040,	0.00021,	0.00022,	  0.0,     	  0.0,     	  0.0,    	  0.0]
            self.carsMediumCarMiles 	     =   [0.27459, 	  0.27161, 	  0.00001 ,	  0.00297, 	  0.30945, 	  0.30833, 	  0.00051, 	  0.00061, 	  0.17534, 	  0.17323, 	  0.00024, 	  0.00187, 	  0.26034,	  0.25705,	  0.00257,	  0.00072,	0.29073,	0.28993,	0.00008,	0.00072,	0.29082,	0.28871,	0.00024,	0.00187,	0.11399,	0.11330,	0.00034,	0.00035,	  0.0,     	  0.0,     	  0.0,    	  0.0]
            self.carsLargeCarKm              =   [0.20947, 	  0.20763, 	  0.000004,	  0.00184, 	  0.28295, 	  0.28225, 	  0.00032, 	  0.00038, 	  0.13177, 	  0.13022, 	  0.00009, 	  0.00146, 	  0.23735,	  0.23531,	  0.00159,	  0.00045,	0.26591,	0.26541,	0.00005,	0.00045,	0.22857,	0.22702,	0.00009,	0.00146,	0.07731,	0.07685,	0.00024,	0.00022,	  0.0,     	  0.0,     	  0.0,    	  0.0]
            self.carsLargeCarMiles           =   [0.33713, 	  0.33415, 	  0.00001 ,	  0.00297, 	  0.45536, 	  0.45424, 	  0.00051, 	  0.00061, 	  0.21207, 	  0.20957, 	  0.00014, 	  0.00236, 	  0.38198,	  0.37869,	  0.00257,	  0.00072,	0.42794,	0.42714,	0.00008,	0.00072,	0.36785,	0.36535,	0.00014,	0.00236,	0.12442,	0.12368,	0.00038,	0.00036,	  0.0,     	  0.0,     	  0.0,    	  0.0]
            self.carsAverageCarKm	     =   [0.17336, 	  0.17152, 	  0.000004,	  0.00184, 	  0.18084, 	  0.18014, 	  0.00032, 	  0.00038, 	  0.11473, 	  0.11346, 	  0.00016, 	  0.00111, 	  0.17803,	  0.17599,	  0.00159,	  0.00045,	0.19901,	0.19851,	0.00005,	0.00045,	0.17710,	0.17583,	0.00016,	0.00111,	0.07075,	0.07033,	0.00021,	0.00021,	  0.0,     	  0.0,     	  0.0,    	  0.0]
            self.carsAverageCarMiles	     =   [0.27901, 	  0.27603, 	  0.00001 ,	  0.00297, 	  0.29103, 	  0.28991, 	  0.00051, 	  0.00061, 	  0.18464, 	  0.18259, 	  0.00026, 	  0.00179, 	  0.28653,	  0.28324,	  0.00257,	  0.00072,	0.32027,	0.31947,	0.00008,	0.00072,	0.28502,	0.28297,	0.00026,	0.00179,	0.11386,	0.11318,	0.00034,	0.00034,	  0.0,     	  0.0,     	  0.0,    	  0.0]
        
        def makeList(self):
                dataTola=[self.carsSmallCarkm,self.carsSmallCarMiles,self.carsMediumCarKm,self.carsMediumCarMiles ,self.carsLargeCarKm        ,self.carsLargeCarMiles     ,self.carsAverageCarKm,self.carsAverageCarMiles]
                return dataTola

class ImpactoTamanosMotocicletas():
        def __init__(self) -> None:
                self.motorbikeSmallKm	          =     [0.08445, 	  0.08241, 	  0.00174, 	  0.0003 ] 
                self.motorbikeSmallMiles	  =     [0.13591, 	  0.13263, 	  0.0028 , 	  0.00048] 
                self.motorbikeMediumKm	          =     [0.10289, 	  0.10004, 	  0.00225, 	  0.0006 ] 
                self.motorbikeMediumKiles	  =     [0.16559, 	  0.1610,	  0.00362, 	  0.00097] 
                self.motorbikeLargeKm	          =     [0.13501, 	  0.13308, 	  0.00133, 	  0.0006 ] 
                self.motorbikeLargeMiles	  =     [0.21729, 	  0.21418, 	  0.00214, 	  0.00097] 
                self.motorbikeAverageKm	          =     [0.11551, 	  0.11314, 	  0.00178, 	  0.00059] 
                self.motorbikeAverageMiles	  =     [0.18589, 	  0.18208, 	  0.00286, 	  0.00095]      

        def makeList(self):
                dataTola=[   self.motorbikeSmallKm	 ,self.motorbikeSmallMiles,self.motorbikeMediumKm	 ,self.motorbikeMediumKiles,self.motorbikeLargeKm	 ,self.motorbikeLargeMiles,self.motorbikeAverageKm	 ,self.motorbikeAverageMiles   ]


class ImpactoTiposVuelos():
        def __init__(self) -> None:
#									Activity	Haul	Class	Unit	With RF	[kg CO2e[0] kg CO2[1]	kg CH4[2] kg N2O[3]] Without RF [kg CO2e[4] kg CO2[5]	kg CH4[6]	kg N2O[7]]

#                                                                                                       [0]            [1]              [2]             [3]             [4]             [5]             [6]             [7]
                self.FlightsDomesticTo_fromUKAveragePassengerPassengerKm                     	=  [0.25493 ,	  0.25355, 	  0.00012 ,	  0.00126, 	  0.13483 ,	  0.13345, 	  0.00012 ,	  0.00126] 
                self.FlightsShortHaulToFromUKAveragePassengerPassengerKm     	                =  [0.15832 ,	  0.15753, 	  0.00001 ,	  0.00078, 	  0.0837  ,	  0.08291, 	  0.00001 ,	  0.00078] 
                self.FlightsShortHaulToFromUKAveragePassengerPassengerKmEconomyPassengerKm   	=  [0.15573 ,	  0.15495, 	  0.00001 ,	  0.00077, 	  0.08233 ,	  0.08155, 	  0.00001 ,	  0.00077] 
                self.FlightsShortHaulToFromUKAveragePassengerKmBusinessClassPassengerKm      	=  [0.2336  ,	  0.23243, 	  0.00001 ,	  0.00116, 	  0.1235  ,	  0.12233, 	  0.00001 ,	  0.00116] 
                self.FlightsLongHaulToFromUKAveragePassengerPassengerKm                         =  [0.19562 ,     0.19464 , 	  0.00001 ,	  0.00097, 	  0.10342 ,	  0.10244, 	  0.00001 ,	  0.00097] 
                self.FlightsLongHaulToFromUKLongHaulToFromUKAveragePassengerEconomyPassengerKm	=  [0.14981 ,	  0.14906, 	  0.00001 ,	  0.00074, 	  0.0792  ,	  0.07845, 	  0.00001 ,	  0.00074] 
                self.FlightsLongHaulToFromUKPremiumEconomyPassengerKm                        	=  [0.2397  ,	  0.2385 , 	  0.00001 ,	  0.00119, 	  0.12673 ,	  0.12553, 	  0.00001 ,	  0.00119] 
                self.FlightsLongHaulToFromUKBusinessPassengerKm                              	=  [0.43446 ,	  0.43229, 	  0.00002 ,	  0.00215, 	  0.22969 ,	  0.22752, 	  0.00002 ,	  0.00215] 
                self.FlightsLongHaulToFromUKFirstPassengerKm                                 	=  [0.59925 ,	  0.59626, 	  0.00002 ,	  0.00297, 	  0.31681 ,	  0.31382, 	  0.00002 ,	  0.00297] 
                self.FlightsInternationalToFromNonUKAveragePassengerPassengerKm              	=  [0.18078 ,	  0.17987, 	  0.00001 ,	  0.0009 , 	  0.09558 ,	  0.09467, 	  0.00001 ,	  0.0009 ] 
                self.FlightsInternationalToFromNonUKEconomyPassengerKm                       	=  [0.138445,	  0.13775, 	  0.000005,	  0.00069, 	  0.073195,	  0.0725 , 	  0.000005,	  0.00069] 
                self.FlightsInternationalToFromNonUKPremiumEconomyPassengerKm                	=  [0.22151 ,	  0.2204 , 	  0.00001 ,	  0.0011 , 	  0.11711 ,	  0.116  , 	  0.00001 ,	  0.0011 ] 
                self.FlightsInternationalToFromNonUKBusinessPassengerKm                      	=  [0.40149 ,	  0.39948, 	  0.00002 ,	  0.00199, 	  0.21226 ,	  0.21025, 	  0.00002 ,	  0.00199] 
                self.FlightsInternationalToFromNonUKFirstPassengerKm                         	=  [0.55376 ,	  0.551  , 	  0.00002 ,	  0.00274, 	  0.29276 ,	  0.29   , 	  0.00002 ,	  0.00274]

        def makeList(self):
                dataTola=[ self.FlightsDomesticTo_fromUKAveragePassengerPassengerKm                     ,self.FlightsShortHaulToFromUKAveragePassengerPassengerKm     	              ,self.FlightsShortHaulToFromUKAveragePassengerPassengerKmEconomyPassengerKm   ,self.FlightsShortHaulToFromUKAveragePassengerKmBusinessClassPassengerKm      
                          ,self.FlightsLongHaulToFromUKAveragePassengerPassengerKm                       ,self.FlightsLongHaulToFromUKLongHaulToFromUKAveragePassengerEconomyPassengerKm,self.FlightsLongHaulToFromUKPremiumEconomyPassengerKm                        ,self.FlightsLongHaulToFromUKBusinessPassengerKm                          
                        ,self.FlightsLongHaulToFromUKFirstPassengerKm                                 ,self.FlightsInternationalToFromNonUKAveragePassengerPassengerKm              ,self.FlightsInternationalToFromNonUKEconomyPassengerKm                       ,self.FlightsInternationalToFromNonUKPremiumEconomyPassengerKm                ,self.FlightsInternationalToFromNonUKBusinessPassengerKm                      ,self.FlightsInternationalToFromNonUKFirstPassengerKm                         ]

                return dataTola

class ImpactoTiposFerries():
        def __init__(self) -> None:
#       Activity	Type	Unit	                        kg CO2e	          kg CO2	kg CH4	           kg N2O             
                self.ferryFootPassengerPassengerKm           =  	  [0.01874,	  0.01848,	  0.00001,	  0.00025]
                self.ferryCarPassengerPassengerKm            =   	  [0.12952,	  0.12774,	  0.00004,	  0.00174]
                self.ferryAveragePassengerPassengerKm        =	          [0.11286,	  0.11131,	  0.00003,	  0.00152] #(all passenger)
        def makeList(self):
                dataTola=[self.ferryFootPassengerPassengerKm ,self.ferryCarPassengerPassengerKm,self.ferryAveragePassengerPassengerKm  ]
                return dataTola

class ImpactoSegmentoMercadoAutomoviles():
        def __init__(self) -> None:

#			Diesel				Petrol				Unknown				Plug-in Hybrid Electric Vehicle				Battery Electric Vehicle			
#Activity	Type	Unit	kg CO2e	kg CO2	kg CH4	kg N2O	kg CO2e	kg CO2	kg CH4	kg N2O	kg CO2e	kg CO2	kg CH4	kg N2O	kg CO2e	kg CO2	kg CH4	kg N2O	kg CO2e	kg CO2	kg CH4	kg N2O
                self.carsMarketSegmentMiniKm        	        =         [0.11009, 	  0.10825, 	  0.000004,	  0.00184, 	  0.13975, 	  0.13905, 	  0.00032, 	  0.00038, 	  0.13958, 	  0.13887, 	  0.00032, 	  0.00039, 					0.05235,	0.05194,	0.00013,	0.00028]
                self.carsMarketSegmentMiniMiles              =	  [0.17719, 	  0.17421, 	  0.00001 ,	  0.00297, 	  0.2249 , 	  0.22378, 	  0.00051, 	  0.00061, 	  0.22463, 	  0.22349, 	  0.00051, 	  0.00063, 					0.08425,	0.08359,	0.00021,	0.00045]
                self.carsMarketSegmentSuperminiKm            =	  [0.13449, 	  0.13265, 	  0.000004,	  0.00184, 	  0.15538, 	  0.15468, 	  0.00032, 	  0.00038, 	  0.15241, 	  0.15155, 	  0.00027, 	  0.00059, 	0.07347,	0.07295,	0.00020,	0.00032,	0.04788,	0.04750,	0.00012,	0.00026]
                self.carsMarketSegmentSuperminiMiles         =	  [0.21647, 	  0.21349, 	  0.00001 ,	  0.00297, 	  0.25006, 	  0.24894, 	  0.00051, 	  0.00061, 	  0.24528, 	  0.24389, 	  0.00044, 	  0.00095, 	0.11823,	0.11740,	0.00032,	0.00051,	0.07704,	0.07644,	0.00019,	0.00041]
                self.carsMarketSegmentLowerMediumKm          =	  [0.14691, 	  0.14507, 	  0.000004,	  0.00184, 	  0.18008, 	  0.17938, 	  0.00032, 	  0.00038, 	  0.16362, 	  0.16235, 	  0.00016, 	  0.00111, 	0.10104,	0.10037,	0.00029,	0.00038,	0.05772,	0.05726,	0.00015,	0.00031]
                self.carsMarketSegmentLowerMediumMiles       =	  [0.23644, 	  0.23346, 	  0.00001 ,	  0.00297, 	  0.2898 , 	  0.28868, 	  0.00051, 	  0.00061, 	  0.26332, 	  0.26128, 	  0.00026, 	  0.00178, 	0.16260,	0.16152,	0.00047,	0.00061,	0.09288,	0.09215,	0.00023,	0.00050]
                self.carsMarketSegmentUpperMediumKm          =	  [0.16533, 	  0.16349, 	  0.000004,	  0.00184, 	  0.20792, 	  0.20722, 	  0.00032, 	  0.00038, 	  0.17537, 	  0.17379, 	  0.00008, 	  0.0015 , 	0.11448,	0.11371,	0.00032,	0.00045,	0.04659,	0.04622,	0.00012,	0.00025]
                self.carsMarketSegmentUpperMediumMiles       =	  [0.2661 , 	  0.26312, 	  0.00001 ,	  0.00297, 	  0.33461, 	  0.33349, 	  0.00051, 	  0.00061, 	  0.28223, 	  0.27969, 	  0.00013, 	  0.00241, 	0.18426,	0.18301,	0.00052,	0.00073,	0.07497,	0.07438,	0.00019,	0.00040]
                self.carsMarketSegmentExecutiveKm            =	  [0.17525, 	  0.17341, 	  0.000004,	  0.00184, 	  0.23659, 	  0.23589, 	  0.00032, 	  0.00038, 	  0.18909, 	  0.1875 , 	  0.00008, 	  0.00151, 	0.12417,	0.12335,	0.00035,	0.00047,				]
                self.carsMarketSegmentExecutiveMiles         =	  [0.28206, 	  0.27908, 	  0.00001 ,	  0.00297, 	  0.38075, 	  0.37963, 	  0.00051, 	  0.00061, 	  0.30432, 	  0.30176, 	  0.00012, 	  0.00244, 	0.19984,	0.19851,	0.00057,	0.00076,				]
                self.carsMarketSegmentLuxuryKm               =	  [0.21286, 	  0.21102, 	  0.000004,	  0.00184, 	  0.33566, 	  0.33496, 	  0.00032, 	  0.00038, 	  0.26919, 	  0.26787, 	  0.00015, 	  0.00117, 	0.14588,	0.14492,	0.00042,	0.00054,	0.07027,	0.06971,	0.00018,	0.00038]
                self.carsMarketSegmentLuxuryMiles            =	  [0.34258, 	  0.3396 , 	  0.00001 ,	  0.00297, 	  0.54019, 	  0.53907, 	  0.00051, 	  0.00061, 	  0.43322, 	  0.43109, 	  0.00024, 	  0.00189, 	0.23477,	0.23323,	0.00068,	0.00086,	0.11309,	0.11219,	0.00029,	0.00061]
                self.carsMarketSegmentSportsKm               =	  [0.17332, 	  0.17148, 	  0.000004,	  0.00184, 	  0.246  , 	  0.2453 , 	  0.00032, 	  0.00038, 	  0.23441, 	  0.23353, 	  0.00027, 	  0.00061, 	0.11895,	0.11818,	0.00034,	0.00043,	0.08968,	0.08897,	0.00023,	0.00048]
                self.carsMarketSegmentSportsMiles            =	  [0.27895, 	  0.27597, 	  0.00001 ,	  0.00297, 	  0.3959 , 	  0.39478, 	  0.00051, 	  0.00061, 	  0.37724, 	  0.37582, 	  0.00043, 	  0.00099, 	0.19144,	0.19019,	0.00055,	0.00070,	0.14432,	0.14318,	0.00036,	0.00078]
                self.carsMarketSegmentDualPurpose4X4Km       =	  [0.20257, 	  0.20073, 	  0.000004,	  0.00184, 	  0.23663, 	  0.23593, 	  0.00032, 	  0.00038, 	  0.20925, 	  0.20762, 	  0.00007, 	  0.00156, 	0.12502,	0.12419,	0.00035,	0.00048,	0.08033,	0.07970,	0.00020,	0.00043]
                self.carsMarketSegmentDualPurpose4X4Miles    =	  [0.32602, 	  0.32304, 	  0.00001 ,	  0.00297, 	  0.38081, 	  0.37969, 	  0.00051, 	  0.00061, 	  0.33675, 	  0.33413, 	  0.00011, 	  0.00251, 	0.20121,	0.19986,	0.00057,	0.00078,	0.12929,	0.12827,	0.00033,	0.00069]
                self.carsMarketSegmentMPVKm                  =	  [0.18101, 	  0.17917, 	  0.000004,	  0.00184, 	  0.1994 , 	  0.1987 , 	  0.00032, 	  0.00038, 	  0.1861 , 	  0.18457, 	  0.00009, 	  0.00144, 					0.06404,	0.06354,	0.00016,	0.00034]
                self.carsMarketSegmentMPVMiles               =	  [0.29133, 	  0.28835, 	  0.00001 ,	  0.00297, 	  0.32089, 	  0.31977, 	  0.00051, 	  0.00061, 	  0.29951, 	  0.29704, 	  0.00015, 	  0.00232, 					0.10306,	0.10225,	0.00026,	0.00055]

        def makeList(self):
                dataTola=[self.carsMarketSegmentMiniKm        	 ,self.carsMarketSegmentMiniMiles          ,self.carsMarketSegmentSuperminiKm        ,self.carsMarketSegmentSuperminiMiles     ,self.carsMarketSegmentLowerMediumKm      ,self.carsMarketSegmentLowerMediumMiles   ,self.carsMarketSegmentUpperMediumKm      ,self.carsMarketSegmentUpperMediumMiles   ,self.carsMarketSegmentExecutiveKm        ,self.carsMarketSegmentExecutiveMiles     ,self.carsMarketSegmentLuxuryKm          
                           ,self.carsMarketSegmentLuxuryMiles        ,self.carsMarketSegmentSportsKm           ,self.carsMarketSegmentSportsMiles        ,self.carsMarketSegmentDualPurpose4X4Km   ,self.carsMarketSegmentDualPurpose4X4Miles,self.carsMarketSegmentMPVKm              ,self.carsMarketSegmentMPVMiles           ]
                return dataTola
class ImpactoTamanoAutomoviles():

        def __init__(self) -> None:
#	                                                 |       		Diesel				 |               Petrol				                 |                              Hybrid				  |                      CNG				         |                       LPG				          |              Unknown				           |                       Plug-in Hybrid Electric Vehicle	|			Battery Electric Vehicle	        |		
#       Activity Type Unit	                         |kg CO2e	   kg CO2	     kg CH4	  kg N2O |       kg CO2e	    kg CO2	   kg CH4	 kg N2O	 |       kg CO2e	    kg CO2	    kg CH4	kg N2O	  |       kg CO2e	kg CO2	          kg CH4	kg N2O	 |       kg CO2e	kg CO2	        kg CH4	        kg N2O	  |         kg CO2e	  kg CO2	kg CH4	           kg N2O  |	 kg CO2e	kg CO2	        kg CH4	        kg N2O	|       kg CO2e	        kg CO2  	kg CH4	        kg N2O  |

                self.CarsSmallCarKm  	             =    [0.14208, 	  0.14024, 	  0.000004,	  0.00184, 	  0.15371, 	  0.15301, 	  0.00032, 	  0.00038, 	  0.1052 , 	  0.10409, 	  0.00021, 	  0.0009 , 									                                                                  0.14958, 	  0.14847, 	  0.00021, 	  0.0009 , 	0.07347,        0.07295,	0.00020,	0.00032,	0.04956,	0.04916,	0.00013,	0.00027]
                self.CarsSmallCarMiles               =    [0.22868, 	  0.2257 , 	  0.00001 ,	  0.00297, 	  0.24736, 	  0.24624, 	  0.00051, 	  0.00061, 	  0.1693 , 	  0.16752, 	  0.00033, 	  0.00145, 									                                                                  0.24072, 	  0.23894, 	  0.00033, 	  0.00145, 	0.11823,	0.11740,	0.00032,	0.00051,	0.07975,	0.07912,	0.00020,	0.00043]
                self.MediumCarKm                     =	  [0.17061, 	  0.16877, 	  0.000004,	  0.00184, 	  0.19228, 	  0.19158, 	  0.00032, 	  0.00038, 	  0.10895, 	  0.10764, 	  0.00015, 	  0.00116, 	  0.16176, 	  0.15972, 	  0.00159, 	  0.00045, 	  0.18066, 	  0.18016, 	  0.00005, 	  0.00045, 	  0.18071, 	  0.1794 , 	  0.00015, 	  0.00116, 	0.10998,	0.10924,	0.00031,	0.00043,	0.05769,	0.05723,	0.00015,	0.00031]
                self.CarsSmallCarMiles               =	  [0.27459, 	  0.27161, 	  0.00001 ,	  0.00297, 	  0.30945, 	  0.30833, 	  0.00051, 	  0.00061, 	  0.17534, 	  0.17323, 	  0.00024, 	  0.00187, 	  0.26034, 	  0.25705, 	  0.00257, 	  0.00072, 	  0.29073, 	  0.28993, 	  0.00008, 	  0.00072, 	  0.29082, 	  0.28871, 	  0.00024, 	  0.00187, 	0.17699,	0.17580,	0.00050,	0.00069,	0.09282,	0.09209,	0.00023,	0.00050]
                self.CarLargeCarKm                   =	  [0.20947, 	  0.20763, 	  0.000004,	  0.00184, 	  0.28295, 	  0.28225, 	  0.00032, 	  0.00038, 	  0.13177, 	  0.13022, 	  0.00009, 	  0.00146, 	  0.23735, 	  0.23531, 	  0.00159, 	  0.00045, 	  0.26591, 	  0.26541, 	  0.00005, 	  0.00045, 	  0.22857, 	  0.22702, 	  0.00009, 	  0.00146, 	0.12567,	0.12483,	0.00036,	0.00048,	0.07256,	0.07199,	0.00018,	0.00039]
                self.CarLargeCarMiles                =	  [0.33713, 	  0.33415, 	  0.00001 ,	  0.00297, 	  0.45536, 	  0.45424, 	  0.00051, 	  0.00061, 	  0.21207, 	  0.20957, 	  0.00014, 	  0.00236, 	  0.38198, 	  0.37869, 	  0.00257, 	  0.00072, 	  0.42794, 	  0.42714, 	  0.00008, 	  0.00072, 	  0.36785, 	  0.36535, 	  0.00014, 	  0.00236, 	0.20225,	0.20090,	0.00057,	0.00078,	0.11677,	0.11585,	0.00029,	0.00063]
                self.CarAverageCarKm                 =	  [0.17336, 	  0.17152, 	  0.000004,	  0.00184, 	  0.18084, 	  0.18014, 	  0.00032, 	  0.00038, 	  0.11473, 	  0.11346, 	  0.00016, 	  0.00111, 	  0.17803, 	  0.17599, 	  0.00159, 	  0.00045, 	  0.19901, 	  0.19851, 	  0.00005, 	  0.00045, 	  0.1771 , 	  0.17583, 	  0.00016, 	  0.00111, 	0.11532,	0.11454,	0.00033,	0.00045,	0.06020,	0.05973,	0.00015,	0.00032]
                self.CarAverageCarMiles              =	  [0.27901, 	  0.27603, 	  0.00001 ,	  0.00297, 	  0.29103, 	  0.28991, 	  0.00051, 	  0.00061, 	  0.18464, 	  0.18259, 	  0.00026, 	  0.00179, 	  0.28653, 	  0.28324, 	  0.00257, 	  0.00072, 	  0.32027, 	  0.31947, 	  0.00008, 	  0.00072, 	  0.28502, 	  0.28297, 	  0.00026, 	  0.00179, 	0.18559,	0.18434,	0.00053,	0.00072,	0.09688,	0.09612,	0.00024,	0.00052]
        def makeList(self):
                dataTola=[
                        self.CarsSmallCarKm  	,self.CarsSmallCarMiles  ,self.MediumCarKm        ,self.CarsSmallCarMiles  ,self.CarLargeCarKm      ,self.CarLargeCarMiles   ,self.CarAverageCarKm    ,self.CarAverageCarMiles 
                ]

                return dataTola

class ImpactoTipoMotocicletas():

        def __init__(self) -> None:
                self.motorbikeSmallKm        	=  [0.08445, 	  0.08241, 	  0.00174, 	  0.0003 ] 
                self.motorbikeSmallMiles     	=  [0.13591, 	  0.13263, 	  0.0028 , 	  0.00048] 
                self.motorbikeMediumKm       	=  [0.10289, 	  0.10004, 	  0.00225, 	  0.0006 ] 
                self.motorbikeMediumMiles    	=  [0.16559, 	  0.161  , 	  0.00362, 	  0.00097] 
                self.motorbikeLargeKm        	=  [0.13501, 	  0.13308, 	  0.00133, 	  0.0006 ] 
                self.motorbikeLargeMiles     	=  [0.21729, 	  0.21418, 	  0.00214, 	  0.00097] 
                self.motorbikeAverageKm      	=  [0.11551, 	  0.11314, 	  0.00178, 	  0.00059] 
                self.motorbikeAverageMiles   	=  [0.18589, 	  0.18208, 	  0.00286, 	  0.00095] 
        
        def makeList(self):
                dataTola=[self.motorbikeSmallKm      ,self.motorbikeSmallMiles   ,self.motorbikeMediumKm     ,self.motorbikeMediumMiles  ,self.motorbikeLargeKm      ,self.motorbikeLargeMiles   ,self.motorbikeAverageKm    ,self.motorbikeAverageMiles ]
                return dataTola
        

class ImpactoTipoTaxi():

        def __init__(self) -> None:
                self.taxisRegularTaxPassengerKm	=       [0.15018, 	  0.14886, 	  0.000003,	  0.00132]
                self.taxisRegularTaxPassengerKm	=       [0.21024, 	  0.2084 , 	  0.000004,	  0.00184]
                self.taxisBlackCabPassengerKm	=       [0.21176, 	  0.21053, 	  0.000003,	  0.00123]
                self.taxisBlackCabPassengerKm	=       [0.31764, 	  0.3158 , 	  0.000004,	  0.00184]

        def makeList(self):
                dataTola=[self.taxisRegularTaxPassengerKm	,self.taxisRegularTaxPassengerKm	,self.taxisBlackCabPassengerKm	,self.taxisBlackCabPassengerKm	]
                return dataTola
        

class ImpactoTipoAutobus():

        def __init__(self) -> None:
#               Activity Type Unit	                    kg CO2e 	kg CO2	        kg CH4	        kg N2O
                self.busLocalBusPassengerKm  	        =  [0.12076, 	  0.11974, 	  0.00003, 	  0.00099]
                self.busLocalLondonBusPassengerKm	=  [0.08208, 	  0.08163, 	  0.00001, 	  0.00044]
                self.busAverageLocalBusPassengerKm	=  [0.10471, 	  0.10391, 	  0.00003, 	  0.00077]
                self.busCoachPassengerKm     	        =  [0.02779, 	  0.02728, 	  0.00002, 	  0.00049]

        def makeList(self):
                dataTola=[self.busLocalBusPassengerKm  	   ,self.busLocalLondonBusPassengerKm,self.busAverageLocalBusPassengerKm,self.busCoachPassengerKm     	   ]
                
                return dataTola

class ImpactoTipoCarril():

        def __init__(self) -> None:

#               Activity	Type	Unit	                kg CO2e	        kg CO2	        kg CH4	        kg N2O
                self.railNationalRailPassengerKm             =	  [0.04115, 	  0.04077, 	  0.00007, 	  0.00031]
                self.railInternationalRailPassengerKm        =	  [0.00597, 	  0.00592, 	  0.00002, 	  0.00003]
                self.railLightRailTramPassengerKm            =	  [0.03508, 	  0.0348 , 	  0.00009, 	  0.00019]
                self.railLondonUndergroundPassengerKm        =	  [0.03084, 	  0.03059, 	  0.00008, 	  0.00017]

        def makeList(self):
                dataTola=[self.railNationalRailPassengerKm     ,self.railInternationalRailPassengerKm ,self.railLightRailTramPassengerKm    ,self.railLondonUndergroundPassengerKm]
                return dataTola


class SubregioneGRID2():

        def __init__(self) -> None:
#eGRID subregion acronym	eGRID subregion name	Total output emission rates										                                   13           	14                              	15
#		lb/MWh												
#                                               		CO2	        CH4	        N2O	        CO2e	        Annual NOx	OzoneSeasonNOx	SO2				kgCO2/kWh	        kgCH4/kWh	                kgN2O/kWh


                self.AKGDASCCAlaskaGrid                      =	[1039.635,	0.082,   	0.011,   	1044.989,	5.47 ,   	5.419,   	1.1,            		0.4715705036,	        0.00003719457434,        	0.00000498951607]
                self.AKMSASCCMiscellaneous                   =	[525.083 ,      0.024,   	0.004,   	526.963 ,	7.712,   	7.844,   	0.677,				0.2381736424,	        0.00001088621688,        	0.00000181436948]
                self.AZNMWECCSouthwest                       =	[1022.355,	0.077,   	0.011,   	1027.548,	0.73 ,   	0.719,   	0.263,				0.4637324274,	        0.00003492661249,        	0.00000498951607]
                self.CAMXWECCCalifornia                      =	[496.536 ,	0.034,   	0.004,   	498.686 ,	0.463,   	0.414,   	0.047,				0.225224941,	        0.00001542214058,        	0.00000181436948]
                self.ERCTERCOTAll                            =	[931.672 ,	0.066,   	0.009,   	936.082 ,	0.545,   	0.554,   	0.829,				0.4225993105,	        0.00002993709642,        	0.00000408233133]
                self.FRCCFRCCAll                             =	[931.842 ,	0.066,   	0.009,   	936.145 ,	0.356,   	0.365,   	0.278,				0.4226764212,	        0.00002993709642,        	0.00000408233133]
                self.HIMSHICCMiscellaneous                   =	[1110.689,	0.118,   	0.018,   	1119.077,	7.638,   	7.582,   	3.969,				0.5038000558,	        0.00005352389966,        	0.00000816466266]
                self.HIOAHICCOahu                            =	[1669.943,	0.18 ,   	0.027,   	1682.596,	3.515,   	3.773,   	7.997,				0.7574734031,	        0.0000816466266	,               0.00001224699399]
                self.MROEMROEast                             =	[1678.016,	0.169,   	0.025,   	1689.651,	0.88 ,   	0.887,   	0.891,				0.7611352543,	        0.00007665711053,        	0.00001133980925]
                self.MROWMROWest                             =	[1239.848,	0.138,   	0.02 ,   	1249.201,	0.977,   	1.009,   	1.351,				0.5623855928,	        0.00006259574706,        	0.0000090718474]
                self.NEWENPCCNewEngland                      =	[522.312 ,	0.082,   	0.011,   	527.564 ,	0.387,   	0.35 ,   	0.136,				0.236916738,	        0.00003719457434,        	0.00000498951607]
                self.NWPPWECCNorthwest                       =	[639.037 ,	0.064,   	0.009,   	643.363 ,	0.58 ,   	0.577,   	0.377,				0.2898623073,	        0.00002902991168,        	0.00000408233133]
                self.NYCWNPCCNYCWestchester                  =	[596.414 ,	0.022,   	0.003,   	597.762 ,	0.251,   	0.249,   	0.026,				0.2705288398,	        0.00000997903214,        	0.00000136077711]
                self.NYLINPCCLongIsland                      =	[1184.241,	0.139,   	0.018,   	1193.091,	0.86 ,   	0.828,   	0.234,				0.5371626818,	        0.00006304933943,        	0.00000816466266]
                self.NYUPNPCCUpstateNY                       =	[253.112 ,	0.018,   	0.002,   	253.889 ,	0.136,   	0.136,   	0.092,				0.114809672,	        0.00000816466266,        	0.00000090718474]
                self.RFCERFCEast                             =	[715.966 ,	0.061,   	0.008,   	719.979 ,	0.333,   	0.288,   	0.48,   			0.3247567148,	        0.00002766913457,        	0.00000362873896]
                self.RFCMRFCMichigan	                     =  [1312.56 ,	0.129,   	0.018,   	1321.185,	0.798,   	0.792,   	1.296,				0.5953672012,	        0.00005851341573,        	0.00000816466266]
                self.RFCWRFCWest                             =	[1166.096,	0.117,   	0.017,   	1174.029,	0.825,   	0.652,   	0.925,				0.5289322483,	        0.00005307030729,        	0.00000771107029]
                self.RMPAWECCRockies                         =	[1273.615,	0.123,   	0.018,   	1281.944,	0.673,   	0.689,   	0.418,				0.5777020463,	        0.00005579186151,        	0.00000816466266]
                self.SPNOSPPNorth                            =	[1163.187,	0.124,   	0.018,   	1171.606,	0.642,   	0.72 ,   	0.333,				0.5276127481,	        0.00005624545388,        	0.00000816466266]
                self.SPSOSPPSouth                            =	[1166.582,	0.091,   	0.013,   	1172.755,	0.832,   	0.882,   	1.242,				0.5291526942,	        0.00004127690567,        	0.00000589670081]
                self.SRMVSERCMississippiValley               =	[854.645 ,	0.055,   	0.008,   	858.369 ,	0.614,   	0.671,   	0.96,   			0.3876604511,	        0.00002494758035,        	0.00000362873896]
                self.SRMWSERCMidwest                         =	[1664.15 ,	0.185,   	0.027,   	1676.782,	1.06 ,   	0.791,   	2.488,				0.7548457425,	        0.00008391458845,        	0.00001224699399]
                self.SRSOSERCSouth                           =	[1027.928,	0.081,   	0.012,   	1033.471,	0.496,   	0.433,   	0.297,				0.4662602977,	        0.00003674098197,        	0.00000544310844]
                self.SRTVSERCTennesseeValley                 =	[1031.537,	0.097,   	0.014,   	1038.127,	0.551,   	0.504,   	0.619,				0.4678973126,	        0.00004399845989,        	0.00000635029318]
                self.SRVCSERCVirginiaCarolina                =	[743.328 ,	0.067,   	0.009,   	747.513 ,	0.437,   	0.426,   	0.263,				0.3371679092,	        0.00003039068879,        	0.00000408233133]
                self.US                                      =  [947.182 ,	0.085,   	0.012,   	952.877 ,	0.619,   	0.58 ,   	0.675,				0.4296345282,	        0.00003855535145,        	0.00000544310844]



                self.NewSouthWalesACT			=			                                                                                                                [0.81,                    	0,                       	0]
                self.Victori 				=			                                                                                                                [1.02,                    	0,                       	0]
                self.Queensland				=			                                                                                                                [0.81,                    	0,                       	0]
                self.SouthAustralia	        		=			                                                                                                        [0.44,                    	0,                       	0]
                self.SWISWesternAustralia			=			                                                                                                        [0.69,                    	0,                       	0]
                self.Tasmania		        	=			                                                                                                                [0.15,                    	0,                       	0]
                self.NorthernTerritory			=			                                                                                                                [0.63,                    	0,                       	0]

        def makeList(self):
                dataTola=[self.AKGDASCCAlaskaGrid          ,self.AKMSASCCMiscellaneous       ,self.AZNMWECCSouthwest           ,self.CAMXWECCCalifornia          ,self.ERCTERCOTAll                ,self.FRCCFRCCAll        
                        ,self.HIMSHICCMiscellaneous       ,self.HIOAHICCOahu                ,self.MROEMROEast                 ,self.MROWMROWest                 ,self.NEWENPCCNewEngland          ,self.NWPPWECCNorthwest        
                        ,self.NYCWNPCCNYCWestchester      ,self.NYLINPCCLongIsland          ,self.NYUPNPCCUpstateNY           ,self.RFCERFCEast                 ,self.RFCMRFCMichigan	         ,self.RFCWRFCWest             
                        ,self.RMPAWECCRockies             ,self.SPNOSPPNorth                ,self.SPSOSPPSouth                ,self.SRMVSERCMississippiValley   ,self.SRMWSERCMidwest             ,self.SRSOSERCSouth            
                        ,self.SRTVSERCTennesseeValley     ,self.SRVCSERCVirginiaCarolina    ,self.US                          ,self.NewSouthWalesACT		,self.Victori 			,self.Queensland			,self.SouthAustralia	        ,self.SWISWesternAustralia	,self.Tasmania		        ,self.NorthernTerritory		]
                return dataTola 

class TipoImpactoSubregion():

        def __init__(self) -> None:

# 	                                                                        Impact Type					2016 (preliminary data)		2016	2017 (preliminary data)					
                self.cACO2Intensity            				=	[140,		140,	        130,			    		        ]		          #(g CO2 / kWh)
                self.cACH4Intensity            				=	[0.01,		0,	        0,					        ]		          #(g CH4 / kWh)
                self.cAN2OIntensity           				=	[0.003,		0,	        0,			130 ,    	0	,        0     ]          #(g N2O / kWh)		
                self.cAGenerationIntensity           			=	[140,		140,	        130,			0.13,    	0	,        0     ]          #(g CO2 eq / kWh)
                self.nLCO2Intensity                   			=	[37,		37,	        40,					                       ]       #(g CO2 / kWh) 	  
                self.nLCH4Intensity                   			=	[0.0006,	0.0006,	        0.0006,					                       ]       #(g CH4 / kWh) 	  
                self.nLN2OIntensity   				        =       [0.001,		0.001,	        0.001,			40   ,   	0.0006	 ,       0.001 ]       #(g N2O / kWh)	  
                self.newfoundlandLabradorGenerationIntensity 	        =       [37,		37,	        40,			0.04 ,   	0.0000006,	0.000001]      #(g CO2 eq / kWh)      
                self.pECO2Intensity          				=	[25,		7,	        14,					]                               #(g CO2 / kWh)
                self.pECH4Intensity          				=	[0.0005,	0.0002,	        0.0005,					]                               #(g CH4 / kWh)
                self.pEN2OIntensity          				=	[0.0005,	0.0001,	        0.0002,			14    ,  	0.0005	  ,      0.0002]#(g N2O / kWh)
                self.princeEdwardIslandGenerationIntensity 			=	[25,		7,	        14,			0.014 ,  	0.0000005,	0.0000002]#(g CO2 eq / kWh)
                self.nSO2Intensity                   			=	[670,		700,	        670,					]#(g CO2 / kWh)
                self.nSCH4Intensity                  			=	[0.02,		0.03,	        0.03,					]#(g CH4 / kWh)
                self.nSN2OIntensity                  			=	[0.01,		0.01,	        0.01,			670   ,  	0.03    ,	0.01]#(g N2O / kWh)
                self.novaScotiaGenerationIntensity				=	[680,		670,	        670,			0.67  ,  	0.00003 ,	0.00001]#(g CO2 eq / kWh)
                self.nBCO2Intensity           				=	[330,		320,	        310,					]                               #(g CO2 / kWh)
                self.nBCH4Intensity           				=	[0.02,		0.02,	        0.02,					]                               #(g CH4 / kWh)
                self.nBN2OIntensity          				=	[0.005,		0.005,	        0.004,			310   ,         0.02 ,   	0.004]          #(g N2O / kWh)
                self.newBrunswickGenerationIntensity 			=	[340,		320,	        310,			0.31  ,  	0.00002, 	0.000004]       #(g CO2 eq / kWh)
                self.qCO2Intensity            				=	[1.2,		1.2,	        1.2,					]#(g CO2 / kWh)
                self.qCH4Intensity            				=	[0,		0,	        0,					]#(g CH4 / kWh)
                self.qN2OIntensity           				=	[0.0001,	0.0001,	        0.0001,			1.2    , 	0       ,	0.0001]#(g N2O / kWh)
                self.quebecGenerationIntensity 				=	[1.3,		1.3,	        1.3,			0.0012 , 	0       ,	0.0000001]#(g CO2 eq / kWh)
                self.oCO2Intensity            				=	[35,		36,	        17,					]#(g CO2 / kWh)
                self.oCH4Intensity            				=	[0.01,		0.01,	        0,					]#(g CH4 / kWh)
                self.oN2OIntensity           				=	[0.001,		0.001,	        0.001,			17     , 	0   ,    	0.001]#(g N2O / kWh)
                self.ontarioGenerationIntensity				=	[36,		37,	        17,			0.017  , 	0   ,    	0.000001]#(g CO2 eq / kWh)
                self.mCO2Intensity             				=	[1.9,		1.9,	        1.9,					]#(g CO2 / kWh)
                self.mCH4Intensity             				=	[0.0001,	0.0001,	        0.0001,					]#(g CH4 / kWh)
                self.mN2OIntensity            				=	[0.0001,	0.0001,	        0.0001,			1.9   ,  	0.0001,  	0.0001]#(g N2O / kWh)
                self.manitobaGenerationIntensity 				=	[1.9,		1.9,	        1.9,			0.0019,  	0.0000001,      0.0000001]#(g CO2 eq / kWh)
                self.sCO2Intensity                   			=	[650,		650,	        650,					]#(g CO2 / kWh)
                self.sCH4Intensity                    			=	[0.05,		0.05,	        0.05,					]#(g CH4 / kWh)
                self.sN2OIntensity                    			=	[0.02,		0.02,	        0.02,			650   ,  	0.05   , 	0.02]#(g N2O / kWh)
                self.saskatchewanGenerationIntensity				=	[660,		660,	        660,			0.65  ,  	0.00005, 	0.00002]#(g CO2 eq / kWh)
                self.aCO2intensity            				=	[760,		740,	        750,					]#(g CO2 / kWh)
                self.aCH4intensity                   			=	[0.04,		0.04,	        0.04,					]#(g CH4 / kWh)
                self.aN2Ointensity                    			=	[0.01,		0.01,	        0.01,			750  ,   	0.04   ,	0.01]#(g N2O / kWh)
                self.albertaGenerationIntensity      			=	[760,		750,	        750,			0.75 ,   	0.00004, 	0.00001]#(g CO2 eq / kWh)
                self.bCCO2intensity            				=	[10.8,		11.2,	        9,					]#(g CO2 / kWh)
                self.bCCH4intensity            				=	[0.003,		0.003,	        0.003,					]#(g CH4 / kWh)
                self.bCN2Ointensity           				=	[0.0008,	0.0008,	        0.0007,			9,	        0.003  , 	0.0007]#(g N2O / kWh)
                self.britishColumbiaGenerationIntensity			=	[11.1,		11,	        9.3,			0.009,	        0.000003,	0.0000007]#(g CO2 eq / kWh)
                self.yCO2Intensity            				=	[43,		43,	        48,					]#(g CO2 / kWh)
                self.yCH4Intensity            				=	[0.003,		0.003,	        0.004,					]#(g CH4 / kWh)
                self.yN2OIntensity           				=	[0.01,		0.01,	        0.01,			48,      	0.004  , 	0.01]#(g N2O / kWh)
                self.yukonGenerationIntensity 				=	[45,		45,	        50,			0.048 ,  	0.000004,	0.00001]#(g CO2 eq / kWh)
                self.nTNCO2Intensity         				=	[190,		190,	        170,					]#(g CO2 / kWh)
                self.nTNCH4Intensity          				=	[0.01,		0.01,	        0.01,					]#(g CH4 / kWh)
                self.nTNN2OIntensity 	        			=	[0.03,		0.03,	        0.02,			170	,        0.01 ,   	0.02]#(g N2O / kWh)
                self.northwestTerritoriesNunavutGenerationIntensity		=	[200,		200,	        180,			0.17,	        0.00001, 	0.00002]#(g CO2 eq / kWh)

                self.northnhinagrid	        				=	              						[0.968,         0,       	0]
                self.chinanortheastgrid	       				=	              						[1.1082, 	0,       	0]
                self.eastchinagrid			        		=	              						[0.8046, 	0,       	0]
                self.centralchinagrid					=	              						[0.9014, 	0,       	0]
                self.chinanorthwestgrid					=	              						[0.9155, 	0,       	0]
                self.chinasoutherngrid					=	              						[0.8367, 	0,      	0]
                self.hainanprovincechinapowergrid 				=	              						[0,             0,       	0]


        def makeList(self):
                dataTola=[self.cACO2Intensity            	,self.cACH4Intensity            	,self.cAN2OIntensity           	,self.cAGenerationIntensity           ,self.nLCO2Intensity                   ,self.nLCH4Intensity                   ,self.nLN2OIntensity   				     ,self.newfoundlandLabradorGenerationIntensity 	     ,self.pECO2Intensity          	,self.pECH4Intensity          	,self.pEN2OIntensity          	,self.princeEdwardIslandGenerationIntensity
                          ,self.nSO2Intensity                   ,self.nSCH4Intensity                  ,self.nSN2OIntensity                  ,self.novaScotiaGenerationIntensity,self.nBCO2Intensity           	,self.nBCH4Intensity           	,self.nBN2OIntensity          	,self.newBrunswickGenerationIntensity ,self.qCO2Intensity            	,self.qCH4Intensity            	,self.qN2OIntensity           	,self.quebecGenerationIntensity 	,self.oCO2Intensity            	,self.oCH4Intensity            	
                          ,self.oN2OIntensity           	,self.ontarioGenerationIntensity	,self.mCO2Intensity             	,self.mCH4Intensity             	,self.mN2OIntensity            	,self.manitobaGenerationIntensity ,self.sCO2Intensity                   ,self.sCH4Intensity                    ,self.sN2OIntensity                    ,self.saskatchewanGenerationIntensity,self.aCO2intensity            	,self.aCH4intensity                   ,self.aN2Ointensity          
                        ,self.albertaGenerationIntensity      ,self.bCCO2intensity            	,self.bCCH4intensity            	,self.bCN2Ointensity           	,self.britishColumbiaGenerationIntensity,self.yCO2Intensity            	,self.yCH4Intensity            	,self.yN2OIntensity           	,self.yukonGenerationIntensity 	,self.nTNCO2Intensity         	,self.nTNCH4Intensity          	,self.nTNN2OIntensity 	        ,self.northwestTerritoriesNunavutGenerationIntensi,self.northnhinagrid	    
                        ,self.chinanortheastgrid	       	,self.eastchinagrid			      ,self.centralchinagrid		,self.chinanorthwestgrid		,self.chinasoutherngrid		,self.hainanprovincechinapowergrid 			]

                return dataTola


class    GlobalWarmingPotentials():
        def __init__(self) -> None:
#               Gas                     	100-Year GWP

                self.CO2 	               =           [ 1 ]
                self.CH4	               =           [ 25 ]
                self.N2O	               =           [ 298 ]
                self.HFC23	               =           [ 14800 ]
                self.HFC32	               =           [ 675 ]
                self.HFC41	               =           [ 92 ]
                self.HFC125	               =           [ 3500 ]
                self.HFC134	               =           [ 1100 ]
                self.HFC134a	               =           [ 1430 ]
                self.HFC143	               =           [ 353 ]
                self.HFC143a	               =           [ 4470 ]
                self.HFC152	               =           [ 53 ]
                self.HFC152a	               =           [ 124 ]
                self.HFC161	               =           [ 12 ]
                self.HFC227ea	               =           [3220 ]
                self.HFC236cb	               =           [1340 ]
                self.HFC236ea	               =           [1370 ]
                self.HFC236fa	               =           [9810 ]
                self.HFC245ca	               =           [693 ]
                self.HFC245fa	               =           [1030 ]
                self.HFC365mfc	               =           [794 ]
                self.HFC4310mee	               =           [1640 ]
                self.SF6 	               =           [22800 ]
                self.NF3	               =           [17200 ]
                self.CF4 	               =           [7390 ]
                self.C2F6 	               =           [12200 ]
                self.C3F8	               =           [8830 ]
                self.cC4F8	               =           [10300 ]
                self.C4F10 	               =           [8860 ]
                self.C5F12	               =           [9160 ]
                self.C6F14	               =           [9300 ]
                self.C10F18	               =           [7500 ]
        
        
        def makeList(self):
                dataTola=[self.CO2 ,self.CH4,self.N2O,self.HFC23,self.HFC32,self.HFC41,self.HFC125,self.HFC134,self.HFC134a,self.HFC143,self.HFC143a,self.HFC152,self.HFC152a,self.HFC161,self.HFC227ea,self.HFC236cb,self.HFC236ea,self.HFC236fa,self.HFC245ca,
                          self.HFC245fa,self.HFC365mfc,self.HFC4310mee,self.SF6 ,self.NF3,self.CF4 ,self.C2F6 ,self.C3F8,self.cC4F8,self.C4F10 ,self.C5F12,self.C6F14,self.C10F18	]
                return dataTola 


class    GlobalWarmingPotentialsBlendedRefrigerants():
        def __init__(self) -> None:
#               ASHRAE #	100-year GWP	        Blend Composition			
                self.R401A	= 16 	                #53% HCFC-22 , 34% HCFC-124 , 13% HFC-152a			
                self.R401B	= 14 	                #61% HCFC-22 , 28% HCFC-124 , 11% HFC-152a			
                self.R401C	= 19 	                #33% HCFC-22 , 52% HCFC-124 , 15% HFC-152a			
                self.R402A	= 2100                 #	38% HCFC-22 , 6% HFC-125 , 2% propane			
                self.R402B	= 1330                 #	6% HCFC-22 , 38% HFC-125 , 2% propane			
                self.R403B	= 3444                 #	56% HCFC-22 , 39% PFC-218 , 5% propane			
                self.R404A	= 3922                 #	44% HFC-125 , 4% HFC-134a , 52% HFC 143a			
                self.R406A	= 0	                #55% HCFC-22 , 41% HCFC-142b , 4% isobutane			
                self.R407A	= 2107                 #	20% HFC-32 , 40% HFC-125 , 40% HFC-134a			
                self.R407B	= 2804                 #	10% HFC-32 , 70% HFC-125 , 20% HFC-134a			
                self.R407C	= 1774                 #	23% HFC-32 , 25% HFC-125 , 52% HFC-134a			
                self.R407D	= 1627                 #	15% HFC-32 , 15% HFC-125 , 70% HFC-134a			
                self.R407E	= 1552                 #	25% HFC-32 , 15% HFC-125 , 60% HFC-134a			
                self.R408A	= 2301                 #	47% HCFC-22 , 7% HFC-125 , 46% HFC 143a			
                self.R409A	= 0	                #60% HCFC-22 , 25% HCFC-124 , 15% HCFC-142b			
                self.R410A	= 2088                 #	50% HFC-32 , 50% HFC-125			
                self.R410B	= 2229                 #	45% HFC-32 , 55% HFC-125 			
                self.R411A	= 1 	                #87.5% HCFC-22 , 11 HFC-152a , 1.5% propylene			
                self.R411B	= 4	                #94% HCFC-22 , 3% HFC-152a , 3% propylene			
                self.R413A	= 2053                 #	88% HFC-134a , 9% PFC-218 , 3% isobutane			
                self.R414A	= 0	                #51% HCFC-22 , 28.5% HCFC-124 , 16.5% HCFC-142b			
                self.R414B	= 0	                #5% HCFC-22 , 39% HCFC-124 , 9.5% HCFC-142b			
                self.R417A	= 2346                 #	46.6% HFC-125 , 5% HFC-134a , 3.4% butane			
                self.R422A	= 3143                 #	85.1% HFC-125 , 11.5% HFC-134a , 3.4% isobutane			
                self.R422D	= 2729                 #	65.1% HFC-125 , 31.5% HFC-134a , 3.4% isobutane			
                self.R423A	= 2280                 #	47.5% HFC-227ea , 52.5% HFC-134a ,  			
                self.R424A	= 2440                 #	50.5% HFC-125, 47% HFC-134a, 2.5% butane/pentane			
                self.R426A	= 1508                 #	5.1% HFC-125, 93% HFC-134a, 1.9% butane/pentane			
                self.R428A	= 3607                 #	77.5% HFC-125 , 2% HFC-143a , 1.9% isobutane			
                self.R434A	= 3245                 #	63.2% HFC-125, 16% HFC-134a, 18% HFC-143a, 2.8% isobutane			
                self.R500	= 32 	                #73.8% CFC-12 , 26.2% HFC-152a , 48.8% HCFC-22			
                self.R502	= 0 	                #48.8% HCFC-22 , 51.2% CFC-115 			
                self.R504	= 325 	                #48.2% HFC-32 , 51.8% CFC-115			
                self.R507	= 3985                 #	5% HFC-125 , 5% HFC143a			
                self.R508A	= 13214                # 	39% HFC-23 , 61% PFC-116			
                self.R508B	= 13396                # 	46% HFC-23 , 54% PFC-116
        
        def makeList(self):
                dataTola=[self.R401A,self.R401B,self.R401C,self.R402A,self.R402B,self.R403B,self.R404A,self.R406A,self.R407A,self.R407B,self.R407C,self.R407D,
                          self.R407E,self.R408A,self.R409A,self.R410A,self.R410B,self.R411A,self.R411B,self.R413A,self.R414A,self.R414B,self.R417A,self.R422A,
                          self.R422D,self.R423A,self.R424A,self.R426A,self.R428A,self.R434A,self.R500,self.R502,self.R504,self.R507,self.R508A,self.R508B]	
                
                return dataTola

class    MobileCombustionCH4N2OOnRoadGasolineVehicles():
        def __init__(self) -> None:

        #Vehicle Type	Year	                    "CH4 Factor (g / mile)"	    "N2O Factor (g / mile)"
                self.gasolinePassengerCars1973_74    	     =  [0.1696 ,        	  0.0197 ]
                self.gasolinePassengerCars1975       	     =  [0.1423 ,        	  0.0443 ]
                self.gasolinePassengerCars1976_77    	     =  [0.1406 ,        	  0.0458 ]
                self.gasolinePassengerCars1978_79    	     =  [0.1389 ,        	  0.0473 ]
                self.gasolinePassengerCars1980       	     =  [0.1326 ,        	  0.0499 ]
                self.gasolinePassengerCars1981       	     =  [0.0802 ,        	  0.0626 ]
                self.gasolinePassengerCars1982       	     =  [0.0795 ,        	  0.0627 ]
                self.gasolinePassengerCars1983       	     =  [0.0782 ,        	  0.0630 ]
                self.gasolinePassengerCars1984_93            =  [0.0704 ,        	  0.0647 ]
                self.gasolinePassengerCars1994       	     =  [0.0531 ,        	  0.0560 ]
                self.gasolinePassengerCars1995       	     =  [0.0358 ,        	  0.0473 ]
                self.gasolinePassengerCars1996       	     =  [0.0272 ,        	  0.0426 ]
                self.gasolinePassengerCars1997       	     =  [0.0268 ,        	  0.0422 ]
                self.gasolinePassengerCars1998       	     =  [0.0241 ,        	  0.0379 ]
                self.gasolinePassengerCars1999       	     =  [0.0216 ,        	  0.0337 ]
                self.gasolinePassengerCars2000       	     =  [0.0178 ,        	  0.0273 ]
                self.gasolinePassengerCars2001       	     =  [0.0110 ,        	  0.0158 ]
                self.gasolinePassengerCars2002       	     =  [0.0107 ,        	  0.0153 ]
                self.gasolinePassengerCars2003       	     =  [0.0115 ,        	  0.0133 ]
                self.gasolinePassengerCars2004       	     =  [0.0157 ,        	  0.0063 ]
                self.gasolinePassengerCars2005       	     =  [0.0164 ,        	  0.0051 ]
                self.gasolinePassengerCars2006       	     =  [0.0161 ,        	  0.0057 ]
                self.gasolinePassengerCars2007       	     =  [0.0170 ,        	  0.0041 ]
                self.gasolinePassengerCars2008       	     =  [0.0172 ,        	  0.0038 ]
                self.gasolinePassengerCars2009_present	     =  [0.0173 ,        	  0.0036 ]#(Vans, Pickup Trucks, SUVs)
                self.gasolineLightDutyTrucks1975     	     =  [0.1634 ,        	  0.0513 ]
                self.gasolineLightDutyTrucks1976     	     =  [0.1594 ,        	  0.0555 ]
                self.gasolineLightDutyTrucks1977_78  	     =  [0.1614 ,        	  0.0534 ]
                self.gasolineLightDutyTrucks1979_80  	     =  [0.1594 ,        	  0.0555 ]
                self.gasolineLightDutyTrucks1981      	     =  [0.1479 ,        	  0.0660 ]
                self.gasolineLightDutyTrucks1982     	     =  [0.1442 ,        	  0.0681 ]
                self.gasolineLightDutyTrucks1983     	     =  [0.1368 ,        	  0.0722 ]
                self.gasolineLightDutyTrucks1984     	     =  [0.1294 ,        	  0.0764 ]
                self.gasolineLightDutyTrucks1985     	     =  [0.1220 ,        	  0.0806 ]
                self.gasolineLightDutyTrucks1986     	     =  [0.1146 ,        	  0.0848 ]
                self.gasolineLightDutyTrucks1987_93  	     =  [0.0813 ,        	  0.1035 ]
                self.gasolineLightDutyTrucks1994     	     =  [0.0646 ,        	  0.0982 ]
                self.gasolineLightDutyTrucks1995     	     =  [0.0517 ,        	  0.0908 ]
                self.gasolineLightDutyTrucks1996     	     =  [0.0452 ,        	  0.0871 ]
                self.gasolineLightDutyTrucks1997     	     =  [0.0452 ,        	  0.0871 ]
                self.gasolineLightDutyTrucks1998     	     =  [0.0412 ,        	  0.0778 ]
                self.gasolineLightDutyTrucks1999     	     =  [0.0333 ,        	  0.0593 ]
                self.gasolineLightDutyTrucks2000     	     =  [0.0340 ,        	  0.0607 ]
                self.gasolineLightDutyTrucks2001     	     =  [0.0221 ,        	  0.0328 ]
                self.gasolineLightDutyTrucks2002     	     =  [0.0242 ,        	  0.0378 ]
                self.gasolineLightDutyTrucks2003     	     =  [0.0225 ,        	  0.0330 ]
                self.gasolineLightDutyTrucks2004     	     =  [0.0162 ,        	  0.0098 ]
                self.gasolineLightDutyTrucks2005     	     =  [0.0160 ,        	  0.0081 ]
                self.gasolineLightDutyTrucks2006     	     =  [0.0159 ,        	  0.0088 ]
                self.gasolineLightDutyTrucks2007     	     =  [0.0161 ,        	  0.0079 ]
                self.gasolineLightDutyTrucks2008Present	     =  [0.0163 ,        	  0.0066 ]
                self.gasolineHeavyDutyVehiclesLess1981	     =  [0.4604 ,        	  0.0497 ]
                self.gasolineHeavyDutyVehiclesLess198284     =  [0.4492 ,        	  0.0538 ]
                self.gasolineHeavyDutyVehiclesLess19858      =  [0.4090 ,        	  0.0515 ]
                self.gasolineHeavyDutyVehiclesLess1987        =  [0.3675,         	  0.0849 ]
                self.gasolineHeavyDutyVehiclesLess1988_1989   =  [0.3492,         	  0.0933 ]
                self.gasolineHeavyDutyVehiclesLess1990_1995   =  [0.3246,         	  0.1142 ]
                self.gasolineHeavyDutyVehiclesLess1996        =  [0.1278,         	  0.1680 ]
                self.gasolineHeavyDutyVehiclesLess1997        =  [0.0924,         	  0.1726 ]
                self.gasolineHeavyDutyVehiclesLess1998        =  [0.0655,         	  0.1750 ]
                self.gasolineHeavyDutyVehiclesLess1999        =  [0.0648,         	  0.1721 ]
                self.gasolineHeavyDutyVehiclesLess2000        =  [0.0630,         	  0.1650 ]
                self.gasolineHeavyDutyVehiclesLess2001        =  [0.0578,         	  0.1435 ]
                self.gasolineHeavyDutyVehiclesLess2002        =  [0.0634,         	  0.1664 ]
                self.gasolineHeavyDutyVehiclesLess2003        =  [0.0603,         	  0.1534 ]
                self.gasolineHeavyDutyVehiclesLess2004        =  [0.0323,         	  0.0195 ]
                self.gasolineHeavyDutyVehiclesLess2005        =  [0.0329,         	  0.0162 ]
                self.gasolineHeavyDutyVehiclesLess2006        =  [0.0318,         	  0.0227 ]
                self.gasolineHeavyDutyVehiclesLess2007        =  [0.0333,         	  0.0134 ]
                self.gasolineHeavyDutyVehiclesLess2008present =  [0.0333,         	  0.0134 ]
                self.gasolineMotorcycles1960_1995             =  [0.0899,         	  0.0087 ]
                self.gasolineMotorcycles1996Present           =  [0.0672,         	  0.0069 ]

        def makeList(self):
                dataTola=[self.gasolinePassengerCars1973_74    	    ,self.gasolinePassengerCars1975       	    ,self.gasolinePassengerCars1976_77    	    ,self.gasolinePassengerCars1978_79    	    ,self.gasolinePassengerCars1980	    ,self.gasolinePassengerCars1981      
                          ,self.gasolinePassengerCars1982       	    ,self.gasolinePassengerCars1983       	    ,self.gasolinePassengerCars1984_93           ,self.gasolinePassengerCars1994       	    ,self.gasolinePassengerCars1995       	    ,self.gasolinePassengerCars1996       	    ,self.gasolinePassengerCars1997       	    ,self.gasolinePassengerCars1998       	    ,self.gasolinePassengerCars1999       	    ,self.gasolinePassengerCars2000       	    ,self.gasolinePassengerCars2001       	    ,self.gasolinePassengerCars2002       	    ,self.gasolinePassengerCars2003       	    ,self.gasolinePassengerCars2004   
                        ,self.gasolinePassengerCars2005      ,self.gasolinePassengerCars2006   ,self.gasolinePassengerCars2007       	    ,self.gasolinePassengerCars2008       	    ,self.gasolinePassengerCars2009_present	    ,self.gasolineLightDutyTrucks1975     	    ,self.gasolineLightDutyTrucks1976     	    ,self.gasolineLightDutyTrucks1977_78  	    ,self.gasolineLightDutyTrucks1979_80  	    ,self.gasolineLightDutyTrucks1981      	    ,self.gasolineLightDutyTrucks1982   
                        ,self.gasolineLightDutyTrucks1983     	    ,self.gasolineLightDutyTrucks1984     	    ,self.gasolineLightDutyTrucks1985     	    ,self.gasolineLightDutyTrucks1986     	    ,self.gasolineLightDutyTrucks1987_93  	    ,self.gasolineLightDutyTrucks1994     	    ,self.gasolineLightDutyTrucks1995     	    ,self.gasolineLightDutyTrucks1996     	    ,self.gasolineLightDutyTrucks1997     	    ,self.gasolineLightDutyTrucks1998     	    ,self.gasolineLightDutyTrucks1999     	    ,self.gasolineLightDutyTrucks2000     	    ,self.gasolineLightDutyTrucks2001     	    ,self.gasolineLightDutyTrucks2002
                        ,self.gasolineLightDutyTrucks2003     	    ,self.gasolineLightDutyTrucks2004     	    ,self.gasolineLightDutyTrucks2005     	    ,self.gasolineLightDutyTrucks2006     	    ,self.gasolineLightDutyTrucks2007     	    ,self.gasolineLightDutyTrucks2008Present	    ,self.gasolineHeavyDutyVehiclesLess1981	    ,self.gasolineHeavyDutyVehiclesLess198284    ,self.gasolineHeavyDutyVehiclesLess19858     ,self.gasolineHeavyDutyVehiclesLess1987      ,self.gasolineHeavyDutyVehiclesLess1988_1989 ,self.gasolineHeavyDutyVehiclesLess1990_1995 ,self.gasolineHeavyDutyVehiclesLess1996      ,self.gasolineHeavyDutyVehiclesLess1997
                        ,self.gasolineHeavyDutyVehiclesLess1998      ,self.gasolineHeavyDutyVehiclesLess1999      ,self.gasolineHeavyDutyVehiclesLess2000      ,self.gasolineHeavyDutyVehiclesLess2001      ,self.gasolineHeavyDutyVehiclesLess2002      ,self.gasolineHeavyDutyVehiclesLess2003      ,self.gasolineHeavyDutyVehiclesLess2004      ,self.gasolineHeavyDutyVehiclesLess2005      ,self.gasolineHeavyDutyVehiclesLess2006      ,self.gasolineHeavyDutyVehiclesLess2007      ,self.gasolineHeavyDutyVehiclesLess2008present,self.gasolineMotorcycles1960_1995           ,self.gasolineMotorcycles1996Present         ]
    
                return dataTola

class     MobileCombustionCH4N2OOnRoadDieselAlternativeFuelVehicles():
        def __init__(self) -> None:
        
        #Vehicle Type	Vehicle Year	                    "CH4 Factor (g / mile)"	"N2O Factor (g / mile)"
                self.dieselPassengerCars1960_1982             	        =  [0.0006,      	        0.0012] 
                self.dieselPassengerCars1983_1995             	        =  [0.0005,      	        0.0010] 
                self.dieselPassengerCars1996Present           	        =  [0.0005,      	        0.0010] 
                self.dieselLightDutyTrucks1960_1982           	        =  [0.0011,      	        0.0017] 
                self.dieselLightDutyTrucks1983_1995           	        =  [0.0009,      	        0.0014] 
                self.dieselLightDutyTrucks1996_present        	        =  [0.0010,      	        0.0015] 
                self.dieselMediumHeavyDutyVehicles1960Present	        =  [0.0051,      	        0.0048] 
                self.CNGLightDutyVehicles		                =  [0.737 ,     	        0.050]  
                self.CNGMediumHeavyDutyVehicles          		=  [1.966 ,     	        0.175]  
                self.CNGBuses                            		=  [1.966 ,     	        0.175]  
                self.LPGLightDutyVehicles                		=  [0.037 ,     	        0.067]  
                self.LPGMediumHeavyDutyVehicles          		=  [0.066 ,     	        0.175]  
                self.LNGMediumHeavyDutyVehicles          		=  [1.966 ,     	        0.175]  
                self.EthanolLightDutyVehicles		                =  [0.055 ,     	        0.067]  
                self.EthanolMediumHeavyDutyVehicles      		=  [0.197 ,     	        0.175]  
                self.EthanolBuses                        		=  [0.197 ,     	        0.175]  
                self.BiodieselLightDutyVehicles          		=  [0.0005,      	        0.001]  
                self.BiodieselMediumHeavyDutyVehicles    		=  [0.005 ,     	        0.005]  
                self.BiodieselBuses                      		=  [0.005 ,     	        0.005]  

        def makeList(self):
                dataTola=[self.dieselPassengerCars1960_1982          ,self.dieselPassengerCars1983_1995          ,self.dieselPassengerCars1996Present        ,self.dieselLightDutyTrucks1960_1982        ,self.dieselLightDutyTrucks1983_1995        ,self.dieselLightDutyTrucks1996_present     ,self.dieselMediumHeavyDutyVehicles1960Present
                          ,self.CNGLightDutyVehicles		   ,self.CNGMediumHeavyDutyVehicles         ,self.CNGBuses                           ,self.LPGLightDutyVehicles               ,self.LPGMediumHeavyDutyVehicles         ,self.LNGMediumHeavyDutyVehicles         ,self.EthanolLightDutyVehicles	  
                          ,self.EthanolMediumHeavyDutyVehicles     ,self.EthanolBuses                       ,self.BiodieselLightDutyVehicles         ,self.BiodieselMediumHeavyDutyVehicles   ,self.BiodieselBuses                      	]
                return dataTola

class     MobileCombustionCH4N2ONonRoadVehicles():
        def __init__(self) -> None:

        # Vehicle Type	                        "CH4 Factor (g / gallon) "	"N2O Factor (g / gallon) "
                self.residualFuelOilShipsBoats   	=     [0.11,                 	  0.57] 
                self.gasolineShipsBoats          	=     [0.64,                 	  0.22] 
                self.dieselShipsBoats            	=     [0.06,                 	  0.45] 
                self.dieselLocomotives                  =     [0.80,                 	  0.26] 
                self.gasolineAgriculturalEquip          =     [1.26,                 	  0.22] 
                self.dieselAgriculturalEquip            =     [1.44,                 	  0.26] 
                self.gasolineConstructionEquip          =     [0.50,                 	  0.22] 
                self.dieselConstructionEquip            =     [0.57,                 	  0.26] 
                self.jetFuelAircraft                    =     [0.00,                 	  0.30] 
                self.aviationGasolineAircraft           =     [7.06,                 	  0.11] 
                self.otherGasolineNonRoadVehicles       =     [0.50,                 	  0.22] 
                self.otherDieselNonRoadVehicles         =     [0.57,                 	  0.26] 
                self.lPGNonRoadVehicles                 =     [0.50,                 	  0.22] 
                self.biodieselNonRoadVehicles           =     [0.57,                 	  0.26] 

        def makeList(self):
                dataTola=[self.residualFuelOilShipsBoats   ,self.gasolineShipsBoats          ,self.dieselShipsBoats            ,self.dieselLocomotives           ,self.gasolineAgriculturalEquip   ,self.dieselAgriculturalEquip     ,self.gasolineConstructionEquip   ,self.dieselConstructionEquip     ,self.jetFuelAircraft             ,self.aviationGasolineAircraft    ,self.otherGasolineNonRoadVehicles,
                          self.otherDieselNonRoadVehicles  ,self.lPGNonRoadVehicles          ,self.biodieselNonRoadVehicles    ]


                return dataTola


class BusinessTravelEmployeeCommuting():
        def __init__(self) -> None:

        #       Vehicle Type	                                            "CO2 Factor (kg / unit)" "CH4 Factor(g / unit)"	"N2O Factor  (g / unit)"	Units
                self.passengerCarA       	                            =    [0.343, 	            0.019,                   	  0.011 ]	#vehicle-mile
                self.lightDutyTruckB     	                            =    [0.472, 	            0.019,                   	  0.018 ]	#vehicle-mile
                self.motorcycle      	                                    =    [0.189, 	            0.070,                   	  0.007 ]	#vehicle-mile
                self.intercityRailC      	                            =    [0.140 ,	            0.0087,                   	  0.0031] #	passenger-mile (i.e. Amtrak) 
                self.commuterRailD       	                            =    [0.161 ,	            0.0081,                   	  0.0032] #	passenger-mile
                self.transitRailE        	                            =    [0.119 ,	            0.0025,                   	  0.0017] #	passenger-mile (i.e. Subway, Tram)
                self.bus                 	                            =    [0.056 ,	            0.0013,                   	  0.0009] #	passenger-mile
                self.airTravelShotHaulLess300miles                          =    [0.225 ,	            0.0039,                   	  0.0072] #	passenger-mile
                self.airTravelMediumHaulMore300MilesLess2300mile            =    [0.136 ,	            0.0006,                   	  0.0043] #   passenger-mile
                self.airTravelLongHaulMore300Miles                    	    =    [0.166 ,	            0.0006,                   	  0.0053] #	passenger-mile

        def makeList(self):
                dataTola=[self.passengerCarA       	                ,self.lightDutyTruckB     	                ,self.motorcycle      	                        ,self.intercityRailC      
                        ,self.commuterRailD       	                ,self.transitRailE        	                ,self.bus                 	                ,self.airTravelShotHaulLess300miles              ,self.airTravelMediumHaulMore300MilesLess2300mile,
                          self.airTravelLongHaulMore300Miles              ]
                return dataTola


class    UpstreamTransportationDistributionDownstreamTransportationDistribution():
        def __init__(self) -> None:


                self.mediumHeavyDutyTruck	=  [1.467, 	  0.014, 	  0.010 ]	#vehicle-mile
                self.passengerCarA              =  [0.343,        0.019,          0.011 ]	#vehicle-mile
                self.lightDutyTruckB     	=  [0.472, 	  0.019, 	  0.018 ]	#vehicle-mile
                self.mediumHeavyDutyTruckC	=  [0.202 ,	  0.0020, 	  0.0015]	#ton-mile
                self.rail                	=  [0.023 ,	  0.0018, 	  0.0006]	#ton-mile
                self.waterborneCraft     	=  [0.059 ,	  0.0005, 	  0.0040]	#ton-mile
                self.aircraft            	=  [1.308 ,	  0.0000, 	  0.0402]	#ton-mile

        def makeList(self):
                dataTola=[self.mediumHeavyDutyTruck,self.passengerCarA       ,self.lightDutyTruckB     ,self.mediumHeavyDutyTruckC
                          ,self.rail                ,self.waterborneCraft     ,self.aircraft            ]
                return dataTola

class ImpactosegmentoMercadoAutomovilesTipoCombustible():
        def __init__(self) -> None:

                self.carsMiniKm                      =	  [0.11009, 	  0.10825, 	  0.000004,	  0.00184, 	  0.13975, 	  0.13905, 	  0.00032, 	  0.00038, 	  0.13958, 	  0.13887, 	  0.00032, 	  0.00039,                                					  0.0 ,   	  0.0,     	  0.0,     	  0.0]     
                self.carsMiniMiles                   =	  [0.17719, 	  0.17421, 	  0.00001 ,	  0.00297, 	  0.2249 , 	  0.22378, 	  0.00051, 	  0.00061, 	  0.22463, 	  0.22349, 	  0.00051, 	  0.00063,                                					  0.0 ,   	  0.0,     	  0.0,     	  0.0]     
                self.carSuperMiniKm                  =	  [0.13449, 	  0.13265, 	  0.000004,	  0.00184, 	  0.15538, 	  0.15468, 	  0.00032, 	  0.00038, 	  0.15241, 	  0.15155, 	  0.00027, 	  0.00059, 	  0.02935, 	  0.02918, 	  0.00009, 	  0.00008, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carSuperMiniMiles               =    [0.21647, 	  0.21349, 	  0.00001 ,	  0.00297, 	  0.25006, 	  0.24894, 	  0.00051, 	  0.00061, 	  0.24528, 	  0.24389, 	  0.00044, 	  0.00095, 	  0.04723, 	  0.04696, 	  0.00014, 	  0.00013, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carLowerMediumKm                =	  [0.14691, 	  0.14507, 	  0.000004,	  0.00184, 	  0.18008, 	  0.17938, 	  0.00032, 	  0.00038, 	  0.16362, 	  0.16235, 	  0.00016, 	  0.00111, 	  0.064  , 	  0.06362, 	  0.0002 , 	  0.00018, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carLowerMediumMiles             =	  [0.23644, 	  0.23346, 	  0.00001 ,	  0.00297, 	  0.2898 , 	  0.28868, 	  0.00051, 	  0.00061, 	  0.26332, 	  0.26128, 	  0.00026, 	  0.00178, 	  0.10299, 	  0.10238, 	  0.00032, 	  0.00029, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carUpperMediumKm                =	  [0.16533, 	  0.16349, 	  0.000004,	  0.00184, 	  0.20792, 	  0.20722, 	  0.00032, 	  0.00038, 	  0.17537, 	  0.17379, 	  0.00008, 	  0.0015 , 	  0.07429, 	  0.07383, 	  0.00022, 	  0.00024, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carUpperMediumMiles             =	  [0.2661 , 	  0.26312, 	  0.00001 ,	  0.00297, 	  0.33461, 	  0.33349, 	  0.00051, 	  0.00061, 	  0.28223, 	  0.27969, 	  0.00013, 	  0.00241, 	  0.11955, 	  0.11882, 	  0.00035, 	  0.00038, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carUpperExecutiveKm             =	  [0.17525, 	  0.17341, 	  0.000004,	  0.00184, 	  0.23659, 	  0.23589, 	  0.00032, 	  0.00038, 	  0.18909, 	  0.1875 , 	  0.00008, 	  0.00151, 	  0.07546, 	  0.07502, 	  0.00023, 	  0.00021] 				
                self.carUpperExecutiveMiles          =	  [0.28206, 	  0.27908, 	  0.00001 ,	  0.00297, 	  0.38075, 	  0.37963, 	  0.00051, 	  0.00061, 	  0.30432, 	  0.30176, 	  0.00012, 	  0.00244, 	  0.12144, 	  0.12073, 	  0.00037, 	  0.00034] 				
                self.carLuxuryKm                     =	  [0.21286, 	  0.21102, 	  0.000004,	  0.00184, 	  0.33566, 	  0.33496, 	  0.00032, 	  0.00038, 	  0.26919, 	  0.26787, 	  0.00015, 	  0.00117, 	  0.09634, 	  0.09577, 	  0.0003 , 	  0.00027, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carLuxuryMiles                  =	  [0.34258, 	  0.3396 , 	  0.00001 ,	  0.00297, 	  0.54019, 	  0.53907, 	  0.00051, 	  0.00061, 	  0.43322, 	  0.43109, 	  0.00024, 	  0.00189, 	  0.15504, 	  0.15413, 	  0.00047, 	  0.00044, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carSportsKm                     =	  [0.17332, 	  0.17148, 	  0.000004,	  0.00184, 	  0.246  , 	  0.2453 , 	  0.00032, 	  0.00038, 	  0.23441, 	  0.23353, 	  0.00027, 	  0.00061, 	  0.07981, 	  0.07935, 	  0.00024, 	  0.00022, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carSportsMiles                  =	  [0.27895, 	  0.27597, 	  0.00001 ,	  0.00297, 	  0.3959 , 	  0.39478, 	  0.00051, 	  0.00061, 	  0.37724, 	  0.37582, 	  0.00043, 	  0.00099, 	  0.12845, 	  0.1277 , 	  0.00039, 	  0.00036, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carDualPurpose4X4Km             =	  [0.20257, 	  0.20073, 	  0.000004,	  0.00184, 	  0.23663, 	  0.23593, 	  0.00032, 	  0.00038, 	  0.20925, 	  0.20762, 	  0.00007, 	  0.00156, 	  0.07626, 	  0.07581, 	  0.00023, 	  0.00022, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carDualPurpose4X4Miles          =	  [0.32602, 	  0.32304, 	  0.00001 ,	  0.00297, 	  0.38081, 	  0.37969, 	  0.00051, 	  0.00061, 	  0.33675, 	  0.33413, 	  0.00011, 	  0.00251, 	  0.12273, 	  0.122  , 	  0.00037, 	  0.00036, 	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carMPVKm                        =	  [0.18101, 	  0.17917, 	  0.000004,	  0.00184, 	  0.1994 , 	  0.1987 , 	  0.00032, 	  0.00038, 	  0.1861 , 	  0.18457, 	  0.00009, 	  0.00144,                                					  0.0,   	  0.0,     	  0.0,     	  0.0]     
                self.carMiles                        =	  [0.29133, 	  0.28835, 	  0.00001 ,	  0.00297, 	  0.32089, 	  0.31977, 	  0.00051, 	  0.00061, 	  0.29951, 	  0.29704, 	  0.00015, 	  0.00232,                                					  0.0 ,   	  0.0,     	  0.0,     	  0.0]     

        def makeList(self):
                dataTola=[self.carsMiniKm            ,self.carsMiniMiles         ,self.carSuperMiniKm        ,self.carSuperMiniMiles     ,self.carLowerMediumKm      ,self.carLowerMediumMiles   ,self.carUpperMediumKm      ,self.carUpperMediumMiles   ,self.carUpperExecutiveKm   ,self.carUpperExecutiveMiles
                          ,self.carLuxuryKm           ,self.carLuxuryMiles        ,self.carSportsKm           ,self.carSportsMiles        ,self.carDualPurpose4X4Km   ,self.carDualPurpose4X4Miles,self.carMPVKm              ,self.carMiles              ]
                return dataTola

class ImpactoTamanoAutomovilesTipoCombustible():
        def __init__(self) -> None:
                
#			                                                Diesel				                        Petrol          				        Hybrid                          				CNG                                     				LPG				                                Unknown				        Plug-in Hybrid Electric Vehicle				                        Battery Electric Vehicle			
#Activity	Type	Unit	                       kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e        	kg CO2  	kg CH   4	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O                
                self.carsSmallCarKm          	=  [0.14208, 	  0.14024, 	  0.000004,	  0.00184, 	  0.15371, 	  0.15301, 	  0.00032, 	  0.00038, 	  0.1052 , 	  0.10409, 	  0.00021, 	  0.0009 , 									                                                                0.14958,	0.14847,	0.00021,	0.00090,	0.02935,	0.02918,	0.00009,	0.00008,	  0.0,     	  0.0,     	  0.0,     	  0.0]    
                self.carsSmallCarMiles       	=  [0.22868, 	  0.2257 , 	  0.00001 ,	  0.00297, 	  0.24736, 	  0.24624, 	  0.00051, 	  0.00061, 	  0.1693 , 	  0.16752, 	  0.00033, 	  0.00145, 									                                                                0.24072,	0.23894,	0.00033,	0.00145,	0.04723,	0.04696,	0.00014,	0.00013,	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carMediumCarKm          	=  [0.17061, 	  0.16877, 	  0.000004,	  0.00184, 	  0.19228, 	  0.19158, 	  0.00032, 	  0.00038, 	  0.10895, 	  0.10764, 	  0.00015, 	  0.00116, 	  0.16176,	  0.15972,	  0.00159,	  0.00045,	0.18066,	0.18016,	0.00005,	0.00045,	0.18071,	0.17940,	0.00015,	0.00116,	0.07083,	0.07040,	0.00021,	0.00022,	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carMediumCarMiles       	=  [0.27459, 	  0.27161, 	  0.00001 ,	  0.00297, 	  0.30945, 	  0.30833, 	  0.00051, 	  0.00061, 	  0.17534, 	  0.17323, 	  0.00024, 	  0.00187, 	  0.26034,	  0.25705,	  0.00257,	  0.00072,	0.29073,	0.28993,	0.00008,	0.00072,	0.29082,	0.28871,	0.00024,	0.00187,	0.11399,	0.11330,	0.00034,	0.00035,	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carLargeCarKm           	=  [0.20947, 	  0.20763, 	  0.000004,	  0.00184, 	  0.28295, 	  0.28225, 	  0.00032, 	  0.00038, 	  0.13177, 	  0.13022, 	  0.00009, 	  0.00146, 	  0.23735,	  0.23531,	  0.00159,	  0.00045,	0.26591,	0.26541,	0.00005,	0.00045,	0.22857,	0.22702,	0.00009,	0.00146,	0.07731,	0.07685,	0.00024,	0.00022,	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carLargeCarmiles        	=  [0.33713, 	  0.33415, 	  0.00001 ,	  0.00297, 	  0.45536, 	  0.45424, 	  0.00051, 	  0.00061, 	  0.21207, 	  0.20957, 	  0.00014, 	  0.00236, 	  0.38198,	  0.37869,	  0.00257,	  0.00072,	0.42794,	0.42714,	0.00008,	0.00072,	0.36785,	0.36535,	0.00014,	0.00236,	0.12442,	0.12368,	0.00038,	0.00036,	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carAverageCarKm         	=  [0.17336, 	  0.17152, 	  0.000004,	  0.00184, 	  0.18084, 	  0.18014, 	  0.00032, 	  0.00038, 	  0.11473, 	  0.11346, 	  0.00016, 	  0.00111, 	  0.17803,	  0.17599,	  0.00159,	  0.00045,	0.19901,	0.19851,	0.00005,	0.00045,	0.17710,	0.17583,	0.00016,	0.00111,	0.07075,	0.07033,	0.00021,	0.00021,	  0.0,     	  0.0,     	  0.0,     	  0.0]     
                self.carAverageCarMiles      	=  [0.27901, 	  0.27603, 	  0.00001 ,	  0.00297, 	  0.29103, 	  0.28991, 	  0.00051, 	  0.00061, 	  0.18464, 	  0.18259, 	  0.00026, 	  0.00179, 	  0.28653,	  0.28324,	  0.00257,	  0.00072,	0.32027,	0.31947,	0.00008,	0.00072,	0.28502,	0.28297,	0.00026,	0.00179,	0.11386,	0.11318,	0.00034,	0.00034,	  0.0,     	  0.0,     	  0.0,     	  0.0]     

        def makeList(self):
                dataTola=[self.carsSmallCarKm    ,self.carsSmallCarMiles ,self.carMediumCarKm    ,self.carMediumCarMiles ,self.carLargeCarKm     ,self.carLargeCarmiles  ,self.carAverageCarKm   ,self.carAverageCarMiles]
                return dataTola


class ImpactoTamanoMotocicletasDistanciaRecorrida(): 
        def __init__(self) -> None:
               
#Activity	Type	Unit	                        kg CO2e	           kg CO2          kg CH4      	  kg N2O
                self.motorbikeSmallKm                =	  [0.08445, 	  0.08241, 	  0.00174, 	  0.0003 ] 
                self.motorbikeSmallMiles             =	  [0.13591, 	  0.13263, 	  0.0028 , 	  0.00048] 
                self.motorbikeMediumKm               =	  [0.10289, 	  0.10004, 	  0.00225, 	  0.0006 ] 
                self.motorbikeMediumKmmiles          =	  [0.16559,       0.1610,	  0.00362, 	  0.00097] 
                self.motorbikeLargeKm                =	  [0.13501, 	  0.13308, 	  0.00133, 	  0.0006 ] 
                self.motorbikeLargeMiles             =	  [0.21729, 	  0.21418, 	  0.00214, 	  0.00097] 
                self.motorbikeAverageKm              =	  [0.11551, 	  0.11314, 	  0.00178, 	  0.00059] 
                self.motorbikeAverageMiles           =	  [0.18589, 	  0.18208, 	  0.00286, 	  0.00095]

        def makeList(self):
                dataTola=[self.motorbikeSmallKm      ,self.motorbikeSmallMiles   ,self.motorbikeMediumKm     ,self.motorbikeMediumKmmiles,
                          self.motorbikeLargeKm      ,self.motorbikeLargeMiles   ,self.motorbikeAverageKm    ,self.motorbikeAverageMiles ]
                return dataTola

class ImpactoTipoddeVueloAero ():
        def __init__(self) -> None:
                self.flightsDomestictoUKAveragePassengerKm	                   =     [0.25493, 	  0.25355, 	  0.00012 ,	  0.00126 ,	  0.13483 ,	  0.13345 ,	  0.00012 ,	  0.00126 ]
                self.flightsShortHaulToUKAveragePassengerKm	                   =     [0.15832, 	  0.15753, 	  0.00001 ,	  0.00078 ,	  0.0837  ,	  0.08291 ,	  0.00001 ,	  0.00078 ]
                self.flightsShortHaulToUKEconomyPassengerKm	                   =     [0.15573, 	  0.15495, 	  0.00001 ,	  0.00077 ,	  0.08233 ,	  0.08155 ,	  0.00001 ,	  0.00077 ]
                self.flightsShortHaulToUKBusinessPassengerKm	                   =     [0.2336 , 	  0.23243, 	  0.00001 ,	  0.00116 ,	  0.1235  ,	  0.12233 ,	  0.00001 ,	  0.00116 ]
                self.flightsLongHaulToUKAveragePassengerKm	                   =     [0.19562, 	  0.19464,  	  0.00001, 	  0.00097, 	  0.10342, 	  0.10244, 	  0.00001, 	  0.00097] 
                self.flightsLongHaulToUKEconomyPassengerKm	                   =     [0.14981, 	  0.14906, 	  0.00001 ,	  0.00074 ,	  0.0792  ,	  0.07845 ,	  0.00001 ,	  0.00074 ]
                self.flightsLongHaulToUKPremiumEconomyPassengerKm                  =     [0.2397 , 	  0.2385 , 	  0.00001 ,	  0.00119 ,	  0.12673 ,	  0.12553 ,	  0.00001 ,	  0.00119 ]
                self.flightsLongHaulToUKBusinessPassengerKm	                   =     [0.43446, 	  0.43229, 	  0.00002 ,	  0.00215 ,	  0.22969 ,	  0.22752 ,	  0.00002 ,	  0.00215 ]
                self.flightsLongHaulToUKFirstPassengerKm	                   =     [0.59925, 	  0.59626, 	  0.00002 ,	  0.00297 ,	  0.31681 ,	  0.31382 ,	  0.00002 ,	  0.00297 ]
                self.flightsInternationalToNonUKAveragePassengerKm	           =     [0.18078, 	  0.17987, 	  0.00001 ,	  0.0009  ,	  0.09558 ,	  0.09467 ,	  0.00001 ,	  0.0009  ]
                self.flightsInternationalToNonUKEconomyPassengerKm	           =     [0.138445,	  0.13775, 	  0.000005,	  0.00069 ,	  0.073195,	  0.0725  ,	  0.000005,	  0.00069 ]
                self.flightsInternationalToNonUKPremiumEconomyClassKm	           =     [0.22151, 	  0.2204 , 	  0.00001 ,	  0.0011  ,	  0.11711 ,	  0.116   ,	  0.00001 ,	  0.0011  ]
                self.flightsInternationalToNonUKBusinessClassKm	                   =     [0.40149, 	  0.39948, 	  0.00002 ,	  0.00199 ,	  0.21226 ,	  0.21025 ,	  0.00002 ,	  0.00199 ]
                self.flightsInternationalToNonUKFirstClassPassengerKm	           =     [0.55376, 	  0.551  , 	  0.00002 ,	  0.00274 ,	  0.29276 ,	  0.29    ,	  0.00002 ,	  0.00274 ]
        
        
        def makeList(self):
                dataTola=[self.flightsDomestictoUKAveragePassengerKm	    ,self.flightsShortHaulToUKAveragePassengerKm	    ,self.flightsShortHaulToUKEconomyPassengerKm	    ,self.flightsShortHaulToUKBusinessPassengerKm	    ,self.flightsLongHaulToUKAveragePassengerKm	    ,self.flightsLongHaulToUKEconomyPassengerKm	    ,self.flightsLongHaulToUKPremiumEconomyPassengerKm
                          ,self.flightsLongHaulToUKBusinessPassengerKm	    ,self.flightsLongHaulToUKFirstPassengerKm	    ,self.flightsInternationalToNonUKAveragePassengerKm,self.flightsInternationalToNonUKEconomyPassengerKm,self.flightsInternationalToNonUKPremiumEconomyClassKm,self.flightsInternationalToNonUKBusinessClassKm	    ,self.flightsInternationalToNonUKFirstClassPassengerKm]
                return dataTola

class  ImpactoTipoFerry():
        def __init__(self) -> None:
                
                self.ferryFootPassengerKm	        =      [0.01874,	  0.01848,	  0.00001,	  0.00025]
                self.ferryCarPassengerKm	        =      [0.12952,	  0.12774,	  0.00004,	  0.00174]
                self.ferryAverageAllPassengerKm 	=      [0.11286,	  0.11131,	  0.00003,	  0.00152]

        def makeList(self):
                dataTola=[self.ferryFootPassengerKm,self.ferryCarPassengerKm,self.ferryAverageAllPassengerKm]
                return dataTola

class ImpactoPorSegmentoMercadoAutomovilesTipoDeCombustible():
        def __init__(self) -> None:

#                                                       			Diesel          				Petrol  				                Unknown				                                        Plug-in Hybrid Electric Vehicle				Battery Electric Vehicle			
#Activity	Type	Unit	                kg CO2e	          kg CO2	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O	        kg CO2e	        kg CO2	        kg CH4  	kg N2O	        kg CO2e	        kg CO2	        kg CH4	        kg N2O	        kg CO2e 	kg CO2	        kg CH4	        kg N2O                

                self.carsMiniKm              =	  [0.11009, 	  0.10825, 	  0.000004,	  0.00184, 	  0.13975, 	  0.13905, 	  0.00032, 	  0.00038, 	  0.13958, 	  0.13887, 	  0.00032, 	  0.00039, 					                                0.05235,	0.05194,	0.00013,	0.00028]
                self.carsMinMiles            =	  [0.17719, 	  0.17421, 	  0.00001 ,	  0.00297, 	  0.2249 , 	  0.22378, 	  0.00051, 	  0.00061, 	  0.22463, 	  0.22349, 	  0.00051, 	  0.00063, 					                                0.08425,	0.08359,	0.00021,	0.00045]
                self.carSuperMiniKm          =	  [0.13449, 	  0.13265, 	  0.000004,	  0.00184, 	  0.15538, 	  0.15468, 	  0.00032, 	  0.00038, 	  0.15241, 	  0.15155, 	  0.00027, 	  0.00059, 	0.07347,	0.07295,	0.00020,	0.00032,	0.04788,	0.04750,	0.00012,	0.00026]
                self.carSuperMiniMiles       =	  [0.21647, 	  0.21349, 	  0.00001 ,	  0.00297, 	  0.25006, 	  0.24894, 	  0.00051, 	  0.00061, 	  0.24528, 	  0.24389, 	  0.00044, 	  0.00095, 	0.11823,	0.11740,	0.00032,	0.00051,	0.07704,	0.07644,	0.00019,	0.00041]
                self.carLowerMediumKm        =	  [0.14691, 	  0.14507, 	  0.000004,	  0.00184, 	  0.18008, 	  0.17938, 	  0.00032, 	  0.00038, 	  0.16362, 	  0.16235, 	  0.00016, 	  0.00111, 	0.10104,	0.10037,	0.00029,	0.00038,	0.05772,	0.05726,	0.00015,	0.00031]
                self.carLowerMediumMiles     =	  [0.23644, 	  0.23346, 	  0.00001 ,	  0.00297, 	  0.2898 , 	  0.28868, 	  0.00051, 	  0.00061, 	  0.26332, 	  0.26128, 	  0.00026, 	  0.00178, 	0.16260,	0.16152,	0.00047,	0.00061,	0.09288,	0.09215,	0.00023,	0.00050]
                self.carUpperMediumKm        =	  [0.16533, 	  0.16349, 	  0.000004,	  0.00184, 	  0.20792, 	  0.20722, 	  0.00032, 	  0.00038, 	  0.17537, 	  0.17379, 	  0.00008, 	  0.0015 , 	0.11448,	0.11371,	0.00032,	0.00045,	0.04659,	0.04622,	0.00012,	0.00025]
                self.carUpperMediuMiles      =	  [0.2661 , 	  0.26312, 	  0.00001 ,	  0.00297, 	  0.33461, 	  0.33349, 	  0.00051, 	  0.00061, 	  0.28223, 	  0.27969, 	  0.00013, 	  0.00241, 	0.18426,	0.18301,	0.00052,	0.00073,	0.07497,	0.07438,	0.00019,	0.00040]
                self.carExecutiveKm          =    [0.17525, 	  0.17341, 	  0.000004,	  0.00184, 	  0.23659, 	  0.23589, 	  0.00032, 	  0.00038, 	  0.18909, 	  0.1875 , 	  0.00008, 	  0.00151, 	0.12417,	0.12335,	0.00035,	0.00047,				]
                self.carExecutiveMiles       =	  [0.28206, 	  0.27908, 	  0.00001 ,	  0.00297, 	  0.38075, 	  0.37963, 	  0.00051, 	  0.00061, 	  0.30432, 	  0.30176, 	  0.00012, 	  0.00244, 	0.19984,	0.19851,	0.00057,	0.00076,				]
                self.carLuxuryKm             =	  [0.21286, 	  0.21102, 	  0.000004,	  0.00184, 	  0.33566, 	  0.33496, 	  0.00032, 	  0.00038, 	  0.26919, 	  0.26787, 	  0.00015, 	  0.00117, 	0.14588,	0.14492,	0.00042,	0.00054,	0.07027,	0.06971,	0.00018,	0.00038]
                self.carLuxuryMiles          =	  [0.34258, 	  0.3396 , 	  0.00001 ,	  0.00297, 	  0.54019, 	  0.53907, 	  0.00051, 	  0.00061, 	  0.43322, 	  0.43109, 	  0.00024, 	  0.00189, 	0.23477,	0.23323,	0.00068,	0.00086,	0.11309,	0.11219,	0.00029,	0.00061]
                self.carSportsKm             =	  [0.17332, 	  0.17148, 	  0.000004,	  0.00184, 	  0.246  , 	  0.2453 , 	  0.00032, 	  0.00038, 	  0.23441, 	  0.23353, 	  0.00027, 	  0.00061, 	0.11895,	0.11818,	0.00034,	0.00043,	0.08968,	0.08897,	0.00023,	0.00048]
                self.carSportsMiles          =	  [0.27895, 	  0.27597, 	  0.00001 ,	  0.00297, 	  0.3959 , 	  0.39478, 	  0.00051, 	  0.00061, 	  0.37724, 	  0.37582, 	  0.00043, 	  0.00099, 	0.19144,	0.19019,	0.00055,	0.00070,	0.14432,	0.14318,	0.00036,	0.00078]
                self.carDualPurpose4X4Km     =    [0.20257, 	  0.20073, 	  0.000004,	  0.00184, 	  0.23663, 	  0.23593, 	  0.00032, 	  0.00038, 	  0.20925, 	  0.20762, 	  0.00007, 	  0.00156, 	0.12502,	0.12419,	0.00035,	0.00048,	0.08033,	0.07970,	0.00020,	0.00043]
                self.carDualPurpose4X4Miles  =	  [0.32602, 	  0.32304, 	  0.00001 ,	  0.00297, 	  0.38081, 	  0.37969, 	  0.00051, 	  0.00061, 	  0.33675, 	  0.33413, 	  0.00011, 	  0.00251, 	0.20121,	0.19986,	0.00057,	0.00078,	0.12929,	0.12827,	0.00033,	0.00069]
                self.carMPVKm                =	  [0.18101, 	  0.17917, 	  0.000004,	  0.00184, 	  0.1994 , 	  0.1987 , 	  0.00032, 	  0.00038, 	  0.1861 , 	  0.18457, 	  0.00009, 	  0.00144, 					                                0.06404,	0.06354,	0.00016,	0.00034]
                self.carMPVMiles             =	  [0.29133, 	  0.28835, 	  0.00001 ,	  0.00297, 	  0.32089, 	  0.31977, 	  0.00051, 	  0.00061, 	  0.29951, 	  0.29704, 	  0.00015, 	  0.00232, 					                                0.10306,	0.10225,	0.00026,	0.00055]

        def makeList(self):
                dataTola=[self.carsMiniKm            ,self.carsMinMiles          ,self.carSuperMiniKm,self.carSuperMiniMiles     ,self.carLowerMediumKm,self.carLowerMediumMiles   ,self.carUpperMediumKm      ,self.carUpperMediuMiles
                          ,self.carExecutiveKm        ,self.carExecutiveMiles     ,self.carLuxuryKm,self.carLuxuryMiles,self.carSportsKm,self.carSportsMiles        ,self.carDualPurpose4X4Km   ,self.carDualPurpose4X4Miles,self.carMPVKm              ,self.carMPVMiles           ]

                return dataTola
class ImpactoTamanoAutomovilesTipoCombustible():
        def __init__(self) -> None:
#			                                                                Diesel				                        Petrol				                                Hybrid          			                	CNG		                	                	LPG				                        Unknown				                        Plug-in Hybrid Electric Vehicle			        	Battery Electric Vehicle			
#Activity	Type	Unit	                        kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O  	kg CO2e 	kg CO2  	kg CH4  	kg N2O                

                self.carsSmallCarKm	       =         [0.14208, 	  0.14024, 	  0.000004,	  0.00184, 	  0.15371, 	  0.15301, 	  0.00032, 	  0.00038, 	  0.1052 , 	  0.10409, 	  0.00021, 	  0.0009 , 									                                                                  0.14958, 	  0.14847, 	  0.00021, 	  0.0009 ,      0.07347,	0.07295,        0.00020,	0.00032,	0.04956,	0.04916,	0.00013,	0.00027]
                self.carsSmallCarMiles	       =         [0.22868, 	  0.2257 , 	  0.00001 ,	  0.00297, 	  0.24736, 	  0.24624, 	  0.00051, 	  0.00061, 	  0.1693 , 	  0.16752, 	  0.00033, 	  0.00145, 									                                                                  0.24072, 	  0.23894, 	  0.00033, 	  0.00145,      0.11823,	0.11740,	0.00032,	0.00051,	0.07975,	0.07912,	0.00020,	0.00043]
                self.carMediumCarKm	       =         [0.17061, 	  0.16877, 	  0.000004,	  0.00184, 	  0.19228, 	  0.19158, 	  0.00032, 	  0.00038, 	  0.10895, 	  0.10764, 	  0.00015, 	  0.00116, 	  0.16176, 	  0.15972, 	  0.00159, 	  0.00045, 	  0.18066, 	  0.18016, 	  0.00005, 	  0.00045, 	  0.18071, 	  0.1794 , 	  0.00015, 	  0.00116, 	0.10998,	0.10924,	0.00031,	0.00043,	0.05769,	0.05723,	0.00015,	0.00031]
                self.carMediumCarMiles	       =         [0.27459, 	  0.27161, 	  0.00001 ,	  0.00297, 	  0.30945, 	  0.30833, 	  0.00051, 	  0.00061, 	  0.17534, 	  0.17323, 	  0.00024, 	  0.00187, 	  0.26034, 	  0.25705, 	  0.00257, 	  0.00072, 	  0.29073, 	  0.28993, 	  0.00008, 	  0.00072, 	  0.29082, 	  0.28871, 	  0.00024, 	  0.00187, 	0.17699,	0.17580,	0.00050,	0.00069,	0.09282,	0.09209,	0.00023,	0.00050]
                self.carLargeCarKm	       =         [0.20947, 	  0.20763, 	  0.000004,	  0.00184, 	  0.28295, 	  0.28225, 	  0.00032, 	  0.00038, 	  0.13177, 	  0.13022, 	  0.00009, 	  0.00146, 	  0.23735, 	  0.23531, 	  0.00159, 	  0.00045, 	  0.26591, 	  0.26541, 	  0.00005, 	  0.00045, 	  0.22857, 	  0.22702, 	  0.00009, 	  0.00146, 	0.12567,	0.12483,	0.00036,	0.00048,	0.07256,	0.07199,	0.00018,	0.00039]
                self.carLargeCarMiles	       =         [0.33713, 	  0.33415, 	  0.00001 ,	  0.00297, 	  0.45536, 	  0.45424, 	  0.00051, 	  0.00061, 	  0.21207, 	  0.20957, 	  0.00014, 	  0.00236, 	  0.38198, 	  0.37869, 	  0.00257, 	  0.00072, 	  0.42794, 	  0.42714, 	  0.00008, 	  0.00072, 	  0.36785, 	  0.36535, 	  0.00014, 	  0.00236, 	0.20225,	0.20090,	0.00057,	0.00078,	0.11677,	0.11585,	0.00029,	0.00063]
                self.carAverageCarKm	       =         [0.17336, 	  0.17152, 	  0.000004,	  0.00184, 	  0.18084, 	  0.18014, 	  0.00032, 	  0.00038, 	  0.11473, 	  0.11346, 	  0.00016, 	  0.00111, 	  0.17803, 	  0.17599, 	  0.00159, 	  0.00045, 	  0.19901, 	  0.19851, 	  0.00005, 	  0.00045, 	  0.1771 , 	  0.17583, 	  0.00016, 	  0.00111, 	0.11532,	0.11454,	0.00033,	0.00045,	0.06020,	0.05973,	0.00015,	0.00032]
                self.carAverageCarMiles	       =         [0.27901, 	  0.27603, 	  0.00001 ,	  0.00297, 	  0.29103, 	  0.28991, 	  0.00051, 	  0.00061, 	  0.18464, 	  0.18259, 	  0.00026, 	  0.00179, 	  0.28653, 	  0.28324, 	  0.00257, 	  0.00072, 	  0.32027, 	  0.31947, 	  0.00008, 	  0.00072, 	  0.28502, 	  0.28297, 	  0.00026, 	  0.00179, 	0.18559,	0.18434,	0.00053,	0.00072,	0.09688,	0.09612,	0.00024,	0.00052]

        def makeList(self):
                dataTola=[self.carsSmallCarKm	,self.carsSmallCarMiles	,self.carMediumCarKm	,self.carMediumCarMiles	,self.carLargeCarKm	,self.carLargeCarMiles	,self.carAverageCarKm	,self.carAverageCarMiles	]

                return dataTola

class 	ImpactoTamanoMotocicleta():
        def __init__(self) -> None:
               					
						
#Activity	Type	Unit	                  kg CO2e 	  kg CO2	   kg CH4  	  kg N2O
                self.motorbikeSmallKm	        =  [0.08445, 	  0.08241, 	  0.00174, 	  0.0003 ] 
                self.motorbikeSmallMiles	=  [0.13591, 	  0.13263, 	  0.0028 , 	  0.00048] 
                self.motorbikeMediumKm	        =  [0.10289, 	  0.10004, 	  0.00225, 	  0.0006 ] 
                self.motorbikeMediumMiles	=  [0.16559, 	  0.161  , 	  0.00362, 	  0.00097] 
                self.motorbikeLargeKm	        =  [0.13501, 	  0.13308, 	  0.00133, 	  0.0006 ] 
                self.motorbikeLargeMiles	=  [0.21729, 	  0.21418, 	  0.00214, 	  0.00097] 
                self.motorbieAverageKm	        =  [0.11551, 	  0.11314, 	  0.00178, 	  0.00059] 
                self.motorbieAverageMiles	=  [0.18589, 	  0.18208, 	  0.00286, 	  0.00095] 

        def makeList(self):
                dataTola=[self.motorbikeSmallKm	 ,self.motorbikeSmallMiles,self.motorbikeMediumKm	 ,self.motorbikeMediumMiles,self.motorbikeLargeKm	 ,self.motorbikeLargeMiles,self.motorbieAverageKm	 ,self.motorbieAverageMiles]
                return dataTola

class 	ImpactoTipoTaxi():
        def __init__(self) -> None:
                
						
#Activity	Type	Unit	                        kg CO2e 	kg CO2  	kg CH4  	kg N2O
                self.taxisRegularTaxiPassengerKm      =  [0.15018, 	  0.14886, 	  0.000003,	  0.00132]
                self.taxisRegularTaxiKm      	      =  [0.21024, 	  0.2084 , 	  0.000004,	  0.00184]
                self.taxisBlackCabPassengerKm	      =  [0.21176, 	  0.21053, 	  0.000003,	  0.00123]
                self.taxisBlackCabKm         	      =  [0.31764, 	  0.3158 , 	  0.000004,	  0.00184]
        def makeList(self):
                dataTola=[self.taxisRegularTaxiPassengerKm,self.taxisRegularTaxiKm      	,self.taxisBlackCabPassengerKm	,self.taxisBlackCabKm ]
                return dataTola
        
class 	ImpactoTipoAutobus():
        def __init__(self) -> None:
                
						
#               Activity	Type	Unit	        kg CO2e 	kg CO2  	kg CH4  	kg N2O
                self.busLocalBusLondonPassengerKm    =	  [0.12076, 	  0.11974, 	  0.00003, 	  0.00099] #(not London)
                self.busLocalLondonBusPassengerKm    =	  [0.08208, 	  0.08163, 	  0.00001, 	  0.00044] 
                self.busAverageLocalBusPassengerKm   =	  [0.10471, 	  0.10391, 	  0.00003, 	  0.00077] 
                self.busCoachPassengerKm             =    [0.02779, 	  0.02728, 	  0.00002, 	  0.00049] 

        def makeList(self):
                dataTola=[self.busLocalBusLondonPassengerKm ,self.busLocalLondonBusPassengerKm ,self.busAverageLocalBusPassengerKm,self.busCoachPassengerKm ]
                return dataTola

class 	ImpactoTipoFerrocarril():
        def __init__(self) -> None:
                pass
#               Activity      	Type	Unit	                kg CO2e 	kg CO2  	kg CH4  	kg N2O
                self.railNationalRailPassengerKm        	=  [0.04115, 	  0.04077, 	  0.00007, 	  0.00031]
                self.railInternationalRailPassengerKm   	=  [0.00597, 	  0.00592, 	  0.00002, 	  0.00003]
                self.railLightRailTramPassengerKm       	=  [0.03508, 	  0.0348 , 	  0.00009, 	  0.00019]
                self.railLondonUndergroundPassengerKm   	=  [0.03084, 	  0.03059, 	  0.00008, 	  0.00017]

        def makeList(self):
                dataTola=[self.railNationalRailPassengerKm     ,self.railInternationalRailPassengerKm,self.railLightRailTramPassengerKm    
                ,self.railLondonUndergroundPassengerKm]

                return dataTola
        

class    GlobalWarmingPotentials(): #(GWPs)
        def __init__(self) -> None:
              #Gas	                100-Year GWP
                self.CO2 	           =     [1 ]
                self.CH4	           =     [25 ]
                self.N2O	           =     [298 ]
                self.HFC23	           =     [14800 ]
                self.HFC32	           =     [675 ]
                self.HFC41	           =     [92 ]
                self.HFC125	           =     [3500 ]
                self.HFC134	           =     [1100 ]
                self.HFC134a	           =     [1430 ]
                self.HFC143	           =     [353 ]
                self.HFC143a	           =     [4470 ]
                self.HFC152	           =     [53 ]
                self.HFC152a	           =     [124 ]
                self.HFC161	           =     [12 ]
                self.HFC227ea	           =     [3220 ]
                self.HFC236cb	           =     [1340 ]
                self.HFC236ea	           =     [1370 ]
                self.HFC236fa	           =     [9810 ]
                self.HFC245ca	           =     [693 ]
                self.HFC245fa	           =     [1030 ]
                self.HFC365mfc	           =     [794 ]
                self.HFC43_10mee	   =     [1640 ]
                self.SF6 	           =     [22800 ]
                self.NF3	           =     [17200 ]
                self.CF4 	           =     [7390 ]
                self.C2F6 	           =     [12200 ]
                self.C3F8	           =     [8830 ]
                self.c_C4F8	           =     [10300 ]
                self.C4F10 	           =     [8860 ]
                self.C5F12	           =     [9160 ]
                self.C6F14	           =     [9300 ]
                self.C10F18	           =     [7500 ]

        def makeList(self):
                dataTola=[self.CO2 	,self.CH4	,self.N2O	,self.HFC23	,self.HFC32	,self.HFC41	,self.HFC125	,self.HFC134	,self.HFC134a	,self.HFC143	,self.HFC143a	,self.HFC152	
                          ,self.HFC152a	,self.HFC161	,self.HFC227ea	,self.HFC236cb	,self.HFC236ea	,self.HFC236fa	,self.HFC245ca	,self.HFC245fa	,self.HFC365mfc	,self.HFC43_10mee,self.SF6 	,self.NF3	
                          ,self.CF4 	,self.C2F6 	,self.C3F8	,self.c_C4F8	,self.C4F10 	,self.C5F12	,self.C6F14	,self.C10F18	]

                return dataTola


class GlobalWarmingPotentialsGWPsBlendedRefrigerants(): #(GWPs) for Blended Refrigerants
        def __init__(self) -> None:
                # ASHRAE #	"100-year GWP	Blend Composition		"	
                self.R_401A  	=  [16 	,       " 53% HCFC-22 , 34% HCFC-124 , 13% HFC-152a"			]
                self.R_401B  	=  [14 	,       " 61% HCFC-22 , 28% HCFC-124 , 11% HFC-152a"			]
                self.R_401C  	=  [19 	,       " 33% HCFC-22 , 52% HCFC-124 , 15% HFC-152a"			]
                self.R_402A  	=  [2100 ,      "  	38% HCFC-22 , 6% HFC-125 , 2% propane"			]
                self.R_402B  	=  [1330 ,      "  	6% HCFC-22 , 38% HFC-125 , 2% propane"			]
                self.R_403B  	=  [3444 ,      "  	56% HCFC-22 , 39% PFC-218 , 5% propane"			]
                self.R_404A  	=  [3922 ,      "  	44% HFC-125 , 4% HFC-134a , 52% HFC 143a"			]
                self.R_406A  	=  [0 	,       " 55% HCFC-22 , 41% HCFC-142b , 4"+"%"+ "isobutane"			]
                self.R_407A  	=  [2107 ,      "  	20% HFC-32 , 40% HFC-125 , 40% HFC-134a"			]
                self.R_407B  	=  [2804 ,      "  	10% HFC-32 , 70% HFC-125 , 20% HFC-134a"			]
                self.R_407C  	=  [1774 ,      "  	23% HFC-32 , 25% HFC-125 , 52% HFC-134a"			]
                self.R_407D  	=  [1627 ,      "  	15% HFC-32 , 15% HFC-125 , 70% HFC-134a"			]
                self.R_407E  	=  [1552 ,      "  	25% HFC-32 , 15% HFC-125 , 60% HFC-134a"			]
                self.R_408A  	=  [2301 ,      "  	47% HCFC-22 , 7% HFC-125 , 46% HFC 143a"			]
                self.R_409A  	=  [0 	,       " 60% HCFC-22 , 25% HCFC-124 , 15% HCFC-142b"			]
                self.R_410A  	=  [2088 ,      "  	50% HFC-32 , 50% HFC-125		"	]
                self.R_410B  	=  [2,229 ,     "   	45% HFC-32 , 55% HFC-125 		"	]
                self.R_411A  	=  [14 	,       " 87.5% HCFC-22 , 11 HFC-152a , 1.5% propylene"			]
                self.R_411B  	=  [4 	,       " 94% HCFC-22 , 3% HFC-152a , 3% propylene	"		]
                self.R_413A  	=  [2053 ,      "  	88% HFC-134a , 9% PFC-218 , 3"+"%"+" isobutane"			]
                self.R_414A  	=  [0 	,       " 51% HCFC-22 , 28.5% HCFC-124 , 16.5% HCFC-142b"			]
                self.R_414B  	=  [0 	,       " 5% HCFC-22 , 39% HCFC-124 , 9.5% HCFC-142b"			]
                self.R_417A  	=  [2346 ,      "  	46.6% HFC-125 , 5% HFC-134a , 3.4"+"%"+"butane"			]
                self.R_422A  	=  [3143 ,      "  	85.1% HFC-125 , 11.5% HFC-134a , 3.4%"+ "isobutane"			]
                self.R_422D  	=  [2729 ,      "  	65.1% HFC-125 , 31.5% HFC-134a , 3.4%" +"isobutane"			]
                self.R_423A  	=  [2280 ,      "  	47.5% HFC-227ea , 52.5% HFC-134a ,  "			]
                self.R_424A  	=  [2440 ,      "  	50.5% HFC-125, 47% HFC-134a, 2.5"+'%' +"butane/pentane"			]
                self.R_426A  	=  [1508 ,      "  	5.1% HFC-125, 93% HFC-134a, 1.9"+'%'+"butane/pentane"			]
                self.R_428A  	=  [3607 ,      "  	77.5% HFC-125 , 2% HFC-143a , 1.9"+'%'+ "isobutane"			]
                self.R_434A  	=  [3245 ,      "  	63.2% HFC-125, 16% HFC-134a, 18% HFC-143a, 2.8"+'%'+ "isobutane"			]
                self.R_500	=  [32 	,       " 73.8% CFC-12 , 26.2% HFC-152a , 48.8% HCFC-22"			]
                self.R_502	=  [0 	,       " 48.8% HCFC-22 , 51.2% CFC-115 			"]
                self.R_504	=  [325, 	",        48.2% HFC-32 , 51.8% CFC-115		"	]
                self.R_507	=  [3985 ,      "  	5% HFC-125 , 5% HFC143a			"]
                self.R_508A  	=  [13214,      "   	39% HFC-23 , 61% PFC-116		"	]
                self.R_508B  	=  [13396,      "   	46% HFC-23 , 54% PFC-116		"	]

        def makeList(self):
                dataTola=[self.R_401A,self.R_401B,self.R_401C,self.R_402A,self.R_402B,self.R_403B,self.R_404A,self.R_406A,self.R_407A,self.R_407B,self.R_407C,self.R_407D,
                          self.R_407E,self.R_408A,self.R_409A,self.R_410A,self.R_410B,self.R_411A,self.R_411B,self.R_413A,self.R_414A,self.R_414B,self.R_417A,self.R_422A,
                          self.R_422D,self.R_423A,self.R_424A,self.R_426A,self.R_428A,self.R_434A,self.R_500,self.R_502,self.R_504,self.R_507,self.R_508A,self.R_508B]
                return dataTola



class FactorEmisionAR():
        def __init__(self) -> None:
                #Common Name	Formula	AR4	AR5
                
                self.CO2        =     	[1,	1]
                self.CH4        =       [25,	28]
                self.N2O        =       [298,	265]
                self.NF3        =	[17200,	16100]
                self.SF6        =	[22800,	23500]
        
        def makeList(self) :
                dataFactorEmission=[self.CO2,self.CH4,self.N2O,self.NF3,self.SF6 ]
                dfEmissionFactor=pd.DataFrame(dataFactorEmission)
                
                return dfEmissionFactor