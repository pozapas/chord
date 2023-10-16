# OD Matrix Chord Diagram Generator
This repository contains code to visualize Origin-Destination (OD) matrices using a chord diagram. The repository includes a Jupyter Notebook (ipynb) for data processing and visualization, as well as a Streamlit app for interactive web-based representation of the chord diagram.
![All_Cities](https://github.com/pozapas/chord/blob/main/All_cities.gif)
![Busiest_cities](https://github.com/pozapas/chord/blob/main/Busiest_cities.gif)
## Key Features:
- *Interactive Chord Diagram:* Offers a clear and intuitive way to understand the flow and magnitude between different origins and destinations in the OD matrix.

- **Streamlit Web App:** Provides an easy-to-use interface for users to input their OD matrix data and generate visualizations on the fly.

- **Flexible Data Input:** Supports various formats for inputting the OD matrix, ensuring compatibility with different data sources.

- **Customizable Visuals:** Parameters can be adjusted to modify the appearance and layout of the chord diagram to better match the dataset's specifics.

## Installation
This project and Chord.ipynb notebook require Python and the following Python packages installed:
- streamlit
- pandas
- numpy
- colorcet
- holoviews
- bokeh
  
To install the Python packages, navigate to the local directory where you have cloned this repository and run the following command:
```bash
pip install -r requirements.txt
```
## Running Streamlit app locally
If you want to run the OD chord diagram generator as a Streamlit app, follow these steps:
- **Navigate to your project directory:**
```bash
cd directory path
```
- **Run your Streamlit app:**
```bash
streamlit run chord.py
