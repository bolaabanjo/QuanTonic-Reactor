#!/usr/bin/env python3
"""
plot_radiance.py

Plots spectral radiance curves of:
1. Ideal blackbody emission I(λ)
2. Emissivity-filtered emission I_mod(λ)

Used to visualize the spectral behavior of the QuanTonic Reactor's emitter system.
"""

import numpy as np
import matplotlib.pyplot as plt
from planck_emission import planck_spectral_radiance, modified_radiance

# Define wavelength range (meters)
λ = np.linspace(0.2e-6, 5e-6, 1000)  # 0.2 µm to 5 µm

# Emitter temperature (Kelvin)
T_e = 1500

# Emissive bandpass window (meters)
λ_min = 0.4e-6
λ_max = 1.1e-6

# Calculate radiance curves
I_bb = planck_spectral_radiance(λ, T_e)
I_mod = modified_radiance(λ, T_e, λ_min, λ_max)

# Convert wavelength to micrometers for plotting
λ_um = λ * 1e6

# Plot setup
plt.figure(figsize=(10, 6))
plt.plot(λ_um, I_bb, label='Blackbody Radiance (I)', color='red', linewidth=2)
plt.plot(λ_um, I_mod, label='Filtered Radiance (I_mod)', color='blue', linewidth=2)

# Bandpass window for visual context
plt.axvspan(λ_min * 1e6, λ_max * 1e6, color='grey', alpha=0.2, label='ε(λ) = 1 Region')

# Labels & Aesthetics
plt.title('Spectral Radiance vs. Wavelength', fontsize=16)
plt.xlabel('Wavelength (µm)', fontsize=14)
plt.ylabel('Spectral Radiance (W/m²·sr·m)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save figure (optional for GitHub or Colab)
plt.savefig("radiance_plot.png", dpi=300)
plt.show()
