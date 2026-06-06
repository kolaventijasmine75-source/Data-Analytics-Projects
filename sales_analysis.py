import pandas as pd 
import matplotlib.pyplot as plt 
data = {'Month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],'Electronics': [45000,48000,52000,49000,55000,61000,58000,63000,70000,68000,75000,80000],'Clothing': [22000,21000,25000,28000,30000,27000,24000,26000,29000,32000,38000,42000],'Groceries': [31000,30000,33000,34000,36000,35000,34000,37000,38000,36000,39000,41000]} 
df = pd.DataFrame(data) 
df['Total'] = df['Electronics'] + df['Clothing'] + df['Groceries'] 
print('Best Sales Month:', df.loc[df['Total'].idxmax(), 'Month']) 
print('Total Annual Revenue: Rs.', df['Total'].sum()) 
df.set_index('Month')[['Electronics','Clothing','Groceries']].plot(kind='bar', figsize=(12,6), colormap='Set2') 
plt.title('Monthly Sales by Category', fontsize=16) 
plt.ylabel('Revenue (Rs.)') 
plt.tight_layout() 
plt.savefig('sales_chart.png') 
plt.show() 
print('Chart saved as sales_chart.png') 
