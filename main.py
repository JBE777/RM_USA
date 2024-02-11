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
df4 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Arizona")][["State","Name","Date","City","Address"]]
df_4 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Arizona")][["State","Name","Date","City","Address"]]
# California
df5 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="California")][["State","Name","Date","City","Address"]]
df6 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="California")][["State","Name","Date","City","Address"]]
df_6 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="California")][["State","Name","Date","City","Address"]]
# Florida
df7 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Florida")][["State","Name","Date","City","Address"]]
df8 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Florida")][["State","Name","Date","City","Address"]]
df_8 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Florida")][["State","Name","Date","City","Address"]]
# Pensilvania
df9 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Pensilvania")][["State","Name","Date","City","Address"]]
df_9 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Pensilvania")][["State","Name","Date","City","Address"]]
df_1 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Pensilvania")][["State","Name","Date","City","Address"]]
# Missouri
df_2 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Missouri")][["State","Name","Date","City","Address"]]
df_3 = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Missouri")][["State","Name","Date","City","Address"]]
df_5 = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Missouri")][["State","Name","Date","City","Address"]]
# Indiana
df_7 = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Indiana")][["State","Name","Date","City","Address"]]
df_  = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Indiana")][["State","Name","Date","City","Address"]]
df7_ = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Indiana")][["State","Name","Date","City","Address"]]
# Tennessee
df_t = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Tennessee")][["State","Name","Date","City","Address"]]
dft = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Tennessee")][["State","Name","Date","City","Address"]]
dfT = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Tennessee")][["State","Name","Date","City","Address"]]
# Luisiana
df_l = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Luisiana")][["State","Name","Date","City","Address"]]
dfl = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Luisiana")][["State","Name","Date","City","Address"]]
dfL = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Luisiana")][["State","Name","Date","City","Address"]]
# Nevada
df_n = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Nevada")][["State","Name","Date","City","Address"]]
dfn = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Nevada")][["State","Name","Date","City","Address"]]
dfN = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Nevada")][["State","Name","Date","City","Address"]]
# Idaho
df_i = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Idaho")][["State","Name","Date","City","Address"]]
dfi = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Idaho")][["State","Name","Date","City","Address"]]
dfI = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Idaho")][["State","Name","Date","City","Address"]]
# Nueva Jersey
df_nj = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Nueva Jersey")][["State","Name","Date","City","Address"]]
dfnj = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Nueva Jersey")][["State","Name","Date","City","Address"]]
dfNJ = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Nueva Jersey")][["State","Name","Date","City","Address"]]
# Delaware
df_d = rm_data[(rm_data["Stars"]==1)&(rm_data["Estado"]=="Delaware")][["State","Name","Date","City","Address"]]
dfd = rm_data[(rm_data["Stars"]==5)&(rm_data["Estado"]=="Delaware")][["State","Name","Date","City","Address"]]
dfD = rm_data[(rm_data["Valoracion"]=="Muy bueno")&(rm_data['Estado']=="Delaware")][["State","Name","Date","City","Address"]]  

col1,col2,col3,col4 = st.columns([2,2,2,2])

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Restaurants in USA", "Recomendations", 'System of recomendation'], 
       icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="vertical")
    selected

if selected == "Home":
    st.title("Welcome to my awesome data science project!")
    st.text("In this project I look into the transactions of mexican restaurants in USA ")
    st.image("Tacos.jpeg")

