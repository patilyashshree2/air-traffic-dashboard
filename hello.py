import preswald
from preswald import text, table, plotly, sidebar
import pandas as pd
import plotly.express as px

# with sidebar():
#     text("✈️ Welcome to Air Traffic Insights")

# Load dataset
df = pd.read_csv("data/Air_Traffic_Passenger_Statistics.csv")

# Filter
filtered_df = df[df["Passenger Count"] > 500000]
filtered_df = filtered_df[["Operating Airline", "Passenger Count"]]

# UI
text("## Air Traffic Analysis ✈️") 
text("Filtered data from high-traffic flights (500K+ passengers) 📊")
table(filtered_df, title="Filtered Data")

# Scatter plot
fig = px.scatter(df, 
                 x="Operating Airline", 
                 y="Passenger Count", 
                 color="Terminal",
                 title="Passenger Count by Airline",
                 labels={'Operating Airline': 'Operating Airline', 'Passenger Count': 'Passenger Count'})

preswald.plotly(fig)
