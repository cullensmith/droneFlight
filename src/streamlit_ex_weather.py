import streamlit as st
import pandas as pd

from weather import get_cell as cell, get_forecast as get_f

st.write('Hourly Forecast')

y,x = 39.7456,-97.0892
the_cell = cell(y,x)
forecast = pd.DataFrame(get_f(the_cell))
forecast.index = pd.to_datetime(forecast.startTime)

st.line_chart(forecast['temperature'])