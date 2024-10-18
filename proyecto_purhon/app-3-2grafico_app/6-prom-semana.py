import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
 
data = pandas.read_csv("./grafico_app/reviews.csv", parse_dates=['Timestamp'])
data['Weekday'] = data['Timestamp'].dt.strftime('%A')
data['Daynumber'] = data['Timestamp'].dt.strftime('%w')
 
weekday_average = data.groupby(['Weekday', 'Daynumber']).mean(numeric_only=True)
weekday_average = weekday_average.sort_values('Daynumber')
 
chart_def = """
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
            text: 'Year'
        },
        categories: [1995, 2000, 2005, 2010, 2015, 2020, 2023]
    },

    yAxis: {
        type: 'logarithmic',
        title: {
            text: 'Number of Internet Users (in millions)'
        }
    },

    tooltip: {
        headerFormat: '<b>{series.name}</b><br />',
        pointFormat: '{point.y} million(s)'
    },

    series: [{
        name: 'Internet Users',
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
 
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Análisis de reseñas de cursos", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="Estos gráficos representan el análisis de la revisión del curso.", classes="q-pa-md")
 
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(weekday_average.index.get_level_values(0))
    hc.options.series[0].data = list(weekday_average['Rating'])
 
    return wp
 
jp.justpy(app)