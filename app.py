import streamlit as st
import ee
import geemap.foliumap as geemap


st.title("IFAD Earth Engine Web App")



m = geemap.Map()
m.add_basemap("OpenTopoMap")
dataset_mig = ee.ImageCollection('projects/sat-io/open-datasets/GLC-FCS30D/annual')
m.addLayer(dataset_mig, {}, 'projects/sat-io/open-datasets/GLC-FCS30D/annual')
m.to_streamlit(height=500)
