import pandas as pd
import csv
import plotly.graph_objects as go

# df here is the whole data file
df=pd.read_csv("teacher.csv")
# data here is only of the given student id
data=df.loc[df["student_id"]=="TRL_xyz"]
print(data.groupby("level")["attempt"].mean())

figure = go.Figure(go.Bar(
    x=data.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2", "Level 3", "Level 4"],
    orientation='h'
))

figure.show()