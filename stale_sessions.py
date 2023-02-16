
import getpass
import pandas as pd
import getpass
import re
from netmiko import ConnectHandler
import streamlit as st

passwordGet=getpass.getpass()
pano = ConnectHandler(device_type='paloalto_panos', ip="10.x.x.x", username="user", password=passwordGet)
pano.send_command("set cli config-output-format json")
out= pano.send_command("show session all filter min-age 300")


sliced = out[338:]
data = (sliced)
data=re.sub("\s+", ",", data.strip())
x = data.split(",")
print(x)
i=0
temp_list=[]
df=pd.DataFrame(columns = ["ID","Application","State","Type","Src[Sport]/Zone/Proto","(translated IP[Port])","Vsys","Dst[Dport]/Zone (translated IP[Port])","Dst[Dport]/Zone (translated IP[Port])"])
liztlength=len(x)
tempI=0
while i<liztlength:
    while tempI<=8 and i<liztlength:
        temp_list.append(x[i])
        i=i+1
        tempI=tempI+1  
    try:
        if df.empty:
            df.loc[0] = temp_list
        else:
            df_length = len(df)
            df.loc[df_length] = temp_list
        tempI=0
        temp_list=[]
    except:
        print(str(temp_list)+"could not be appended")
df.to_csv('stale.csv')

data = st.cache(pd.read_csv) (r'C:\Users\user\Downloads\stale.csv',nrows=1000)

# Select some rows using st.multiselect. This will break down when you have >1000 rows.
st.write('### Full Dataset', data)
selected_indices = st.multiselect('Select rows:', data.index)
print(type(data))
selected_rows = data.loc[selected_indices]
st.write('### Selected Rows', selected_rows)
if st.button('Clear sessions'):
    st.write('Clearing Sessions')
    for item in selected_rows["ID"]:
        #where you input your clear session command
        #pano.send_command(f"clear session id {item}")
        st.write(item)
else:
    pass    
if st.button('Close SSH'):
    st.write('Closing SSH')
    pano.disconnect()
