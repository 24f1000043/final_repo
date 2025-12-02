# analysis.py
"""
Equipment Efficiency Rate - 2024 Quarterly Data analysis
Generates a trend chart and prints the computed average (rounded to 2 dp)
"""

import math
import pandas as pd
import matplotlib.pyplot as plt

# Data (quarter, value)
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Efficiency": [69.28, 73.52, 80.54, 75.51]
}
df = pd.DataFrame(data)

# Compute sum and average (explicit)
total = df["Efficiency"].sum()          # 298.85
average_exact = total / len(df)        # 74.7125
average_rounded = round(average_exact, 2)  # 74.71 (as required)

print(f"Total = {total:.2f}")
print(f"Average (exact) = {average_exact}")
print(f"Average (rounded, 2 dp) = {average_rounded:.2f}")

# Plot: trend with industry benchmark
benchmark = 90

plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Efficiency"], marker="o", linewidth=2)
plt.axhline(benchmark, linestyle="--", linewidth=1.5, label=f"Industry Target = {benchmark}")
plt.title("Equipment Efficiency Rate — 2024 (Quarterly)")
plt.ylabel("Efficiency (%)")
plt.ylim(min(df["Efficiency"].min(), benchmark) - 5, max(df["Efficiency"].max(), benchmark) + 5)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Ensure 'figures' exists or create it
import os
os.makedirs("figures", exist_ok=True)
png_path = os.path.join("figures", "efficiency_trend.png")
plt.savefig(png_path, dpi=200)
print(f"Saved figure to {png_path}")
