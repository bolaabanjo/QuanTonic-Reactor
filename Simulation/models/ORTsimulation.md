# Section 11: Optical Ray Trace Simulation

## Overview

This section simulates the optical behavior of photons emitted from the QT-Reactor's blackbody emitter. Using a Monte Carlo ray trace method, we evaluate how photons interact with the spectral filter, vacuum gap, and thermophotovoltaic (TPV) surface. The objective is to determine the optical efficiency of the reactor — i.e., how many usable photons are successfully captured by the TPV cell versus those lost or reflected.

---

## Simulation Parameters

| Parameter | Value |
|----------:|:------|
| Number of rays | 20,000 |
| Emitter radius | 45 mm |
| TPV radius | 45 mm |
| Emitter temperature | 1800 K |
| Spectral filter band | 0.4 µm – 1.1 µm |
| Gap distance (emitter → TPV) | 10 mm |
| Emission model | Lambertian (cosθ distribution) |
| Wavelength sampling | Uniform (within filter band) |

---

## Methodology

1. Photons were emitted from random positions on the emitter surface.
2. Each photon was given:
   - A random Lambertian emission direction
   - A wavelength within the filter band (0.4 µm – 1.1 µm)
3. Ray direction and emission angle determined its hit position on the TPV plane.
4. Only photons landing within the circular TPV area were counted as absorbed.
5. Photons that missed were considered escaped or reflected.

---

## Results

| Metric | Value |
|--------|-------|
| % of valid rays absorbed by TPV | **80.1%** |
| % of valid rays escaped or missed TPV | **19.9%** |

This shows that the QT-Reactor's core geometry — emitter directly above TPV with precision spectral filtering — provides a highly efficient optical transfer. The majority of filtered photons are successfully absorbed by the TPV cell.

---

## Photon Hit Map

The figure below shows the spatial distribution of photons on the TPV plane:

- Gray points: All photons that passed the spectral filter  
- Green points: Photons that hit within the TPV radius  
- Dashed circle: Boundary of TPV surface

![Photon Hit Map](../visuals/QT-reactor_optical_raytrace_simulation.png)

This confirms that the majority of emitted photons fall within the optical acceptance region of the TPV cell.

---

## Interpretation

This simulation validates the optical design of the QT-Reactor:

- The gap spacing, emission cone, and TPV radius are well-matched.
- Photon escape is minimized through tight coupling and directional emission.
- Minor losses can be improved further using photon recycling mirrors or cavity optics (Section 13).

---

## Next Steps

- Expand simulation to wavelength-weighted sampling using true Planck distribution.
- Add photon power tracking to convert absorption rate into real energy delivery (W/m²).
- Proceed to Section 12: Thermal FEA Simulation for heat distribution analysis.

---
