# Spectral Radiance Visualization

## Location
`/simulation/visuals/plot_radiance.py`

## Purpose

This module visualizes the spectral behavior of the QuanTonic Reactor’s emitter using Planck’s Law and a defined emissivity window. It provides visual insight into the difference between total thermal emission and the portion usable by the PV system.

---

## What It Shows

- **Blackbody Radiance** — the full spectrum of energy emitted by the high-temperature emitter.
- **Filtered Radiance** — the subset of that energy which passes through a wavelength-selective emissivity filter, representing usable photon energy.
- **Emissivity Band Region** — the shaded passband ([λ₁, λ₂]) that represents where ε(λ) = 1.

This helps validate your design assumption:  
> Engineering ε(λ) is essential for controlling what energy reaches the PV converter.

---

## Input Parameters

| Parameter         | Value     | Units    |
|------------------|-----------|----------|
| Temperature (Tₑ) | 1500       | K        |
| Wavelength Range | 0.2 to 5.0 | µm       |
| Emissive Band    | 0.4 to 1.1 | µm       |
| Resolution       | 1000 pts   | —        |

---

## Sample Plot Output

- Red Curve: Ideal blackbody spectral radiance (I(λ))
- Blue Curve: Filtered spectral radiance after ε(λ)
- Grey Band: Emissive passband (where ε(λ) = 1)

The filtered curve lies under the red one and overlaps only in the defined passband, illustrating efficiency tradeoffs.

---

## How to Run

1. Open `plot_radiance.py` in Colab or Replit.
2. Ensure `planck_spectral_radiance()` and `modified_radiance()` functions are present.
3. Run the script to display and save the plot as `radiance_plot.png`.

You can also change:
- `Tₑ` to simulate different emitter temperatures
- `λ_min` / `λ_max` to simulate different filter configurations

---

## Files
```
/visuals/
├── plot_radiance.py        # Plotting script
├── radiance_plot.png       # Generated spectral plot
└── README.md               # Module documentation
```
---

## Next

We proceed to:
- Simulate how usable energy output changes with temperature
- Perform emitter temperature sweeps across 1000 K–2500 K
- Identify the optimal operating range for peak conversion efficiency
