import requests
import pandas as pd
import matplotlib.pyplot as plt

#Pedir el token propio en la web: https://estadisticasbcra.com/api/registracion
token = "BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDkyMzA1NDUsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiI3dTh6cmlwQGZ4bWFpbC53cyJ9.NHbKjrofmRwy5-8aLScTETzQO81BOUOy8SDl389OHGCUaGoUjcvzbiM-HYIldAr1ffISmmO5_lx0Ugp56yhIUw"

#endopint al que se llama (Ver listado de endpoins)
endpoint = "base_usd"

#datos para el llamado
url = "https://api.estadisticasbcra.com/"+endpoint
headers = {"Authorization": token}

#Llamado
data_json = requests.get(url, headers=headers).json()

#Armamos una tabla con los datos
data = pd.DataFrame(data_json)

#Le asignamos la fecha como indice
data.set_index('d', inplace=True, drop=True)


plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = [15, 6]
data.plot()
plt.show()

print(data.tail())


'''
ENDPOINTS : Descripcion


milestones : eventos relevantes (presidencia, ministros de economía, presidentes del BCRA, cepo al dólar)
base : base monetaria
base_usd: base monetaria dividida USD
reservas : reservas internacionales
base_div_res : base monetaria dividida reservas internacionales
usd : cotización del USD
usd_of : cotización del USD Oficial
usd_of_minorista : cotización del USD Oficial (Minorista)
var_usd_vs_usd_of : porcentaje de variación entre la cotización del USD y el USD oficial
circulacion_monetaria : circulación monetaria
billetes_y_monedas : billetes y monedas
efectivo_en_ent_fin : efectivo en entidades financieras
depositos_cuenta_ent_fin : depositos de entidades financieras en cuenta del BCRA
depositos : depósitos
cuentas_corrientes : cuentas corrientes
cajas_ahorro : cajas de ahorro
plazo_fijo : plazos fijos
tasa_depositos_30_dias : tasa de interés por depósitos
prestamos : prestamos
tasa_prestamos_personales : tasa préstamos personales
tasa_adelantos_cuenta_corriente : tasa adelantos cuenta corriente
porc_prestamos_vs_depositos : porcentaje de prestamos en relación a depósitos
lebac : LEBACs
leliq : LELIQs
lebac_usd : LEBACs en USD
leliq_usd : LELIQs en USD
tasa_leliq : Tasa de LELIQs
m2_privado_variacion_mensual : M2 privado variación mensual
cer : CER
uva : UVA
uvi : UVI
tasa_badlar : tasa BADLAR
tasa_baibar : tasa BAIBAR
tasa_tm20 : tasa TM20
tasa_pase_activas_1_dia : tasa pase activas a 1 día
tasa_pase_pasivas_1_dia : tasa pase pasivas a 1 día
zona_de_no_intervencion_cambiaria_limite_inferior : zona de no intervención cambiaria límite inferior
zona_de_no_intervencion_cambiaria_limite_superior : zona de no intervención cambiaria límite superior
inflacion_mensual_oficial : inflación mensual oficial
inflacion_interanual_oficial : inflación inteanual oficial
inflacion_esperada_oficial : inflación esperada oficial
dif_inflacion_esperada_vs_interanual : diferencia entre inflación interanual oficial y esperada
var_base_monetaria_interanual : variación base monetaria interanual
var_usd_interanual : variación USD interanual
var_usd_oficial_interanual : variación USD (Oficial) interanual
var_merval_interanual : variación merval interanual
merval : MERVAL
merval_usd : MERVAL dividido cotización del USD

'''