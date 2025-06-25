import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k
from scipy.integrate import simpson

# ----------  Core physics functions  ----------

def planck_spectral_radiance(wavelength, temperature):
    """Blackbody spectral radiance I(λ, Tₑ)."""
    exponent   = h * c / (wavelength * k * temperature)
    pre_factor = 2 * h * c**2 / wavelength**5
    return pre_factor / (np.exp(exponent) - 1)

def emissivity_step(wavelength, lambda_min, lambda_max):
    """Step-function ε(λ): 1 inside [λ_min, λ_max], else 0."""
    eps = np.zeros_like(wavelength)
    eps[(wavelength >= lambda_min) & (wavelength <= lambda_max)] = 1.0
    return eps

def filtered_radiance(wavelength, temperature, lambda_min, lambda_max):
    """I_filtered = ε(λ) · I(λ, Tₑ)."""
    return emissivity_step(wavelength, lambda_min, lambda_max) * \
           planck_spectral_radiance(wavelength, temperature)

# ----------  Simulation parameters  ----------

λ = np.linspace(0.2e-6, 5.0e-6, 1200)   # 0.2 µm → 5 µm (meters)
T_e        = 1800                       # Emitter temperature (Kelvin)
λ_pass_min = 0.4e-6                     # Pass-band lower bound (meters)
λ_pass_max = 1.1e-6                     # Pass-band upper bound (meters)

# ----------  Compute spectra  ----------

I_raw  = planck_spectral_radiance(λ, T_e)
I_filt = filtered_radiance(λ, T_e, λ_pass_min, λ_pass_max)

# ----------  Plotting  ----------

λ_um = λ * 1e6  # meters → micrometres

plt.figure(figsize=(10, 6))
plt.plot(λ_um, I_raw,  label='Raw Radiance  I(λ)',         color='red',  linewidth=2)
plt.plot(λ_um, I_filt, label='Filtered Radiance  Iₑ(λ)',   color='blue', linewidth=2)
plt.axvspan(λ_pass_min*1e6, λ_pass_max*1e6,
            color='grey', alpha=0.2, label='ε(λ)=1  pass-band')

plt.title('Emitter Spectrum  –  Raw vs. ε(λ)-Filtered', fontsize=16)
plt.xlabel('Wavelength  λ  (µm)', fontsize=14)
plt.ylabel('Spectral Radiance  (W / m²·sr·m)', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("filtered_spectrum.png", dpi=300)
plt.show()
