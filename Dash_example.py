import dash
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dash import html


#link url do site http://127.0.0.1:8050/

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] #importação do css de um link externo


app = dash.Dash(__name__, external_stylesheets =external_stylesheets)#estilo do css

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    dcc.Markdown(
        '''
        # Hello, Dash!

        Olá, mundo!
        '''
    ),

 
     dcc.Dropdown(
    id='dropdown',
    options=[

   {'label':'All','value':'ALL'},
   {'label':'Montreal','value':'MTL'},
   {'label':'San Francisco','value':'SF'},

   #nesse bloco eu estou mudando o dropdown de lugar,
    #estava abaixo do grafico, coloquei acima
    #todo componente pode ter um ID, que voce consegue referenciar cada linha de codigo 
],
value='ALL'

), 

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),


])

@app.callback( #função que vai disparar o evento
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)


def changeText(value): #retorno do parametro value

    if value == 'ALL':
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    
    elif value == 'MTL':
        return px.bar(df[df['City'] == "Montreal"], x="Fruit", y="Amount")
    
    else:
    
        return px.bar(df[df['City'] == "SF"], x="Fruit", y="Amount")

    return value + '10'

# de acordo com o que o usuario clicar, ele vai trazer o resultado de cada grafico separadamente.




if __name__ == '__main__': app.run_server(debug=True)
