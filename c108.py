import csv
import pandas as pd
import plotly.figure_factory as ff

f = pd.read_csv("data.csv")
fig = ff.create_distplot([f["Weight(Pounds)"].tolist()],["Weight"], show_hist= False)

fig.show()