import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
scores = [1.57, 6.19, 7.47, 3.39]
avg_score = 4.66
benchmark = 4.5

# Create DataFrame
df = pd.DataFrame({'Quarter': quarters, 'Score': scores})

# Plot
plt.figure(figsize=(8,5))
plt.plot(df['Quarter'], df['Score'], marker='o', label='Patient Satisfaction Score', color='blue')
plt.axhline(y=benchmark, color='red', linestyle='-', label='Industry Benchmark (4.5)')
plt.axhline(y=avg_score, color='green', linestyle='--', label='Company Average (4.66)')
plt.title('2024 Quarterly Patient Satisfaction Scores')
plt.xlabel('Quarter')
plt.ylabel('Satisfaction Score')
plt.ylim(0, max(scores)+2)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('patient_satisfaction_2024.png')
plt.close()
df.to_csv('quarterly_patient_satisfaction_2024.csv', index=False)