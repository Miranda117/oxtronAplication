from .formulas import *
import pandas as pd

from .emissionFactor import *
from .conversiones import *
from .data import *
import json


position=originalUnit().originalUnit()

scope2Class=Scope2Form()


class ParameterInput():
    def __init__(self, nameBusines="Phantom company",prepared=" ", GWPdataSet="2014 IPCC Fifth Assessment",
                 B_A_T_E_RFFactors=False, inventoryData=[], facilityInformation=[], NameCustomEF=" ", Scope="Scope1",
                 activityType="",SourEmiFac="", Emission=[]	  ) -> None:
        #Uplift to Business Air Travel emissions using RF factors
        self.nameBusines= nameBusines
        self.prepared= prepared
        self.GWPdataSet= GWPdataSet
        self.B_A_T_E_RFFactors= B_A_T_E_RFFactors
        self.inventoryData= inventoryData
        self.facilityInformation= facilityInformation
        self.NameCustomEF =NameCustomEF
        self.Scope=Scope
        self.activityType=activityType
        self.SourEmiFac=SourEmiFac
        self.Emission=Emission

class Validaciones():
    def __init__(self,data=[]) -> None:
        self.data=data
    
    def seleccionProceso(self):
        pass

    def recepcionDatos(self):
        pass
    
    def camposVacios(self):
        pass

    def validacionProcesso(self):
        pass




validacion=Validaciones()


class DataFrame():
    def separadorDeDatos(self,userSuppliedData):
        dictStationaryCombustion={}
        for i in userSuppliedData:
            for j in range(len(i)):
                key=j
                
                valor = dictStationaryCombustion.get(key)
                if valor is not None:  # comprobamos que el valor no es None
                    dictStationaryCombustion[key].append(i[j])
                else:
                    dictStationaryCombustion[key]=[i[j]]
                    #dictStationaryCombustion[key].append(j)
                
        return (dictStationaryCombustion)

    def separadorDeDatos2(self,userSuppliedData):
#        sas=str(userSuppliedData)


        dictStationaryCombustion={}
        userSuppliedDataJson = json.dumps(userSuppliedData)
        data = json.loads(str(userSuppliedDataJson))

        datos = []
        for scope in data:
            for key, value in scope.items():
                    datos.append(value)
                    if key in dictStationaryCombustion:

                        dictStationaryCombustion[key].append(value)
                        
                        

                    else:
                        #print('La llave "d" existe en el diccionario.')
                        dictStationaryCombustion[key]=[value]
        print(dictStationaryCombustion)
        return (dictStationaryCombustion)
    

