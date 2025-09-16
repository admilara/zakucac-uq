# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 09:45:26 2025

@author: Tin Pakasin
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# ======= EDIT THESE LIMITS =======
# Q in Mvar (left<0 capacitive, right>0 inductive), P in MW
Q_kapmin = -100     # left tick label position (capacitive min)
Q_indmax =  100    # right tick label position (inductive max)
Q_box_min, Q_box_max = -100, 100   # rectangle left/right
P_box_min, P_box_max =  40, 100  # rectangle bottom/top
# Axis ranges (pad so the box isn’t cramped)
Q_min, Q_max = -150, 150
P_min, P_max = 0, 150
# =================================

fig, ax = plt.subplots(figsize=(5.5, 5.0), dpi=300)

ax.xaxis.set_major_locator(MultipleLocator(20))  # every 0.5
ax.xaxis.set_minor_locator(MultipleLocator(20))  # every 0.1
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


# Capability rectangle
rect = plt.Rectangle((Q_box_min, P_box_min),
                     Q_box_max - Q_box_min, P_box_max - P_box_min,
                     fill=False, linewidth=1.5, edgecolor="black")#,
#                     hatch="/", hatch_linewidth=0.3, zorder=3)
ax.add_patch(rect)

ax.text(2, P_box_max+1, r"$P_{\mathrm{max}}$", ha="left", va="bottom", fontsize=10, clip_on=False)
ax.text(2, P_box_min-2, r"$P_{\mathrm{min}}$", ha="left", va="top", fontsize=10, clip_on=False)
#ax.text(2, 2)
# Labels
ax.set_xlabel("")
ax.text(Q_max - 20, -7, "Q (Mvar)", ha="left", va="center", fontsize=11)

# Remove the default ylabel
ax.set_ylabel("")
ax.text(0, P_max + 0.05, "P (MW)", ha="center", va="bottom", fontsize=11)

# Custom ticks: show only Q_kapmin / Q_indmax on x; none on y
ax.set_xticks([Q_kapmin, 0, Q_indmax])
ax.set_xticklabels([r"$Q_{\mathrm{min}}$", "0", r"$Q_{\mathrm{max}}$"])
ax.set_yticks([])


ax.vlines(Q_box_min, 0, P_box_min, linestyles="dotted", colors="black")
ax.vlines(Q_box_max, 0, P_box_min, linestyles="dotted", colors="black")

# Limits & proportions
ax.set_xlim(Q_min, Q_max)
ax.set_ylim(P_min, P_max)
#ax.set_aspect('equal', adjustable='box')  # 1:1 look (engineering style)

# Clean frame
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)



plt.tight_layout()
#plt.grid(True)
#plt.savefig("pq-capability-no-grid.pdf")   # crisp vector
#plt.savefig("pq-capability-no-grid.svg")   # optional SVG
plt.savefig("pq-grid-no-hatch.png")
print("Saved: pq_capability.pdf / .svg")