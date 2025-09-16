# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 11:50:57 2025

@author: admilara
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# ================== EDITABLE PARAMETERS ==================
Qmax = 1.0          # per instructions
Qmin = -1.0         # can be e.g. -0.8
s    = 0.05         # droop sensitivity
DZU  = 0.01         # dead zone half-width (±1%)

Uref = 1.0
U    = np.arange(0.90, 1.10 + 1e-12, 0.001)   # 0.90:0.001:1.10

PLOT_MODE = "U"     # "U" -> plot Qs(U), "dU" -> plot Qs(dU)
# =========================================================

def compute_Qs(U, Uref, s, DZU, Qmin, Qmax):
    dU = U - Uref
    # raw droop with dead zone: -1/s * (dU - sign(dU)*DZU) for |dU| >= DZU, else 0
    mask = np.abs(dU) >= DZU
    raw  = (-1.0 / s) * (dU - np.sign(dU) * DZU)
    Qs   = np.where(mask, raw, 0.0)
    # normalize to pu of Qmax and clamp to [Qmin/Qmax, Qmax/Qmax]
    Qs   = np.clip(Qs / Qmax, Qmin / Qmax, Qmax / Qmax)
    return dU, Qs

dU, Qs = compute_Qs(U, Uref, s, DZU, Qmin, Qmax)

# ===================== PLOTTING ==========================
fig, ax = plt.subplots(figsize=(6.5, 5.2), dpi=300)

# Choose x-axis variable
if PLOT_MODE.lower() == "du":
    x = dU
    x_label = r"$\Delta U = U - U_{\mathrm{ref}}$ (p.u.)"
    x_dead_left, x_dead_right = -DZU, DZU
    xmin, xmax = dU.min(), dU.max()
else:
    x = U
    x_label = r"$U_{VN}$ (p.u.)"
    x_dead_left, x_dead_right = Uref - DZU, Uref + DZU
    xmin, xmax = U.min(), U.max()

# Axes with arrowheads
ax.axhline(0, color="black", linewidth=1.2)
ax.axvline(0 if PLOT_MODE.lower() == "du" else Uref, color="black", linewidth=1.0, linestyle="-", alpha=0.6)

ax.annotate("", xy=(xmax, 0), xytext=(xmax - 1e-9, 0),
            arrowprops=dict(arrowstyle="-|>", lw=1.2, color="black"))
# y-axis arrow at top
ymax_plot = 1.15
ax.annotate("", xy=(x.min(), ymax_plot), xytext=(x.min(), ymax_plot - 1e-9),
            arrowprops=dict(arrowstyle="-|>", lw=1.2, color="black"))

# Main curve
ax.plot(x, Qs, lw=1.8, color="black", label=r"$Q_s/Q_{\max}$")

# Dead-zone markers (vertical dashed lines)
ax.axvline(x_dead_left, color="black", lw=1.0, linestyle="--")
ax.axvline(x_dead_right, color="black", lw=1.0, linestyle="--")

# Saturation reference lines
ax.axhline(1.0,  color="black", lw=1.0, linestyle=":")
ax.axhline(Qmin / Qmax, color="black", lw=1.0, linestyle=":")

# Grid
ax.grid(which="major", linestyle=":", linewidth=0.5, alpha=0.8)
ax.xaxis.set_major_locator(MultipleLocator(0.02 if PLOT_MODE.lower()=="du" else 0.02))
#ax.yaxis.set_major_locator(MultipleLocator(0.1))

# Labels
ax.set_xlabel(x_label, fontsize=11)
ax.set_ylabel(r"$Q_{VN}/Q_{\max}$ (p.u.)", fontsize=11)

# Helpful annotations
if PLOT_MODE.lower() == "du":
    ax.text(0.0, 1.06, r"$\Delta U = 0$", ha="center", va="bottom", fontsize=9)
else:
    ax.text(Uref, 1.06, r"$U_{\mathrm{ref}}$", ha="center", va="bottom", fontsize=9)

ax.text(x_dead_left-0.01, 1.06,  r"$-\mathrm{DZU}$", ha="center", va="bottom", fontsize=9)
ax.text(x_dead_right+0.01, 1.06, r"$+\mathrm{DZU}$", ha="center", va="bottom", fontsize=9)
ax.text(x.min()+0.002, 1.01, r"$Q_{\max}/Q_{\max}=1$", ha="left", va="bottom", fontsize=9)
ax.text(x.min()+0.002, (Qmin/Qmax)-0.06, r"$Q_{\min}/Q_{\max}$", ha="left", va="top", fontsize=9)

# Limits & styling
xpad = 0.01 * (xmax - xmin)
ax.set_xlim(xmin - xpad, xmax + xpad)
ax.set_ylim((Qmin / Qmax) - 0.15, 1.15)

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

plt.tight_layout()

fname = f"qs_vs_{'dU' if PLOT_MODE.lower()=='du' else 'U'}.png"
plt.savefig(fname)
print(f"Saved: {fname}")