class Scope1():

    
    def iterationFacts(self,GWPDataSet,facilityID=0,convertion=26,fuel="",
   amountOfFuel=0,emissionFactor=[]):
        s1=AnalisisCombustible()
        emissionsScope11=[]
        
        
        dFconvertion=TablaConvertions().makeDataFrame()
        arSet=FactorEmisionAR().makeList()
        
        global position
    
        ar=arSet.iloc[:, GWPDataSet]
        for i in range (len(facilityID)):
            multiplicacion=[]
            
            
            oUnit=position.index(emissionFactor[fuel[i]][7])
        
            for j in range(1,5):
                           

                convert=dFconvertion.iloc[oUnit,convertion[i]]
                
                amount=amountOfFuel[i]
                l=emissionFactor[fuel[i]][j]
                
                
                
                
                analisisOperation=s1.analisisCombustible1(combustibleV=amount,EF1=l,conversition=convert)
                multiplicacion.append(analisisOperation)

            multiplicacion[0],multiplicacion[1],multiplicacion[2],multiplicacion[3]=multiplicacion[0]/1000,multiplicacion[1]/1000000,multiplicacion[2]/1000000,multiplicacion[3]/1000
            esmissions=s1.CO2e(multiplicacion,ar)
            allEmissionFactor=s1.EF(emissionFactor[fuel[i]],GWPDataSet)
            esmissions.append(allEmissionFactor)
            emissionsScope11.append(esmissions)
        return emissionsScope11

    
    
    def iterationScope12(self,GWPDataSet,activityType=0,facilityID=0,convertion=26,fuel="",originalUnit=24,amountOfFuel=0,emissionFactor=[]):
        emissionsScope12=[]
    
       
        dFconvertion=TablaConvertions().makeDataFrame()
        arSet=FactorEmisionAR().makeList()
      
        cMovil=CombustionMovil()
        ar=arSet.iloc[:, GWPDataSet]

        for i in range (len(facilityID)):
            multiplicacion=[]
            if activityType[i]==0:
                
        
                for j in range(0,4):
                    oUnit=position.index(emissionFactor[fuel[i]][6])
                    convert=dFconvertion.iloc[oUnit,convertion[i]]

                    amount=amountOfFuel[i]
                    
                    analisis=cMovil.analisisCombustible1(combustibleV=amount,EF=emissionFactor[fuel[i]][j],convertion=convert)
                    
                    
                    multiplicacion.append(analisis)

                multiplicacion[0],multiplicacion[1],multiplicacion[2],multiplicacion[3]=multiplicacion[0]/1000,multiplicacion[1]/1000,multiplicacion[2]/1000,multiplicacion[3]/1000
                esmissions=cMovil.CO2e(multiplicacion,ar)
                allEmissionFactor=cMovil.EF(emissionFactor[fuel[i]],GWPDataSet)
                esmissions.append(allEmissionFactor)
                
            
            if activityType[i]==1:

                oUnit=position.index(emissionFactor[fuel[i]][9])

                convert=dFconvertion.iloc[oUnit,convertion[i]]
   
                finalAct=cMovil.distance(efficiency=emissionFactor[fuel[i]][8],activityMount=amount,convertion=convert)

                for j in range(0,4):
                    
                    amount=int(amountOfFuel[i])
                     
                    analisisOperation=cMovil.distanceEmissions(emission=emissionFactor[fuel[i]][j],finalActity=finalAct)

                    multiplicacion.append(analisisOperation)

                esmissions=cMovil.CO2e(multiplicacion,ar)   
                allEmissionFactor=cMovil.EF(emissionFactor[fuel[i]],GWPDataSet)
                esmissions.append(allEmissionFactor)
                

            emissionsScope12.append(esmissions)
        return emissionsScope12

    def iterationScope13(self,GWPDataSet,refrigerantUsedlist=[],facilityID=0,amountOfFuel=0,
                        rib=0,rie=0,refrigerantReturnedAfterRecyReclamation=0,e=0,
                        reChEquip=0,reDeliveEquipUsers=0, RefriReturnedequipUsers=[],  refrigeReRefrigerant=0,k=0,l=0,nameplateCapacityPartiallyChargedEquipment=0,
                        densityPressureParticalCharge=0,	densityPressureCharge=0       ):
        
        
      
        
        totalData=[]
        for i in range (len(facilityID)):
            parcialData=[]
            
            

            scope13=Refr()
           
            _,I,o,p=scope13.refrigerantEmissions(rib=rib[i],rie=rie[i],RefriReturnedequipUsers= RefriReturnedequipUsers[i],refrigerantReturnedAfterRecyReclamation=refrigerantReturnedAfterRecyReclamation[i],
                     reChEquip=reChEquip[i],reDeliveEquipUsers=reDeliveEquipUsers[i], e=e[i],refrigeReRefrigerant=refrigeReRefrigerant[i],k=k[i],l=l[i])
            
            r= scope13.gwpRefrigerant(refrigerantUsed=refrigerantUsedlist[i],eFRefrigerants=eFRefrigerants().listofEF(),GWPDataSet=GWPDataSet)
            s=scope13.CO2EquivalentEmissions (totalRefrigerant=p, conversionFactor=0.001, gwpRefrigerant =r)
            z= scope13.refrigerantChargedEquipment(nameplateCapacityPartiallyChargedEquipment[i], densityPressureParticalCharge[i],	densityPressureCharge[i])

            parcialData.append(s)
            parcialData.append(z)
            totalData.append(parcialData)
            
           
        return totalData
       
            

