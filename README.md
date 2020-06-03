# Bursatil Argentina Python
> Ejemplos prácticos para empezar a programar aplicaciones del ámbito bursatil en python
La idea era hacer un instructivo bien simple para quienes quieran empezar a codear sus primeras lineas. 

<br><br>
# Instalación

Instalar el paquete Anaconda
Descarga de la pagina oficial https://www.anaconda.com/products/individual
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



<br><br>
# Archivos

* [PrimerosPasos](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/analisis%20activo.py) Bajar datos de mercado por activo
* [CCLs](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/ccls.py) Calculo del CCL para diferentes tickers (GGAL, PAM, YPF, etc)
* [Brechas](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/brechas.py) TDC oficial, MEP y CCL, Brecha actual CCL-Oficial, MEP-Oficial, CCL-MEP
* [BCRA](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/bcra.py) +40 Endpoints de series historicas del BCRA (como reservas internacionales, tdc, m2, tasas, etc) 
* [Bot de Trading](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/Bot%20basico%20BTCpy.py) Ejemplo a fines dídácticos de como funciona un bot de trading
* [CAGR idea](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/CAGR2.py) Ejemplo de estrategia de Holdear las peores o mejores 5 acciones de una lista segun rendimiento de semana previa, idea de @camilocr3 https://twitter.com/camilocr3
* [Futures](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/CAGR2.py) Comparación de Futuros de commodities como el WTI el oro etc, vs precios y volumenes de "X" dias atras, idea de @lucasgday  https://twitter.com/lucasgday
* [Black&Scholes](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/black_scholes.py) Cálculo de VI en opciones mediante modelo de Black&Scholes y griegas
* [Dolar Blue](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/blue.py) Scrapper del valor del dolar Blue de todo un año y download en un excel
* [DrawDowns Merval](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/caidas%20desde%20max%20merval.py) Análisis de las máximas cáidas del panel general del merval (derrape 2018-2020) y sus potenciales upsides hasta maximos
* [MachineLearning KMeans](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/clusterOIL.py) Clusterización de coeficientes de correlación OIL vs Petroleras
* [Graficos 3D](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/graf%203D-Points.py) Perfil de volumen-precio en un graf 3D con matplotlib
* [Panel Opciones Byma](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/opcionesByma.py) Scrapper de la página de Rava a DataFrame y download a excel
* [Transcribir Video de YouTube](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/transcribir%20video.py) Analizador, contador y comparador de las palabras de un video de youtube
* [Google Sheets / Google Finance](https://github.com/gauss314/Bursatil-Argentina-Python/blob/master/googleSheets.py) Lectura sencilla de tabla de planilla de googlesheet online y pasaje a dataframe



<br>
> Hilo de twitter donde se inició esta idea: 
https://twitter.com/JohnGalt_is_www/status/1210981218768044033



<br><br>

## Créditos

Utilizamos las librerías:
- yfinance https://github.com/ranaroussi/yfinance
