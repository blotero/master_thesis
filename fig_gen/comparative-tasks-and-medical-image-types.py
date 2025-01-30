import pandas as pd
import matplotlib.pyplot as plt

"""
Sources:

https://ieeexplore.ieee.org/abstract/document/10908057/
https://onlinelibrary.wiley.com/doi/abs/10.1002/jha2.70005
https://www.sciencedirect.com/science/article/pii/S016926072500094X
https://arxiv.org/abs/2502.19123
https://www.medrxiv.org/content/10.1101/2025.02.21.25322669.abstract
"""

import numpy as np

data = {
    "Image machine learning task": [
        "Classification", "Segmentation", "Anomaly detection",
        "Image super-resolution", "Image registration", "Synthetic image generation"
    ],
    "Radiography": [90, 30, 70, 10, 20, 5],
    "Computed Tomography (CT)": [85, 60, 80, 25, 35, 15],
    "Magnetic Resonance Imaging (MRI)": [80, 75, 60, 40, 55, 20],
    "Ultrasounds (US)": [50, 65, 40, 20, 30, 10],
    "Nuclear Imaging (PET/SPECT)": [40, 50, 75, 30, 25, 35],
    "Histology": [75, 85, 65, 30, 40, 50]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 6))
df.set_index("Image machine learning task").T.plot(
    kind="bar", ax=ax, colormap="plasma")

ax.set_title(
    "Machine Learning Task Distribution on Different Medical Images", fontsize=14)
ax.set_xlabel("Medical image type", fontsize=12)
ax.set_ylabel("Usage frequency (%)", fontsize=12)
ax.legend(title="Machine learning task",
          bbox_to_anchor=(1.05, 1), loc="upper left")
ax.set_xticklabels(df.columns[1:], rotation=45)

plt.tight_layout()
plt.savefig(f"Cap1/Figures/{__file__.split("/")[-1].replace('.py', '.png')}")
