# Simulation Module: Planck Radiation & Emissivity Integrator

import numpy as np
from scipy.constants import h, c, k
from scipy.integrate import simps

def planck_spectral_radiance(wavelength, temperature):
    """
    Calculate ideal blackbody spectral radiance I(λ, T).
    
    Parameters:
        wavelength (ndarray): Wavelength array in meters.
        temperature (float): Absolute temperature in Kelvin.
        
    Returns:
        ndarray: Spectral radiance values (W / (m^2 · sr · m)).
    """
    # Planck’s Law: I(λ, T) = (2hc^2/λ^5) * 1/(exp(hc/(λkT)) - 1)
    exponent = h * c / (wavelength * k * temperature)
    pre_factor = 2 * h * c**2 / wavelength**5
    return pre_factor / (np.exp(exponent) - 1)


def emissivity_function(wavelength, lambda_min, lambda_max):
    """
    Define a simple step-function emissivity ε(λ):
      ε = 1 for λ in [lambda_min, lambda_max], else 0.
      
    Parameters:
        wavelength (ndarray): Wavelength array in meters.
        lambda_min (float): Lower bound of emissive band (m).
        lambda_max (float): Upper bound of emissive band (m).
        
    Returns:
        ndarray: Emissivity values (0 or 1).
    """
    eps = np.zeros_like(wavelength)
    mask = (wavelength >= lambda_min) & (wavelength <= lambda_max)
    eps[mask] = 1.0
    return eps


def modified_radiance(wavelength, temperature, lambda_min, lambda_max):
    """
    Compute spectral radiance after applying emissivity ε(λ).
    
    Parameters:
        wavelength (ndarray): Wavelength array in meters.
        temperature (float): Emitter temperature in Kelvin.
        lambda_min (float): Lower bound of emissive band (m).
        lambda_max (float): Upper bound of emissive band (m).
        
    Returns:
        ndarray: Modified spectral radiance.
    """
    I_bb = planck_spectral_radiance(wavelength, temperature)
    eps = emissivity_function(wavelength, lambda_min, lambda_max)
    return eps * I_bb


def integrated_power(wavelength, spectral_radiance):
    """
    Numerically integrate spectral radiance over wavelength.
    
    Parameters:
        wavelength (ndarray): Wavelength array in meters.
        spectral_radiance (ndarray): Radiance values (W/(m^2·sr·m)).
        
    Returns:
        float: Total radiated power (W/(m^2·sr)).
    """
    # Use Simpson’s rule for numerical integration
    return simps(spectral_radiance, wavelength)


if __name__ == "__main__":
    # Example usage
    # Define wavelength range (0.2 µm to 5 µm)
    λ = np.linspace(0.2e-6, 5e-6, 1000)
    T_e = 1500  # Emitter temperature in Kelvin
    λ_min = 0.4e-6  # Lower emissive bound (e.g., PV bandgap)
    λ_max = 1.1e-6  # Upper emissive bound

    # Compute spectra
    I_bb = planck_spectral_radiance(λ, T_e)
    I_mod = modified_radiance(λ, T_e, λ_min, λ_max)

    # Compute integrated power
    P_bb = integrated_power(λ, I_bb)
    P_mod = integrated_power(λ, I_mod)

    print(f"Ideal blackbody power: {P_bb:.3e} W/m^2·sr")
    print(f"Emissivity-filtered power: {P_mod:.3e} W/m^2·sr")
