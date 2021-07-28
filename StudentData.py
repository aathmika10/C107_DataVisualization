import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("teacher.csv")
print(df.groupby("level")["attempt"].mean())

figure = go.Figure(go.Bar(
    x=df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2", "Level 3", "Level 4"],
    orientation='h'
))

figure.show()