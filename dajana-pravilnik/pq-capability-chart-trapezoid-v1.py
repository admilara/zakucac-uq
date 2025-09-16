# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 09:48:07 2025

@author: Tin Pakasin
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon

# ======= EDIT THESE LIMITS =======
# Q in Mvar (left<0 capacitive, right>0 inductive), P in MW
# Tick label positions (left=capacitive, right=inductive)
Q_kapmin = -120   # left tick label position
Q_indmax =  120   # right tick label position

# Trapezoid definition:
# Top edge (at P_max): Q_min1 ... Q_max1
# Bottom edge (at P_min): Q_min2 ... Q_max2
# Must satisfy: Q_min2 < Q_min1 and Q_max2 > Q_max1
Q_min1, Q_max1 = -60, 60       # top width at P_max
Q_min2, Q_max2 = -120, 120     # bottom width at P_min

P_box_min, P_box_max = 40, 100  # P_min, P_max

# Axis ranges (pad so the shape isn’t cramped)
Q_min, Q_max = -150, 150
P_min, P_max = 0, 150
# =================================

fig, ax = plt.subplots(figsize=(5.5, 5.0), dpi=300)

ax.xaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_minor_locator(MultipleLocator(20))
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.set_minor_locator(MultipleLocator(20))
ax.set_yticklabels([])

# grid lines
ax.grid(which="major", color="lightgray", linestyle=":", linewidth=0.4)
ax.grid(which="minor", color="lightgrey", linestyle=":", linewidth=0.4)

# Axes (with arrows)
ax.axhline(0, color="black", linewidth=1.2)
ax.axvline(0, color="black", linewidth=1.2)
# tiny arrowheads
ax.annotate("", xy=(Q_max, 0), xytext=(Q_max-1e-9, 0),
            arrowprops=dict(arrowstyle="-|>", lw=1.2, color="black"))
ax.annotate("", xy=(0, P_max), xytext=(0, P_max-1e-9),
            arrowprops=dict(arrowstyle="-|>", lw=1.2, color="black"))

# ===== Trapezoid capability area =====
# Vertices are (Q, P) pairs, ordered around the shape
trapezoid_pts = [
    (Q_min1, P_box_max),  # top-left  at P_max
    (Q_max1, P_box_max),  # top-right at P_max
    (Q_max2, P_box_min),  # bottom-right at P_min
    (Q_min2, P_box_min),  # bottom-left at P_min
]

poly = Polygon(trapezoid_pts, closed=True, fill=False, linewidth=1.5, edgecolor="black")
ax.add_patch(poly)

# Labels for P_min / P_max
ax.text(2, P_box_max+1, r"$P_{\mathrm{max}}$", ha="left", va="bottom", fontsize=10, clip_on=False)
ax.text(2, P_box_min-2, r"$P_{\mathrm{min}}$", ha="left", va="top", fontsize=10, clip_on=False)

# Axis labels
ax.set_xlabel("")
ax.text(Q_max - 10, -7, "Q (Mvar)", ha="left", va="center", fontsize=11)

ax.set_ylabel("")
ax.text(0, P_max + 0.05, "P (MW)", ha="center", va="bottom", fontsize=11)

# Custom ticks: show only capacitive/inductive extremes on x; none on y
xticks = [Q_min2, Q_min1, Q_max1, Q_max2]  # Q_min2 < Q_min1 < Q_max1 < Q_max2
ax.set_xticks(xticks)
ax.set_xticklabels([
    r"$Q_{\mathrm{min2}}$",
    r"$Q_{\mathrm{min1}}$",
    r"$Q_{\mathrm{max1}}$",
    r"$Q_{\mathrm{max2}}$",
])
ax.set_yticks([])


# Optional helper lines from top-edge Qs down to P=0 (similar to your rectangle guides)
ax.vlines([Q_min1, Q_max1], 0, P_box_max, linestyles="dotted", colors="black")
ax.vlines([Q_min2, Q_max2], 0, P_box_min, linestyles="dotted", colors="black")

# Limits & proportions
ax.set_xlim(Q_min, Q_max)
ax.set_ylim(P_min, P_max)
# ax.set_aspect('equal', adjustable='box')  # 1:1 look if desired

# Clean frame
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig("pq-trapezoid.png")
print("Saved: pq-trapezoid.png")
