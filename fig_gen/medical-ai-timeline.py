import matplotlib.pyplot as plt


def generate_offsets(num_items, offset_values):
    return [offset_values[i % len(offset_values)] for i in range(num_items)]


ai_milestones = [
    {"year": 1943, "text": "First model of neurons\n in a network"},
    {"year": 1950, "text": "Turing’s paper"},
    {"year": 1956, "text": "Birth of AI \n(Dartmouth conference)"},
    {"year": 1958, "text": "Perceptron"},
    {"year": 1963, "text": "Decision tree \nlearning and SVM"},
    {"year": 1965, "text": "Expert systems "},
    {"year": 1980, "text": "Image recognition:\ndeep neural network"},
    {"year": 1989, "text": "CNN: \nimage classification"},
    {"year": 1990, "text": "Ensemble machine \nlearning by boosting"},
    {"year": 1997, "text": "LSTM for \nsignal analysis"},
    {"year": 1998, "text": "AI beats a human \nat chess"},
    {"year": 2012, "text": "Imagenet challenge \nwon by a CNN"},
    {"year": 2014, "text": "First GAN"},
    {"year": 2017, "text": "AI beats a human\n at Go game"},
    {"year": 2022, "text": "ChatGPT released"},
    {"year": 2023, "text": "GPT-4"},
    {"year": 2024, "text": "Claude Sonnet"},
    {"year": 2025, "text": "DeepSeek-R1"}
]

medical_ai = [
    {"year": 1963, "text": "ML in \nradiographies"},
    {"year": 1966, "text": "ELIZA chatbot"},
    {"year": 1978, "text": "CASNET (glaucoma)"},
    {"year": 1982, "text": "Internist-I\nexpert system for \ngeneral medicine"},
    {"year": 1986, "text": "Segmentation using \nclustering"},
    {"year": 1994, "text": "Image features and ML"},
    {"year": 1995, "text": "Neural networks \nidentify nodules"},
    {"year": 1998, "text": "Commercial CAD system"},
    {"year": 2010, "text": "The term \n'radiomics' \nis coined"},
    {"year": 2011, "text": "Images uploaded on TCIA"},
    {"year": 2015, "text": "U-net"},
    {"year": 2017, "text": "IBM Watson \nidentifies SLA protein"},
    {"year": 2018, "text": "CNN \nfor reconstruction"},
    {"year": 2023, "text": "GPT-4 in radiology"}
]

ai_offsets = generate_offsets(len(ai_milestones), [1.4, 1.2, 1.0, 0.8])
medical_offsets = generate_offsets(len(medical_ai), [-0.2, -0.4, -0.6, -0.8])

fig, ax = plt.subplots(figsize=(12, 6))

for milestone, default_offset in zip(ai_milestones, ai_offsets):
    year = milestone["year"]
    event = milestone["text"]
    milestone_offset = milestone.get("offset", default_offset)
    ax.scatter(year, 1, color="darkturquoise",
               s=100, edgecolors="black", zorder=2)
    ax.annotate(f"{event}\n({year})", (year, 1), xytext=(year, milestone_offset), ha="center", fontsize=8, weight="bold",
                bbox=dict(facecolor="darkturquoise", alpha=0.6),
                arrowprops=dict(arrowstyle="-", color="gray", linestyle="dashed"))

for milestone, default_offset in zip(medical_ai, medical_offsets):
    year = milestone["year"]
    event = milestone["text"]
    milestone_offset = milestone.get("offset", default_offset)
    ax.scatter(year, 0, color="orchid",
               s=100, edgecolors="black", zorder=2)
    ax.annotate(f"{event}\n({year})", (year, 0), xytext=(year, milestone_offset), ha="center", fontsize=8, weight="bold",
                bbox=dict(facecolor="orchid", alpha=0.6),
                arrowprops=dict(arrowstyle="-", color="gray", linestyle="dashed"))

ax.plot([1940, 2025], [1, 1], "gray", linestyle="dashed",
        alpha=0.6)  # AI milestones line
ax.plot([1940, 2025], [0, 0], "gray", linestyle="dashed",
        alpha=0.6)  # Medical imaging AI line

ax.text(1970, 0.3, "First winter of AI", fontsize=16, color="black",
        weight="bold", bbox=dict(facecolor="lightcoral", alpha=0.7))
ax.text(1990, 0.3, "Second winter of AI", fontsize=16, color="black",
        weight="bold", bbox=dict(facecolor="lightcoral", alpha=0.7))

ax.set_xlim(1940, 2025)
ax.set_ylim(-0.9, 1.7)
ax.set_yticks([])
ax.set_xticks(range(1940, 2030, 10))
ax.set_title("AI and Medical Imaging Milestones Timeline", fontsize=14)
fig.set_size_inches(16, 12)
plt.savefig(f"Cap1/Figures/{__file__.split('/')[-1].replace('.py', '.png')}")


ai_offsets = generate_offsets(len(ai_milestones), [1.4, 1.2, 1.0, 0.8])
medical_offsets = generate_offsets(
    len(medical_ai), [0, -0.2, -0.4, -0.6, -0.8])

fig, ax = plt.subplots(figsize=(12, 6))
