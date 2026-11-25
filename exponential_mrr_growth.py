import matplotlib.pyplot as plt
import numpy as np

# Dummy business/economics data:
# x = Months since launch (0 to 6)
# y = Monthly Recurring Revenue (in $1,000 units) following y = a * exp(k * x)
x_discrete = np.array([0, 1, 2, 3, 4, 5, 6])
a, k = 5.0, 0.35
y_discrete = a * np.exp(k * x_discrete)

# Smooth curve for plotting the continuous exponential function
x_smooth = np.linspace(0, 6, 300)
y_smooth = a * np.exp(k * x_smooth)

# Create the plot
plt.figure(figsize=(9, 5.5))
plt.plot(
    x_smooth,
    y_smooth,
    label=r"$y = 5e^{0.35x}$ (Compounding Growth)",
    linewidth=2.2,
)
plt.scatter(
    x_discrete,
    y_discrete,
    zorder=5,
    label="Monthly Milestones",
)

# Annotate points with month and dollar values
for x_val, y_val in zip(x_discrete, y_discrete):
  plt.annotate(
      f"(M{x_val}, ${y_val:.1f}k)",
      (x_val, y_val),
      textcoords="offset points",
      xytext=(0, 8),
      ha="center",
      fontsize=8,
  )

plt.title("Exponential Growth: Monthly Recurring Revenue (MRR)")
plt.xlabel("Months Since Launch (x)")
plt.ylabel("MRR ($1,000s)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
