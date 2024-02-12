import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

rm_data = pd.read_csv('dataset_stream.csv')
# System of recomendation
df = rm_data[(rm_data["Valoracion"]=="Muy bueno")][["State","Name","Date","City","Address","Estado"]]
df1 = rm_data[(rm_data["Stars"]==5)][["State","Name","Date","City","Address","Estado"]]
df2 = rm_data[(rm_data["Stars"]==1)][["State","Name","Date","City","Address","Estado"]]
# Arizona
df3 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Arizona")][["State","Name","Date","City","Address"]]
df3_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Arizona")][["State","Name","Date","City","Address"]]
df3_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Arizona")][["State","Name","Date","City","Address"]]
df3_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Arizona")][["State","Name","Date","City","Address"]]
df4 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Arizona")][["State","Name","Date","City","Address"]]
df_4 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Arizona")][["State","Name","Date","City","Address"]]
# California
df5 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="California")][["State","Name","Date","City","Address"]]
df5_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="California")][["State","Name","Date","City","Address"]]
df5_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="California")][["State","Name","Date","City","Address"]]
df5_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="California")][["State","Name","Date","City","Address"]]
df6 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="California")][["State","Name","Date","City","Address"]]
df_6 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="California")][["State","Name","Date","City","Address"]]
# Florida
df7 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Florida")][["State","Name","Date","City","Address"]]
df7_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Florida")][["State","Name","Date","City","Address"]]
df7_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Florida")][["State","Name","Date","City","Address"]]
df7_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Florida")][["State","Name","Date","City","Address"]]
df8 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Florida")][["State","Name","Date","City","Address"]]
df_8 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Florida")][["State","Name","Date","City","Address"]]
# Pensilvania
df9 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Pensilvania")][["State","Name","Date","City","Address"]]
df9_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Pensilvania")][["State","Name","Date","City","Address"]]
df9_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Pensilvania")][["State","Name","Date","City","Address"]]
df9_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Pensilvania")][["State","Name","Date","City","Address"]]
df_9 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Pensilvania")][["State","Name","Date","City","Address"]]
df_1 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Pensilvania")][["State","Name","Date","City","Address"]]
# Missouri
df_2 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Missouri")][["State","Name","Date","City","Address"]]
df_2_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Missouri")][["State","Name","Date","City","Address"]]
df_2_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Missouri")][["State","Name","Date","City","Address"]]
df_2_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Missouri")][["State","Name","Date","City","Address"]]
df_3 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Missouri")][["State","Name","Date","City","Address"]]
df_5 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Missouri")][["State","Name","Date","City","Address"]]
# Indiana
df_7 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Indiana")][["State","Name","Date","City","Address"]]
df_7_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Indiana")][["State","Name","Date","City","Address"]]
df_7_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Indiana")][["State","Name","Date","City","Address"]]
df_7_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Indiana")][["State","Name","Date","City","Address"]]
df_  = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Indiana")][["State","Name","Date","City","Address"]]
df7_ = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Indiana")][["State","Name","Date","City","Address"]]
# Tennessee
df_t = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Tennessee")][["State","Name","Date","City","Address"]]
df_t_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Tennessee")][["State","Name","Date","City","Address"]]
df_t_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Tennessee")][["State","Name","Date","City","Address"]]
df_t_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Tennessee")][["State","Name","Date","City","Address"]]
dft = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Tennessee")][["State","Name","Date","City","Address"]]
dfT = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Tennessee")][["State","Name","Date","City","Address"]]
# Luisiana
df_l = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Luisiana")][["State","Name","Date","City","Address"]]
df_l_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Luisiana")][["State","Name","Date","City","Address"]]
df_l_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Luisiana")][["State","Name","Date","City","Address"]]
df_l_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Luisiana")][["State","Name","Date","City","Address"]]
dfl = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Luisiana")][["State","Name","Date","City","Address"]]
dfL = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Luisiana")][["State","Name","Date","City","Address"]]
# Nevada
df_n = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Nevada")][["State","Name","Date","City","Address"]]
df_n_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Nevada")][["State","Name","Date","City","Address"]]
df_n_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Nevada")][["State","Name","Date","City","Address"]]
df_n_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Nevada")][["State","Name","Date","City","Address"]]
dfn = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Nevada")][["State","Name","Date","City","Address"]]
dfN = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Nevada")][["State","Name","Date","City","Address"]]
# Idaho
df_i = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Idaho")][["State","Name","Date","City","Address"]]
df_i_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Idaho")][["State","Name","Date","City","Address"]]
df_i_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Idaho")][["State","Name","Date","City","Address"]]
df_i_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Idaho")][["State","Name","Date","City","Address"]]
dfi = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Idaho")][["State","Name","Date","City","Address"]]
dfI = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Idaho")][["State","Name","Date","City","Address"]]
# Nueva Jersey
df_nj = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Nueva Jersey")][["State","Name","Date","City","Address"]]
df_nj_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Nueva Jersey")][["State","Name","Date","City","Address"]]
df_nj_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Nueva Jersey")][["State","Name","Date","City","Address"]]
df_nj_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Nueva Jersey")][["State","Name","Date","City","Address"]]
dfnj = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Nueva Jersey")][["State","Name","Date","City","Address"]]
dfNJ = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Nueva Jersey")][["State","Name","Date","City","Address"]]
# Delaware
df_d = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Delaware")][["State","Name","Date","City","Address"]]
df_d_a = rm_data[(rm_data["Stars"]==2)&(rm_data["Estado"]=="Delaware")][["State","Name","Date","City","Address"]]
df_d_b = rm_data[(rm_data["Stars"]==3)&(rm_data["Estado"]=="Delaware")][["State","Name","Date","City","Address"]]
df_d_c = rm_data[(rm_data["Stars"]==4)&(rm_data["Estado"]=="Delaware")][["State","Name","Date","City","Address"]]
dfd = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Delaware")][["State","Name","Date","City","Address"]]
dfD = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Delaware")][["State","Name","Date","City","Address"]]
# Maps
data = rm_data[["Latitude","Longitude"]]
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
        st.write(rm_data.head()) 
    if col2.button("$⭐_{Stars}$"):
        dir_data_dist = pd.DataFrame(rm_data["Stars"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)
    if col2.button("$🌮_{Valoracion}$"):
        dir_data_dist = pd.DataFrame(rm_data["Valoracion"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)

if selected == "Recomendations":
    if st.sidebar.checkbox("$Top\ 5\ mexican\ restaurants\ in\ USA$"):
        if col2.button("$The\ Best\ Ones$"):
            st.write(df.head())
        if col2.button("$⭐⭐⭐⭐⭐\ Stars$"):
            st.write(df1.head())
        if col2.button("$⭐\ Star$"):
            st.write(df2.head())
    
if selected == 'System of recomendation':
    if st.sidebar.checkbox("Mexican restaurants"):
        if st.sidebar.checkbox("$⭐\ Star$"):
            if col1.button("$Arizona$"):
                st.write(df3.head())
            if col1.button("$California$"):
                st.write(df5.head())
            if col1.button("$Florida$"):
                st.write(df7.head())
            if col1.button("$Pensilvania$"):
                st.write(df9.head())
            if col2.button("$Missouri$"):
                st.write(df_2.head())
            if col2.button("$Indiana$"):
                st.write(df_7.head())
            if col2.button("$Tennessee$"):
                st.write(df_t.head())
            if col2.button("$Luisiana$"):
                st.write(df_l.head())
            if col3.button("$Nevada$"):
                st.write(df_n.head())
            if col3.button("$Idaho$"):
                st.write(df_i.head())
            if col3.button("$Nueva\ Jersey$"):
                st.write(df_nj.head())
            if col3.button("$Delaware$"):
                st.write(df_d.head())
        if st.sidebar.checkbox("$⭐\ ⭐\ Stars$"):
            if col1.button("$Arizona$"):
                st.write(df3_a.head()) 
            if col1.button("$California$"):
                st.write(df5_a.head())
            if col1.button("$Florida$"):
                st.write(df7_a.head())
            if col1.button("$Pensilvania$"):
                st.write(df9_a.head())
            if col2.button("$Missouri$"):
                st.write(df_2_a.head())
            if col2.button("$Indiana$"):
                st.write(df_7_a.head())
            if col2.button("$Tennessee$"):
                st.write(df_t_a.head())
            if col2.button("$Luisiana$"):
                st.write(df_l_a.head())
            if col3.button("$Nevada$"):
                st.write(df_n_a.head())
            if col3.button("$Idaho$"):
                st.write(df_i_a.head())
            if col3.button("$Nueva\ Jersey$"):
                st.write(df_nj_a.head())
            if col3.button("$Delaware$"):
                st.write(df_d_a.head())
        if st.sidebar.checkbox("$⭐\ ⭐\ ⭐\ Stars$"):
            if col1.button("$Arizona$"):
                st.write(df3_b.head()) 
            if col1.button("$California$"):
                st.write(df5_b.head()) 
            if col1.button("$Florida$"):
                st.write(df7_b.head())
            if col1.button("$Pensilvania$"):
                st.write(df9_b.head())
            if col2.button("$Missouri$"):
                st.write(df_2_b.head())
            if col2.button("$Indiana$"):
                st.write(df_7_b.head())
            if col2.button("$Tennessee$"):
                st.write(df_t_b.head())
            if col2.button("$Luisiana$"):           
                st.write(df_l_b.head())
            if col3.button("$Nevada$"):
                st.write(df_n_b.head())
            if col3.button("$Idaho$"):
                st.write(df_i_b.head())
            if col3.button("$Nueva\ Jersey$"):
                st.write(df_nj_b.head())
            if col3.button("$Delaware$"):
                st.write(df_d_b.head())
        if st.sidebar.checkbox("$⭐\ ⭐\ ⭐\ ⭐\ Stars$"):
            if col1.button("$Arizona$"):
                st.write(df3_c.head())  
            if col1.button("$California$"):
                st.write(df5_c.head()) 
            if col1.button("$Florida$"):
                st.write(df7_c.head()) 
            if col1.button("$Pensilvania$"):
                st.write(df9_c.head())
            if col2.button("$Missouri$"):
                st.write(df_2_c.head())
            if col2.button("$Indiana$"):
                st.write(df_7_c.head())
            if col2.button("$Tennessee$"):
                st.write(df_t_c.head())
            if col2.button("$Luisiana$"):
                st.write(df_l_c.head())
            if col3.button("$Nevada$"):
                st.write(df_n_c.head())
            if col3.button("$Idaho$"):
                st.write(df_i_c.head())
            if col3.button("$Nueva\ Jersey$"):
                st.write(df_nj_c.head())
            if col3.button("$Delaware$"):
                st.write(df_d_c.head())
        if st.sidebar.checkbox("$⭐\ ⭐\ ⭐\ ⭐\ ⭐\ Stars$"):
            if col1.button("$Arizona$"):
                st.write(df4.head())
            if col1.button("$California$"):
                st.write(df6.head())
            if col1.button("$Florida$"):
                st.write(df8.head())
            if col1.button("$Pensilvania$"):
                st.write(df_9.head())
            if col2.button("$Missouri$"):
                st.write(df_3.head())
            if col2.button("$Indiana$"):
                st.write(df_.head())
            if col2.button("$Tennessee$"):
                st.write(dfT.head())
            if col2.button("$Luisiana$"):
                st.write(dfl.head())
            if col3.button("$Nevada$"):
                st.write(dfn.head())
            if col3.button("$Idaho$"):
                st.write(dfi.head())
            if col3.button("$Nueva\ Jersey$"):
                st.write(dfnj.head())
            if col3.button("$Delaware$"):
                st.write(dfd.head())
        if st.sidebar.checkbox("$The\ Best\ Ones$"):   
            if col1.button("$Arizona$"):
                st.write(df_4.head())
            if col1.button("$California$"):
                st.write(df_6.head())
            if col1.button("$Florida$"):
                st.write(df_8.head())
            if col1.button("$Pensilvania$"):
                st.write(df_1.head())
            if col2.button("$Missouri$"):
                st.write(df_5.head())
            if col2.button("$Indiana$"):
                st.write(df7_.head())
            if col2.button("$Tennessee$"):
                st.write(dfL.head())
            if col2.button("$Luisiana$"):
                st.write(dfL.head())
            if col3.button("$Nevada$"):
                st.write(dfN.head())
            if col3.button("$Idaho$"):
                st.write(dfI.head())
            if col3.button("$Nueva\ Jersey$"):
                st.write(dfNJ.head())
            if col3.button("$Delaware$"):
                st.write(dfD.head())
if selected == "Location":
    if st.sidebar.checkbox("$Food$"):
        if st.button("$World\ Map$"):
            st.map()
        if st.button("$Mexican\ food\ in\ USA$"):
            dir_data_dist = pd.DataFrame(rm_data["Name"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if st.button("$States\ in\ USA$"):
            dir_data_dist = pd.DataFrame(rm_data["Estado"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if st.button("$Cities\ in\ USA$"):
            dir_data_dist = pd.DataFrame(rm_data["City"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if st.button("$Dates$"):
            dir_data_dist = pd.DataFrame(rm_data["Date"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if st.button("$Years$"):
            dir_data_dist = pd.DataFrame(rm_data["Year"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)
        if st.button("$Quarters$"):
            dir_data_dist = pd.DataFrame(rm_data["Trimestre"].value_counts()).head(50)
            st.bar_chart(dir_data_dist)


    