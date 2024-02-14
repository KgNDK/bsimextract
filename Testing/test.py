import pandas as pd
import xml.etree.ElementTree as ET

import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import openpyxl
from plotly.subplots import make_subplots


#! Importing XML file and conversion to dataframe
tree = ET.parse(r'C:\Users\Mikkel H. Lauridsen\OneDrive - Aalborg Universitet\Undervisning\05 Projekt\11 Be18+BSim\Myretuen eksisterende_nylayout_V2(FV)_Design_res1.xml')
root = tree.getroot()

data = []
columns = []
first_row = True  # Flag to identify the first row

for table in root.findall('table'):
    for row in table.findall('row'):
        if first_row:
            columns = [child.tag for child in row]  # Get the names of elements in the first row
            first_row = False  # Reset the flag
        data.append([child.text for child in row])

df = pd.DataFrame(data, columns=columns)


# df = df.transpose()
# print(df.iloc[:, 0])

# if "Varme" in str(df.iloc[:, 0]):
#     print("yes")

# print(df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "kWh/m²"].index[0], 1:].str.replace(',', '.').astype(float).head(12))
# print(df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "kWh/m²"].index[6], 1:].str.replace(',', '.').astype(float).head(12))

# print(df)
# print(df[df.iloc[:, 1]].index.get_loc("Varme"))

# print(df.iloc[:, 0][df.iloc[:, 0] == "kWh/m²"].index[6])
# print(df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "kWh/m²"].index[6], 1:].str.replace(',', '.').astype(float).head(12))
# print(df.iloc[74, 1:].str.replace(',', '.').astype(float).head(12))


# Print the column names
# print("Column names:", columns)

# print(str(df.iloc["Varme", :]))
# print(df)
# df.to_csv('output.txt', sep='\t', index=False, encoding='ISO-8859-1')


#! plot 1

