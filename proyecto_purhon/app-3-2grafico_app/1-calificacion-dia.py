import justpy as Jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
import time
dt = pd.read_csv("C:/Users/USUARIO/Documents/proyecto_purhon/grafico_app/reviews.csv", parse_dates=['Timestamp'])
dt['Day'] = dt['Timestamp'].dt.date
day_average = dt.groupby(['Day']).mean(numeric_only=True)

grafica_char = """
 {
    title: {
        text: 'Growth of Internet Users Worldwide (logarithmic scale)'
    },

    accessibility: {
        point: {
            valueDescriptionFormat:
                '{xDescription}{separator}{value} million(s)'
        }
    },

    xAxis: {
        title: {
            text: 'Fecha'
        },
        categories: [1995, 2000, 2005, 2010, 2015, 2020, 2023]
    },

    yAxis: {
        type: 'Promedio',
        title: {
            text: 'Number of Internet Users (in millions)'
        }
    },

    tooltip: {
        headerFormat: '<b>{series.name}</b><br />',
        pointFormat: '{point.y} promedio rango(s)'
    },

    series: [{
        name: 'Promedio por persona',
        keys: ['y', 'color'],
        data: [
            [16, '#0000ff'],
            [361, '#8d0073'],
            [1018, '#ba0046'],
            [2025, '#d60028'],
            [3192, '#eb0014'],
            [4673, '#fb0004'],
            [5200, '#ff0000']
        ],
        color: {
            linearGradient: {
                x1: 0,
                x2: 0,
                y1: 1,
                y2: 0
            },
            stops: [
                [0, '#0000ff'],
                [1, '#ff0000']
            ]
        }
    }]
}
"""

grafica_char2 = """
{
    chart: {
        type: 'spline',
        inverted: true
    },
    title: {
        text: 'Atmosphere Temperature by Altitude',
        align: 'left'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model',
        align: 'left'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""

timestamps = [int(time.mktime(d.timetuple()) * 1000) for d in day_average.index]

def app():
    wp = Jp.QuasarPage()
    h1 = Jp.QDiv(a=wp, text = "no se que dice el original",classes="text-h2 text-center q-pa-lg")
    p1 = Jp.QDiv(a=wp, text = "curso de analisis y no se  uqe mas")
    hc =Jp.HighCharts(a=wp, options=grafica_char)
    hc.options.title.text = "Promedio del curso"

    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list((day_average['Rating']))


#    h2 = Jp.HighCharts(a=wp, options=grafica_char)
#    h2.options.series[0].data = [
#    [1262304000000, 0.7537],
#    [1262563200000, 0.6951],
#    [1262649600000, 0.6925],
#    [1262736000000, 0.697],
#    [1262822400000, 0.6992]
#]

    return wp

Jp.justpy(app)