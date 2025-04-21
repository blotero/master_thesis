import graphviz

# Create a new directed graph
dot = graphviz.Digraph(
    "Solution Architecture", comment="Overall Solution Architecture"
)
dot.attr(rankdir="TB", size="8,5")
dot.attr("node", shape="box", style="filled", fillcolor="lightblue")
dot.attr("edge", color="gray50")

# Add nodes for the main components
with dot.subgraph(name="cluster_0") as c:
    c.attr(label="Feature Extraction")
    c.attr(style="filled", color="lightgray")
    c.node("input", "Input Data")
    c.node("gp1", "Gaussian Process 1")
    c.node("gp2", "Gaussian Process 2")
    c.node("gp3", "Gaussian Process 3")
    c.node("features", "Extracted Features")

    # Connect GP chain
    c.edge("input", "gp1")
    c.edge("gp1", "gp2")
    c.edge("gp2", "gp3")
    c.edge("gp3", "features")

with dot.subgraph(name="cluster_1") as c:
    c.attr(label="UNet CNN Architecture")
    c.attr(style="filled", color="lightgray")
    c.node("unet", "UNet with ResNet34 Backbone")
    c.node("imagenet", "ImageNet Pretrained Weights")

    # Connect UNet components
    c.edge("imagenet", "unet")

with dot.subgraph(name="cluster_2") as c:
    c.attr(label="Custom Loss Function")
    c.attr(style="filled", color="lightgray")
    c.node("loss", "Annotator Reliability Loss")
    c.node("annotators", "Multiple Annotators")

    # Connect loss components
    c.edge("annotators", "loss")

# Connect main components
dot.edge("features", "unet")
dot.edge("unet", "loss")

# Save and render the diagram
dot.render("../Cap5/Figures/solution_architecture", format="png", cleanup=True)
