# http://blog.sina.com.cn/s/blog_53a8a9d40101krae.html

import random
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF


data = []
for m in range(1, 13):
    data.append((2018, m, random.randrange(100, 200), random.randrange(130, 300), random.randrange(80, 150)))


pred = [r[2] for r in data]
height = [r[3] for r in data]
low = [r[4] for r in data]
times = [r[0]+r[1]/12 for r in data]

# print(pred)
# print(height)
# print(low)
# print(times)

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [
    list(zip(times, pred)),
    list(zip(times, height)),
    list(zip(times, low)),
]

lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.black
lp.lines[2].strokeColor = colors.red

a = Drawing(400, 200)
a.add(lp)
renderPDF.drawToFile(a, 'report2.pdf', 'Sunspots')