if selected == "Restaurants in USA":
    if st.sidebar.checkbox("$Dataset$"):
        st.success("$I\ found\ this\ dataset\ on\ Kaggle.com$")
        st.write(rm_data.head())
    if col2.button("$Mexican\ restaurants$"):
        dir_data_dist = pd.DataFrame(rm_data["Name"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)
    if col2.button("$States$"):
        dir_data_dist = pd.DataFrame(rm_data["Estado"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)
    if col2.button("$Cities$"):
        dir_data_dist = pd.DataFrame(rm_data["City"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)
    if col2.button("$Dates$"):
        dir_data_dist = pd.DataFrame(rm_data["Date"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)
    if col2.button("$Years$"):
        dir_data_dist = pd.DataFrame(rm_data["Year"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)
    if col2.button("$Quarters$"):
        dir_data_dist = pd.DataFrame(rm_data["Trimestre"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)
    if col2.button("$Stars$"):
        dir_data_dist = pd.DataFrame(rm_data["Stars"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)
    if col2.button("$Valoracion$"):
        dir_data_dist = pd.DataFrame(rm_data["Valoracion"].value_counts()).head(50)
        st.bar_chart(dir_data_dist)

if selected == "Recomendations":
    if st.sidebar.checkbox("$Top\ 5$"):
        if col2.button("$The\ best\ mexican\ restaurants\ in\ USA.$"):
            st.write(df.head())
        if col2.button("$5\ Stars\ mexican\ restaurants\ by\ state\ in\ USA.$"):
            st.write(df1.head())
        if col2.button("$1\ Star\ mexican\ restaurants\ by\ state\ in\ USA$"):
            st.write(df2.head())
    
if selected == 'System of recomendation':
    if st.sidebar.checkbox("$1\ Star\ mexican\ restaurants$"):
        if col1.button("$⭐_{Arizona}$"):
            st.write("$1\ Star\ Restaurants$", df3.head())
        if col2.button("$⭐_{California}$"):
            st.write("$1\ Star\ Restaurants$",df5.head())
        if col3.button("$⭐_{Florida}$"):
            st.write("$1\ Star\ Restaurants$",df7.head())
        if col1.button("$⭐_{Pensilvania}$"):
            st.write("$1\ Star\ Restaurants$",df9.head())
        if col2.button("$⭐_{Missouri}$"):
            st.write("$1\ Star\ Restaurants$",df_2.head())
        if col3.button("$⭐_{Indiana}$"):
            st.write("$1\ Star\ Restaurants$",df_7.head())
        if col1.button("$⭐_{Tennessee}$"):
            st.write("$1\ Star\ Restaurants$",df_t.head())
        if col2.button("$⭐_{Luisiana}$"):
            st.write("$1\ Star\ Restaurants$",df_l.head())
        if col3.button("$⭐_{Nevada}$"):
            st.write("$1\ Star\ Restaurants$",df_n.head())
        if col1.button("$⭐_{Idaho}$"):
            st.write("$1\ Star\ Restaurants$",df_i.head())
        if col2.button("$⭐_{Nueva\ Jersey}$"):
            st.write("$1\ Star\ Restaurants$",df_nj.head())
        if col3.button("$⭐_{Delaware}$"):
            st.write("$1\ Star\ Restaurants$",df_d.head())
    if st.sidebar.checkbox("$5\ Stars\ mexican\ restaurants$"):
        if col1.button("$5⭐_{Arizona}$"):
            st.write("$5\ Stars\ Restaurants$", df4.head())
        if col2.button("$5⭐_{California}$"):
            st.write("$5\ Stars\ Restaurants$",df6.head())
        if col3.button("$5⭐_{Florida}$"):
            st.write("$5\ Stars\ Restaurants$",df8.head())
        if col1.button("$5⭐_{Pensilvania}$"):
            st.write("$5\ Stars\ Restaurants$",df_9.head())
        if col2.button("$5⭐_{Missouri}$"):
            st.write("$5\ Stars\ Restaurants$",df_3.head())
        if col3.button("$5⭐_{Indiana}$"):
            st.write("$5\ Stars\ Restaurants$",df_.head())
        if col1.button("$5⭐_{Tennessee}$"):
            st.write("$5\ Stars\ Restaurants$",dfT.head())
        if col2.button("$5⭐_{Luisiana}$"):
            st.write("$5\ Stars\ Restaurants$",dfl.head())
        if col3.button("$5⭐_{Nevada}$"):
            st.write("$5\ Stars\ Restaurants$",dfn.head())
        if col1.button("$5⭐_{Idaho}$"):
            st.write("$5\ Stars\ Restaurants$",dfi.head())
        if col2.button("$5⭐_{Nueva\ Jersey}$"):
            st.write("$5\ Stars\ Restaurants$",dfnj.head())
        if col3.button("$5⭐_{Delaware}$"):
            st.write("$5\ Stars\ Restaurants$",dfd.head())
    if st.sidebar.checkbox("$The\ best\ mexican\ restaurants$"):    
        if col1.button("$✅_{Arizona}$"): 
            st.write("$The\ best\ restaurants$",df_4.head())
        if col2.button("$✅_{California}$"):
            st.write("$The\ best\ restaurants$",df_6.head())
        if col3.button("$✅_{Florida}$"):
            st.write("$The\ best\ restaurants$",df_8.head())
        if col1.button("$✅_{Pensilvania}$"):
            st.write("$The\ best\ restaurants$",df_1.head())
        if col2.button("$✅_{Missouri}$"):
            st.write("$The\ best\ restaurants$",df_5.head())
        if col3.button("$✅_{Indiana}$"):
            st.write("$The\ best\ restaurants$",df7_.head())
        if col1.button("$✅_{Tennessee}$"):
            st.write("$The\ best\ restaurants$",dfL.head())
        if col2.button("$✅_{Luisiana}$"):
            st.write("$The\ best\ restaurants$",dfL.head())
        if col3.button("$✅_{Nevada}$"):
            st.write("$The\ best\ restaurants$",dfN.head())
        if col1.button("$✅_{Idaho}$"):
            st.write("$The\ best\ restaurants$",dfI.head())
        if col2.button("$✅_{Nueva\ Jersey}$"):
            st.write("$The\ best\ restaurants$",dfNJ.head())
        if col3.button("$✅_{Delaware}$"):
            st.write("$The\ best\ restaurants$",dfD.head())




    