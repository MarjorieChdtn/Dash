import dash
from dash import Dash, html, dash_table, dcc, Input, Output
import pandas as pd
import plotly_express as px

df = pd.read_csv('df/dash02.csv')
df_sorted = df.sort_values(by='num_pages', ascending=False)
df_top10 = df_sorted.head(10)

app = Dash(__name__)

# Définir la mise en page du tableau de bord
app.layout = html.Div([
    html.H1("Top 10 des livres avec le plus grand nombre de pages"), 
    html.Label('Choisis un auteur :'),
    dcc.Dropdown(
        id='auteur-dropdown',
        options=[
            {'label': auteur, 'value': auteur} for auteur in df_top10['authors'].unique()
        ],
        multi=True,
        placeholder='Choisis un auteur...'
    ),
    
    html.Div([
        html.Label('Entrez un nombre de pages :'),
        dcc.Input(
            id='pages-input',
            type='number',
            value=df_top10['num_pages'].max(),
            placeholder='Choisis un nombre de pages...'
        ),
    ]),

    html.Div([
        dcc.Graph(figure = px.bar(df_top10, x='title', y='num_pages',))
    ])
], className="body")

# Fin layout de base

if __name__ == '__main__':
    app.run_server(debug=True)