import math #necesario para calculos como logaritmos, raices, pi, exponentes etc

#Funcion normal acumulada (es una aproximacion por taylor 6 decimales)
def  fi(x):
      Pi = 3.141592653589793238;
      a1 = 0.319381530;
      a2 = -0.356563782;
      a3 = 1.781477937;
      a4 = -1.821255978;
      a5 = 1.330274429;
      L = abs(x);
      k = 1 / ( 1 + 0.2316419 * L);
      p = 1 - 1 / pow(2 * Pi, 0.5) * math.exp( -pow(L, 2) / 2 ) * (a1 * k + a2 * pow(k, 2)
          + a3 * pow(k, 3) + a4 * pow(k, 4) + a5 * pow(k, 5) );
      if (x >= 0) :
          return p
      else:
          return 1-p

def normalInv(x):
    return ((1/math.sqrt(2*math.pi)) * math.exp(-x*x*0.5))


#Funciones de Calculo de primas y griegas 
def bsCall(S0, K, r, T, sigma, q=0):
    ret = {}
    if (S0 > 0 and K > 0 and r >= 0 and T > 0 and sigma > 0):        
        d1 = ( math.log(S0/K) + (r -q +sigma*sigma*0.5)*T ) / (sigma * math.sqrt(T))
        d2 = d1 - sigma*math.sqrt(T)
        ret['call'] = math.exp(-q*T) * S0 * fi(d1)- K*math.exp(-r*T)*fi(d2)
        ret['delta'] = math.exp(-q*T) * fi(d1)
        ret['gamma'] = (normalInv(d1) * math.exp(-q*T)) / (S0 * sigma * math.sqrt(T))
        ret['vega'] = 0.01 * S0 * math.exp(-q*T) * normalInv(d1) * math.sqrt(T)
        ret['theta'] = (1/365) * ( -((S0*sigma*math.exp(-q*T))/(2*math.sqrt(T))) * normalInv(d1) - r*K*(math.exp(-r*T))*fi(d2) + q*S0*(math.exp(-q*T)) * fi(d1) )
        ret['rho'] = 0.01 * K * T * math.exp(-r*T) * fi(d2)
    else:
        ret['errores']= "Se Ingresaron valores incorrectos"
    return ret


def bsPut(S0, K, r, T, sigma, q=0):
    ret = {}
    if (S0 > 0 and K > 0 and r >= 0 and T > 0 and sigma > 0):        
        d1 = ( math.log(S0/K) + (r -q +sigma*sigma*0.5)*T ) / (sigma * math.sqrt(T))
        d2 = d1 - sigma*math.sqrt(T)
        ret['put'] = K*math.exp(-r*T)*fi(-d2) - math.exp(-q*T) * S0 * fi(-d1)
        ret['delta'] = - math.exp(-q*T) * fi(-d1)
        ret['gamma'] = math.exp(-q*T) * normalInv(d1) / (S0 * sigma * math.sqrt(T))
        ret['vega'] = 0.01* S0 * math.exp(-q*T) * normalInv(d1) * math.sqrt(T)
        ret['theta'] =  (1/365) * ( -((S0*sigma*math.exp(-q*T))/(2*math.sqrt(T))) * normalInv(d1) + r*K*(math.exp(-r*T))*fi(-d2) - q*S0*(math.exp(-q*T)) * fi(-d1) )
        ret['rho'] = -0.01 * K * T * math.exp(-r*T) * fi(-d2)
    else:
        ret['errores']= "Se Ingresaron valores incorrectos"
    return ret
    

def viCall(S0, K, r, T, prima, q=0):
    if (S0 > 0 and K > 0 and r >= 0 and T > 0):        
        maximasIteraciones = 300
        pr_techo = prima
        pr_piso = prima
        vi_piso = maximasIteraciones
        vi = maximasIteraciones
        for number in range(1,maximasIteraciones):
            sigma = (number)/100
            primaCalc = bsCall(S0, K, r, T, sigma, q)['call']
            if primaCalc>prima:
                vi_piso = number -1
                pr_techo = primaCalc
                break
            else:
                pr_piso = primaCalc
        
        rango = (prima - pr_piso) / (pr_techo - pr_piso)
        vi = vi_piso + rango
    else:
        vi = "No se puede calcular VI porque los valores ingresados son incorrectos"
    return(vi)


def viPut(S0, K, r, T, prima, q=0):
    if (S0 > 0 and K > 0 and r >= 0 and T > 0):        
        maximasIteraciones = 300
        pr_techo = prima
        pr_piso = prima
        vi_piso = maximasIteraciones
        vi = maximasIteraciones
        for number in range(1,maximasIteraciones):
            sigma = (number)/100
            primaCalc = bsPut(S0, K, r, T, sigma, q)['put']
            if primaCalc>prima:
                vi_piso = number -1
                pr_techo = primaCalc
                break
            else:
                pr_piso = primaCalc
        
        rango = (prima - pr_piso) / (pr_techo - pr_piso)
        vi = vi_piso + rango
    else:
        vi = "No se puede calcular VI porque los valores ingresados son incorrectos"
    return(vi)
                      

    
#INGRESO DE DATOS
    
S0 = 100 #Spot subyacente
K = 100 #strike o base del contrato
r = 0.018 #tasa libre de riesgo
T = 30/365 #tiempo en años para expiracion
sigma = 0.2  #volatilidad anualizada
q = 0.01 #dividend yield (ojo los highYield que en USA no se limpian las bases ex div)


#CALCULO DE PRIMAS Y GRIEGAS
call = bsCall(S0, K, r, T, sigma, q)
put = bsPut(S0, K, r, T, sigma, q)


#IMPRESION EN PANTALLA
print(call)
print(put)

#CALCULO DE VI DADO PRECIO DE MERCADO
vi = viCall(S0, K, r, T, 2, q)
print(vi)


