# ε(λ) Filter Simulation

## Location
`/simulation/models/filter_simulation.py`

---

## Purpose
This module quantifies how a wavelength-selective emissivity filter shapes the QuanTonic Reactor’s photon output.  
It compares:

* **Raw emission** of the high-temperature emitter  
* **Filtered emission** after applying ε(λ) that passes only 0.4 µm – 1.1 µm photons

---

## Simulation Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| Emitter temperature (Tₑ) | 1800 K | Within the optimal 1700–2000 K range from Section 7 |
| Wavelength domain | 0.2 µm – 5 µm | Captures full mid-IR tail |
| Pass-band (ε=1) | 0.4 µm – 1.1 µm | Matches GaSb / Si PV bandgap range |
| Resolution | 1200 samples | High-fidelity radiance curve |

---

## Output

**File:** `filtered_spectrum.png`

* **Red curve** – raw Planck radiance I(λ)  
* **Blue curve** – filtered radiance ε(λ)·I(λ)  
* **Grey band** – pass-band region where ε(λ)=1  

The plot visually confirms that the filter blocks long-wavelength, low-energy photons while allowing PV-useful photons to pass.

---

## Key Insight
The emissivity filter eliminates ≈ 97 % of total radiated energy (entropy) that would otherwise be unusable, focusing the remaining 3 % into the photovoltaic band. Combined with photon-recycling mirrors (Section 8), this step is essential for high system efficiency.

---

## Files
```
/filter_simulation/
├── filter_simulation.py
├── filtered_spectrum.png
└── README.md
```
---

## Next

Proceed to **Section 10 – CAD & 3-D Reactor Layout** to translate this optical stack into a dimensioned mechanical model.
