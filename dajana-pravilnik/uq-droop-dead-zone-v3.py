# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 12:09:06 2025

@author: admilara
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from math import sqrt
# ================== PARAMETERS ==================
Qmax = 1.0       # per-unit
Qmin = -1.0      # can set to e.g. -0.8
s    = 0.05      # droop slope
DZU  = 0.01      # dead-zone ±1%
band = -0.1       # tolerance band around Qs

Uref = 1.0
U    = np.arange(0.90, 1.10 + 1e-12, 0.001)

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
ax.plot(dU, Qs, lw=1.8, color="black", label="Qs")

# Band around Qs

upper = np.clip(Qs + band, Qmin/Qmax-0.1, Qmax/Qmax+0.1)
lower = np.clip(Qs - band, Qmin/Qmax-0.1, Qmax/Qmax+0.1)
ax.plot(dU, upper, ls="--", lw=1.0, color="black")
ax.plot(dU, lower, ls="--", lw=1.0, color="black")
ax.fill_between(dU, lower, upper, color="gray", alpha=0.2)

# Dead-zone markers
ax.axvline(-DZU, color="black", lw=1.0, linestyle="--")
ax.axvline(+DZU, color="black", lw=1.0, linestyle="--")

# Saturation reference lines
ax.axhline(1.0,  color="black", lw=1.0, linestyle=":")
ax.axhline(Qmin/Qmax, color="black", lw=1.0, linestyle=":")


xmax=0.1
ymax=1.2
# Axes with arrowheads
ax.axhline(0, color="black", linewidth=1.0)
ax.axvline(0, color="black", linewidth=1.0)
ax.annotate("", xy=(xmax, 0), xytext=(xmax-1e-9, 0),
            arrowprops=dict(arrowstyle="-|>", lw=1.2))
ax.annotate("", xy=(0, ymax), xytext=(0, ymax-1e-9),
            arrowprops=dict(arrowstyle="-|>", lw=1.2))
ax.annotate("$Q/Q_{max}$", xy=(dU.max(), 0), xytext=(dU.max()-1e-9, 0))
ax.annotate("$U_{ref}$", xy=(0, 1.15), xytext=(0, 1.15-0.01))

ax.annotate("-5 Mvar\nili\n-5% " + r"$Q_{max}$",
            xy=(-0.04, 0.5),         # point on the band line (target)
            xytext=(-0.05, 0.15),      # position of the text (adjust to taste)
            textcoords="data",
            fontsize=9, ha="right", va="center",
            arrowprops=dict(arrowstyle="->", lw=0.8, color="black"))

# Example for the -5% label (left side)
ax.annotate("+5 Mvar\nili\n+5% " + r"$Q_{max}$",
            xy=(0.04, -0.5),         # point on the band line (target)
            xytext=(0.05, -0.15),      # text position
            textcoords="data",
            fontsize=9, ha="left", va="center",
            arrowprops=dict(arrowstyle="->", lw=0.8, color="black"))

ax.annotate("$U_{VN, ref}$",
            xy=(0.0, 0.0),         # point on the band line (target)
            xytext=(0.02, 0.2),      # text position
            textcoords="data",
            fontsize=9, ha="left", va="center",
            arrowprops=dict(arrowstyle="->", lw=0.8, color="black"))



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

# Limits symmetric around zero
xmax = max(abs(dU.min()), abs(dU.max()))
ax.set_xlim(-xmax, xmax)
ax.set_ylim((Qmin/Qmax) - 0.2, 1.2)

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig("qs_vs_dU_with_band.png")
print("Saved: qs_vs_dU_with_band.png")
