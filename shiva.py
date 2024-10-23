import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Sample JSON data
data = [
    {
        "State": "Alabama",
        "TotalPopulation": 5028090,
        "WhiteNonHispanic": 3247260,
        "BlackNonHispanic": 1318390,
        "Hispanic": 232407,
        "Employment": 2300000,
        "Unemployment": 150000,
        "Industries": {
            "Manufacturing": {"count": 1200, "members": 25000},
            "Healthcare": {"count": 700, "members": 15000},
            "Education": {"count": 800, "members": 12000}
        },
        "Cars": [
            {"Type": "Sedan", "Count": 1500000},
            {"Type": "SUV", "Count": 800000},
            {"Type": "Truck", "Count": 400000}
        ]
    },
    {
        "State": "Alaska",
        "TotalPopulation": 734821,
        "WhiteNonHispanic": 428802,
        "BlackNonHispanic": 22400,
        "Hispanic": 54890,
        "Employment": 300000,
        "Unemployment": 20000,
        "Industries": {
            "Oil & Gas": {"count": 300, "members": 5000},
            "Tourism": {"count": 600, "members": 15000},
            "Fishing": {"count": 500, "members": 8000}
        },
        "Cars": [
            {"Type": "Sedan", "Count": 100000},
            {"Type": "SUV", "Count": 60000},
            {"Type": "Truck", "Count": 30000}
        ]
    },
    {
        "State": "Arizona",
        "TotalPopulation": 7172280,
        "WhiteNonHispanic": 3801120,
        "BlackNonHispanic": 307726,
        "Hispanic": 2297510,
        "Employment": 3500000,
        "Unemployment": 250000,
        "Industries": {
            "Manufacturing": {"count": 1500, "members": 30000},
            "Technology": {"count": 1000, "members": 50000},
            "Healthcare": {"count": 800, "members": 25000}
        },
        "Cars": [
            {"Type": "Sedan", "Count": 1200000},
            {"Type": "SUV", "Count": 700000},
            {"Type": "Truck", "Count": 300000}
        ]
    },
    {
        "State": "Arkansas",
        "TotalPopulation": 3018670,
        "WhiteNonHispanic": 2103780,
        "BlackNonHispanic": 454728,
        "Hispanic": 243321,
        "Employment": 1500000,
        "Unemployment": 100000,
        "Industries": {
            "Agriculture": {"count": 1200, "members": 20000},
            "Manufacturing": {"count": 900, "members": 18000},
            "Retail": {"count": 1000, "members": 15000}
        },
        "Cars": [
            {"Type": "Sedan", "Count": 800000},
            {"Type": "SUV", "Count": 400000},
            {"Type": "Truck", "Count": 200000}
        ]
    },
    {
        "State": "California",
        "TotalPopulation": 39356100,
        "WhiteNonHispanic": 13848300,
        "BlackNonHispanic": 2102510,
        "Hispanic": 15617900,
        "Employment": 20000000,
        "Unemployment": 1500000,
        "Industries": {
            "Technology": {"count": 5000, "members": 250000},
            "Entertainment": {"count": 3000, "members": 150000},
            "Agriculture": {"count": 2000, "members": 100000}
        },
        "Cars": [
            {"Type": "Sedan", "Count": 6000000},
            {"Type": "SUV", "Count": 4000000},
            {"Type": "Truck", "Count": 2000000}
        ]
    },
    {
        "State": "Colorado",
        "TotalPopulation": 5770790,
        "WhiteNonHispanic": 3821580,
        "BlackNonHispanic": 221211,
        "Hispanic": 1273760,
        "Employment": 3000000,
        "Unemployment": 200000,
        "Industries": {
            "Technology": {"count": 1500, "members": 30000},
            "Tourism": {"count": 1000, "members": 25000},
            "Agriculture": {"count": 800, "members": 15000}
        },
        "Cars": [
            {"Type": "Sedan", "Count": 900000},
            {"Type": "SUV", "Count": 500000},
            {"Type": "Truck", "Count": 300000}
        ]
    },
    {
        "State": "Connecticut",
        "TotalPopulation": 3611320,
        "WhiteNonHispanic": 2308640,
        "BlackNonHispanic": 355970,
        "Hispanic": 627408,
        "Employment": 1500000,
        "Unemployment": 100000,
        "Industries": {
            "Finance": {"count": 1000, "members": 60000},
            "Healthcare": {"count": 800, "members": 20000},
            "Manufacturing": {"count": 600, "members": 12000}
        },
        "Cars": [
            {"Type": "Sedan", "Count": 600000},
            {"Type": "SUV", "Count": 300000},
            {"Type": "Truck", "Count": 150000}
        ]
    },
    {
        "State": "Delaware",
        "TotalPopulation": 993635,
        "WhiteNonHispanic": 597532,
        "BlackNonHispanic": 213516,
        "Hispanic": 98696,
        "Employment": 450000,
        "Unemployment": 25000,
        "Industries": {
            "Finance": {"count": 500, "members": 25000},
            "Healthcare": {"count": 300, "members": 10000},
            "Manufacturing": {"count": 400, "members": 8000}
        },
        "Cars": [
            {"Type": "Sedan", "Count": 200000},
            {"Type": "SUV", "Count": 100000},
            {"Type": "Truck", "Count": 50000}
        ]
    },
    {
        "State": "District of Columbia",
        "TotalPopulation": 670587,
        "WhiteNonHispanic": 243730,
        "BlackNonHispanic": 291880,
        "Hispanic": 77168,
        "Employment": 390000,  
        "Unemployment": 25000, 
        "Industries": {
            "Finance": {"count": 500, "members": 15000}, 
            "Healthcare": {"count": 300, "members": 5000}, 
            "Manufacturing": {"count": 100, "members": 2000} 
        },
        "Cars": [
            {"Type": "Sedan", "Count": 100000}, 
            {"Type": "SUV", "Count": 50000},    
            {"Type": "Truck", "Count": 20000}   
        ]
    },
      {
        "State": "Florida",
        "TotalPopulation": 21634500,
        "WhiteNonHispanic": 11242500,
        "BlackNonHispanic": 3232870,
        "Hispanic": 5738280,
        "Employment": 13000000, 
        "Unemployment": 500000, 
        "Industries": {
            "Finance": {"count": 800, "members": 50000}, 
            "Healthcare": {"count": 600, "members": 25000}, 
            "Manufacturing": {"count": 700, "members": 15000} 
        },
        "Cars": [
            {"Type": "Sedan", "Count": 8000000}, 
            {"Type": "SUV", "Count": 4000000},   
            {"Type": "Truck", "Count": 2000000} 
        ]
    }
]

