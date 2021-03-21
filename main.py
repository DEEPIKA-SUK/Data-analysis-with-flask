from flask import Flask,send_file,render_template
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import csv
data=pd.read_csv('./globalterrorismdb_0718dist.csv',encoding = "ISO-8859-1")

#----Plot1----
attack=data['country_txt'].value_counts()[:5].reset_index()
attack.columns=['Country','Total Attacks']
plt.bar(attack['Country'], attack['Total Attacks'])
plt.ylabel('y - axis')
plt.xlabel('x - axis')
plt.title('My bar chart!')
plt.savefig('static/images/plot.png')


a=[]
for i in range(1,21):
    t=data.iloc[i];
    a.append(t)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',headings=data.columns[:12],data=a)

if __name__ == "__main__":
    app.run(debug=True)


