# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 09:49:35 2025

@author: admilara
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon
# ===== editable =====
xmin, xmax = -1.2, 1.2
ymin, ymax = -1.2, 1.2
band = 0.1          # set to 0.05 for ±5% band; 0 for none
# ====================

fig, ax = plt.subplots(figsize=(6.2, 5.2), dpi=300)

# Axes with arrowheads
ax.axhline(0, color="black", linewidth=1.2)
ax.axvline(0, color="black", linewidth=1.2)
ax.annotate("", xy=(xmax, 0), xytext=(xmax-1e-9, 0),
            arrowprops=dict(arrowstyle="-|>", lw=1.2))
ax.annotate("", xy=(0, ymax), xytext=(0, ymax-1e-9),
            arrowprops=dict(arrowstyle="-|>", lw=1.2))

ax.set_yticklabels([-1,1])

# --- main droop (clamped) ---
# central sloped segment
ax.plot([-1, 1], [1, -1], color="black", lw=1.5)

# horizontal saturations
ax.hlines(1, xmin, -1, color="black", lw=1.5)   # flat at y=+1 for x<-1
ax.hlines(-1, 1, xmax, color="black", lw=1.5)   # flat at y=-1 for x>1

# --- optional ±band that also clamps horizontally ---
if band > 0:
    # central sloped band lines
    ax.plot([-1, 1], [1+band, -1+band], ls="--", color="black", lw=1.0)
    ax.plot([-1, 1], [1-band, -1-band], ls="--", color="black", lw=1.0)
    # vertical clamps for the band
    ax.plot([-1, xmin], [1+band, 1+band], ls="--", color="black", lw=1.0)
    ax.plot([-1, xmin], [1-band, 1-band], ls="--", color="black", lw=1.0)
    ax.plot([ 1,  xmax], [-1+band, -1+band], ls="--", color="black", lw=1.0)
    ax.plot([ 1,  xmax], [-1-band, -1-band], ls="--", color="black", lw=1.0)
    

# Labels / ticks
# remove default labels
ax.set_xlabel("")
ax.set_ylabel("")

# add custom labels at arrow tips
#ax.text(xmax - 0.2, -0.1, r"$U_{VN}$ (p.u.)",
#        ha="left", va="center", fontsize=11)

#ax.text(0, ymax + 0.05, r"$Q_{VN}/Q_{max}$ (p.u.)",
#        ha="center", va="bottom", fontsize=11)

ax.annotate("+5 Mvar\nili\n+5% " + r"$Q_{max}$",
            xy=(-0.5, 0.6),         # point on the band line (target)
            xytext=(-0.1, 0.8),      # position of the text (adjust to taste)
            textcoords="data",
            fontsize=9, ha="right", va="center",
            arrowprops=dict(arrowstyle="->", lw=0.8, color="black"))

# Example for the -5% label (left side)
ax.annotate("-5 Mvar\nili\n-5% " + r"$Q_{max}$",
            xy=(0.5, -0.6),         # point on the band line (target)
            xytext=(0.1, -0.8),      # text position
            textcoords="data",
            fontsize=9, ha="left", va="center",
            arrowprops=dict(arrowstyle="->", lw=0.8, color="black"))

ax.annotate("$U_{VN, ref}$",
            xy=(0.0, 0.0),         # point on the band line (target)
            xytext=(0.2, 0.2),      # text position
            textcoords="data",
            fontsize=9, ha="left", va="center",
            arrowprops=dict(arrowstyle="->", lw=0.8, color="black"))

ax.set_xticks([-1, 1])
ax.set_xticklabels([])


ax.set_yticks([-1, 1])

# Styling
ax.set_xlim(xmin, xmax); ax.set_ylim(ymin, ymax)
for s in ("top", "right"): ax.spines[s].set_visible(False)
plt.tight_layout()
#plt.savefig("uq-staticka-grid-color.pdf"); #plt.savefig("uq-staticka-grid-color.svg")


plt.savefig("uq-staticka-no-grid-bnw.png")
print("Saved droop_qu_clamped.pdf / .svg")




