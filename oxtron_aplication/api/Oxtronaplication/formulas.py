#datos=data()

# Alcance 1
#  Combustión estacionaria
'''Estas fuentes incluyen combustibles estándar, de biomasa y derivados de desechos. Se utilizará uno de los dos métodos siguientes para calcular las emisiones 
de combustión estacionaria, dependiendo de la información disponible para el combustible.

Documento de referencia de la EPA: Guía de inventario de gases de efecto invernadero: emisiones directas de fuentes de combustión estacionarias (EPA.gov)

Método de análisis de combustible 1
En este método, se utiliza la siguiente ecuación para calcular las emisiones:'''
class AnalisisCombustible():
   


    def analisisCombustible1(self,combustibleV=0,EF1=0,conversition=0):

        emisiones = (EF1/conversition)*(combustibleV)
#        Aquí hay una explicación de la ecuación:
        #emisiones =          Masa de CO2, CH4 o N2O que se emite
        #self.combustibleV = input asa o volumen de combustible que se quema
        #EF1 = input () factor de emisión de CO2, CH4 o N2O por unidad de masa o volumen
        return emisiones
    
    def CO2e(self,listEmissions,  AR):
        
        co2e=listEmissions[0]*AR[0]+listEmissions[1]*AR[1]+listEmissions[2]*AR[2]
        #co2e=sum(listEmissions)
        listEmissions.append(co2e)

        return listEmissions
    def EF (self,emissionFactor,  AR):
          eFactor=emissionFactor[5+AR]
          return eFactor
          
          
        
          
          

#El método 1 se usa cuando se desconoce el contenido de calor del combustible, 
# o cuando el consumo de combustible se conoce solo en unidades de masa o volumen. Debido a que hay menos certeza, este método es menos preferido que el método 2.

    '''Método de análisis de combustible 2
En este método, se utiliza la siguiente ecuación para calcular las emisiones:'''
    def analisisCombustible2(self):
        
        emisiones = self.combustibleV * self.HHV * self.EF2

        return emisiones
#Aquí hay una explicación de la ecuación:
        #emisiones   Masa de CO2, CH4 o N2O que se emite
        #self.combustibleV  Masa o volumen de combustible que se quema
        #HHV (poder calorífico superior) = Contenido calorífico del combustible, en unidades de energía por masa o volumen de combustible
        #EF2 = factor de emisión de CO2, CH4 o N2O por unidad de energía

#El método 2 es el método preferido cuando el uso de combustible se proporciona en unidades de energía, como termias o unidades térmicas británicas (BTU), y cuando se conoce el contenido de calor del combustible.

#Para obtener información sobre los factores de emisión, consulte Factores de emisión para inventarios de gases de efecto invernadero (libro de trabajo de Excel).

'''Combustión móvil
Microsoft Sustainability Manager sigue la metodología de la EPA para calcular las emisiones de alcance 1 de fuentes de combustión móviles. Los cálculos difieren de los cálculos para las emisiones de combustión estacionaria en que existen ecuaciones separadas para CO2 y para N20 y CH4.
emisiones de CO2'''

#Para el CO2, se utilizará uno de los dos métodos siguientes para calcular las emisiones de combustión móvil, dependiendo de la información que esté disponible para el combustible.
class CombustionMovil():
    
    
    def analisisCombustible1(self,combustibleV=0,convertion=0,EF=0):

        emisiones = (EF/convertion)*(combustibleV)
#        Aquí hay una explicación de la ecuación:
        #emisiones =          Masa de CO2, CH4 o N2O que se emite
        #self.combustibleV = input asa o volumen de combustible que se quema
        #EF1 = input () factor de emisión de CO2, CH4 o N2O por unidad de masa o volumen
        return emisiones
    
    def CO2e(self,listEmissions,  AR):
        
        co2e=listEmissions[0]*AR[0]+listEmissions[1]*AR[1]+listEmissions[2]*AR[2]
        #co2e=sum(listEmissions)
        listEmissions.append(co2e)

        return listEmissions
    

    def EF (self,emissionFactor,  AR):
          eFactor=emissionFactor[4+AR]
          return eFactor
          #EF1 = factor de emisión de CO2 por unidad de masa o volumen
    
    
    def distance(self,activityMount=0,efficiency=0,convertion=1): 
        finalActity=(activityMount/(efficiency*convertion))

        return finalActity
    
                    #emisiones = Masa de CO2 que se emite
                    #combustibleV = Masa o volumen de combustible que se quema
                    #HHV (poder calorífico superior) = Contenido calorífico del combustible, en unidades de energía por masa o volumen de combustible
                    #EF2 = factor de emisión de CO2 por unidad de energía

    
    
    def distanceEmissions(self,emission=0,finalActity=0):
          eF=emission*finalActity/1000
          return eF

    def emisionesN2OCH4Carretera(self,distancia,EF):
        emisiones = distancia * EF
        return emisiones

                    #emisiones = Masa de CH4 o N2O que se emite
                    #distancia = distancia que recorrió el vehículo
                    #EF4 = factor de emisión de CH4 o N2O por unidad de distancia
                    #Cálculo de emisiones de N2O y CH4 de vehículos no de carretera
                    #Cálculo de emisiones de N2O y CH4 de vehículos que no son de carretera
    def emisionesN2OCH4Carretera(self):


        emisiones = self.combustibleV * self.EF5
        return emisiones
              #Aquí hay una explicación de la ecuación:
              #emisiones = Masa de CH4 o N2O que se emite
              #combustibleV = Volumen de combustible que se quema
              #EF5 = factor de emisión de CH4 o N2O por unidad de volumen


          