# Initialize Dash app
app = dash.Dash(__name__)

server = app.server

# Layout
app.layout = html.Div(style={'backgroundColor': 'rgb(74 58 127 / 59%)', 'padding': '20px'}, children=[
    html.Div(
        html.H1(
            "Exploring US State Demographics",
            style={
                'textAlign': 'center',
                'fontSize': '70px',
                'fontWeight': 'bold',
                'textShadow': 'rgba(255, 255, 255, 0.7) 2px 2px 4px',
                'color': '#000',
                'padding': '20px'
            }
        ),
    ),
    html.Div(
        dcc.Graph(id='bar-chart', style={'height': '600px', 'width': '100%'}),
        style={'border': '2px solid #007bff', 'border-radius': '10px', 'padding': '0px', 'margin': '10px', 'backgroundColor': 'white'}
    ),
    html.Div(id='additional-graphs', style={'display': 'none'}, children=[
        html.Div([
            html.Div([
                dcc.Graph(id='pie-chart', style={'height': '600px', 'width': '100%'}),
                html.H4(id='pie-chart-title', children="Racial Composition", style={'fontSize': '28px'})
            ], style={'border': '2px solid #007bff', 'border-radius': '10px', 'padding': '10px', 'margin': '10px', 'flex': '1', 'backgroundColor': 'white'}),
            html.Div([
                dcc.Graph(id='industry-line-chart', style={'height': '600px', 'width': '100%'}),
                html.H4(id='industry-line-chart-title', children="Industry Members Over Time", style={'fontSize': '28px'})
            ], style={'border': '2px solid #007bff', 'border-radius': '10px', 'padding': '10px', 'margin': '10px', 'flex': '1', 'backgroundColor': 'white'})
        ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'}),
        html.Div([
            html.Div([
                dcc.Graph(id='employment-figurewidget', style={'height': '600px', 'width': '100%'}),
                html.H4(id='employment-figurewidget-title', children="Employment Data", style={'fontSize': '28px'})
            ], style={'border': '2px solid #007bff', 'border-radius': '10px', 'padding': '10px', 'margin': '10px', 'flex': '1', 'backgroundColor': 'white'}),
            html.Div([
                dcc.Graph(id='cars-chart', style={'height': '600px', 'width': '100%'}),
                html.H4(id='cars-chart-title', children="Cars by Type", style={'fontSize': '28px'})
            ], style={'border': '2px solid #007bff', 'border-radius': '10px', 'padding': '10px', 'margin': '10px', 'flex': '1', 'backgroundColor': 'white'})
        ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'})
    ])
])

# Define custom colors
bar_colors = px.colors.qualitative.Plotly  
pie_colors = ['#636EFA', '#EF553B', '#00CC96']  

@app.callback(
    Output('bar-chart', 'figure'),
    Output('pie-chart', 'figure'),
    Output('industry-line-chart', 'figure'),
    Output('employment-figurewidget', 'figure'),
    Output('cars-chart', 'figure'),
    Output('additional-graphs', 'style'),
    Input('bar-chart', 'clickData')
)
def update_graph(clickData):
    states = [d['State'] for d in data]
    totals = [d['TotalPopulation'] for d in data]

    bar_fig = px.bar(
        x=states,
        y=totals,
        title="Total Population by State",
        labels={'x': 'State', 'y': 'Total Population'},
        color=states,
        color_discrete_sequence=bar_colors
    )
    bar_fig.update_layout(
        title_font_size=30,
        xaxis_title_font_size=20,
        yaxis_title_font_size=20,
        legend_font_size=16
    )

    pie_fig = go.Figure()
    industry_line_fig = go.Figure()
    employment_fig = go.Figure()
    cars_fig = go.Figure()

    additional_graphs_style = {'display': 'none'}

    if clickData:
        selected_state = clickData['points'][0]['x']
        selected_data = next(item for item in data if item["State"] == selected_state)
        
        racial_composition = {
            'White': selected_data['WhiteNonHispanic'],
            'Black': selected_data['BlackNonHispanic'],
            'Hispanic': selected_data['Hispanic']
        }

        pie_fig = px.pie(
            values=list(racial_composition.values()),
            names=list(racial_composition.keys()),
            title=f"Racial Composition of {selected_state}",
            color_discrete_sequence=pie_colors  
        )
        pie_fig.update_layout(
            title_font_size=30,
            legend_font_size=16
        )

        industry_names = list(selected_data['Industries'].keys())
        industry_members = [info['members'] for info in selected_data['Industries'].values()]
        industry_years = ['2018', '2019', '2020', '2021', '2022']  # Example years
        
        for name in industry_names:
            industry_line_fig.add_trace(go.Scatter(
                x=industry_years,
                y=[info['members'] for info in selected_data['Industries'].values()],
                mode='lines+markers',
                name=name
            ))

        industry_line_fig.update_layout(
            title=f"Industry Members Over Time in {selected_state}",
            xaxis_title='Year',
            yaxis_title='Number of Members',
            title_font_size=30,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            legend_font_size=16
        )

        employment_data = {
            'Employment': selected_data['Employment'],
            'Unemployment': selected_data['Unemployment']
        }

        employment_fig = go.Figure(data=[    
            go.Pie(
                labels=list(employment_data.keys()),
                values=list(employment_data.values()),
                hole=.3,
                marker=dict(colors=bar_colors[:2])
            )
        ])
        employment_fig.update_layout(
            title=f"Employment Data in {selected_state}",
            title_font_size=30,
            legend_font_size=16
        )

        car_types = [car['Type'] for car in selected_data['Cars']]
        car_counts = [car['Count'] for car in selected_data['Cars']]

        cars_fig = px.bar(
            x=car_types,
            y=car_counts,
            title=f"Cars by Type in {selected_state}",
            labels={'x': 'Car Type', 'y': 'Count'},
            color=car_types,
            color_discrete_sequence=bar_colors
        )
        cars_fig.update_layout(
            title_font_size=30,
            xaxis_title_font_size=20,
            yaxis_title_font_size=20,
            legend_font_size=16
        )

        additional_graphs_style = {'display': 'block'}

    return bar_fig, pie_fig, industry_line_fig, employment_fig, cars_fig, additional_graphs_style

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
