import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

# Read data
df = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv'
)

# Extract Year + Month (keep month number for correct sorting)
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month_num'] = df['Date'].dt.month
df['Month'] = df['Date'].dt.month_name()

years = sorted(df['Year'].unique())
regions = ["NSW", "NT", "QL", "SA", "TA", "VI", "WA"]

# Layout
app.layout = html.Div(children=[
    html.H1(
        'Australia Wildfire Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 26}
    ),

    # Outer division
    html.Div(style={'display': 'flex', 'gap': '20px'}, children=[

        # First inner division (Inputs)
        html.Div(style={
            'flex': '1',
            'border': '1px solid #ddd',
            'borderRadius': '10px',
            'padding': '15px'
        }, children=[
            html.H2('Select Region:', style={'marginBottom': '10px'}),

            dcc.RadioItems(
                id='region',
                options=[{'label': r, 'value': r} for r in regions],
                value='NSW',
                inline=True
            ),

            html.Br(), html.Br(),

            html.H2('Select Year:', style={'marginBottom': '10px'}),

            dcc.Dropdown(
                id='year',
                options=[{'label': y, 'value': y} for y in years],
                value=years[0],
                clearable=False
            )
        ]),

        # Second inner division (Outputs)
        html.Div(style={
            'flex': '2',
            'border': '1px solid #ddd',
            'borderRadius': '10px',
            'padding': '15px'
        }, children=[
            html.Div(id='plot1'),
            html.Div(id='plot2')
        ])
    ])
])

# Callback
@app.callback(
    Output('plot1', 'children'),
    Output('plot2', 'children'),
    Input('region', 'value'),
    Input('year', 'value')
)
def reg_year_display(input_region, input_year):
    y_r_data = df[(df['Region'] == input_region) & (df['Year'] == input_year)].copy()

    # Monthly Average Estimated Fire Area
    est_data = (y_r_data
                .groupby(['Month_num', 'Month'], as_index=False)['Estimated_fire_area']
                .mean()
                .sort_values('Month_num'))

    fig1 = px.pie(
        est_data,
        values='Estimated_fire_area',
        names='Month',
        title=f"{input_region}: Monthly Average Estimated Fire Area in year {input_year}"
    )

    # Monthly Average Count of Pixels for Presumed Vegetation Fires
    veg_data = (y_r_data
                .groupby(['Month_num', 'Month'], as_index=False)['Count']
                .mean()
                .sort_values('Month_num'))

    fig2 = px.bar(
        veg_data,
        x='Month',
        y='Count',
        title=f"{input_region}: Average Count of Pixels for Presumed Vegetation Fires in year {input_year}"
    )

    return dcc.Graph(figure=fig1), dcc.Graph(figure=fig2)

if __name__ == '__main__':
    app.run(debug=True)