fig1 = go.Figure(
        layout=go.Layout(
            # title="Opvarmning vs. Forbrug",
            yaxis_title="[kWh/m^2 pr. år]",
            barmode="group",
            height=300,
            width=1000,
            yaxis_showticklabels=True,
            yaxis_showgrid=True,
            # yaxis_range=[0, max(max(df["Rumopvarmning"] + df["Varmt brugsvand"]), max(df["Solindfald"] + df["Internt tilskud"] + df["Fra rør og VVB"]))+0.5],
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

# print(df.iloc[:, 0][df.iloc[:, 0] == "MWh"]) # Used to retrieve month index of "MWh" in danish. If english use "MWh" instead. Only used if Be18 is updated with new xml layout
# print(df.iloc[:, 0][df.iloc[:, 0] == "kWh/m²"].index[3]) # Used to retrieve index of "kWh/m²" in danish at the 3th position. If english use "Heating requirement" instead. Only used if Be18 is updated with new xml layout
fig1.add_bar(
    x = df.iloc[0, 1:].str.replace(',', '.').astype(str).head(12),
    y = df.iloc[18, 1:].str.replace(',', '.').astype(float).head(12),
    name='Rumopvarmning',
    offsetgroup=0,
    marker=dict(color="#cc4444"),
)

# print(df.iloc[:, 0][df.iloc[:, 0] == "kWh/m²"].index[6]) # Used to retrieve index of "kWh/m²" in danish at the 6th position. If english use "kWh/m²" instead. Only used if Be18 is updated with new xml layout
fig1.add_bar(
    x=df.iloc[0, 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[74, 1:].str.replace(',', '.').astype(float).head(12),
    name='Varmt brugsvand',
    offsetgroup=0,
    base = df.iloc[177, 1:].str.replace(',', '.').astype(float).head(12),
    marker=dict(color="#ae2f2f"),
)

# print(df.iloc[:, 0][df.iloc[:, 0] == "Solindfald"]) # Used to retrieve index of "Solindfald" in danish. If english use "Incident solar radiation" instead. Only used if Be18 is updated with new xml layout
fig1.add_bar(
    x=df.iloc[0, 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[170, 1:].str.replace(',', '.').astype(float).head(12),
    name='Solindfald',
    offsetgroup=1,
    marker=dict(color="#312679"),
)

# print(df.iloc[:, 0][df.iloc[:, 0] == "Internt tilskud"]) # Used to retrieve index of "Internt tilskud" in danish. If english use "Internal supplement" instead. Only used if Be18 is updated with new xml layout
fig1.add_bar(
    x=df.iloc[0, 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[171, 1:].str.replace(',', '.').astype(float).head(12),
    name='Internt tilskud',
    offsetgroup=1,
    base=df.iloc[170, 1:].str.replace(',', '.').astype(float).head(12),
    marker=dict(color="#5341c4"),
)

# print(df.iloc[:, 0][df.iloc[:, 0] == "Fra rør og VVB"]) # Used to retrieve index of "Fra rør og VVB" in danish. If english use "From pipes and water container" instead. Only used if Be18 is updated with new xml layout
fig1.add_bar(
    x=df.iloc[0, 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[172, 1:].str.replace(',', '.').astype(float).head(12),
    name='Fra rør og VVB',
    offsetgroup=1,
    base=df.iloc[170, 1:].str.replace(',', '.').astype(float).head(12) + df.iloc[171, 1:].str.replace(',', '.').astype(float).head(12),
    marker=dict(color="#7668d0"),
)

# print(df.iloc[:, 0][df.iloc[:, 0] == "Udnyttelses-faktor"]) # Used to retrieve index of "Udnyttelses-faktor" in danish. If english use "From pipes and water container" instead. Only used if Be18 is updated with new xml layout
fig1.add_trace(go.Scatter(
    x=df.iloc[0, 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[175, 1:].str.replace(',', '.').astype(float).head(12)*100,
    name='Udnyttelses-faktor',
    yaxis="y3",
    line=dict(color="#1c8eae", width=3),
))


fig1.update_layout(yaxis3=dict(
    title="[%]",
    overlaying="y",
    side="right",
    range=[0,100], showgrid=False
))
fig1.update_layout(paper_bgcolor="white", plot_bgcolor="white")
fig1.update_yaxes(gridcolor='LightGrey')

fig1.show()

# fig1.write_image("opvarmning_vs_forbrug.png", engine="kaleido")

#? Area
# print(df.iloc[:, 0][df.iloc[:, 0] == "I alt til bygningsdrift"]) # 30 # Used if Be18 is updated with new xml layout
# print(df.iloc[:, 0][df.iloc[:, 0] == "I alt"]) # 139 # Used if Be18 is updated with new xml layout
area = round((sum((df.iloc[30, 1:].str.replace(',', '.').astype(float).head(13) / df.iloc[31, 1:].str.replace(',', '.').astype(float).head(13)) / len(df.iloc[30, 1:].str.replace(',', '.').astype(float).head(13))) +
         sum((df.iloc[139, 1:].str.replace(',', '.').astype(float).head(13) / df.iloc[140, 1:].str.replace(',', '.').astype(float).head(13)) / len(df.iloc[139, 1:].str.replace(',', '.').astype(float).head(13)))) / 2, 2)

#? axis
fig2values = [
    round((df.iloc[4, 1:].str.replace(',', '.').astype(float).iloc[12] * 1000) / area, 2),
    round(df.iloc[18, 1:].str.replace(',', '.').astype(float).iloc[12], 2),
    round(df.iloc[28, 1:].str.replace(',', '.').astype(float).iloc[12] / area, 2),
    round(df.iloc[29, 1:].str.replace(',', '.').astype(float).iloc[12] / area, 2),
    round((df.iloc[30, 1:].str.replace(',', '.').astype(float).iloc[12] - df.iloc[28, 1:].str.replace(',', '.').astype(float).iloc[12] / area - df.iloc[29, 1:].str.replace(',', '.').astype(float).iloc[12]) / area, 2),
    round(df.iloc[74, 1:].str.replace(',', '.').astype(float).iloc[12], 2)
]

ratio = round(1. / sum(fig2values), 5)
tick_pos = range(0, int(max(fig2values)) + 1, 7)
tick_text = [str(int(ratio * pos * 100)) + ' %' for pos in tick_pos]

fig2 = go.Figure(
        layout=go.Layout(
            barmode="group",
            height=500,
            width=700,
            yaxis_showticklabels=True,
            yaxis_showgrid=True,
            font=dict(family="Calibri", size=20),
        hovermode="x",
        margin=dict(b=0,t=10,l=0,r=10)

    )
)

fig2.add_bar(y=[round((df.iloc[4, 1:].str.replace(',', '.').astype(float).iloc[12] * 1000) / area, 2)], x=["Overtemperatur i rum"], marker_color = "#211a52")
fig2.add_bar(y=[round(df.iloc[18, 1:].str.replace(',', '.').astype(float).iloc[12], 2)], x=["Rumopvarmning"], marker_color = "#54616e")
fig2.add_bar(y=[round(df.iloc[28, 1:].str.replace(',', '.').astype(float).iloc[12] / area, 2)], x=["Køling"], marker_color = "#594fbf")
fig2.add_bar(y=[round(df.iloc[29, 1:].str.replace(',', '.').astype(float).iloc[12] / area, 2)], x=["Belysning"], marker_color = "#bb5b17")
fig2.add_bar(y=[round((df.iloc[30, 1:].str.replace(',', '.').astype(float).iloc[12] - df.iloc[28, 1:].str.replace(',', '.').astype(float).iloc[12] / area - df.iloc[29, 1:].str.replace(',', '.').astype(float).iloc[12]) / area, 2)], x=["Eltilbygningsdrift"], marker_color = "#007fa3")
fig2.add_bar(y=[round(df.iloc[74, 1:].str.replace(',', '.').astype(float).iloc[12], 2)], x=["Varmtbrugsvand"], marker_color = "#0e8563")

fig2.add_trace(go.Scatter(
    x=[],
    y=[],
    yaxis="y3",
    opacity=0,
))

fig2.update_layout(
    yaxis=dict(
        title="[kWh/m^2 pr. år]",
        range=[0, max(fig2values) + 0.5],
    ),
    yaxis3=dict(
        title="[%]",
        overlaying="y",
        side="right",
        range=[0, max(fig2values)*ratio*100],
        showgrid=False
))

fig2.update_layout(paper_bgcolor="white", plot_bgcolor="white", showlegend=False)
fig2.update_yaxes(gridcolor='LightGrey')
fig2.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'})

fig2.show()