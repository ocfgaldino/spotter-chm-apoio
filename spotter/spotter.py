import numpy as np
import plotly.express as px
from datetime import datetime
import pandas as pd 
from datetime import timezone
import plotly.graph_objects as go


def get_spotter_data(spt, start_date, end_date):
    
    spotter_data = spt.grab_data(
        limit=500,
        start_date=start_date,
        end_date=end_date,
        include_track=True,
        include_wind=True
    )
    
    return spotter_data



def plot_waves_hs(spt_waves):
    
    waves_hs = spt_waves[['timestamp', 'significantWaveHeight']]
    waves_hs.columns = ['DATA HORA', 'ALTURA SIGNIFICATIVA']
    
    wave_plot = px.line(waves_hs, x='DATA HORA', y="ALTURA SIGNIFICATIVA")
    wave_plot.update_traces(line=dict(color="Blue", width=2), marker=dict(size=4),mode="lines+markers") 
    wave_plot.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='LightPink')
    wave_plot.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='LightPink')
    
    return wave_plot


def plot_waves_tp(spt_waves):
    
    waves_tp = spt_waves[['timestamp', 'peakPeriod']]
    waves_tp.columns = ['DATA HORA', 'PERÍODO DE PICO']
    
    wave_plot = px.line(waves_tp, x='DATA HORA', y="PERÍODO DE PICO")
    wave_plot.update_traces(line=dict(color="Blue", width=2), marker=dict(size=4),mode="lines+markers") 
    wave_plot.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='LightPink')
    wave_plot.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='LightPink')
    
    return wave_plot
    
def plot_waves_wvdir(spt_waves):
    
    waves_tp = spt_waves[['timestamp', 'meanDirection']]
    waves_tp.columns = ['DATA HORA', 'DIREÇÃO MÉDIA DE ONDA']
    
    wave_plot = px.line(waves_tp, x='DATA HORA', y="DIREÇÃO MÉDIA DE ONDA")
    wave_plot.update_traces(line=dict(color="Blue", width=2), marker=dict(size=4),mode="lines+markers") 
    wave_plot.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='LightPink')
    wave_plot.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='LightPink')
    
    
    
    return wave_plot

def plot_waves_pkdir(spt_waves):
    
    waves_tp = spt_waves[['timestamp', 'peakDirection']]
    waves_tp.columns = ['DATA HORA', 'DIREÇÃO DE PICO DE ONDA']
    
    wave_plot = px.line(waves_tp, x='DATA HORA', y="DIREÇÃO DE PICO DE ONDA")
    wave_plot.update_traces(line=dict(color="Blue", width=2), marker=dict(size=4),mode="lines+markers") 
    wave_plot.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='LightPink')
    wave_plot.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='LightPink')
    
    return wave_plot


def df_time_interval(df):
    
    dt = datetime.utcnow()
    
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    
    df1 = df.copy()
    
    df1['timestamp'] = pd.to_datetime(df1['timestamp'])
    df1.sort_values(by="timestamp", inplace=True)
    
    df1['Intervalo de Tempo | HORAS'] = np.round(((df1['timestamp'].values.astype(np.int64) // 10 ** 9) - utc_timestamp)/3600,2)
    
    return df1
    
def plot_map_time(spt_waves, mapbox_token):
    
    config = {"responsive":True}
    
    
    spt_waves = df_time_interval(spt_waves)

    last_lat = float(spt_waves['latitude'].iloc[-1])
    last_lon = float(spt_waves['longitude'].iloc[-1])
    last_time = str(spt_waves['timestamp'].iloc[-1])
    
    
    fig = px.scatter_mapbox(spt_waves, lat="latitude", lon="longitude", color='Intervalo de Tempo | HORAS',
                  color_continuous_scale=["black", "purple", "red" ], size_max=30, zoom=14,
                  hover_data = {'latitude':True, 'longitude':True, 'timestamp':True, 'Intervalo de Tempo | HORAS':True},
                  height = 700, width = 800, #center = dict(lat = g.center)
                       # title='Histórico | Tempo trajetória',
                        mapbox_style="open-street-map"
                       )
    
    fig.update_layout(coloraxis_showscale=False)
    
    fig.update_traces(marker=dict(size=10), mode="markers+lines")
    
    
    fig.add_trace(go.Scattermapbox(
        lat=[last_lat],
        lon=[last_lon],
        mode='markers',
		name = 'Última Posição',
        marker=go.scattermapbox.Marker(
            size=18,
            color='rgb(255, 255, 0)',
			symbol = 'circle'
        ),
        showlegend=True,
        text = last_time,
        hoverinfo='text + lat + lon'
        
    ))
    
    fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
    ))
    
    fig.update_layout(font_size=16,  title={'xanchor': 'center','yanchor': 'top', 'y':0.9, 'x':0.5,}, 
        title_font_size = 24, mapbox_accesstoken=mapbox_token)

    
    
    return fig
    
    
    
    
        
    



    
    
        
    

    
    