class scope2():
    def __init__(self,gridRegion,GWPDataSet) -> None:
        self.gridRegion=gridRegion
        self.GWPDataSet=GWPDataSet
   
    def operationEmission(self,i,listEmission=[],convertion=0,originalUnit=0,amountOfElectricity=0,emissionFactor=0,
                        fuel=0  ,ar=0):
        tableConvertion=TablaConvertions().makeDataFrame()
        emissionGHG=[]
        for j in range(1,4):
            convert=tableConvertion.iloc[originalUnit,convertion[i]]
            amount=amountOfElectricity[i]
            
            emission=scope2Class.emission(emiFactor=emissionFactor[fuel[i]][j],amount=amount,conver=convert)
            
            emissionGHG.append(emission)
            
                

        listEmission=scope2Class.coe2(listEmissions=emissionGHG,aRList=ar)
        listEmission.append(scope2Class.EF(emissionFactor=emissionFactor[fuel[i]]))
        return  listEmission
    

    def iterationFacts(self,typeEF,gwp=1,facilityID=[],convertion=21,arSet=FactorEmisionAR().makeList(),amountOfElectricity=0,emissionFactor=[],
                       originalUnit=43,fuel=0):
        emissionsScope11=[]
   
        
        ar=arSet.iloc[:, gwp]
        
       
        for i in range (len(facilityID)):
            listEmission=[]

            if typeEF[i]==0:
                
                emiFact=PurchasedElectricityLoc().listOfEF()
              
            
            elif typeEF[i]==1 :
                emiFact=EFPurchasedElectricityMix().listofEF()
                
            elif typeEF[i]==2:
                fuel[i]=0
                emiFact=SteamHeat().listOfEF()
                
            
            elif typeEF[i]==3:
                return 0
            

            oUnit=position.index(emiFact[fuel[i]][7])
            
            listEmission=self.operationEmission(i,listEmission=[],convertion=convertion,originalUnit=oUnit,amountOfElectricity=amountOfElectricity,emissionFactor=emiFact,
                        fuel=fuel  ,ar=ar)
            #_______
            emissionsScope11.append(listEmission)
        return emissionsScope11
    
class Scope3():
    def iterationFacts(self,GWPDataSet=1,Year=[],emissionFactor=[],vehicleType=[],unitSM=[],
                       amountActiviyType=[]):
        
        
        
        s3=Scope3form()
        emissionsScope3=[]
        
        
        
        #dFconvertion=TablaConvertions().makeDataFrame()
        arSet=FactorEmisionAR().makeList()
        
        global position
        units=Disctance()
    
        ar=arSet.iloc[:, GWPDataSet]
        for i in range (len(Year)):
            multiplicacion=[]
            dfConvertion=units.makeList()

            originalUnitE= dfConvertion.loc[:,0] == emissionFactor[vehicleType[i]][7]
            dfConvertion = dfConvertion.loc[originalUnitE]
            


            UnitConvert=dfConvertion.loc[:,1]==unitSM[i]

            newUnit=dfConvertion.loc[UnitConvert]
            convert=float(newUnit[2])
            
            #oUnit=position.index(emissionFactor[vehicleType[i]][7])
        
            for j in range(1,5):
                           

                #convert=dFconvertion.iloc[oUnit,vehicleType[i]]
                
                amount=amountActiviyType[i]
               
                l=emissionFactor[vehicleType[i]][j]
                
                
                
                
                analisisOperation=s3.analisisCombustible1(combustibleV=amount,EF1=l,conversition=convert)
                multiplicacion.append(analisisOperation)

            multiplicacion[0],multiplicacion[1],multiplicacion[2],multiplicacion[3]=multiplicacion[0]/1000,multiplicacion[1]/1000000,multiplicacion[2]/1000000,multiplicacion[3]/1000
            esmissions=s3.CO2e(multiplicacion,ar)
            allEmissionFactor=s3.EF(emissionFactor[vehicleType[i]],GWPDataSet)
            esmissions.append(allEmissionFactor)
            emissionsScope3.append(esmissions)
        return emissionsScope3

class StationaryCombustion(Scope1) :
    
    def __init__(self, userSuppliedData=[],GWPDataSet=1):
        
        
        dictStationaryCombustion={}
        
        dictStationaryCombustion=data.separadorDeDatos2(userSuppliedData)
    
        self.allData=dictStationaryCombustion
        self.facilityID=dictStationaryCombustion['facilityID']
        self.Year=dictStationaryCombustion['year']
        self.customEmissionFactors=dictStationaryCombustion["cef"]
        self.fuel=dictStationaryCombustion['fuelType']
        self.amountOfFuel=dictStationaryCombustion['fuelAmount']
        self.Units      =dictStationaryCombustion['fuelUnit']
        self.GWPDataSet =GWPDataSet
        
    def operaciones(self):

        emissionsScope11=[]
        emussionFactor=eFStationaryCombustion().listOfEF()
        
        emissionsScope11=self.iterationFacts(self.GWPDataSet,facilityID=self.facilityID,convertion=self.Units,fuel=self.fuel,amountOfFuel=self.amountOfFuel
                                             ,emissionFactor=emussionFactor)
      

        dataEmission,co2esumary=self.asignacion(emissionsScope11)

        return dataEmission,co2esumary

    def asignacion(self, emissionsScope11):
        listColumns= ["Facility ID", "Year",	"Custom Emission Factors",	"Fuel",	"Amount of fuel",	
                  "Units (e.g., kg or kWh)",	"CO2 (tonnes)",	"CH4 (tonnes)",	"N2O (tonnes)",	 "Biofuel CO2(tonnes)","CO2e (tonnes)","EF (kgCO2e/unit)"]

        self.lisScope=df = pd.DataFrame(self.allData)
        df = pd.DataFrame(emissionsScope11)
        dataEmission=pd.concat([self.lisScope,df], axis=1,ignore_index=True)
        dataEmission.columns=listColumns
        resumeSumary=self.resumenSumary( dataEmission)
    #    emisionPrint = dsd.iloc[:, 6:-1]

        return dataEmission,resumeSumary
    

    def resumenSumary(self, dtSocpe1):
        resumeSumary = dtSocpe1.groupby(['Facility ID', 'Year'])[['CO2e (tonnes)', "Biofuel CO2(tonnes)"]].sum().reset_index()
        return resumeSumary

    
    


