import plotly.graph_objs as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import numpy as np

# Generate random data for elements
def generate_data(num_elements):
    data = {}
    for i in range(num_elements):
        element_data = []
        base_time = datetime(2024, 5, 10, 0)
        for j in range(24):
            timestamp = base_time + timedelta(hours=j)
            timestamp = np.datetime64(timestamp)

            value = np.random.rand() * np.pi * np.sin(j * np.pi / 12)
            element_data.append((timestamp, value))
        print(type(timestamp))
        data[f'Element{i+1}'] = element_data
    return data

# Generate data for 26 elements
elements_data = generate_data(26)

# Divide elements into three groups: first 9, next 9, and remaining
print(elements_data)



first_9_elements = list(elements_data.keys())[:9] # top 10 gainers
next_9_elements = list(elements_data.keys())[9:18] # top 10 loser
remaining_elements = list(elements_data.keys())[18:] # remaining ones

# Create traces for first subplot (9 elements)
traces1 = []
for element in first_9_elements:
    data = elements_data[element]
    x_values = [x[0] for x in data]
    y_values = [x[1] for x in data]
    trace = go.Scatter(x=x_values, y=y_values, mode='lines', name=element)
    traces1.append(trace)

# Create traces for second subplot (9 elements)
traces2 = []
for element in next_9_elements:
    data = elements_data[element]
    x_values = [x[0] for x in data]
    y_values = [x[1] for x in data]
    trace = go.Scatter(x=x_values, y=y_values, mode='lines', name=element)
    traces2.append(trace)

# Create traces for third subplot (remaining 8 elements)
traces3 = []
for element in remaining_elements:
    data = elements_data[element]
    x_values = [x[0] for x in data]
    y_values = [x[1] for x in data]
    trace = go.Scatter(x=x_values, y=y_values, mode='lines', name=element)
    traces3.append(trace)


# Create subplots with custom size
fig = make_subplots(rows=3, cols=1, subplot_titles=("First 9 Elements", "Next 9 Elements", "Remaining 8 Elements"),
                    vertical_spacing=0.1)

# Add traces to first subplot
for trace in traces1:
    fig.add_trace(trace, row=1, col=1)

# Add traces to second subplot
for trace in traces2:
    fig.add_trace(trace, row=2, col=1)

# Add traces to third subplot
for trace in traces3:
    fig.add_trace(trace, row=3, col=1)

# Update layout with larger figure size
fig.update_layout(title='Time Series Data',
                  xaxis=dict(title='Time', type='date', tickformat='%I:%M %p'),
                  yaxis=dict(title='Values'),
                  hovermode='closest',
                  height=900,  # Adjust height as needed
                  width=1000   # Adjust width as needed
                 )

# Show plot
fig.show()
