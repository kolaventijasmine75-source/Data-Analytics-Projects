import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
np.random.seed(42) 
n = 500 
df = pd.DataFrame({'CustomerID': range(1,n+1),'Age': np.random.randint(18,65,n),'MonthlyCharges': np.random.uniform(20,120,n).round(2),'Tenure_Months': np.random.randint(1,72,n),'SupportTickets': np.random.randint(0,10,n),'Churned': np.random.choice([0,1],n,p=[0.73,0.27])}) 
churn_rate = df['Churned'].mean() * 100 
print(f'Churn Rate: {churn_rate:.1f}%') 
print(f'Avg Charges Churned: {df[df.Churned==1].MonthlyCharges.mean():.2f}') 
print(f'Avg Charges Stayed: {df[df.Churned==0].MonthlyCharges.mean():.2f}') 
fig, axes = plt.subplots(1,2,figsize=(12,5)) 
df.groupby('Churned')['MonthlyCharges'].mean().plot(kind='bar',ax=axes[0],color=['green','red'],title='Avg Charges: Stayed vs Churned') 
axes[0].set_xticklabels(['Stayed','Churned'],rotation=0) 
df.groupby('Churned')['Tenure_Months'].mean().plot(kind='bar',ax=axes[1],color=['blue','orange'],title='Avg Tenure: Stayed vs Churned') 
axes[1].set_xticklabels(['Stayed','Churned'],rotation=0) 
plt.tight_layout() 
plt.savefig('churn_chart.png') 
plt.show() 
print('Chart saved as churn_chart.png') 
