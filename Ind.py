import json
import pandas as pd
import plotly.express as px
import numpy as np

india_states = json.load(open('states_india.geojson', 'r'))

state_id_map = {}

for feature in india_states['features']:
    feature['id'] = feature['properties']['state_code']
    state_id_map[feature['properties']['st_nm']] = feature['id']
    
df = pd.read_csv('india_census.csv')
df['Density'] = df['Density[a]'].apply(lambda x: int(x.split('/')[0].replace(',','')))
df['id'] = df['State or union territory'].apply(lambda x: state_id_map[x])

df['Log Scale Density'] = np.log10(df['Density'])

fig = px.choropleth(df,
                    locations = 'id',
                    geojson = india_states,
                    color = 'Log Scale Density',
                    hover_name = 'State or union territory',
                    hover_data = ['Density'],
                    title = 'India Population Density 2011')
fig.update_geos(fitbounds = 'locations', visible = False)
fig.show()