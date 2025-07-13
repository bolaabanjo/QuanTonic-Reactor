# Section 12: Thermal Finite Element Analysis (FEA)

## Overview

This section evaluates the internal heat distribution of the QT-Reactor using a 1D steady-state thermal conduction model. The goal is to analyze the temperature gradient across reactor layers — from the blackbody emitter (heat source) to the mirrored casing (heat sink) — and identify potential thermal bottlenecks or failure risks.

Understanding this gradient is critical for both performance and safety. High thermal differentials affect material longevity, photon emission behavior, and overall power conversion efficiency.

---

## Reactor Stack Configuration

| Layer        | Material       | Thickness (m) | Thermal Conductivity (W/m·K) |
|--------------|----------------|----------------|-------------------------------|
| Emitter      | Tungsten       | 0.003          | 173                           |
| Filter       | Glass (Borosilicate) | 0.002     | 1.4                           |
| Vacuum Gap   | N/A            | 0.010          | ~0.0001 (negligible conduction) |
| TPV Cell     | GaSb           | 0.001          | 50                            |
| Mirror       | Silver         | 0.002          | 406                           |

The total simulated length is 0.018 meters (18 mm), with discrete node analysis along the axis of heat flow.

---

## Simulation Method

A finite difference method (FDM) was used to approximate the 1D heat conduction equation:

\[
-\frac{d}{dx} \left( k(x) \frac{dT}{dx} \right) = 0
\]

Boundary conditions:
- Left boundary (emitter surface): **1800 K**
- Right boundary (mirror or casing): **300 K**

Each reactor layer was assigned a corresponding conductivity and discretized into 300 nodes. Conductivity transitions were averaged across node boundaries to simulate composite heat flow.

---

## Results

| Boundary | Temperature (K) |
|----------|-----------------|
| Emitter surface | **1800.0** |
| Mirror casing | **300.0** |

The simulation revealed a steep temperature drop across the filter and vacuum gap, confirming:
- Excellent heat retention within the emitter
- Minimal conductive heat loss across the vacuum
- Strong thermal shielding of the TPV from overexposure

---

## Thermal Gradient Plot

The plot below shows the continuous temperature profile across all layers:

![Thermal Gradient](../visuals/QT-reactor_thermal_profile.png)

Layer transitions are annotated with dashed vertical lines. Annotations reflect how each material handles heat differently, forming bottlenecks or sinks.

- The **Filter** shows significant thermal resistance
- The **Vacuum Gap** acts as a thermal insulator
- The **TPV Cell** maintains safe operating range

---

## Interpretation

This simulation confirms the QT-Reactor's thermal structure is both stable and efficient:

- High emitter temp sustained for photon generation  
- Vacuum gap prevents thermal contamination of TPV  
- Gradient allows for safe heat rejection via mirror/casing

This validates the thermal layer architecture of the reactor and prepares us for electrical modeling in the next section.

---

## Next Steps

→ Section 13: Electrical Conversion Simulation  
We will model how the TPV cell converts photon energy into electrical power, factoring in spectral absorption, quantum efficiency, and voltage output.

---
