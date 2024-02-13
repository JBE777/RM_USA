import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

rm_data = pd.read_csv('dataset_rm.csv')
# System of recomendation
df = rm_data[(rm_data["Sentiment"]=="Muy bueno")][["State","Mexican restaurant","Date","City","Address","state"]]
df1 = rm_data[(rm_data["Stars"]==5)][["State","Mexican restaurant","Date","City","Address","state"]]
df2 = rm_data[(rm_data["Stars"]==1)][["State","Mexican restaurant","Date","City","Address","state"]]
# Arizona
df3 = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Arizona")][["State","Mexican restaurant","Date","City","Address"]]
df3_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Arizona")][["State","Mexican restaurant","Date","City","Address"]]
df3_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Arizona")][["State","Mexican restaurant","Date","City","Address"]]
df3_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Arizona")][["State","Mexican restaurant","Date","City","Address"]]
df4 = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Arizona")][["State","Mexican restaurant","Date","City","Address"]]
df_4 = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Arizona")][["State","Mexican restaurant","Date","City","Address"]]
# California
df5 = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="California")][["State","Mexican restaurant","Date","City","Address"]]
df5_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="California")][["State","Mexican restaurant","Date","City","Address"]]
df5_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="California")][["State","Mexican restaurant","Date","City","Address"]]
df5_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="California")][["State","Mexican restaurant","Date","City","Address"]]
df6 = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="California")][["State","Mexican restaurant","Date","City","Address"]]
df_6 = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="California")][["State","Mexican restaurant","Date","City","Address"]]
# Florida
df7 = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Florida")][["State","Mexican restaurant","Date","City","Address"]]
df7_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Florida")][["State","Mexican restaurant","Date","City","Address"]]
df7_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Florida")][["State","Mexican restaurant","Date","City","Address"]]
df7_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Florida")][["State","Mexican restaurant","Date","City","Address"]]
df8 = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Florida")][["State","Mexican restaurant","Date","City","Address"]]
df_8 = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Florida")][["State","Mexican restaurant","Date","City","Address"]]
# Pensilvania
df9 = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Pensilvania")][["State","Mexican restaurant","Date","City","Address"]]
df9_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Pensilvania")][["State","Mexican restaurant","Date","City","Address"]]
df9_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Pensilvania")][["State","Mexican restaurant","Date","City","Address"]]
df9_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Pensilvania")][["State","Mexican restaurant","Date","City","Address"]]
df_9 = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Pensilvania")][["State","Mexican restaurant","Date","City","Address"]]
df_1 = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Pensilvania")][["State","Mexican restaurant","Date","City","Address"]]
# Missouri
df_2 = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Missouri")][["State","Mexican restaurant","Date","City","Address"]]
df_2_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Missouri")][["State","Mexican restaurant","Date","City","Address"]]
df_2_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Missouri")][["State","Mexican restaurant","Date","City","Address"]]
df_2_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Missouri")][["State","Mexican restaurant","Date","City","Address"]]
df_3 = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Missouri")][["State","Mexican restaurant","Date","City","Address"]]
df_5 = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Missouri")][["State","Mexican restaurant","Date","City","Address"]]
# Indiana
df_7 = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Indiana")][["State","Mexican restaurant","Date","City","Address"]]
df_7_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Indiana")][["State","Mexican restaurant","Date","City","Address"]]
df_7_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Indiana")][["State","Mexican restaurant","Date","City","Address"]]
df_7_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Indiana")][["State","Mexican restaurant","Date","City","Address"]]
df_  = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Indiana")][["State","Mexican restaurant","Date","City","Address"]]
df7_ = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Indiana")][["State","Mexican restaurant","Date","City","Address"]]
# Tennessee
df_t = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Tennessee")][["State","Mexican restaurant","Date","City","Address"]]
df_t_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Tennessee")][["State","Mexican restaurant","Date","City","Address"]]
df_t_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Tennessee")][["State","Mexican restaurant","Date","City","Address"]]
df_t_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Tennessee")][["State","Mexican restaurant","Date","City","Address"]]
dft = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Tennessee")][["State","Mexican restaurant","Date","City","Address"]]
dfT = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Tennessee")][["State","Mexican restaurant","Date","City","Address"]]
# Luisiana
df_l = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Luisiana")][["State","Mexican restaurant","Date","City","Address"]]
df_l_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Luisiana")][["State","Mexican restaurant","Date","City","Address"]]
df_l_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Luisiana")][["State","Mexican restaurant","Date","City","Address"]]
df_l_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Luisiana")][["State","Mexican restaurant","Date","City","Address"]]
dfl = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Luisiana")][["State","Mexican restaurant","Date","City","Address"]]
dfL = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Luisiana")][["State","Mexican restaurant","Date","City","Address"]]
# Nevada
df_n = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Nevada")][["State","Mexican restaurant","Date","City","Address"]]
df_n_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Nevada")][["State","Mexican restaurant","Date","City","Address"]]
df_n_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Nevada")][["State","Mexican restaurant","Date","City","Address"]]
df_n_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Nevada")][["State","Mexican restaurant","Date","City","Address"]]
dfn = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Nevada")][["State","Mexican restaurant","Date","City","Address"]]
dfN = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Nevada")][["State","Mexican restaurant","Date","City","Address"]]
# Idaho
df_i = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Idaho")][["State","Mexican restaurant","Date","City","Address"]]
df_i_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Idaho")][["State","Mexican restaurant","Date","City","Address"]]
df_i_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Idaho")][["State","Mexican restaurant","Date","City","Address"]]
df_i_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Idaho")][["State","Mexican restaurant","Date","City","Address"]]
dfi = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Idaho")][["State","Mexican restaurant","Date","City","Address"]]
dfI = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Idaho")][["State","Mexican restaurant","Date","City","Address"]]
# Nueva Jersey
df_nj = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Nueva Jersey")][["State","Mexican restaurant","Date","City","Address"]]
df_nj_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Nueva Jersey")][["State","Mexican restaurant","Date","City","Address"]]
df_nj_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Nueva Jersey")][["State","Mexican restaurant","Date","City","Address"]]
df_nj_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Nueva Jersey")][["State","Mexican restaurant","Date","City","Address"]]
dfnj = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Nueva Jersey")][["State","Mexican restaurant","Date","City","Address"]]
dfNJ = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Nueva Jersey")][["State","Mexican restaurant","Date","City","Address"]]
# Delaware
df_d = rm_data[(rm_data["Stars"]==1)&(rm_data["state"]=="Delaware")][["State","Mexican restaurant","Date","City","Address"]]
df_d_a = rm_data[(rm_data["Stars"]==2)&(rm_data["state"]=="Delaware")][["State","Mexican restaurant","Date","City","Address"]]
df_d_b = rm_data[(rm_data["Stars"]==3)&(rm_data["state"]=="Delaware")][["State","Mexican restaurant","Date","City","Address"]]
df_d_c = rm_data[(rm_data["Stars"]==4)&(rm_data["state"]=="Delaware")][["State","Mexican restaurant","Date","City","Address"]]
dfd = rm_data[(rm_data["Stars"]==5)&(rm_data["state"]=="Delaware")][["State","Mexican restaurant","Date","City","Address"]]
dfD = rm_data[(rm_data["Sentiment"]=="Muy bueno")&(rm_data['state']=="Delaware")][["State","Mexican restaurant","Date","City","Address"]]

