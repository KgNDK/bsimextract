import pandas as pd
import xml.etree.ElementTree as ET

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import openpyxl
from plotly.subplots import make_subplots


#! my try 1
# df = pd.read_xml(r'C:\Users\Mikkel H. Lauridsen\OneDrive - Aalborg Universitet\Undervisning\05 Projekt\11 Be18+BSim\Myretuen eksisterende_nylayout_V2(FV)_Design_res1.xml', encoding='ISO-8859-1')
# df.replace(",", ".", regex=True, inplace=True)
# print(df)
# df.to_csv('output.txt', sep='\t', index=False, encoding='ISO-8859-1')

#! my try 2

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

print(df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Rumopvarmning"].index[0], 1:].str.replace(',', '.').astype(float).head(12))

# Print the column names
# print("Column names:", columns)
# print(str(df.iloc["Varme", :]))
# print(df)
# df.to_csv('output.txt', sep='\t', index=False, encoding='ISO-8859-1')


#! plot

fig1 = go.Figure(
        layout=go.Layout(
            # title="Opvarmning vs. Forbrug",
            yaxis_title="[kWh pr. år]",
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

fig1.add_bar(
    # x=df["Month"],
    x = df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "MWh"].index[0], 1:].str.replace(',', '.').astype(str).head(12),
    # y=df["Rumopvarmning"],
    y = df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Varmebehov"].index[0], 1:].str.replace(',', '.').astype(float).head(12),
    name='Rumopvarmning',
    offsetgroup=0,
    marker=dict(color="#cc4444"),
)

# print(df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "MWh"].index[0], 1:].str.replace(',', '.').astype(str).head(12))
# print(df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Rumopvarmning"].index[0], 1:].str.replace(',', '.').astype(float).head(12))


fig1.add_bar(
    x=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "MWh"].index[0], 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Varmt brugsvand"].index[0], 1:].str.replace(',', '.').astype(float).head(12),
    name='Varmt brugsvand',
    offsetgroup=0,
    base = df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Varmebehov"].index[0], 1:].str.replace(',', '.').astype(float).head(12),
    marker=dict(color="#ae2f2f"),
)

fig1.add_bar(
    x=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "MWh"].index[0], 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Solindfald"].index[0], 1:].str.replace(',', '.').astype(float).head(12),
    name='Solindfald',
    offsetgroup=1,
    marker=dict(color="#312679"),
)

fig1.add_bar(
    x=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "MWh"].index[0], 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Internt tilskud"].index[0], 1:].str.replace(',', '.').astype(float).head(12),
    name='Internt tilskud',
    offsetgroup=1,
    base=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Solindfald"].index[0], 1:].str.replace(',', '.').astype(float).head(12),
    marker=dict(color="#5341c4"),
)

fig1.add_bar(
    x=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "MWh"].index[0], 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Fra rør og VVB"].index[0], 1:].str.replace(',', '.').astype(float).head(12),
    name='Fra rør og VVB',
    offsetgroup=1,
    base=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Solindfald"].index[0], 1:].str.replace(',', '.').astype(float).head(12)+df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Internt tilskud"].index[0], 1:].str.replace(',', '.').astype(float).head(12),
    marker=dict(color="#7668d0"),
)

fig1.add_trace(go.Scatter(
    x=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "MWh"].index[0], 1:].str.replace(',', '.').astype(str).head(12),
    y=df.iloc[df.iloc[:, 0][df.iloc[:, 0] == "Udnyttelses-faktor"].index[0], 1:].str.replace(',', '.').astype(float).head(12)*100,
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
fig1.update_layout(paper_bgcolor="white", plot_bgcolor="white")
fig1.update_yaxes(gridcolor='LightGrey')

fig1.show()

fig1.write_image("opvarmning_vs_forbrug.png", engine="kaleido")