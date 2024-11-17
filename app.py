import pandas as pd
import plotly.graph_objs as go
from flask import Flask, render_template
import os

# Initialize Flask app
app = Flask(__name__)

# Route to generate and display the graph and related information
@app.route('/')
def index():
    try:
        # Load data from the CSV file
        csv_path = os.path.join(os.path.dirname(__file__), 'indian_petrol_diesel_prices_2024.csv')
        df = pd.read_csv(csv_path)

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
            hovermode='closest',
            margin=dict(l=40, r=40, t=40, b=80),
        )

        fig = go.Figure(data=[trace_petrol, trace_diesel], layout=layout)
        graph_html = fig.to_html(full_html=False)

        date_range = df['Date'].min(), df['Date'].max()
        average_petrol_price = df['Petrol Price (INR)'].mean()
        average_diesel_price = df['Diesel Price (INR)'].mean()

        return render_template('index.html',
                             start_date=date_range[0],
                             end_date=date_range[1],
                             avg_petrol_price=round(average_petrol_price, 2),
                             avg_diesel_price=round(average_diesel_price, 2),
                             graph_html=graph_html)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Create the application object
application = app

if __name__ == '__main__':
    # Get port from environment variable or default to 10000
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)