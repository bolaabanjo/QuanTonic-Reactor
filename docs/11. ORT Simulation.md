# Section 11: Optical Ray Trace Simulation

## Overview

In this section, we simulate the optical behavior of photons emitted from the QT-Reactor's thermal emitter. The goal is to quantify how much radiated energy successfully reaches the TPV cell after interacting with intermediate layers — including the spectral filter, vacuum gap, and reflective mirror. This simulation acts as a validation of the system’s optical efficiency and helps identify design optimizations for maximal photon delivery and spectral alignment.

We treat the thermal emitter as a Lambertian source operating at ~1800 K, emitting according to the blackbody distribution modulated by an engineered spectral emissivity profile, ε(λ). The photons are subject to geometrical constraints, material interfaces, and selective transmission windows before reaching the TPV surface.

---

## Simulation Objectives

- Model photon emission paths from the emitter surface
- Evaluate angular and spectral transmission through the spectral filter
- Quantify the photon incidence rate on the TPV cell
- Compute escape loss, internal reflection, and back-reflection contribution
- Estimate the net spectral power reaching the TPV cell (W/m²·sr)
- Visualize ray paths to demonstrate photon behavior inside the stack

---

## Theoretical Basis

### Planck Radiation Emission

The radiance of a blackbody at temperature $$\( T \)$$ is given by the Planck function:

$$\[
I(\lambda, T) = \frac{2hc^2}{\lambda^5} \cdot \frac{1}{e^{\frac{hc}{\lambda kT}} - 1}
\]$$

Where:
- $$\( I(\lambda, T) \)$$ is the spectral radiance $$(W·sr⁻¹·m⁻³)$$
- $$\( h \)$$ is Planck’s constant $$(\(6.626 \times 10^{-34}\) J·s)$$
- $$\( c \)$$ is the speed of light $$(\(3.0 \times 10^8\) m/s)$$
- $$\( k \)$$ is Boltzmann’s constant $$(\(1.381 \times 10^{-23}\) J/K)$$
- $$\( \lambda \)$$ is the wavelength $$(m)$$
- $$\( T \)$$ is the emitter temperature $$(K)$$

This defines the initial spectral power emitted per unit area, angle, and wavelength.

---

### Lambertian Emission

For most real surfaces — especially thermal ones like tungsten — radiation follows Lambert’s cosine law. The power emitted at angle \( \theta \) from the normal is:

$$\[
I(\lambda, \theta) = I(\lambda, 0) \cdot \cos(\theta)
\]$$

This results in isotropic hemispherical emission, which must be ray-traced over the full angular range (0° to 90°).

---

### Spectral Filter Transfer Function

The spectral filter enforces a custom transmission window:

$$\[
T(\lambda) = 
\begin{cases}
1 & \text{if } \lambda_{\text{min}} \leq \lambda \leq \lambda_{\text{max}} \\
0 & \text{otherwise}
\end{cases}
\]$$

Typical bounds:
- $$\( \lambda_{\text{min}} \approx 0.4\ \mu m \)$$
- $$\( \lambda_{\text{max}} \approx 1.1\ \mu m \)$$

Photons outside this band are either reflected back toward the emitter or absorbed.

---

## Geometry Setup

- Emitter diameter: 90 mm
- Gap (vacuum): 1 mm
- Spectral filter: transparent disc (optical glass)
- TPV surface: flat, directly beneath the filter
- Mirror: silvered back layer

All components are coaxial and parallel to one another.

---

## Ray Trace Simulation Methodology

### Emission Source

- Rays are emitted from the emitter surface at random points
- Each ray is assigned:
  - A direction (randomized in a Lambertian cone)
  - A wavelength (sampled from the Planck distribution at T=1800K)

### Propagation Logic

1. Each ray hits the spectral filter.
   - If $$\( \lambda \in [0.4, 1.1]\ \mu m \)$$: transmit
   - Else: reflect back

2. Transmitted rays proceed through vacuum gap to TPV.
   - Compute incidence angle and spatial hit position

3. Absorbed at TPV = success  
   Reflected at TPV = tracked bounce  
   Missed TPV (escaped system) = counted as loss

4. Rays hitting the mirror:
   - Reflect back and re-run logic

### View Factor

The **view factor** $$\( F_{ET} \)$$ between the emitter and the TPV can be computed analytically for disc-disc geometries or numerically via Monte Carlo integration.

---

## Expected Metrics

| Metric | Definition | Estimated Range |
|--------|------------|-----------------|
| Angular Acceptance (TPV) | % of rays hitting TPV within working cone | 40–60% |
| Spectral Transmission Efficiency | Filter pass band vs. total emitted | ~15% |
| Optical Path Efficiency | Net % of rays absorbed at TPV | 10–25% |
| Escape Ratio | Rays leaving system unabsorbed | 30–50% |

---

## Visualization

You are encouraged to plot:

- Photon path traces (lines from emitter to TPV or mirror)
- Intensity density map on TPV surface
- Spectral power histogram before/after filter

**Optional Tools**:
- [Raysect](https://github.com/raysect/source): Python-based ray-tracing engine
- [openRayTrace](https://github.com/OpenRayTrace/OpenRayTrace): C++/Python for ray simulation
- Blender + scripting (Cycles emission sources)

---

## Next Steps

- Implement Python-based Monte Carlo ray trace (100k+ rays)
- Record % of rays reaching TPV vs escaping
- Integrate result into efficiency model (Section 12)
- Begin coupling optical simulation with thermal map (next section)

---

## References

- Siegel & Howell, “Thermal Radiation Heat Transfer”
- Modest, “Radiative Heat Transfer”
- [NREL TPV Design Resources](https://www.nrel.gov/)
- Wien, M. (2020). “Ray Tracing for Radiant Energy Conversion Devices.”

---
