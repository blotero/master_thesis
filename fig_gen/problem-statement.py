from graphviz import Digraph

dot = Digraph("Problem Statement", format="png")

# Set global styles
dot.attr(kw="graph", fontname="Verdana")
dot.attr(kw="node", fontname="Verdana")
dot.attr(kw="edge", fontname="Times-Italic")

# Main problem node
dot.node(
    "P",
    "Inter-Observer Variability\nin Medical Image Segmentation",
    shape="box",
    style="filled",
    fillcolor="lightblue",
    fontsize="14",
    fontcolor="black",
    penwidth="2",
    height="1.5",
)

causes_kwargs = {
    "shape": "ellipse",
    "style": "filled",
    "fillcolor": "#ffcc99",
    "fontsize": "12",
    "height": "1",
}

# SubCauses
dot.node("SC1", "Variability in Expertise", **causes_kwargs)
dot.node("SC2", "Bias from Guidelines", **causes_kwargs)

# Causes
dot.node("C1", "Subjectivity in Interpretation", **causes_kwargs)
dot.node("C2", "Technical Constraints", **causes_kwargs)

# Consequences
dot.node(
    "E1",
    "Noisy & Inconsistent Labels",
    shape="diamond",
    style="filled",
    fillcolor="peachpuff",
    fontsize="12",
    height="1",
)
dot.node(
    "E2",
    "Decreased reliability in CNN models",
    shape="diamond",
    style="filled",
    fillcolor="lightcoral",
    fontsize="12",
    height="1",
)


# Edges with styles
dot.edge(
    "SC1", "C1", style="dashed", color="black", penwidth="1.5", label="Lead to"
)
dot.edge(
    "SC2", "C1", style="dashed", color="black", penwidth="1.5", label="Lead to"
)
dot.edge("C1", "P", style="dashed", color="black", penwidth="1.5")
dot.edge("C2", "P", style="dashed", color="black", penwidth="1.5")

dot.edge("P", "E1", color="darkred", penwidth="2", label="Consequences")
dot.edge("E1", "E2", color="darkred", penwidth="2")


# Render and view
dot.render("Cap1/Figures/problem_statement_diagram")
