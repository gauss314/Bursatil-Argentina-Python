# Bursatil Argentina Python
> Ejemplos prácticos para empezar a programar aplicaciones del ámbito bursatil en python
La idea era hacer un instructivo bien simple para quienes quieran empezar a codear sus primeras lineas. 

<br><br>
# Instalación

Instalar el paquete Anaconda
Descarga de la pagina oficial https://www.anaconda.com/distribution/
<br>Abrir el prompt anaconda para instalar paquete de yahoo finance

<div align="center">
  <img border="0"  src="https://pbs.twimg.com/media/EM5FAeIWoAEtDT-?format=jpg&name=large" width="600">
</div>

<br>

> Luego, desde el prompt anaconda instalar el paquete de Yahoo Finance para bajar datos de mercado
> Para ello tipear la siguiente linea de codigo:

```sh
pip install yfinance
```
<br>


> Desde el prompt anaconda instalar tambien el paquete de pyfolio
Este paquete Pyfolio es un paquete para análisis cuantitativo


```sh
pip install pyfolio
```

<br><br>
# Archivos

* [PrimerosPasos](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/analisis%20activo.py) Bajar datos de mercado por activo
* [PyFolio](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/cartera%20pyfolio.py) Analisis QUANT de cartera flat
* [CCLs](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/ccls.py) Calculo del CCL para diferentes tickers (GGAL, PAM, YPF, etc)
* [Brechas](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/brechas.py) TDC oficial, MEP y CCL, Brecha actual CCL-Oficial, MEP-Oficial, CCL-MEP
* [BCRA](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/bcra.py) +40 Endpoints de series historicas del BCRA (como reservas internacionales, tdc, m2, tasas, etc) 🚀

<br>
> Hilo de twitter donde se inició esta idea: 
https://twitter.com/JohnGalt_is_www/status/1210981218768044033

<br>
> Algunas capturas de los graficos
<table>
  <tr>
    <td><img src="https://pbs.twimg.com/media/EM5FHfVXYAEWrmM?format=jpg&name=medium" width="350"></td>
    <td><img src="https://pbs.twimg.com/media/EM5FH6lW4AMKkR2?format=jpg&name=medium" width="350"></td>
    <td><img src="https://pbs.twimg.com/media/EM5FIXhXUAYOjpe?format=jpg&name=medium" width="350"></td>
  </tr>
</table>
<br><br>


<br><br>
## EndPoints BCRA

- milestones : eventos relevantes (presidencia, ministros de economía, presidentes del BCRA, cepo al dólar)
- base : base monetaria
- base_usd: base monetaria dividida USD
- reservas : reservas internacionales
- base_div_res : base monetaria dividida reservas internacionales
- usd : cotización del USD
- usd_of : cotización del USD Oficial
- usd_of_minorista : cotización del USD Oficial (Minorista)
- var_usd_vs_usd_of : porcentaje de variación entre la cotización del USD y el USD oficial
- circulacion_monetaria : circulación monetaria
- billetes_y_monedas : billetes y monedas
- efectivo_en_ent_fin : efectivo en entidades financieras
- depositos_cuenta_ent_fin : depositos de entidades financieras en cuenta del BCRA
- depositos : depósitos
- cuentas_corrientes : cuentas corrientes
- cajas_ahorro : cajas de ahorro
- plazo_fijo : plazos fijos
- tasa_depositos_30_dias : tasa de interés por depósitos
- prestamos : prestamos
- tasa_prestamos_personales : tasa préstamos personales
- tasa_adelantos_cuenta_corriente : tasa adelantos cuenta corriente
- porc_prestamos_vs_depositos : porcentaje de prestamos en relación a depósitos
- lebac : LEBACs
- leliq : LELIQs
- lebac_usd : LEBACs en USD
- leliq_usd : LELIQs en USD
- tasa_leliq : Tasa de LELIQs
- m2_privado_variacion_mensual : M2 privado variación mensual
- cer : CER
- uva : UVA
- uvi : UVI
- tasa_badlar : tasa BADLAR
- tasa_baibar : tasa BAIBAR
- tasa_tm20 : tasa TM20
- tasa_pase_activas_1_dia : tasa pase activas a 1 día
- tasa_pase_pasivas_1_dia : tasa pase pasivas a 1 día
- zona_de_no_intervencion_cambiaria_limite_inferior : zona de no intervención cambiaria límite inferior
- zona_de_no_intervencion_cambiaria_limite_superior : zona de no intervención cambiaria límite superior
- inflacion_mensual_oficial : inflación mensual oficial
- inflacion_interanual_oficial : inflación inteanual oficial
- inflacion_esperada_oficial : inflación esperada oficial
- dif_inflacion_esperada_vs_interanual : diferencia entre inflación interanual oficial y esperada
- var_base_monetaria_interanual : variación base monetaria interanual
- var_usd_interanual : variación USD interanual
- var_usd_oficial_interanual : variación USD (Oficial) interanual
- var_merval_interanual : variación merval interanual
- merval : MERVAL
- merval_usd : MERVAL dividido cotización del USD




<br><br>

## Créditos

Utilizamos las librerías:
- pyfolio https://github.com/quantopian/pyfolio
- yfinance https://github.com/ranaroussi/yfinance
