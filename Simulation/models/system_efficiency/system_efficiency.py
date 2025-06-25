"""
system_efficiency.py

Calculates system-wide efficiency of the QuanTonic Reactor:
η_total(T) = η_thermal(T) × η_pv
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k
from scipy.integrate import simpson

# --- Physical Constants & Functions ---

def planck_spectral_radiance(wavelength, temperature):
    exponent = h * c / (wavelength * k * temperature)
    pre_factor = 2 * h * c**2 / wavelength**5
    return pre_factor / (np.exp(exponent) - 1)

def η_thermal(wavelength, temperature, λ_cutoff):
    """
    Calculates thermal efficiency = usable radiative energy / total radiative energy
    """
    I = planck_spectral_radiance(wavelength, temperature)
    I_usable = np.copy(I)
    I_usable[wavelength > λ_cutoff] = 0

    P_total = simpson(I, wavelength)
    P_usable = simpson(I_usable, wavelength)

    return P_usable / P_total

# --- PV Settings ---

λ_cutoff = 1.8e-6  # GaSb bandgap = ~0.7 eV
η_pv = 0.35        # Realistic quantum efficiency of GaSb

# --- Sweep Setup ---

λ = np.linspace(0.2e-6, 5.0e-6, 1000)  # Wavelength domain
T_range = np.arange(1000, 2600, 100)   # Emitter temperature domain

η_thermal_list = []
η_total_list = []

for T in T_range:
    η_th = η_thermal(λ, T, λ_cutoff)
    η_thermal_list.append(η_th)
    η_total_list.append(η_th * η_pv)

# --- Plotting ---

plt.figure(figsize=(10, 6))
plt.plot(T_range, np.array(η_thermal_list)*100, label='Thermal Efficiency η_thermal (%)', color='orange', linewidth=2)
plt.plot(T_range, np.array(η_total_list)*100, label='System Efficiency η_total (%)', color='green', linewidth=2)

plt.title('QuanTonic Reactor Efficiency vs Emitter Temperature', fontsize=16)
plt.xlabel('Emitter Temperature (K)', fontsize=14)
plt.ylabel('Efficiency (%)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig("system_efficiency.png", dpi=300)
plt.show()
