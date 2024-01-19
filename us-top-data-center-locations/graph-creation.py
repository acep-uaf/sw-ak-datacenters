# Importing necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# Loading in the data
# Data center information:  https://dgtlinfra.com/united-states-data-centers/#:~:text=The%20primary%20data%20center%20markets,Washington)%2C%20and%20Los%20Angeles
# Commercial Price (AK): https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a 
df=pd.read_csv('us-top-10-data-centers.csv')

# Setting up the figure
fig, ax = plt.subplots(figsize=(7, 4))
fig.set_dpi(600)
fig.suptitle('United States Data Centers: Top 10 Locations', fontsize=12, fontweight = 'bold',y=1.1)
#plt.title('Source: Dgtl Infra (2023), EIA (2023)', fontsize=10)

# Bar plot for the data centers
ax = df['Data Centers'].plot(kind='bar', color='#236192')

# Line plot for price data
ax2 = ax.twinx()
ax2.plot(ax.get_xticks(),df['p_avg'], color='#FFCD00',linewidth=3, label='$/kWh')
ax2.plot(ax.get_xticks(),df['p_ak_com'], color='red',linewidth=3, label='$/kWh AK Average (Commercial)')
ax2.plot(ax.get_xticks(),df['p_us_com'], color='blue',linewidth=3, linestyle='dashed', label='$/kWh US Average (Commercial)')

# Adjusting look of bar plot
ax.set_title('Source: Dgtl Infra (2023), EIA Electric Power Monthly (October 2023)', fontsize=10, pad=35)
ax.set_xticklabels(df['Location'],rotation=45, ha='right')
ax.set_ylabel('Number of Data Centers')
ax.set_ylim(bottom=0,top=300)
ax.grid(axis ='y')
ax.set_axisbelow(True)

# Adjusting look of line plots
ax2.set_ylabel('$/kWh')
ax2.set_ylim(bottom=0,top=0.25)
ax2labels = [item.get_text() for item in ax2.get_yticklabels()]
for i in range(len(ax2labels)):
    ax2labels[i] = '$' + ax2labels[i] # New labels with a $ in front
ax2.set_yticklabels(ax2labels)

# Figure legend

fig.legend(loc=(0.20,.83), ncols=2, fancybox=False, framealpha=0) # hard coding location (not ideal)

plt.savefig('us-top-data-center-locations-with-prices.pdf', bbox_inches = 'tight')
plt.savefig('us-top-data-center-locations-with-prices.png', bbox_inches = 'tight')