col1,col2,col3,col4 = st.columns([2,2,2,2])
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Restaurants in USA", "Recomendations", 'System of recomendation','Location'], 
       icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="vertical")
    selected

if selected == "Home":
    st.title("Welcome to my awesome data science project!")
    st.text("In this project I look into the transactions of mexican restaurants in USA ")
    st.image("Tacos.jpeg")

if selected == "Restaurants in USA":
    if st.sidebar.checkbox("$Dataset$"):
        if col1.button("USA"):
            st.write(rm_data.head()) 
    if st.sidebar.checkbox("$📊_{Graphs}$"):    
        if col1.button("$Stars$"):
            dir_data_dist = pd.DataFrame(rm_data["Stars"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if col1.button("$Sentiments$"):
            dir_data_dist = pd.DataFrame(rm_data["Sentiment"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if col2.button("$Dates$"):
            dir_data_dist = pd.DataFrame(rm_data["Date"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if col2.button("$Years$"):
            dir_data_dist = pd.DataFrame(rm_data["Year"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if col2.button("$Quarters$"):
            dir_data_dist = pd.DataFrame(rm_data["Quarter"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if col3.button("$States$"):
            dir_data_dist = pd.DataFrame(rm_data["state"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if col3.button("$Cities$"):
            dir_data_dist = pd.DataFrame(rm_data["City"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)

if selected == "Recomendations":
    if st.sidebar.checkbox("$Top\ 5\ mexican\ restaurants\ in\ USA$"):
        if col2.button("$The\ Best\ Ones$"):
            st.write(df.head())
        if col2.button("$⭐⭐⭐⭐⭐$"):
            st.write(df1.head())
        if col2.button("$⭐$"):
            st.write(df2.head())
    
if selected == 'System of recomendation':
    if st.sidebar.checkbox("Mexican restaurants"):
        if col1.button("$USA$"):
            st.write(rm_data.head())
    if st.sidebar.checkbox("$⭐\ Star$"):
        if col1.button("$Arizona_{⭐}$"):
            st.write(df3.head())
        if col1.button("$California_{⭐}$"):
            st.write(df5.head())
        if col1.button("$Florida_{⭐}$"):
            st.write(df7.head())
        if col1.button("$Pensilvania_{⭐}$"):
            st.write(df9.head())
        if col2.button("$Missouri_{⭐}$"):
            st.write(df_2.head())
        if col2.button("$Indiana_{⭐}$"):
            st.write(df_7.head())
        if col2.button("$Tennessee_{⭐}$"):
            st.write(df_t.head())
        if col2.button("$Luisiana_{⭐}$"):
            st.write(df_l.head())
        if col3.button("$Nevada_{⭐}$"):
            st.write(df_n.head())
        if col3.button("$Idaho_{⭐}$"):
            st.write(df_i.head())
        if col3.button("$Nueva\ Jersey_{⭐}$"):
            st.write(df_nj.head())
        if col3.button("$Delaware_{⭐}$"):
            st.write(df_d.head())
    if st.sidebar.checkbox("$⭐\ ⭐\ Stars$"):
        if col1.button("$Arizona_{⭐⭐}$"):
            st.write(df3_a.head()) 
        if col1.button("$California_{⭐⭐}$"):
            st.write(df5_a.head())
        if col1.button("$Florida_{⭐⭐}$"):
            st.write(df7_a.head())
        if col1.button("$Pensilvania_{⭐⭐}$"):
            st.write(df9_a.head())
        if col2.button("$Missouri_{⭐⭐}$"):
            st.write(df_2_a.head())
        if col2.button("$Indiana_{⭐⭐}$"):
            st.write(df_7_a.head())
        if col2.button("$Tennessee_{⭐⭐}$"):
            st.write(df_t_a.head())
        if col2.button("$Luisiana_{⭐⭐}$"):
            st.write(df_l_a.head())
        if col3.button("$Nevada_{⭐⭐}$"):
            st.write(df_n_a.head())
        if col3.button("$Idaho_{⭐⭐}$"):
            st.write(df_i_a.head())
        if col3.button("$Nueva\ Jersey_{⭐⭐}$"):
            st.write(df_nj_a.head())
        if col3.button("$Delaware_{⭐⭐}$"):
            st.write(df_d_a.head())
    if st.sidebar.checkbox("$⭐\ ⭐\ ⭐\ Stars$"):
        if col1.button("$Arizona$"):
            st.write(df3_b.head()) 
        if col1.button("$California_{⭐⭐⭐}$"):
            st.write(df5_b.head()) 
        if col1.button("$Florida_{⭐⭐⭐}$"):
            st.write(df7_b.head())
        if col1.button("$Pensilvania_{⭐⭐⭐}$"):
            st.write(df9_b.head())
        if col2.button("$Missouri_{⭐⭐⭐}$"):
            st.write(df_2_b.head())
        if col2.button("$Indiana_{⭐⭐⭐}$"):
            st.write(df_7_b.head())
        if col2.button("$Tennessee_{⭐⭐⭐}$"):
            st.write(df_t_b.head())
        if col2.button("$Luisiana_{⭐⭐⭐}$"):           
            st.write(df_l_b.head())
        if col3.button("$Nevada_{⭐⭐⭐}$"):
            st.write(df_n_b.head())
        if col3.button("$Idaho_{⭐⭐⭐}$"):
            st.write(df_i_b.head())
        if col3.button("$Nueva\ Jersey_{⭐⭐⭐}$"):
            st.write(df_nj_b.head())
        if col3.button("$Delaware_{⭐⭐⭐}$"):
            st.write(df_d_b.head())
    if st.sidebar.checkbox("$⭐\ ⭐\ ⭐\ ⭐\ Stars$"):
        if col1.button("$Arizona_{⭐⭐⭐⭐}$"):
            st.write(df3_c.head())  
        if col1.button("$California_{⭐⭐⭐⭐}$"):
            st.write(df5_c.head()) 
        if col1.button("$Florida_{⭐⭐⭐⭐}$"):
            st.write(df7_c.head()) 
        if col1.button("$Pensilvania_{⭐⭐⭐⭐}$"):
            st.write(df9_c.head())
        if col2.button("$Missouri_{⭐⭐⭐⭐}$"):
            st.write(df_2_c.head())
        if col2.button("$Indiana_{⭐⭐⭐⭐}$"):
            st.write(df_7_c.head())
        if col2.button("$Tennessee_{⭐⭐⭐⭐}$"):
            st.write(df_t_c.head())
        if col2.button("$Luisiana_{⭐⭐⭐⭐}$"):
            st.write(df_l_c.head())
        if col3.button("$Nevada_{⭐⭐⭐⭐}$"):
            st.write(df_n_c.head())
        if col3.button("$Idaho_{⭐⭐⭐⭐}$"):
            st.write(df_i_c.head())
        if col3.button("$Nueva\ Jersey_{⭐⭐⭐⭐}$"):
            st.write(df_nj_c.head())
        if col3.button("$Delaware_{⭐⭐⭐⭐}$"):
            st.write(df_d_c.head())
    if st.sidebar.checkbox("$⭐\ ⭐\ ⭐\ ⭐\ ⭐\ Stars$"):
        if col1.button("$Arizona_{⭐⭐⭐⭐⭐}$"):
            st.write(df4.head())
        if col1.button("$California_{⭐⭐⭐⭐⭐}$$"):
            st.write(df6.head())
        if col1.button("$Florida_{⭐⭐⭐⭐⭐}$$"):
            st.write(df8.head())
        if col1.button("$Pensilvania_{⭐⭐⭐⭐⭐}$$"):
            st.write(df_9.head())
        if col2.button("$Missouri_{⭐⭐⭐⭐⭐}$$"):
            st.write(df_3.head())
        if col2.button("$Indiana_{⭐⭐⭐⭐⭐}$$"):
            st.write(df_.head())
        if col2.button("$Tennessee_{⭐⭐⭐⭐⭐}$$"):
            st.write(dfT.head())
        if col2.button("$Luisiana_{⭐⭐⭐⭐⭐}$$"):
            st.write(dfl.head())
        if col3.button("$Nevada_{⭐⭐⭐⭐⭐}$$"):
            st.write(dfn.head())
        if col3.button("$Idaho_{⭐⭐⭐⭐⭐}$$"):
            st.write(dfi.head())
        if col3.button("$Nueva\ Jersey_{⭐⭐⭐⭐⭐}$$"):
            st.write(dfnj.head())
        if col3.button("$Delaware_{⭐⭐⭐⭐⭐}$$"):
            st.write(dfd.head())
    if st.sidebar.checkbox("$The\ Best\ Ones$"):   
        if col1.button("$Arizona_{✅}$"):
            st.write(df_4.head())
        if col1.button("$California_{✅}$"):
            st.write(df_6.head())
        if col1.button("$Florida_{✅}$"):
            st.write(df_8.head())
        if col1.button("$Pensilvania_{✅}$"):
            st.write(df_1.head())
        if col2.button("$Missouri_{✅}$"):
            st.write(df_5.head())
        if col2.button("$Indiana_{✅}$"):
            st.write(df7_.head())
        if col2.button("$Tennessee_{✅}$"):
            st.write(dfL.head())
        if col2.button("$Luisiana_{✅}$"):
            st.write(dfL.head())
        if col3.button("$Nevada_{✅}$"):
            st.write(dfN.head())
        if col3.button("$Idaho_{✅}$"):
            st.write(dfI.head())
        if col3.button("$Nueva\ Jersey_{✅}$"):
            st.write(dfNJ.head())
        if col3.button("$Delaware_{✅}$"):
            st.write(dfD.head())

if selected == "Location":
    if st.sidebar.checkbox("$Map$"):
        if st.button("$World\ Map$"):
            st.map()
   
     


