import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Read the website traffic data
with open('website_traffic.txt', 'r') as f:
    lines = f.readlines()

# Skip the header comment and read the data
data_str = ''.join(lines[1:])
df = pd.read_csv(StringIO(data_str), sep=r'\s+')

# Convert date column to datetime objects
df['date'] = pd.to_datetime(df['date'])

# Print basic statistics
print("Website Traffic Analysis:")
print("========================")
print(f"Total days analysed: {len(df)}")
print(f"Average page views: {df['page_views'].mean():.0f}")
print(f"Average unique visitors: {df['unique_visitors'].mean():.0f}")
print(f"Peak traffic day: {df.loc[df['unique_visitors'].idxmax(), 'date'].date()} with {df['unique_visitors'].max()} unique visitors")
print(f"Average bounce rate: {df['bounce_rate'].mean():.1f}%")

# Create a visualisation
fig, ax1 = plt.subplots(figsize=(14, 7))
sns.set_style("whitegrid")

# Plot page views and unique visitors
ax1.plot(df['date'], df['page_views'], marker='o', color='dodgerblue', label='Page Views')
ax1.plot(df['date'], df['unique_visitors'], marker='o', color='darkorange', label='Unique Visitors')
ax1.set_xlabel('Date')
ax1.set_ylabel('Count', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.tick_params(axis='x', rotation=45)

# Add bounce rate as bars on a secondary axis
ax2 = ax1.twinx()
ax2.bar(df['date'], df['bounce_rate'], alpha=0.3, color='crimson', width=0.5, label='Bounce Rate')
ax2.set_ylabel('Bounce Rate (%)', color='crimson')
ax2.tick_params(axis='y', labelcolor='crimson')
ax2.set_ylim(0, df['bounce_rate'].max() * 1.2) # Adjust y-limit for better visibility

# Formatting
fig.suptitle('30-Day Website Traffic Report', fontsize=18)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure
plt.savefig('traffic_analysis.png')
print("Analysis complete. Results saved to 'traffic_analysis.png'")