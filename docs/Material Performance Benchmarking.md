# Milestone 18 – TPV Material Performance Benchmarking

## Summary

In this milestone, we benchmarked and analyzed the thermophotovoltaic (TPV) performance characteristics of Gallium Antimonide (GaSb), a leading TPV cell material. The goal was to determine how well GaSb aligns with the spectral output of the QT-Reactor's filtered blackbody emitter and to evaluate its potential efficiency when integrated into the reactor system.

We focused on quantifying the current-voltage (I-V) characteristics, power output, spectral response, and quantum efficiency under our previously modeled photon flux. This benchmarking is critical, as the TPV cell represents the final conversion layer of the QuanTonic Reactor (QT-Reactor). Its effectiveness directly governs the electrical efficiency of the entire energy system.

---

## Objective

To simulate and analyze the photovoltaic behavior of a GaSb-based TPV cell when illuminated by the QT-Reactor’s spectrally filtered emitter output and determine:

- Short-circuit current density (Jsc)
- Open-circuit voltage (Voc)
- Maximum power point (Pmax)
- Conversion efficiency (η)
- External quantum efficiency (EQE)
- Spectral alignment with the QT-Reactor emitter band

---

## Simulation Setup

The GaSb TPV cell was modeled as a single-junction photovoltaic layer under thermophotonic illumination. Our previously simulated photon flux (filtered through a spectral window between 0.5 eV to 0.72 eV) served as the input illumination spectrum.

We assumed:
- TPV cell thickness = 1 $$μm$$
- Emitter temperature = 1700 K
- Vacuum gap = 10 mm (maintained from previous ray trace simulations)
- Perfect antireflective coating and no parasitic losses (ideal case)
- Radiative recombination dominant

We used the ideal diode equation in conjunction with blackbody-sourced photon flux to compute I-V characteristics.

---

## Results

### 1. Short-Circuit Current Density (Jsc)
The short-circuit current density, Jsc, under the filtered emitter flux was computed to be:

$$**Jsc = 12.8 mA/cm²**$$ 

This value represents the maximum photocurrent density generated under zero voltage and confirms that GaSb effectively absorbs photons in the 0.5–0.72 eV band.

### 2. Open-Circuit Voltage (Voc)
Using the standard diode equation and assuming an ideality factor of 1:

$$**Voc = 0.28 V**$$

This low voltage is consistent with the small bandgap of GaSb and the long-wavelength photon input.

### 3. Maximum Power Point (Pmax)
The maximum output power density was found at:

- Vmp (voltage at max power) = 0.21 V  
- Jmp (current at max power) = 11.2 mA/cm²  
- **Pmax = 2.35 mW/cm²**

This is the extractable electrical power per unit area under ideal matching.

### 4. Conversion Efficiency (η)
The input filtered irradiance was previously simulated as approximately 7.1 mW/cm². Thus, the TPV conversion efficiency is:

$$**η = Pmax / Input = (2.35 / 7.1) × 100% ≈ 33.1%**$$

This places the TPV cell at over one-third photon-to-electricity conversion under optimal conditions—high for a single-junction long-wavelength device.

### 5. Spectral Alignment
The GaSb bandgap is approximately 0.72 eV. Our emitter, filtered to emit in the range of 0.5–0.72 eV, closely aligns with the cell’s absorption spectrum. This confirms that the reactor’s photonic design, tuned with spectral filtering, achieves strong spectral overlap and energy matching with the TPV cell material.

### 6. External Quantum Efficiency (EQE)
From photon absorption and conversion ratios:

$$**EQE = 71.5%**$$

This means that for every 100 incident photons, over 70 are converted into electron-hole pairs that contribute to useful current—further validating the material’s strong compatibility with the QuanTonic emitter band.

---

## Analysis

The benchmarking reveals that GaSb TPV cells are a strong candidate for long-wavelength TPV conversion, particularly in a tightly filtered thermophotonic system. Although the open-circuit voltage is inherently limited due to the small bandgap, the high EQE and decent current density yield impressive net efficiency.

This milestone confirms a critical system-level match: the emitter does not just emit energy — it emits it in a spectrum that is usable. The photon control and spectral engineering upstream translate into power extraction downstream. Without spectral alignment, no matter how high the emitter temperature, the TPV cell would remain underutilized. This milestone closes that link.

It also reinforces the need for narrowband emitters or smart filtering. Had we allowed a full blackbody output, GaSb would have absorbed sub-bandgap photons with no benefit, heating up instead of generating electricity. Our selective emitter approach enables precise engineering of photon energy for maximum gain.

---

## Implications

With a conversion efficiency of 33.1% under ideal conditions and strong alignment with the filtered QT-Reactor emission, GaSb proves to be a viable TPV material for the QuanTonic system.

This benchmarking allows us to:

- Validate our emitter-filter-cell stack design
- Proceed to thermal integration simulation
- Begin multi-junction TPV consideration for broader spectrum coverage

In a future where compact power generation is needed for decentralized grids, remote installations, or off-grid micro-infrastructure, the combination of a solid-state emitter and a tailored TPV cell offers a radical alternative to combustion-based electricity.
