from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas as pd
import datetime
import time
from pandas_datareader import data


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", text=None, btn=None)

@app.route('/success-table', methods=['POST'])
def success_table():
    global filename
    if request.method == "POST":
        file = request.files['file']
        try:
            df = pd.read_csv(file)
            # Usando un user_agent personalizado para evitar el error
            gc = Nominatim(user_agent="mi_aplicacion_geocoder", timeout=5)

            def geocode_address(address):
                retries = 3
                for i in range(retries):
                    try:
                        return gc.geocode(address)
                    except Exception as e:
                        print(f"Error geocodificando {address}: {e}")
                        time.sleep(1) 
                return None  

            df["coordinates"] = df["Address"].apply(geocode_address)
            df['Latitude'] = df['coordinates'].apply(lambda x: x.latitude if x is not None else None)
            df['Longitude'] = df['coordinates'].apply(lambda x: x.longitude if x is not None else None)
            df = df.drop("coordinates", axis=1)

            filename = datetime.datetime.now().strftime("sample_files/%Y-%m-%d-%H-%M-%S-%f" + ".csv")
            df.to_csv(filename, index=None)

            return render_template("index.html", text=df.to_html(), btn='download.html')
        except Exception as e:
            return render_template("index.html", text=str(e), btn=None)

@app.route("/download-file/")
def download():
    return send_file(filename, download_name='yourfile.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
