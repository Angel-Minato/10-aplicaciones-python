import justpy as Jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

dt = pd.read_csv("./grafico_app/reviews.csv", parse_dates=['Timestamp'])
shara = dt.groupby(['Course Name'])['Rating'].count()
print(shara)

grafica_char = """
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Egg Yolk Composition'
    },
    tooltip: {
        valueSuffix: '%'
    },
    subtitle: {
        text:
        'Source:<a href="https://www.mdpi.com/2072-6643/11/3/684/htm" target="_default">MDPI</a>'
    },
    plotOptions: {
        series: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: [{
                enabled: true,
                distance: 20
            }, {
                enabled: true,
                distance: -40,
                format: '{point.percentage:.1f}%',
                style: {
                    fontSize: '1.2em',
                    textOutline: 'none',
                    opacity: 0.7
                },
                filter: {
                    operator: '>',
                    property: 'percentage',
                    value: 10
                }
            }]
        }
    },
    series: [
        {
            name: 'Percentage',
            colorByPoint: true,
            data: [
                {
                    name: 'Water',
                    y: 55.02
                },
                {
                    name: 'Fat',
                    sliced: true,
                    selected: true,
                    y: 26.71
                },
                {
                    name: 'Carbohydrates',
                    y: 1.09
                },
                {
                    name: 'Protein',
                    y: 15.5
                },
                {
                    name: 'Ash',
                    y: 1.68
                }
            ]
        }
    ]
}
"""

def app():
    wp = Jp.QuasarPage()
    h1 = Jp.QDiv(a=wp, text = "no se que dice el original",classes="text-h3 text-center q-pa-lg")
    p1 = Jp.QDiv(a=wp, text = "curso de analisis y no se  uqe mas", classes="q-pa-lg")

    hc = Jp.HighCharts(a=wp, options=grafica_char)
    hc_data = [{"name":v1, "y":v2}for v1, v2 in zip(shara.index, shara)]
    hc.options.series[0].data = hc_data

    return wp

Jp.justpy(app)
