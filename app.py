import pandas as pd
import plotly.graph_objs as go
from flask import Flask, render_template
import os

# Initialize Flask app
app = Flask(__name__)

# Route to generate and display the graph and related information
@app.route('/')
def index():
    # Load data from the CSV file
    df = pd.read_csv('indian_petrol_diesel_prices_2024.csv')

    # Create the Plotly graph
    trace_petrol = go.Scatter(
        x=pd.to_datetime(df['Date']),
        y=df['Petrol Price (INR)'], 
        mode='lines+markers',
        name='Petrol Price (INR)',
        marker=dict(color='blue', size=6, line=dict(width=2, color='blue')),
        hovertemplate="<b>Date:</b> %{x}<br><b>Price:</b> ₹%{y:.2f}<br><extra></extra>"
    )

    trace_diesel = go.Scatter(
        x=pd.to_datetime(df['Date']),
        y=df['Diesel Price (INR)'],
        mode='lines+markers',
        name='Diesel Price (INR)',
        marker=dict(color='orange', size=6, line=dict(width=2, color='orange')),
        hovertemplate="<b>Date:</b> %{x}<br><b>Price:</b> ₹%{y:.2f}<br><extra></extra>"
    )

    layout = go.Layout(
        title='Petrol and Diesel Prices in India (2024)',
        xaxis=dict(title='Date', tickangle=45, tickmode='array'),
        yaxis=dict(title='Price (INR)'),
        showlegend=True,
        hovermode='closest',  # Show closest point when hovered
        margin=dict(l=40, r=40, t=40, b=80),  # Adjust margins to prevent overlap
    )

    # Combine the traces and layout into a figure
    fig = go.Figure(data=[trace_petrol, trace_diesel], layout=layout)

    # Save the graph to an HTML file and pass it to the template
    graph_html = fig.to_html(full_html=False)

    # Pass data to the template (date and prices for text explanation)
    date_range = df['Date'].min(), df['Date'].max()
    average_petrol_price = df['Petrol Price (INR)'].mean()
    average_diesel_price = df['Diesel Price (INR)'].mean()

    return render_template('index.html', 
                           start_date=date_range[0], 
                           end_date=date_range[1],
                           avg_petrol_price=round(average_petrol_price, 2), 
                           avg_diesel_price=round(average_diesel_price, 2),
                           graph_html=graph_html)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
