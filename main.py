import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import signal


# Configuração do layout do Streamlit
st.title("Diagrama de Bode de um Filtro RLC Série")
st.sidebar.header("Parâmetros do Filtro RLC")

# Combobox para selecionar a frequência
frequencia = st.sidebar.selectbox("Frequência (Hz)", options=[50, 60], index=0)

# Sliders para os valores do circuito
R = st.sidebar.slider("Resistência (Ohm)", min_value=1e-3, max_value=1.0, value=0.1, step=1e-3, format="%0.3f")
L = st.sidebar.slider("Indutância (mH)", min_value=0.1, max_value=500.0, value=100.0, step=0.1, format="%0.1f")
C = st.sidebar.slider("Capacitância (µF)", min_value=1.0, max_value=100.0, value=10.0, step=1.0, format="%0.1f")

# Conversão dos valores
L = L * 1e-3  # mH to H
C = C * 1e-6  # µF to F

# Frequências para o cálculo
frequencies = np.arange(frequencia, 10*frequencia, frequencia/1000)  # Frequências de 10 Hz a 1 MHz
w = 2 * np.pi * frequencies  # Frequência angular

# Função de transferência da impedância do filtro RLC série
den = [C, 0]
num = [L * C, R * C, 1]
system = signal.TransferFunction(num, den)

# Cálculo da resposta em frequência
w, mag, phase = signal.bode(system, w=w)

# Gráficos com Plotly
y=10**(mag / 20)
print(y[0])
fig_mag = go.Figure()
fig_mag.add_trace(go.Scatter(x=frequencies, y=y, mode='lines', name='Magnitude'))
fig_mag.update_layout(title='Diagrama de Bode - Magnitude',
                      xaxis_title='Frequência (Hz)',
                      yaxis_title='Magnitude',
                      yaxis_range=[0, y[0]],
                      template='plotly_dark')

fig_phase = go.Figure()
fig_phase.add_trace(go.Scatter(x=frequencies, y=phase, mode='lines', name='Fase (graus)'))
fig_phase.update_layout(title='Diagrama de Bode - Fase',
                        xaxis_title='Frequência (Hz)',
                        yaxis_title='Fase (graus)',
                        template='plotly_dark')

# Exibindo os gráficos
st.plotly_chart(fig_mag)
st.plotly_chart(fig_phase)
