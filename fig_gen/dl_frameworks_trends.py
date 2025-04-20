import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set the style for the plot
plt.style.use("seaborn-v0_8-paper")
sns.set_context("paper", font_scale=1.5)

# Read the data
data = pd.read_csv("../Cap2/Figures/Data/trends.csv", skiprows=1)


# Convert dates to datetime objects
data["Semana"] = pd.to_datetime(data["Semana"])


# Create the figure
plt.figure(figsize=(12, 6))

# Plot the data
plt.plot(
    data["Semana"],
    data["tensorflow"],
    label="TensorFlow",
    linewidth=2.5,
    color="#FF6B6B",
)
plt.plot(
    data["Semana"],
    data["pytorch"],
    label="PyTorch",
    linewidth=2.5,
    color="#4ECDC4",
)

# Customize the plot
plt.title(
    "Comparative Trends of Deep Learning Frameworks",
    pad=20,
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Relative Interest (Google Trends)", fontsize=14)

# Format the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.xticks(rotation=45)

# Add grid
plt.grid(True, linestyle="--", alpha=0.7)

# Add legend
plt.legend(fontsize=12, frameon=True, shadow=True)

# Adjust layout
plt.tight_layout()

plt.savefig(
    "../Cap2/Figures/dl_frameworks_trends.png",
    dpi=300,
    bbox_inches="tight",
    format="png",
)

# Show the plot
plt.show()
