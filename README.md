# air-traffic-dashboard
Air Traffic Analysis for https://catalog.data.gov/dataset/air-traffic-passenger-statistics

Data Set: https://catalog.data.gov/dataset/air-traffic-passenger-statistics


✈️ Air Traffic Passenger Analysis with Preswald
Overview
This Preswald app analyzes U.S. air traffic data using a no-code/low-code approach with Python. It loads and filters a dataset of airline passenger statistics, builds an interactive UI, and visualizes insights using Plotly charts.

🔧 Technologies Used
Preswald for data app UI and deployment


Pandas for data manipulation


Plotly Express for interactive visualizations


CSV dataset: Air_Traffic_Passenger_Statistics.csv


🔢 Step-by-Step Breakdown
1. Load the Dataset
python
CopyEdit
df = pd.read_csv('data/Air_Traffic_Passenger_Statistics.csv')

The dataset is loaded using pandas.read_csv() from the local data/ folder.


This approach is used because preswald.get_df() didn't successfully register the file.


2. Filter and Select Data
python
CopyEdit
filtered_df = df[df["Passenger Count"] > 500000]
filtered_df = filtered_df[["Operating Airline", "Passenger Count"]]

Filters the data to include only flights with more than 500,000 passengers.


Selects two important columns for display:


Operating Airline


Passenger Count


3. Build Interactive UI
python
CopyEdit
text("## My Data Analysis App")
text("### Flights with More Than 500,000 Passengers")
table(filtered_df, title="Filtered High Count Flights")

Displays informative headings using text().


Shows the filtered DataFrame using table() with a descriptive title.

4. Visualize with Plotly
python
CopyEdit
fig = px.scatter(df, 
                 x="Operating Airline", 
                 y="Passenger Count", 
                 color="Terminal",
                 title="Passenger Count by Airline",
                 labels={'Operating Airline': 'Operating Airline', 'Passenger Count': 'Passenger Count'})
preswald.plotly(fig)

Creates a scatter plot to compare airlines by passenger count.


The plot is colored by terminal type, helping to visually distinguish traffic types (e.g., Domestic vs. International terminals).


Enhances understanding of airline load distribution across terminals.


📝 Summary
This app demonstrates how to:
Load and filter real-world datasets using pandas


Create interactive dashboards with Preswald components


Build data-driven visualizations to uncover insights


It is a lightweight, efficient example of using low-code tools like Preswald with Python to explore public datasets quickly and visually.


EXPECTED RESULT:

<img width="693" alt="image" src="https://github.com/user-attachments/assets/a2fe3ea3-9de3-488a-b638-35a85e2da4ae" />
<img width="684" alt="image" src="https://github.com/user-attachments/assets/787c28ac-ff43-424e-a4e8-a7f8725ad1fc" />






