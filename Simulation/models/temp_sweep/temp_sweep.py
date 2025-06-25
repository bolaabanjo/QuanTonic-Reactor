import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k
from scipy.integrate import simpson

# --- Reuse simulation functions from planck_emission.py ---

def planck_spectral_radiance(wavelength, temperature):
    exponent = h * c / (wavelength * k * temperature)
    pre_factor = 2 * h * c**2 / wavelength**5
    return pre_factor / (np.exp(exponent) - 1)

def emissivity_function(wavelength, lambda_min, lambda_max):
    eps = np.zeros_like(wavelength)
    eps[(wavelength >= lambda_min) & (wavelength <= lambda_max)] = 1.0
    return eps

def modified_radiance(wavelength, temperature, lambda_min, lambda_max):
    I_bb = planck_spectral_radiance(wavelength, temperature)
    eps = emissivity_function(wavelength, lambda_min, lambda_max)
    return eps * I_bb

def integrated_power(wavelength, spectral_radiance):
    return simpson(spectral_radiance, wavelength)

# --- Sweep Settings ---

# Fixed wavelength range
λ = np.linspace(0.2e-6, 5.0e-6, 1000)

# Fixed emissive band: 0.4 µm – 1.1 µm
λ_min = 0.4e-6
λ_max = 1.1e-6

# Temperature sweep from 1000 K to 2500 K
T_range = np.arange(1000, 2600, 100)

# Storage for results
P_bb_list = []
P_mod_list = []

for T in T_range:
    I_bb = planck_spectral_radiance(λ, T)
    I_mod = modified_radiance(λ, T, λ_min, λ_max)
    P_bb = integrated_power(λ, I_bb)
    P_mod = integrated_power(λ, I_mod)
    
    P_bb_list.append(P_bb)
    P_mod_list.append(P_mod)

# --- Plotting ---
plt.figure(figsize=(10, 6))
plt.plot(T_range, P_bb_list, label='Total Radiated Power', color='red', linewidth=2)
plt.plot(T_range, P_mod_list, label='Filtered Usable Power', color='blue', linewidth=2)

plt.title('Power Output vs Emitter Temperature', fontsize=16)
plt.xlabel('Emitter Temperature (K)', fontsize=14)
plt.ylabel('Radiated Power (W/m²·sr)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save plot
plt.savefig("temp_sweep.png", dpi=300)
plt.show()
