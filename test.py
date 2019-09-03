

import plotly.plotly as py
import plotly

plotly.tools.set_credentials_file(username='bokepa', api_key='n7znZoigIpfie9g79bee')

import urllib.request, json

import urllib.request

with urllib.request.urlopen("https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json") as url:
	s = url.read()
	print(s)

data = json.loads(s.decode("utf-8"))

data_trace = dict(
    type='sankey',
    domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
    orientation = "h",
    valueformat = ".0f",
    valuesuffix = "TWh",
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    )
)

layout =  dict(
    title = "Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
    font = dict(
      size = 10
    )
)

fig = dict(data=[data_trace], layout=layout)
plotly.plotly.plot(fig, validate=False)

