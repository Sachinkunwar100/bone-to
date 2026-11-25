import matplotlib.pyplot as plt
import numpy as np

# Dummy business/economics data:
# x = Monthly Marketing Spend (in $10,000 units, i.e., 1 = $10k, 64 = $640k)
# y = Monthly Revenue (in $100,000 units) following y = a + b * log10(x)
x_discrete = np.array([1, 2, 4, 8, 16, 32, 64])
a, b = 10.0, 15.0
y_discrete = a + b * np.log10(x_discrete)

# Smooth curve for plotting the continuous logarithmic function
x_smooth = np.linspace(1, 64, 300)
y_smooth = a + b * np.log10(x_smooth)

# Create the plot
plt.figure(figsize=(9, 5.5))
plt.plot(
    x_smooth,
    y_smooth,
    label=r"$y = 10 + 15\log_{10}(x)$ (Diminishing Returns)",
    linewidth=2.2,
)
plt.scatter(
    x_discrete,
    y_discrete,
    zorder=5,
    label="Sampled Spend Tiers",
)

# Annotate points with dollar values
for x_val, y_val in zip(x_discrete, y_discrete):
  plt.annotate(
      f"(${x_val*10}k, ${y_val*100:.0f}k)",
      (x_val, y_val),
      textcoords="offset points",
      xytext=(0, 8),
      ha="center",
      fontsize=8,
  )

plt.title("Logarithmic Diminishing Returns: Ad Spend vs. Revenue")
plt.xlabel("Ad Spend Index (x = $10k units)")
plt.ylabel("Revenue Index (y = $100k units)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()import matplotlib.pyplot as plt
import numpy as np

# Dummy business/economics data:
# x = Monthly Marketing Spend (in $10,000 units, i.e., 1 = $10k, 64 = $640k)
# y = Monthly Revenue (in $100,000 units) following y = a + b * log10(x)
x_discrete = np.array([1, 2, 4, 8, 16, 32, 64])
a, b = 10.0, 15.0
y_discrete = a + b * np.log10(x_discrete)

# Smooth curve for plotting the continuous logarithmic function
x_smooth = np.linspace(1, 64, 300)
y_smooth = a + b * np.log10(x_smooth)

# Create the plot
plt.figure(figsize=(9, 5.5))
plt.plot(
    x_smooth,
    y_smooth,
    label=r"$y = 10 + 15\log_{10}(x)$ (Diminishing Returns)",
    linewidth=2.2,
)
plt.scatter(
    x_discrete,
    y_discrete,
    zorder=5,
    label="Sampled Spend Tiers",
)

# Annotate points with dollar values
for x_val, y_val in zip(x_discrete, y_discrete):
  plt.annotate(
      f"(${x_val*10}k, ${y_val*100:.0f}k)",
      (x_val, y_val),
      textcoords="offset points",
      xytext=(0, 8),
      ha="center",
      fontsize=8,
  )

plt.title("Logarithmic Diminishing Returns: Ad Spend vs. Revenue")
plt.xlabel("Ad Spend Index (x = $10k units)")
plt.ylabel("Revenue Index (y = $100k units)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
