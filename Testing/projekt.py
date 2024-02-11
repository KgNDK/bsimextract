"""
Plotly plot for project in Uni

#!Remove later!
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import openpyxl
from plotly.subplots import make_subplots

# importing data
df = pd.read_excel(r'C:\Users\Mikkel H. Lauridsen\OneDrive - Aalborg Universitet\Programmer\06 Be18Extract\TestArk.xlsx')
df.replace(",", ".", regex=True, inplace=True)
print(df)

fig1 = go.Figure(
        layout=go.Layout(
            # title="Opvarmning vs. Forbrug",
            yaxis_title="[kWh pr. år]",
            barmode="group",
            height=300,
            width=1000,
            yaxis_showticklabels=True,
            yaxis_showgrid=True,
            yaxis_range=[0, max(max(df["Rumopvarmning"] + df["Varmt brugsvand"]), max(df["Solindfald"] + df["Internt tilskud"] + df["Fra rør og VVB"]))+0.5],
            font=dict(family="Calibri", size=20),

        yaxis2=go.layout.YAxis(
            visible=False,
            matches="y",
            overlaying="y",
            anchor="x",
            # plot_bgcolor="white",
        ),
        legend=dict(
            x=0,
            y=-0.15,
            bgcolor="White",
            orientation="h",
            font=dict(
                size=16,
                color="black",
                family="Calibri",
                ),
            ),
        hovermode="x",
        margin=dict(b=0,t=10,l=0,r=10)

    )
)

fig1.add_bar(
    x=df["Month"],
    y=df["Rumopvarmning"],
    name='Rumopvarmning',
    offsetgroup=0,
    marker=dict(color="#cc4444"),
)

fig1.add_bar(
    x=df["Month"],
    y=df["Varmt brugsvand"],
    name='Varmt brugsvand',
    offsetgroup=0,
    base = df["Rumopvarmning"],
    marker=dict(color="#ae2f2f"),
)

fig1.add_bar(
    x=df["Month"],
    y=df["Solindfald"],
    name='Solindfald',
    offsetgroup=1,
    marker=dict(color="#312679"),
)

fig1.add_bar(
    x=df["Month"],
    y=df["Internt tilskud"],
    name='Internt tilskud',
    offsetgroup=1,
    base=df["Solindfald"],
    marker=dict(color="#5341c4"),
)

fig1.add_bar(
    x=df["Month"],
    y=df["Fra rør og VVB"],
    name='Fra rør og VVB',
    offsetgroup=1,
    base=df["Internt tilskud"]+df["Solindfald"],
    marker=dict(color="#7668d0"),
)

fig1.add_trace(go.Scatter(
    x=df["Month"],
    y=df["Udnyttelses-faktor"]*100,
    name='Udnyttelses-faktor',
    yaxis="y3",
    line=dict(color="#bb5b17", width=3),
))


fig1.update_layout(yaxis3=dict(
    title="[%]",
    overlaying="y",
    side="right",
    range=[0,100], showgrid=False
))
fig1.update_layout(template="simple_white")

fig1.show()

fig1.write_image("opvarmning_vs_forbrug.png", engine="kaleido")

fig2 = go.Figure(go.Pie(
    labels=df["kWh/m2 år"],
    values=df["Forbrug"],
    marker=dict(colors=["#211a52", "#54616e", "#594fbf", "#bb5b17", "#007fa3", "#0e8563", "#cc445b", "#97701f", "#a1654"]),
))

fig2.update_layout(
    width=800,
    height=800,
    font=dict(family="Calibri", size=20),
    legend=dict(
        x=0.05,
        y=-0.02,
        bgcolor="White",
        orientation="h",
        font=dict(
            size=18,
            color="black",
            family="Calibri",
        ),
    )
)

fig2.show()

fig1.write_image("elforbrug_pie.png", engine="kaleido")