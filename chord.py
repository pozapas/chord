########################################
# Author: Amir Rafe (amir.rafe@usu.edu)
# About: How to plot a chord diagram 
# Date: 2021 Winter
# File: Chord.py
########################################

##########Dependencies###################
import pandas as pd
from pandas import DataFrame
import numpy as np
import colorcet as cc
import holoviews as hv
from holoviews import opts, dim
import streamlit as st
import colorcet as cc
########################################

##########Initialization################
hv.extension('bokeh')
hv.output(size=400)

# Title of the app
st.title('Chord Diagram App')
st.write(f'[Amir Rafe](https://www.linkedin.com/in/amir-rafe-08770854/)')

# Load dataset
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    ##########Dataset_Preparation#############

    # Replace NA values with zero
    df = df.fillna(0)

    # Create Nodes dataframe 
    Nodes = pd.DataFrame(columns=['استان','مجموع سفرها'] , index = range(0,31))
    Nodes['استان'] = df['مبداء  -   مقصد']
    Nodes['مجموع سفرها'] = df.sum(axis=1 , numeric_only=True)

    # Create linkes dataframe
    temp = df
    temp.drop(temp.columns[[0]], axis=1, inplace=True)
    temp.columns = np.arange(len(temp.columns))
    temp = temp.T
    links = temp.stack().reset_index()
    links.columns = ['From', 'To', 'Value']
    links['Value'] = links['Value'].astype(int)

    ##########Chord_all_cities#############
    nodes = hv.Dataset(Nodes,'index')
    chord = hv.Chord((links, nodes)).select(value=(5, None))
    chord.opts(
        opts.Chord(cmap=cc.cm.glasbey_bw, edge_cmap=cc.cm.glasbey_warm, edge_color=dim('From').str(),
                edge_alpha= 0.8, node_selection_fill_color=None, edge_nonselection_line_alpha=0.01,
                edge_selection_line_color='green', edge_hover_line_color='black',
                node_color=dim('index').str()))
    label_data = chord.nodes.data.drop(['index'], axis=1)

    # Using the node's angle as a rotation value
    label_data['rotation'] = np.arctan((label_data.y / label_data.x))

    # Repositioning the label a bit away from the nodes
    label_data['y'] = label_data['y'].apply(lambda x: x * 1.2)
    label_data['x'] = label_data['x'].apply(lambda x: x * 1.2)

    # Creating label element with node data
    labels = hv.Labels(label_data)
    labels.opts(
    opts.Labels(text_font_size='16pt', text_font_style='bold', padding=0.08, angle= dim('rotation') * 1260/22 ))

    # Adding labels to chord
    Chord_1 = chord * labels

    ##########Chord_busiest_cities#############
    route_counts = links
    nodes = hv.Dataset(Nodes, 'index')
    chordb = hv.Chord((route_counts, nodes), ['From', 'To'], ['Value'])

    # Select the 10 busiest cities
    busiest = list(links.groupby('From').sum().sort_values('Value').iloc[-10:].index.values)
    busiest_Links = chord.select(index=busiest, selection_mode='nodes')

    busiest_Links.opts(
        opts.Chord(cmap=cc.cm.glasbey_bw, edge_cmap=cc.cm.glasbey_warm, edge_color=dim('From').str(),
                edge_alpha= 0.8, node_selection_fill_color=None, edge_nonselection_line_alpha=0.01,
                edge_selection_line_color='green', edge_hover_line_color='black',
                node_color=dim('index').str()))
    label_data = busiest_Links.nodes.data.drop(['index'], axis=1)

    # Using the node's angle as a rotation value
    label_data['rotation'] = np.arctan((label_data.y / label_data.x))

    # Repositioning the label a bit away from the nodes
    label_data['y'] = label_data['y'].apply(lambda x: x * 1.18)
    label_data['x'] = label_data['x'].apply(lambda x: x * 1.18)

    # Creating label element with node data
    labels = hv.Labels(label_data)
    labels.opts(
    opts.Labels(text_font_size='16pt', text_font_style='bold', padding=0.08, angle= dim('rotation') * 1260/22 ))

    # Adding labels to chord
    Chord_2 = busiest_Links * labels

    # Display Chord Diagram for all cities
    st.subheader('Chord Diagram - All Cities')
    st.write(hv.render(chord_1_plot, backend='bokeh'))
    chord_1_plot = hv.render(Chord_1, backend='bokeh')
    st.bokeh_chart(chord_1_plot)

    # Display Chord Diagram for busiest cities
    st.subheader('Chord Diagram - Busiest Cities')
    chord_2_plot = hv.render(Chord_2, backend='bokeh')
    st.bokeh_chart(chord_2_plot)
    

##############END###################
