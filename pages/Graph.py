import pickle
import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 10})
plt.rcParams["figure.figsize"] = (20,10)

df = pickle.load(open("mypickle.pickle",'rb'))

option = st.selectbox(
     'Select Subject',
     ("HMI", "DC",'HPC','NLP','AWN','PM','FM','EDM','HRM','PECSR','RM','IPRP','DBM','EM','HMI Lab','DC Lab','CC Lab','C Lab 2','Major Project','SEM-8','SEM-1','SEM-2','SEM-3','SEM-4','SEM-5','SEM-6','SEM-7','CGPA'))

option2 = st.selectbox(
     'Filter By College',
     ("VIT", "RAIT","af","All"))

if option2=='All' :
    option2=""

df.drop(df[df[option] == '--'].index, inplace = True)
df.drop(df[df[option] == 'null'].index, inplace = True)
df.drop(df[df[option] == 0].index, inplace = True)
df.drop(df[df[option] == '0;'].index, inplace = True)
df.drop(df[df[option] == '00;'].index, inplace = True)
df.drop(df[df[option] == '.00;'].index, inplace = True)
df.drop(df[df[option] == '--'].index, inplace = True)
df.drop(df[df[option] == '--;'].index, inplace = True)
df.drop(df[df[option] == '0'].index, inplace = True)








df = df.sort_values(by=[option], ascending=False)
pd.to_numeric(df[option])
df=df[df['College'].str.contains(option2)]



arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(df[option], bins=50)
st.pyplot(fig)
c1, c2= st.columns([3, 1])
c1.write(df[['Full Name','Seat No.','College',option]].head())
c2.write("Highest Marks Scored : "+str(df[option].astype(int).max().round(2)))
c2.write("Average Marks Scored : "+str(df[option].astype(int).mean().round(2)))
c2.write("Lowest Marks Scored : "+str(df[option].astype(int).min().round(2)))


