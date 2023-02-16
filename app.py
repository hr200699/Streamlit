import streamlit as st
import pandas as pd

st.image("https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/NEDUET_logo.svg/1200px-NEDUET_logo.svg.png", width=100)
st.title("Assignment on: Streamlit Geograph of 20 Branches of UBL")


st.text("Student of PGD in Data Sciences with AI, Batch 3")
st.text("Course: Data Visualization")

df=pd.read_excel("UBL Branch List.xlsx")
st.write("Data of UBL Branches in Pakistan")
st.write(df)
i=st.multiselect('Select Branch(/es):',df["Branch Name"].unique())

j=pd.DataFrame(df.groupby(['Branch Name'])[['Region']])
st.write(j)
a=df["Branch Name"]
st.write(a)

import re
b=list(a)
e=[]
for rows in b:
    c=str(rows)
    d=re.findall(r"\b(.*) Karachi",c)
    e.append(d)

f=[]
for rows in e:
    for columns in rows:
        if columns!=[]:
            f.append(columns)
df1=pd.DataFrame(f)
st.text("Karachi Branches")
st.write(df1)

#graph
df2=df1.loc[0:19]
st.write("Top 20 Karachi Branches")
st.write(df2)
st.write("GeoGraph")
df3 = pd.DataFrame(
    {"lat":[24.85009582822219,24.85070298883003,24.854929575693433,24.866000689938303,24.849038148647775,24.845841376311807,24.845654308135114,24.910808220273505,24.86524058297912,24.852877971295378,24.849934632316433,24.861434697216772,24.87616989330356,24.871861183278252,24.88150675478632,24.890147586713283,24.93070099663016,24.94406055620441,24.853811905032547,24.822083996184176],
    'lon':[67.21096226472672,66.99882094631272,67.00287570772007,67.0253443078142,67.00109480767473,67.05433994870197,67.05499153222794,67.01393502159333,67.02549913746076,67.00734523747147,66.99916465012531, 67.00284971945908,67.02084759841559,67.05991713020295,67.0663145234605,67.06106935079133,67.2013488130465,67.07278523295044,67.07380872797414,67.04648667301632]},columns=['lat', 'lon'])
st.map(df3)