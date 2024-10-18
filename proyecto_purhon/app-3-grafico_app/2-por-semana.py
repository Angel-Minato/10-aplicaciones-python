import justpy as Jp
import pandas as pd
from datetime import datetime
from pytz import utc
import time
dt = pd.read_csv("./app-3-2grafico_app/reviews.csv", parse_dates=['Timestamp'])
dt['Week'] = dt['Timestamp'].dt.strftime('%Y-%U')
Week_average = dt.groupby(['Week']).mean(numeric_only=True)

grafica_char= """
{
    chart: {
        type: 'spline',
        inverted: false
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

def app():
    wp = Jp.QuasarPage()
    h1 = Jp.QDiv(a=wp, text = "no se que dice el original",classes="text-h2 text-center q-pa-lg")
    p1 = Jp.QDiv(a=wp, text = "curso de analisis y no se  uqe mas")
    hc =Jp.HighCharts(a=wp, options=grafica_char)

    hc.options.xAxis.categories = list(Week_average.index)
    hc.options.series[0].data = list((Week_average['Rating']))

    return wp

Jp.justpy(app)