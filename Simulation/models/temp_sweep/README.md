# Emitter Temperature Sweep Simulation

## Location
`/simulation/models/temp_sweep.py`

## Purpose

This module simulates and plots how thermal power output varies with emitter temperature for the QuanTonic Reactor. It evaluates:

- Total thermal emission (ideal blackbody)
- Emissivity-filtered usable output (ε(λ) limited to PV-usable range)

This analysis is critical for selecting the optimal operating temperature of the reactor.

---

## Simulation Overview

- **Wavelength Range (λ):** 0.2 µm to 5.0 µm
- **Emissivity Passband:** 0.4 µm to 1.1 µm
- **Temperature Range (Tₑ):** 1000 K to 2500 K in 100 K steps
- **Resolution:** 1000 samples across λ

For each temperature, the simulation calculates:
1. Ideal total radiated power
2. Power within the filtered passband (representing useful photon energy)

---

## Output

The plot `temp_sweep.png` shows two curves:

- **Red**: Total blackbody radiation power (W/m²·sr)
- **Blue**: Emissivity-filtered usable power (W/m²·sr)

These curves rise with temperature, but not linearly — showing a steep gain in energy around 1800–2300 K.

---

## Key Insight

> Although higher temperatures produce more power, the **usable-to-total power ratio decreases** with temperature due to spectrum broadening beyond the PV bandgap.

This creates an engineering tradeoff between thermal loss and photon productivity. The plot helps pinpoint the sweet spot for maximum reactor efficiency.

---

## Files
```
/models/
├── temp_sweep.py         # Temperature sweep simulation script
├── temp_sweep.png        # Output plot of power vs. T
└── README.md             # Module documentation
```

---

## How to Run

1. Paste `temp_sweep.py` into a IDE
2. Ensure the Planck + emissivity functions are included (or imported)
3. Run the script
4. View and export the temperature-performance plot

---

## Next

Proceeding to:
- Determine thermal load & PV matching strategy
- Simulate entropy losses & reflectivity recovery
- Begin emitter–absorber–reflector system design
