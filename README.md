# Diagrama de Bode de um Filtro RLC Série

Este projeto implementa uma aplicação web interativa utilizando [Streamlit](https://streamlit.io/) para calcular e exibir o diagrama de Bode (magnitude e fase) de um filtro RLC série. O usuário pode ajustar os parâmetros do circuito (resistência, indutância, capacitância) e visualizar os gráficos gerados dinamicamente.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework para criação de aplicações web interativas em Python.
- **NumPy**: Biblioteca para cálculos matemáticos e manipulação de arrays.
- **Plotly**: Biblioteca para criação de gráficos interativos.
- **SciPy**: Utilizada para o cálculo da resposta em frequência do sistema RLC.

## Funcionalidades

- Interface gráfica para ajuste dinâmico de parâmetros do filtro RLC (resistência, indutância, capacitância).
- Seleção da frequência base do sistema.
- Cálculo da resposta em frequência (magnitude e fase) utilizando a função de transferência do sistema.
- Exibição dos gráficos do diagrama de Bode (magnitude e fase) utilizando a biblioteca Plotly.

## Como Executar

Antes de executar o código, certifique-se de que você tem as bibliotecas Python necessárias instaladas. Você pode instalá-las executando o seguinte comando:

```bash
pip install streamlit numpy plotly scipy
```

Para executar o aplicativo, siga os seguintes passos:

1. Clone este repositório.
2. Navegue até o diretório do projeto.
3. Execute o seguinte comando no terminal:

```bash
streamlit run app.py
```

4. O aplicativo será aberto no navegador padrão, onde você poderá ajustar os parâmetros do circuito e visualizar o diagrama de Bode.

## Estrutura do Código

### 1. Configuração da Interface Streamlit

O layout do Streamlit é configurado com um título principal e uma barra lateral que permite ao usuário ajustar os parâmetros do filtro RLC:

```python
st.title("Diagrama de Bode de um Filtro RLC Série")
st.sidebar.header("Parâmetros do Filtro RLC")
```

### 2. Definição dos Parâmetros do Circuito

Os parâmetros do circuito (frequência, resistência, indutância e capacitância) são definidos utilizando sliders e comboboxes na barra lateral:

```python
frequencia = st.sidebar.selectbox("Frequência (Hz)", options=[50, 60], index=0)
R = st.sidebar.slider("Resistência (Ohm)", min_value=1e-3, max_value=1.0, value=0.1, step=1e-3, format="%0.3f")
L = st.sidebar.slider("Indutância (mH)", min_value=0.1, max_value=500.0, value=100.0, step=0.1, format="%0.1f")
C = st.sidebar.slider("Capacitância (µF)", min_value=1.0, max_value=100.0, value=10.0, step=1.0, format="%0.1f")
```

### 3. Conversão dos Parâmetros

Os valores de indutância e capacitância são convertidos para as unidades corretas (Henry e Farad) para os cálculos:

```python
L = L * 1e-3  # mH to H
C = C * 1e-6  # µF to F
```

### 4. Definição da Função de Transferência

A função de transferência do filtro RLC série é definida utilizando o módulo `signal` da biblioteca `scipy`. A função de transferência depende dos parâmetros do circuito, e é calculada da seguinte forma:

```python
den = [C, 0]
num = [L * C, R * C, 1]
system = signal.TransferFunction(num, den)
```

### 5. Cálculo da Resposta em Frequência

A resposta em frequência (magnitude e fase) é calculada utilizando a função `bode` da biblioteca `scipy`:

```python
w, mag, phase = signal.bode(system, w=w)
```

### 6. Plotagem dos Gráficos

Dois gráficos são gerados para exibir a magnitude e a fase do diagrama de Bode. Utilizamos a biblioteca Plotly para gerar gráficos interativos:

- **Gráfico de Magnitude**:

  ```python
  y = 10**(mag / 20)
  fig_mag = go.Figure()
  fig_mag.add_trace(go.Scatter(x=frequencies, y=y, mode='lines', name='Magnitude'))
  fig_mag.update_layout(title='Diagrama de Bode - Magnitude',
                        xaxis_title='Frequência (Hz)',
                        yaxis_title='Magnitude',
                        yaxis_range=[0, y[0]],
                        template='plotly_dark')
  ```

- **Gráfico de Fase**:

  ```python
  fig_phase = go.Figure()
  fig_phase.add_trace(go.Scatter(x=frequencies, y=phase, mode='lines', name='Fase (graus)'))
  fig_phase.update_layout(title='Diagrama de Bode - Fase',
                          xaxis_title='Frequência (Hz)',
                          yaxis_title='Fase (graus)',
                          template='plotly_dark')
  ```

### 7. Exibição dos Gráficos no Streamlit

Os gráficos são exibidos diretamente na página do Streamlit utilizando o método `st.plotly_chart`:

```python
st.plotly_chart(fig_mag)
st.plotly_chart(fig_phase)
```

## Como Contribuir

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo `LICENSE` para mais informações.
```

Este arquivo de `README.md` fornece uma descrição detalhada do projeto, instruções de execução e uma visão geral do código, sendo útil para quem deseja entender ou contribuir para o projeto.