data=DataFrame()

class MobileCombustion(Scope1) :

    def __init__(self, userSuppliedData=[],GWPDataSet=1):
        #Se debe crean variables que almacenaran listas de listas, para poder tener un mejor manejo en los data frame.
        
        dictUserSuppliedData=data.separadorDeDatos2(userSuppliedData)
        self.allData=dictUserSuppliedData
        self.Year=dictUserSuppliedData['year']
        self.facilityID=dictUserSuppliedData["facilityID"]
        self.activityType=dictUserSuppliedData['activityType']
        self.vehicleType=dictUserSuppliedData['vehicleType']
        self.activityAmount=dictUserSuppliedData['fuelAmount']
        self.unitOfFuelAmount=dictUserSuppliedData["fuelUnit"]
        self.GWPDataSet=GWPDataSet
        
          


    def operaciones(self):
        #data =validacion()
        emussionFactor=efMobilCombustion().listofEf()
    
      
              
        emissionsScope12=self.iterationScope12(self.GWPDataSet,activityType=self.activityType,facilityID=self.facilityID,convertion=self.unitOfFuelAmount,fuel=self.vehicleType,amountOfFuel=self.activityAmount,emissionFactor=emussionFactor)

        dFScope, sumaryC02E=self.asignacion(emissionsScope12)
        
        return dFScope, sumaryC02E

    def asignacion(self, emissionsScope11):
        listColumns= ["Year",		"Facility ID",	"Activity Type",	"Vehicle Type",
						"Activity Amount",	"Unit of Fuel Amount",	"CO2 (tonnes)",	"CH4 (tonnes)",	"N2O (tonnes)","Biofuel CO2",	"CO2e (tonnes)"
                        , "EF (kgCO2e/unit)"]
        dFUser=pd.DataFrame(self.allData)
        df = pd.DataFrame(emissionsScope11)


        
        
        dFScope=pd.concat([dFUser,df], axis=1,ignore_index=True)
        dFScope.columns=listColumns
        #emisionPrint = dFScope.iloc[:, 6:-1]
       
 
        sumaryC02E = self.resumenSumary(dFScope)
        return dFScope, sumaryC02E
    
    def resumenSumary(self, dtSocpe1):
        sumaryCOE2 = dtSocpe1.groupby(['Facility ID', 'Year'])['CO2e (tonnes)'].sum().reset_index()
    
        return sumaryCOE2
        
    


    