class Refr():
    


    def decreaseRefrigerantInventory(self,rib=0,rie=0):
        e = rib - rie

        return e

    def totalRefrigerantPurchasesAcquisitions(self,decreRefrigInvent=0,	refrigerantReturnedEquipmentUsers=0, refrigerantReturAfterReclamation=0):
    
        i =float(decreRefrigInvent )+float( refrigerantReturnedEquipmentUsers) + float( refrigerantReturAfterReclamation)
        
        return i
    
    def totalRefrigerantSalesDisbursements(self,refrigerantChargedEquipment=0, refrigerantDeliveredEquipmentUsers=0, refrigerantReturnedRefrigerantProducers=0,
                                            refrigerantSentRecyclingReclamation=0, refrigerantSentDestruction=0):

				

        o =   refrigerantChargedEquipment + refrigerantDeliveredEquipmentUsers + refrigerantReturnedRefrigerantProducers + refrigerantSentRecyclingReclamation + refrigerantSentDestruction

        return o
    
    def refrigerantEmissions(self,rib=0,rie=0,e=0,RefriReturnedequipUsers=0,refrigerantReturnedAfterRecyReclamation=0,reChEquip=0,reDeliveEquipUsers=0,
                              refrigeReRefrigerant=0,k=0,l=0 ):
        E=self.decreaseRefrigerantInventory(rib=rib,rie=rie)
        i=self.totalRefrigerantPurchasesAcquisitions(decreRefrigInvent=e,refrigerantReturnedEquipmentUsers=RefriReturnedequipUsers
                                                     ,refrigerantReturAfterReclamation=refrigerantReturnedAfterRecyReclamation)
        o=self.totalRefrigerantSalesDisbursements( refrigerantChargedEquipment=reChEquip, refrigerantDeliveredEquipmentUsers=reDeliveEquipUsers, refrigerantReturnedRefrigerantProducers=refrigeReRefrigerant,
                                            refrigerantSentRecyclingReclamation=k, refrigerantSentDestruction=l)
        p= E  + i - o

         
        return E,i,o,p
    
    def gwpRefrigerant(self,refrigerantUsed=0,eFRefrigerants=[],GWPDataSet=1):
        if GWPDataSet==1:
            
        
            return eFRefrigerants[refrigerantUsed][4]
        else:
            
             return eFRefrigerants[refrigerantUsed][2]
    
    def CO2EquivalentEmissions (self,totalRefrigerant=0, conversionFactor=0.001, gwpRefrigerant =0):
     
        s=totalRefrigerant*conversionFactor*gwpRefrigerant
        return s

    

    def refrigerantUsed(self,refrigerantUsed):
         re=refrigerantUsed
         return re
         

    def refrigerantChargedEquipment(self, nameplateCapacityPartiallyChargedEquipment, densityPressureParticalCharge,	densityPressureCharge):
		
        z=nameplateCapacityPartiallyChargedEquipment * densityPressureParticalCharge /	densityPressureCharge

        return z
    
 
    
#---------------------




    def emisionesEstimadasInstalacion(self):
        emisionesInstalación = self.CN * (self.k / 100)
        return emisionesInstalación
                    #CN = Cantidad de refrigerante que se cargó en el nuevo equipo
                    #k = Pérdidas de montaje como porcentaje del importe cobrado

#Ecuación 2: emisiones estimadas de la operación

    def EmisionesEstimadasOperacion(self):
       
        emisionesOperacion = self.C * (self.x / 100) * self.T

        return emisionesOperacion
#Aquí hay una explicación de la ecuación:
#C = Capacidad frigorífica del equipo
#x = tasa de fuga anual como porcentaje de la capacidad
#T = Tiempo en años que se usó el equipo durante el período del informe (por ejemplo, T es igual a 0,5 si el equipo se usó durante la mitad del período del informe y luego se eliminó).
#
    def  emisionesEstimadasEliminacion(self):
                 
        emisionesEliminacion = self.CD * (self.y / 100) * (1 - self.z / 100)

        return emisionesEliminacion
#Aquí hay una explicación de la ecuación:
#CD = Capacidad de refrigerante del equipo que se va a desechar
#y = Porcentaje de la capacidad que queda al momento de la enajenación
#z = Porcentaje del refrigerante que se recupera

#Equipos de extinción de incendios
class EquiposExtincionIncendios():
        def __init__(self) -> None:
            pass
        def calculoSistemaFijos(self,total):
            dosPorciento= (total*2)/100
            return dosPorciento
    
        def calculoSistemaPortatiles(self,total):
            tresPorciento= (total*3.5)/100
            return tresPorciento


            

# Alcance 2


