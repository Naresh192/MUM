import pickle
import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 10})
plt.rcParams["figure.figsize"] = (20,10)

df = pickle.load(open("mypickle.pickle",'rb'))

sn1 = st.text_input('Enter a Seat No.', '7280255')
sn2 = st.text_input('Enter another Seat No.', '7280326')


df1=df[df['Seat No.']==sn1]
df2=df[df['Seat No.']==sn2]
df3=df.columns
df1
df2

df1a=[int(i) for i in df1.values.tolist()[0][2:21]]
df2b=[int(i) for i in df2.values.tolist()[0][2:21]]
df3a=df3.values.tolist()[2:21]

fig, ax = plt.subplots()
ax.bar(df3a,df1a,+0.4,align='edge',bottom=0)
ax.bar(df3a,df2b,-0.4,align='edge',bottom=0)
fig.tight_layout()
st.pyplot(fig)

df31=[float(i) if str(i).replace('.','',1).isnumeric() else 0 for i in df1.values.tolist()[0][21:-1]]
df4=[float(i) if str(i).replace('.','',1).isnumeric() else 0 for i in df2.values.tolist()[0][21:-1]]
df3=df3.values.tolist()[21:-1]
fig2, ax2 = plt.subplots()
ax2.bar(df3,df31,+0.4,align='edge',bottom=0)
ax2.bar(df3,df4,-0.4,align='edge',bottom=0)
fig2.tight_layout()
st.pyplot(fig2)