class Refrigerantes(Scope1) :

    def __init__(self, userSuppliedData=[]):
        #Se debe crean variables que almacenaran listas de listas, para poder tener un mejor manejo en los data frame.
    
        dictUserSuppliedData                                    =data.separadorDeDatos2(userSuppliedData)
        self.allData                                            =dictUserSuppliedData
        self.Year                                               =dictUserSuppliedData["year"]
        self.facilityID                                         =dictUserSuppliedData['facilityID']
        self.refrigerantUsedlist                                =dictUserSuppliedData['refrigerantUsed']
        self.refrigerantInventoryBeginning                      =dictUserSuppliedData['initialAmount']      #Refrigerant inventory (in storage, not equipment) at the beginning of the Year
        self.refrigerantInventoryEnd                            =dictUserSuppliedData['finalAmount']            #	Refrigerant inventory (in storage, not equipment) at the end of the Year	
        self.refrigerantPurchasedFromPD                         =dictUserSuppliedData['purchases']
        self.refrigerantEquipmentUsers                          =dictUserSuppliedData['returnsByUser']
        self.refrigerantAfterRecyclinReclamation                =dictUserSuppliedData['returnsByRecycling']
        self.refrigerantChargedIntoEquipment                    =dictUserSuppliedData['used']
        self.refrigerantDeliveredEquipmentUsersInContainers     =dictUserSuppliedData['delivered']
        self.refrigerantrRturnedRefrigerantProducers            =dictUserSuppliedData['returnsToProducers']
        self.refrigerantSentRecyclingReclamation                =dictUserSuppliedData['offSiteRecycling']
        self.refrigerantsSentDestruction                        =dictUserSuppliedData['offSiteDestruction']
        self.nameplateCapacityPartiallyChargedEquipment         =dictUserSuppliedData['partialCapacityCharge']
        self.densityPressureParticalCharge                      =dictUserSuppliedData['partialChargeAmount']
        self.densityPressureFullCharge                          =dictUserSuppliedData['fullChargeAmount']
        self.GWPDataSet                                         =1
    
        
                                                    



    def operaciones(self):
        
        #emussionFactor=efMobilCombustion().listofEf()
        #s13=Refr()
        
        
       
        
        emissionsScope13=self.iterationScope13(self.GWPDataSet, refrigerantUsedlist=self.refrigerantUsedlist,RefriReturnedequipUsers=self.refrigerantEquipmentUsers
                                               ,facilityID=self.facilityID,rib= self.refrigerantInventoryBeginning,rie=self.refrigerantInventoryEnd,e=self.refrigerantPurchasedFromPD,refrigerantReturnedAfterRecyReclamation=self.refrigerantAfterRecyclinReclamation,reChEquip=self.refrigerantChargedIntoEquipment,
                                                reDeliveEquipUsers=self.refrigerantDeliveredEquipmentUsersInContainers,   refrigeReRefrigerant=self.refrigerantrRturnedRefrigerantProducers,k=self.refrigerantSentRecyclingReclamation,l=self.refrigerantsSentDestruction,
                                                nameplateCapacityPartiallyChargedEquipment=self.nameplateCapacityPartiallyChargedEquipment,
                                                densityPressureParticalCharge=self.densityPressureParticalCharge,	densityPressureCharge= self.densityPressureFullCharge  )        

        dfAsignacion,resumeSumary=self.asignacion(emissionsScope13)
        
        return dfAsignacion,resumeSumary
    
    def asignacion(self, emissionsScope13):
        listColumns= ["Year",	"Facility ID",   		"Refrigerant Used",	"Refrigerant inventory at the beginning of the Year",	"Refrigerant inventory at the end of the Year",	"Refrigerant purchased from producers/ distributors",	"Refrigerant returned by equipment users",	"Refrigerant returned after off-site recycling or reclamation",	"Refrigerant charged into equipment",
	"Refrigerant delivered to equipment users in containers",	"Refrigerant returned to refrigerant producers",	"Refrigerant sent off-site for recycling or reclamation",	"Refrigerant sent off-site for destruction","Nameplate Capacity of Partially Charged Equipment",	"Density or Pressure of partical charge","Density or Pressure of full charge",
    "CO2-Equivalent Emissions (tonnes)",     "Z = WX/Y"]
		
        dFUser=pd.DataFrame(self.allData)
        df = pd.DataFrame(emissionsScope13)
       
        

        dFScope=pd.concat([dFUser,df], axis=1,ignore_index=True)
        dFScope.columns=listColumns
       
        resumeSumary=self.resumenSumary(dFScope)
        #emisionPrint = dFScope.iloc[:, 8:-1]
      
        
        return dFScope,resumeSumary
    

    def resumenSumary(self, dtSocpe1):
        sumaryCOE2 = dtSocpe1.groupby(['Facility ID', 'Year'])['CO2-Equivalent Emissions (tonnes)'].sum().reset_index()
        
        return sumaryCOE2





