import os 

import pandas as pd 
from PIL import Image
from datetime import datetime
from datetime import timedelta
from dotenv import load_dotenv
import plotly.express as px
import streamlit as st 
import streamlit_authenticator as stauth
import folium
from pysofar.sofar import SofarApi
from spotter.spotter import get_spotter_data, plot_waves_hs, plot_waves_tp, plot_waves_wvdir, plot_waves_pkdir,plot_map_time


load_dotenv()


import streamlit as st

mb = Image.open("images/favicon.ico")

hashed_passwords = stauth.hasher([os.environ["password"]]).generate()

st.set_page_config(layout="wide", page_title = "Boia Spotter CHM", page_icon=mb)

authenticator = stauth.authenticate([os.environ["user_full_name"]],[os.environ["username"]],hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status = authenticator.login('Login','main')


if authentication_status:
    
    api = SofarApi()

    spotter_id = "SPOT-0745"
    mapbox_token = "pk.eyJ1Ijoib2NmZ2FsZGlubyIsImEiOiJja2ZieDh3MjQwdnRzMnFxZXNjbHVpaWhjIn0.cqPgkudLwvydJThx9eGBgw"

    spotter_grid = api.get_spotters()

    spt = spotter_grid[1]

    date_now = datetime.utcnow()
    start_date = date_now - timedelta(days=5)

    spotter_data = get_spotter_data(spt, start_date, date_now)

    # wavedf 
    

    waves = pd.json_normalize(spotter_data, record_path="waves")
    wind = pd.json_normalize(spotter_data, record_path="wind")
    
    waves = waves[["timestamp", "latitude", "longitude", "significantWaveHeight", "peakPeriod", "meanDirection", "peakDirection"]]
    
    date_time = pd.to_datetime(waves['timestamp'])
    
    last_time = datetime.strftime(date_time.iloc[-1], format = "%Y-%m-%d %H:%M")
    last_hs = float(waves['significantWaveHeight'].iloc[-1])
    last_tp = float(waves['peakPeriod'].iloc[-1])
    last_wvdir = float(waves['meanDirection'].iloc[-1])
    
    last_wspd = float(wind['speed'].iloc[-1])
    last_wdir = float(wind['direction'].iloc[-1])
    
    
    st.write('Olá *%s*' % (name))
    st.markdown("### Sistema desenvolvido pelo Centro de Hidrografia da Marinha - Oceanografia Operacional")
    st.title('Sistema de Ondas em Tempo Real')
    
    
    
    
    c1, c2, c3, c4, c5, c6 = st.columns((1,1,1,1,1,1))
    
    c1.metric("Último dado", last_time)
    c2.metric("Hs", str(last_hs) + " m")
    c3.metric("Tp", str(last_tp) + " s")
    c4.metric("Direção Onda", str(round(last_wvdir,1)) + " °")
    c5.metric("Velocidade Vento", str(round(last_wspd,1)) + " m/s")
    c6.metric("Direção Vento", str(last_wdir) + " °")
    
    
    c7, c8 = st.columns(2)
    
    c7.plotly_chart(plot_map_time(waves, mapbox_token), use_container_width=True)
    c8.dataframe(waves, height = 600)
    
    

    
    
    col3, col4 = st.columns(2)
    col3.header("Altura Significativa (Hs)")
    col3.plotly_chart(plot_waves_hs(waves))
    
    col4.header("Período de Pico (Tp)")
    col4.plotly_chart(plot_waves_tp(waves))
    
    col5, col6 = st.columns(2)
    col5.header("Direção Média de Onda")
    col5.plotly_chart(plot_waves_wvdir(waves))
    
    col6.header("Pico da Direção de Onda")
    col6.plotly_chart(plot_waves_pkdir(waves))
    
  #  st.write("Vento*")
   # st.table(wind)
    
elif authentication_status == False:
    st.error('Usuário/Senha incorreta')
elif authentication_status == None:
    st.warning('Por favor, digite seu usuário e senha.')
    
    

    
    
