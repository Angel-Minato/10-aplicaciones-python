import yfinance as yf
import datetime

# Definir las fechas
start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2024, 3, 10)

# Descargar datos de Ubisoft usando su símbolo de cotización
df = yf.download("UBI.PA", start=start, end=end)

# Mostrar los primeros datos
print(df.head())