class PurchasedElectricity(scope2) :

    def __init__(self, gwp=0,gridRegion=[],userSuppliedData=[]):
        #Se debe crean variables que almacenaran listas de listas, para poder tener un mejor manejo en los data frame.
        dictUserSuppliedData=data.separadorDeDatos2(userSuppliedData)
        self.Year                           = dictUserSuppliedData["Year"]
        self.facilityID                     = dictUserSuppliedData['facilityID']
        self.amountElectricityConsumption   = dictUserSuppliedData['energyConsumption']
        self.units                          = dictUserSuppliedData['units']
        self.calculationApproach            = dictUserSuppliedData['CalculationApproach']
        self.typeofEmissionFactor           = dictUserSuppliedData['typeOfEmissionFactor']
        self.allData                        =dictUserSuppliedData
        #self.customEmissionFactor           = dictUserSuppliedData[6]
        dictUserSuppliedDataGris=data.separadorDeDatos2(gridRegion)
        self.GWPDataSet                     =gwp
        self.idGrid                         =dictUserSuppliedDataGris["facilityID"]
        self.gridRegion                     =dictUserSuppliedDataGris["Grid Region"]


    def operaciones(self):


        emissionsScope2=self.iterationFacts(self.typeofEmissionFactor,facilityID=self.facilityID, convertion=self.units, amountOfElectricity=self.amountElectricityConsumption,
                       fuel=self.gridRegion)
        
       
      

        dFScope,resumenSumary=self.asignacion(emissionsScope2)
        
        return dFScope,resumenSumary
        

    def asignacion(self, emissionsScope11):
        dFUser=pd.DataFrame(self.allData)
        df = pd.DataFrame(emissionsScope11)
        

        dFScope=pd.concat([dFUser,df], axis=1,ignore_index=True)
        listColumns= ["Year",	"Facility ID",	"Amount of Electricity Consumption",	"Units",	"Calculation Approach",	"Type of Emission Factor",	"CO2 (tonnes)",	"CH4 (tonnes)",	"N2O (tonnes)",	"CO2e (tonnes)",	"EF (kgCO2e/kWh)"]
        dFScope.columns=listColumns
        #emisionPrint = dFScope.iloc[:, 8:-1]
        resumenSumary=self.resumenSumary(dFScope)
        return dFScope,resumenSumary
    

    def resumenSumary(self, dtSocpe1):
        sumaryCOE2 = dtSocpe1.groupby(['Facility ID', 'Year'])["CO2e (tonnes)"].sum().reset_index()
      
        return sumaryCOE2



    
    
class Transportation(Scope3) :

    def __init__(self, userSuppliedData=[],params=0,gwp=1):
        #Se debe crean variables que almacenaran listas de listas, para poder tener un mejor manejo en los data frame.
        dictUserSuppliedData            =data.separadorDeDatos2(userSuppliedData)
        self.allData                    =dictUserSuppliedData
        self.Year                       =dictUserSuppliedData['year']
        self.vehicleType                =dictUserSuppliedData['vehicleType']
        self.amountofActivityType       =dictUserSuppliedData['amountOfActivityType']
        self.unitsofMeasurement         =dictUserSuppliedData['units']
        self.GWPDataSet=params
        self.gwp                        =gwp



    def operaciones(self):
       # data =validacion()
       
        #iterationFacts(self,facilityID,convertion,amountOfFuel,datapat,temporal):
        
        emissionFactor=efTransport().listofEF()

        
        df=Scope3().iterationFacts(Year=self.Year,GWPDataSet=self.gwp ,emissionFactor=emissionFactor,vehicleType=self.vehicleType,
                       amountActiviyType= self.amountofActivityType,unitSM=self.unitsofMeasurement )

        dFScope,resumenSumary=self.asignacion(df)
        
        return dFScope,resumenSumary
    

    def asignacion(self, emissionsScope13):
        dFUser=pd.DataFrame(self.allData)

        df = pd.DataFrame(emissionsScope13)
        
        lista=["Year",	"Category","Vehicle Type","Amount of Activity Type",	"Units of Measurement",
                    "CO2 (tonnes)",	"CH4 (tonnes)",	"N2O (tonnes)","Biofuel CO2",	"CO2e (tonnes)","EF (kgCO2e/unit)"]
        dFScope=pd.concat([dFUser,df], axis=1,ignore_index=True)
        dFScope.columns=lista
        #emisionPrint = dFScope.iloc[:, 8:-1]

    
        resumenSumary=self.resumenSumary( dFScope)
        return dFScope,resumenSumary

    def resumenSumary(self, dtSocpe1):
        sumaryCOE2 = dtSocpe1.groupby(['Year', 'Vehicle Type'])['CO2e (tonnes)'].sum().reset_index()
        sumaryCOE2Category = dtSocpe1.groupby(['Year','CO2e (tonnes)'])['Category'].sum().reset_index()
        dFScope=pd.concat([sumaryCOE2,sumaryCOE2Category], axis=1,ignore_index=True)
        print(dFScope)
 
        return dFScope



    


