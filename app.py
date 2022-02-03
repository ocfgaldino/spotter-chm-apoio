import os 

import pandas as pd 

from datetime import datetime
from datetime import timedelta
from dotenv import load_dotenv
import plotly.express as px
import streamlit as st 
import streamlit_authenticator as stauth
from pysofar.sofar import SofarApi
from spotter.spotter import get_spotter_data, plot_waves_hs, plot_waves_tp


load_dotenv()


api = SofarApi()

spotter_id = "SPOT-0745"

spotter_grid = api.get_spotters()

spt = spotter_grid[1]

date_now = datetime.utcnow()
start_date = date_now - timedelta(days=5)

spotter_data = get_spotter_data(spt, start_date, date_now)

# wavedf 

waves = pd.json_normalize(spotter_data, record_path="waves")
wind = pd.json_normalize(spotter_data, record_path="wind")


hashed_passwords = stauth.hasher(os.getenv("password")).generate()

st.set_page_config(layout="wide")

authenticator = stauth.authenticate(os.getenv("user_full_name"),os.getenv("username"),hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status = authenticator.login('Login','main')


if authentication_status:
    
    
    
    st.write('Olá *%s*' % (name))
    st.markdown("### Sistema desenvolvido pelo Centro de Hidrografia da Marinha - Oceanografia Operacional")
    st.title('Sistema de Ondas em Tempo Real')
    
    
    col3, col4 = st.columns(2)
    col3.header("Altura Significativa (Hs)")
    col3.plotly_chart(plot_waves_hs(waves))
    
    col4.header("Período de Pico (Tp)")
    col4.plotly_chart(plot_waves_tp(waves))
    
  #  st.write("Vento*")
   # st.table(wind)
    
elif authentication_status == False:
    st.error('Usuário/Senha incorreta')
elif authentication_status == None:
    st.warning('Por favor, digite seu usuário e senha.')
    
    

    
    
