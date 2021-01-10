import pandas as pd
import numpy as np
import altair as alt
import yfinance as yf
import streamlit as st
import time 
import plotly.graph_objects as go

col1, col2= st.beta_columns(2)


with col1:
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
  # Update the progress bar with each iteration.
        latest_iteration.text(f'Gerando ... {i+1} %')
        bar.progress(i + 1)
        time.sleep(0.1)
    st.write("""
           # Simple Stock Price App
            Shown are the stock **closing price** and ***volume*** of Google!
            """)
    pressed = col1.button('Press me?')
    if pressed:
        col2.write("Woohoo!")

    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some really, really long explanations...")


    # https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
    #define the ticker symbol
    tickerSymbol = 'GOOGL'
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2020-12-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    ######################################################
    # Exemplos de graficos que tem na biblioteca yfinance#
    ######################################################
    st.write("""
        ## Closing Price
        """)
    st.area_chart(tickerDf.Close)
    st.write("""
        ## Volume Price
        """)
    st.area_chart(tickerDf.Volume)

with col2:
    ######################################################
    #>>>>>>>>>>>>>> Exemplos de latex <<<<<<<<<<<<<<<<<<<#
    ######################################################
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')
    #######################################################



    ######################################################
    #>>>> Exemplo de pandas e outras bibliotecas <<<<<<<<#
    ######################################################

    #datraframe
    df = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])

    #grafico
    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.write(c)
    ########################################################

    fig = go.Figure(data=go.Bar(y=[2, 3, 1]))

    st.write(fig)

    ##################################################


#col1, col2, col3, col4  = st.beta_columns(4)

#original = Image.open(image)
#col1.header("Original")
#col1.image(original, use_column_width=True)

#grayscale = original.convert('LA')
#col2.header("Grayscale")
#col2.image(grayscale, use_column_width=True)