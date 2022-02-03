import plotly.express as px

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
    
    return wave_plot


def plot_waves_tp(spt_waves):
    
    waves_tp = spt_waves[['timestamp', 'peakPeriod']]
    waves_tp.columns = ['DATA HORA', 'PERÍODO DE PICO']
    
    wave_plot = px.line(waves_tp, x='DATA HORA', y="PERÍODO DE PICO")
    
    return wave_plot
    
def plot_waves_wvdir(spt_waves):
    
    waves_tp = spt_waves[['timestamp', 'meanDirection']]
    waves_tp.columns = ['DATA HORA', 'DIREÇÃO MÉDIA DE ONDA']
    
    wave_plot = px.line(waves_tp, x='DATA HORA', y="DIREÇÃO MÉDIA DE ONDA")
    
    return wave_plot

def plot_waves_pkdir(spt_waves):
    
    waves_tp = spt_waves[['timestamp', 'peakDirection']]
    waves_tp.columns = ['DATA HORA', 'DIREÇÃO DE PICO DE ONDA']
    
    wave_plot = px.line(waves_tp, x='DATA HORA', y="DIREÇÃO DE PICO DE ONDA")
    
    return wave_plot
    
    
    
    
        
    



    
    
        
    

    
    

