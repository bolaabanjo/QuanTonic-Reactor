# Section 13: TPV Electrical Conversion Simulation

## Overview

This section models the conversion of thermal radiation to electricity within the QT-Reactor’s thermophotovoltaic (TPV) subsystem. The TPV cell is the core mechanism responsible for converting high-temperature blackbody radiation into usable electrical power using solid-state principles.

Our analysis simulates:
- The photon spectrum incident on the TPV cell
- Material-specific bandgap filtering
- Quantum efficiency limitations
- Output electrical power density

---

## TPV System Configuration

The selected TPV material is **Gallium Antimonide (GaSb)**, a proven semiconductor in mid-infrared photovoltaics. GaSb offers a bandgap of:

- **Bandgap (Eg):** 0.72 eV  
- **Cutoff Wavelength (λg):** ~1720 nm

Only photons with energies **greater than or equal to** this bandgap can generate electrical current. The rest are filtered or converted to waste heat.

---

## Simulation Parameters

| Variable | Value | Description |
|----------|-------|-------------|
| **T** | 1800 K | Temperature of the blackbody emitter |
| **Emissivity** | 0.1–0.3–0.05 | Filtered spectral window design |
| **Quantum Efficiency (QE)** | 0.8 | Assumed constant for GaSb |
| **Photon Energy Range** | 300–2500 nm | Full incoming spectrum |
| **Bandgap Cutoff** | ≥ 0.72 eV | Only these photons contribute |

---

## Results

| Metric | Value |
|--------|-------|
| **Current Density (J)** | 13.48 MA/m² |
| **Voltage Output (V)** | 0.72 V |
| **Power Density (P)** | 9.7 MW/m² |

These numbers represent **ideal theoretical output** under optimal spectral matching and TPV absorption. Real-world performance will depend on material quality, thermal management, and photon recycling efficiency.

---

## Spectrum Analysis

The figure below shows the spectrum of filtered radiation incident on the TPV surface. The orange region represents the usable energy band — photons with energy above the GaSb bandgap.

![TPV Spectrum](../visuals/QT-reactor_TPV_spectrum.png)

- **Dark red line:** Full filtered radiance from the emitter  
- **Orange fill:** Portion usable by TPV (above 0.72 eV)  
- **Dashed line:** Bandgap wavelength cutoff (~1720 nm)

---

## Interpretation

The QT-Reactor’s TPV architecture, powered by a spectrally tailored blackbody emitter and high-efficiency GaSb cell, theoretically delivers **multi-megawatt output per square meter** of surface area. This is significantly higher than conventional solar panels due to:

- Higher source temperatures (1800 K vs. 5800 K for Sun, but focused and filtered)  
- Tuned spectral filters maximizing photon-to-electron conversion  
- Near-zero thermal conduction losses (due to vacuum isolation)

---

## Next Steps

→ Section 14: IV Curve Simulation  
We will now simulate the full I–V (Current–Voltage) characteristics of the TPV cell, including open-circuit voltage, short-circuit current, and power tracking for real operating conditions.

---
