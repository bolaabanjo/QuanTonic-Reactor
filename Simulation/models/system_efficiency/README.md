# QuanTonic Reactor — System Efficiency Simulation

## Location
`/simulation/models/system_efficiency.py`

---

## Purpose

This module simulates the system-wide energy conversion efficiency of the QuanTonic Reactor. It combines:

1. Thermal efficiency: how much emitted radiation is usable by the PV layer
2. PV quantum efficiency: how much of that radiation becomes electricity

It answers a critical engineering question:
> “At what emitter temperature does the reactor operate with peak efficiency?”

---

## Simulation Details

| Component | Value |
|-----------|-------|
| Wavelength range | 0.2 µm to 5.0 µm |
| Emitter temperature sweep | 1000 K → 2500 K |
| PV bandgap (GaSb) | 1.8 µm (≈ 0.7 eV) |
| Quantum efficiency | 35% (real-world TPV estimate) |

The simulation uses Planck's Law to compute total and usable radiative power at each temperature.

---

## Output Plot

- **Orange Line** — η_thermal(T): % of total radiation below λ_cutoff
- **Green Line** — η_total(T): actual electrical conversion efficiency

These curves show how the reactor's output depends heavily on temperature.

> Usable energy increases with Tₑ, peaks, then declines due to spectral overflow (wavelengths > λ_cutoff).

---

## Key Insight

| Temperature | Thermal Efficiency | Total System Efficiency |
|-------------|--------------------|--------------------------|
| ~1700–2000 K | ~55–65%           | ~20–24% (η_total)        |

The optimal performance band for the QuanTonic Reactor lies between **1700 K and 2000 K**.  
Beyond 2000 K, waste energy rises due to emission outside the PV spectrum.

This informs both:
- Material selection (emitter survivability)
- PV tuning (bandgap engineering)

---

## Files
```
/system_efficiency/
├── system_efficiency.py       # Simulation script
├── system_efficiency.png      # Output plot
└── README.md                  # This documentation
```

---

## How to Run

1. Open `system_efficiency.py` in Colab or Replit
2. Run the script
3. Review the output plot for thermal and total efficiency
4. Adjust PV λ_cutoff and η_pv values to simulate other materials (e.g. InGaAs, Ge)

---

## Next 

We proceed to:
- Begin the optical + thermal design of the emitter–PV–reflector system
- Simulate multilayer photon recycling
- Explore entropy minimization and passive heat rejection design
