# Planck Emission Simulation Module

## Location
`/simulation/core_math/planck_emission.py`

## Purpose

This module simulates thermal radiation from the QuanTonic Reactor’s emitter using Planck’s Law and applies a wavelength-dependent emissivity filter to calculate the usable portion of the radiated energy.

It forms the foundational mathematical engine for all spectral behavior modeling in the system, feeding into the Spectral Filter and PV Efficiency modules.

---

## Description

### What it Does

- Computes blackbody spectral radiance I(λ, Tₑ) using Planck's Law
- Applies an emissivity function ε(λ) that passes only a selected wavelength band (e.g. 0.4 µm to 1.1 µm)
- Calculates the **ideal** total emitted power and the **filtered** usable power
- Outputs both values in W/m²·sr (watts per square meter per steradian)

---

## Key Equations

**Planck’s Law (Spectral Radiance):**

$$
\[
I(λ, Tₑ) = \frac{2hc^2}{λ^5} \cdot \frac{1}{\exp\left(\frac{hc}{λkTₑ}\right) - 1}
\]
$$

**Emissivity Filtering:**

$$
\[
I_{mod}(λ, Tₑ) = ε(λ) \cdot I(λ, Tₑ)
\]
$$

**Integrated Power:**

$$
\[
P = \int_{\lambda_{min}}^{\lambda_{max}} I(λ, Tₑ) \, dλ
\]
$$

---

## Inputs

| Parameter       | Symbol | Example Value | Description |
|----------------|--------|----------------|-------------|
| Temperature     | Tₑ     | 1500 K         | Emitter temperature |
| Wavelength range | λ     | 0.2 µm – 5 µm  | Simulated wavelength domain |
| Emissive window | [λ₁, λ₂] | 0.4–1.1 µm    | Band where ε(λ) = 1 |
| Resolution      | —      | 1000 points    | Number of wavelength samples |

---

## Output Results

**Run Date:** [Insert your date]  
**Configuration:**  
- Tₑ = 1500 K  
- Emissive band = [0.4 µm – 1.1 µm]

**Results:**
```bash
Ideal blackbody power:           7.624e+04 W/m²·sr 
Emissivity-filtered power:       2.202e+03 W/m²·sr
```

**Usable energy ratio:**  

$$
\[
\frac{P_{filtered}}{P_{ideal}} \approx 2.89\%
\]
$$

---

## File Structure
```bash
/core_math/
└── planck_emission.py   # Main simulation file
```

---

## How to Run

1. Copy `planck_emission.py` into your Python IDE.
2. Make sure SciPy and NumPy are installed.
3. Run the script.
4. It will print both total and filtered power outputs.

> Uses `scipy.integrate.simpson()` for numerical integration

---

## Dependencies

- numpy
- scipy

To install manually:
```bash
pip install numpy scipy