class Scope2Form():
    def gridRegion(self):

        pass


    def emission(self, emiFactor=0,amount=0,conver=0):
        eF=(emiFactor/conver)*amount/1000
        return eF

    def coe2(self, listEmissions=[],aRList=[] ):
        co2e=listEmissions[0]*aRList[0]+listEmissions[1]*aRList[1]+listEmissions[2]*aRList[2]
        #co2e=sum(listEmissions)
        listEmissions.append(co2e)
        return listEmissions

    def EF (self,emissionFactor=[],  AR=1):
          eFactor=emissionFactor[5+AR]
          return eFactor
    


class Scope3form():
    

    def analisisCombustible1(self,combustibleV=0,EF1=0,conversition=0):

        emisiones = (EF1/conversition)*(combustibleV)
#        Aquí hay una explicación de la ecuación:
        #emisiones =          Masa de CO2, CH4 o N2O que se emite
        #self.combustibleV = input asa o volumen de combustible que se quema
        #EF1 = input () factor de emisión de CO2, CH4 o N2O por unidad de masa o volumen
        return emisiones
    
    def CO2e(self,listEmissions,  AR):
        
        co2e=listEmissions[0]*AR[0]+listEmissions[1]*AR[1]+listEmissions[2]*AR[2]
        #co2e=sum(listEmissions)
        listEmissions.append(co2e)

        return listEmissions
    def EF (self,emissionFactor,  AR):
          eFactor=emissionFactor[5+AR]
          return eFactor
        
    '''def __init__(self,electricidadComprada,factorEmisionLineaDirecta,factorEmisionRegional, factorEmisionNacional,certificadosAtributosEnergeticos,contratos,factorEmisiónEspecificoProveedor,
                factorEezclaResidual,factorEmisiónRegional) -> None:
        self.electricidadComprada=electricidadComprada
        self.factorEmisionLineaDirecta=factorEmisionLineaDirecta
        self.factorEmisionRegional=factorEmisionRegional
        self.factorEmisionNacional=factorEmisionNacional
        self.certificadosAtributosEnergeticos=certificadosAtributosEnergeticos
        self.contratos=contratos
        self.factorEmisiónEspecificoProveedor=factorEmisiónEspecificoProveedor
        self.factorEezclaResidual=factorEezclaResidual
        self.factorEmisiónRegional=factorEmisiónRegional
        self.factorEmisionNacional=factorEmisionNacional
    '''
          
          
          





class CalcularEmisionesAlcances3():
       def __init__(self,Electricidad, EF) -> None:
              self.Electricidad=Electricidad
              self.EF=EF
       def calculadora(self):
              
            emisiones = self.Electricidad * self.EF
            
            return emisiones
#Aquí hay una explicación de la ecuación:
#emisiones = Masa de dióxido de carbono (CO2), metano (CH4) u óxido nitroso (N2O) que se emite
#Electricidad = Cantidad de electricidad que se compra
#EF = factor de emisión de CO2, CH4 o N2O
""" 
Multiplique las emisiones de CH4 y N2O por el potencial de calentamiento global (GWP) correspondiente para calcular las emisiones de CO2 equivalente
(CO2e). El GWP para CH4 es 25 y el GWP para N2O es 298. Estos valores se tomaron del Panel Intergubernamental sobre Cambio Climático (IPCC), Cuarto Informe de Evaluación (AR4),
2007. Las emisiones totales de CO2e se calculan como la suma de las emisiones de CO2e las emisiones de CH4 y N2O y las emisiones de CO2.

Unidades de datos de actividad
Las unidades de medida en las que se informan los datos de actividad en las facturas de servicios públicos u otros registros de compra pueden variar entre electricidad, vapor, calor y refrigeración. En el caso de la electricidad, la calefacción y la refrigeración, los datos de actividad normalmente se notifican en unidades de energía. Para la electricidad, los kilovatios-hora (kWh) o los megavatios-hora (MWh) son los más utilizados. El calor y el enfriamiento se pueden informar en varias unidades de energía. Una unidad de medida común para el enfriamiento es la tonelada-hora. Una tonelada-hora equivale a 12.000 unidades térmicas británicas (BTU). El vapor se puede informar en unidades de energía o unidades de masa. Si solo está disponible la información de costos, le recomendamos que se comunique con el proveedor para proporcionar datos para las unidades de energía.

emisiones de calor y electricidad combinados
Las emisiones de una planta combinada de calor y electricidad se basan en el tipo de combustible que se utiliza. La emisión debe asignarse proporcionalmente a cada flujo de energía. Los siguientes tres métodos se utilizan con mayor frecuencia para asignar las emisiones de una planta combinada de calor y electricidad:
Método de eficiencia: este método es el método preferido cuando las emisiones de gases de efecto invernadero se asignan en función de los insumos de energía que se utilizan para producir los productos separados de vapor y electricidad.
Método del contenido de energía: las emisiones de gases de efecto invernadero se asignan en función del contenido de energía de los productos de vapor y electricidad de salida.
Método del potencial de trabajo: las emisiones de gases de efecto invernadero se asignan en función del contenido de energía de los productos de vapor y electricidad.

 """