import streamlit as st
import streamlit_book as stb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk 

st.title("Don't Forget Maps")
st.write('https://docs.streamlit.io/library/api-reference/charts/st.map')

st.markdown('## st.map')
st.code('st.map(data=None, zoom=None, use_container_width=True)', language='python')
chart_data = df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [42.35, -83.05], columns=['lat', 'lon'])
chartData = '''
df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])
'''
map = "st.map(df)"
st.code(chartData, language='python')
st.code(map, language='python')
st.map(df)
st.write('---')

st.markdown('## st.pydeck_chart')
pyDeckCode = '''
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [42.35, -83.05],
    columns=['lat', 'lon'])
st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=42.35,
         longitude=-83.05,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))
'''
st.code(pyDeckCode, language='python')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [42.35, -83.05],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=42.35,
         longitude=-83.05,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))