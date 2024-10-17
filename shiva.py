import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px

# Sample JSON data
data = [
    {
        "State": "Alabama",
        "TotalPopulation": 5028090,
        "WhiteNonHispanic": 3247260,
        "BlackNonHispanic": 1318390,
        "Hispanic": 232407
    },
    {
        "State": "Alaska",
        "TotalPopulation": 734821,
        "WhiteNonHispanic": 428802,
        "BlackNonHispanic": 22400,
        "Hispanic": 54890
    },
    {
        "State": "Arizona",
        "TotalPopulation": 7172280,
        "WhiteNonHispanic": 3801120,
        "BlackNonHispanic": 307726,
        "Hispanic": 2297510
    },
    {
        "State": "Arkansas",
        "TotalPopulation": 3018670,
        "WhiteNonHispanic": 2103780,
        "BlackNonHispanic": 454728,
        "Hispanic": 243321
    },
    {
        "State": "California",
        "TotalPopulation": 39356100,
        "WhiteNonHispanic": 13848300,
        "BlackNonHispanic": 2102510,
        "Hispanic": 15617900
    },
    {
        "State": "Colorado",
        "TotalPopulation": 5770790,
        "WhiteNonHispanic": 3821580,
        "BlackNonHispanic": 221211,
        "Hispanic": 1273760
    },
    {
        "State": "Connecticut",
        "TotalPopulation": 3611320,
        "WhiteNonHispanic": 2308640,
        "BlackNonHispanic": 355970,
        "Hispanic": 627408
    },
    {
        "State": "Delaware",
        "TotalPopulation": 993635,
        "WhiteNonHispanic": 597532,
        "BlackNonHispanic": 213516,
        "Hispanic": 98696
    }
]

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("State Demographics Visualization"),
    
    # Bar chart for total population with click functionality
    dcc.Graph(id='bar-chart'),
    
    # Pie chart for racial composition
    dcc.Graph(id='pie-chart')
])

# Define custom colors
bar_colors = px.colors.qualitative.Plotly  # You can also define your own colors
pie_colors = ['#636EFA', '#EF553B', '#00CC96']  # Custom colors for racial composition

# Callback for updating the bar chart and initializing it
@app.callback(
    Output('bar-chart', 'figure'),
    Output('pie-chart', 'figure'),
    Input('bar-chart', 'clickData')
)
def update_graph(clickData):
    # Create bar chart
    states = [d['State'] for d in data]
    totals = [d['TotalPopulation'] for d in data]

    bar_fig = px.bar(
        x=states,
        y=totals,
        title="Total Population by State",
        labels={'x': 'State', 'y': 'Total Population'},
        color=states,  # Use state names as colors
        color_discrete_sequence=bar_colors  # Set custom colors for the bar chart
    )

    # If a bar is clicked, update the pie chart
    if clickData:
        selected_state = clickData['points'][0]['x']
        selected_data = next(item for item in data if item["State"] == selected_state)
        
        # Create pie chart with racial composition
        racial_composition = {
            'White': selected_data['WhiteNonHispanic'],
            'Black': selected_data['BlackNonHispanic'],
            'Hispanic': selected_data['Hispanic']
        }

        pie_fig = px.pie(
            values=list(racial_composition.values()),
            names=list(racial_composition.keys()),
            title=f"Racial Composition of {selected_state}",
            color_discrete_sequence=pie_colors  # Set custom colors for the pie chart
        )
    else:
        # Default pie chart if no state is clicked
        pie_fig = px.pie(
            values=[0],  # Empty initial pie
            names=['No Data'],
            title="Select a state from the bar chart"
        )

    return bar_fig, pie_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
