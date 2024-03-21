import streamlit as st
import ee
import geemap.foliumap as geemap
from google.oauth2 import service_account
from ee import oauth

st.title("IFAD Earth Engine Web App")

credentials = service_account.Credentials.from_service_account_info(st.secrets, scopes=oauth.SCOPES) 
ee.Initialize(credentials)

m = geemap.Map()
m.add_basemap("OpenTopoMap")
dataset_mig = ee.ImageCollection('projects/sat-io/open-datasets/GLC-FCS30D/annual')
m.addLayer(dataset_mig, {}, 'projects/sat-io/open-datasets/GLC-FCS30D/annual')
m.to_streamlit(height=500)
