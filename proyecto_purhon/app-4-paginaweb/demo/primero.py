from flask import Flask, render_template
import yfinance as yf
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

app = Flask(__name__)

@app.route('/plot/')
def plot():
    start = datetime.datetime(2023, 10, 1)
    end = datetime.datetime(2024, 3, 15)

    df = yf.download("UBI.PA", start=start, end=end)

    def inc_dec(c, o):
        if c > o:
            value = "Incremento"
        elif c < o:
            value = "Decremento"
        else:
            value = "Igual"
        return value

    df["status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open + df.Close) / 2
    df["altura"] = abs(df.Close - df.Open)
    df = df.dropna()

    p = figure(x_axis_type='datetime', width=1000, height=400, title="Gráfica de Precios", sizing_mode="scale_width")
    p.title.text = "Gráfica de Ubisoft"
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12 * 60 * 60 * 1000

    p.segment(df.index, df.High, df.index, df.Low, color="Black")

    p.rect(df.index[df.status == "Incremento"], df.Middle[df.status == "Incremento"],
           hours_12, df.altura[df.status == "Incremento"], fill_color='green', line_color="black")

    p.rect(df.index[df.status == "Decremento"], df.Middle[df.status == "Decremento"],
           hours_12, df.altura[df.status == "Decremento"], fill_color='red', line_color="black")

    script1, div1 = components(p)
    
    cnd_js = CDN.js_files[0] if CDN.js_files else None
    clon_css = CDN.css_files[0] if CDN.css_files else None
    print(cnd_js+' hola1')
    print(clon_css)

    return render_template("plot.html", script1=script1, div1=div1, cnd_js=cnd_js, clon_css=clon_css)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/otro-lugar/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)