# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 11:57:34 2025

@author: Tin Pakasin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# ================== PARAMETERS ==================
Qmax = 1.0       # per-unit
Qmin = -1.0      # can set to e.g. -0.8
s    = 0.05      # droop slope
DZU  = 0.01      # dead-zone ±1%

Uref = 1.0
U    = np.arange(0.90, 1.10 + 1e-12, 0.001)

# always plot vs dU so x-axis is centered at 0
# =================================================

def compute_Qs(U, Uref, s, DZU, Qmin, Qmax):
    dU = U - Uref
    mask = np.abs(dU) >= DZU
    raw  = (-1.0 / s) * (dU - np.sign(dU) * DZU)
    Qs   = np.where(mask, raw, 0.0)
    Qs   = np.clip(Qs / Qmax, Qmin / Qmax, Qmax / Qmax)
    return dU, Qs

dU, Qs = compute_Qs(U, Uref, s, DZU, Qmin, Qmax)

# ===================== PLOTTING ==================
fig, ax = plt.subplots(figsize=(6.5, 5.0), dpi=300)

# Main curve
ax.plot(dU, Qs, lw=1.8, color="black")

# Dead-zone markers
ax.axvline(-DZU, color="black", lw=1.0, linestyle="--")
ax.axvline(+DZU, color="black", lw=1.0, linestyle="--")

# Saturation reference lines
ax.axhline(1.0,  color="black", lw=1.0, linestyle=":")
ax.axhline(Qmin/Qmax, color="black", lw=1.0, linestyle=":")

# Axes with arrowheads
ax.axhline(0, color="black", linewidth=1.0)
ax.axvline(0, color="black", linewidth=1.0)
ax.annotate("", xy=(dU.max(), 0), xytext=(dU.max()-1e-9, 0),
            arrowprops=dict(arrowstyle="-|>", lw=1.2))
ax.annotate("", xy=(0, 1.15), xytext=(0, 1.15-1e-9),
            arrowprops=dict(arrowstyle="-|>", lw=1.2))

# Labels
ax.set_xlabel(r"$\Delta U$ (p.u.)", fontsize=11)
ax.set_ylabel(r"$Q_{VN}/Q_{\max}$ (p.u.)", fontsize=11)

# Dead zone annotation
ax.text(-DZU-0.01, 1.05, r"$-\mathrm{DZU}$", ha="center", va="bottom", fontsize=9)
ax.text(+DZU+0.01, 1.05, r"$+\mathrm{DZU}$", ha="center", va="bottom", fontsize=9)
#ax.text(0, 1.07, r"$\Delta U=0$", ha="center", va="bottom", fontsize=9)

# Ticks and grid
ax.xaxis.set_major_locator(MultipleLocator(0.02))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.grid(which="major", linestyle=":", linewidth=0.5, alpha=0.8)

xmin, xmax = -1.2, 1.2
ymin, ymax = -1.2, 1.2
band = 0.1




#xmin, xmax = -1.2, 1.2
#ymin, ymax = -1.2, 1.2
#band = 0.1
#if band > 0:
#    # central sloped band lines
#    ax.plot([-1, 1], [1+band, -1+band], ls="--", color="black", lw=1.0)
#    ax.plot([-1, 1], [1-band, -1-band], ls="--", color="black", lw=1.0)
#    # vertical clamps for the band
#    ax.plot([-1, xmin], [1+band, 1+band], ls="--", color="black", lw=1.0)
#    ax.plot([-1, xmin], [1-band, 1-band], ls="--", color="black", lw=1.0)
#    ax.plot([ 1,  xmax], [-1+band, -1+band], ls="--", color="black", lw=1.0)
#    ax.plot([ 1,  xmax], [-1-band, -1-band], ls="--", color="black", lw=1.0)
    
# Limits symmetric around zero
xmax = max(abs(dU.min()), abs(dU.max()))
ax.set_xlim(-xmax, xmax)
ax.set_ylim((Qmin/Qmax) - 0.1, 1.15)

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig("qs_vs_dU_centered.png")
print("Saved: qs_vs_dU_centered.png")
