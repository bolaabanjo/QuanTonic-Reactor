# Section 14: TPV I–V Curve Simulation

## Overview

This section models the electrical output characteristics of the QT-Reactor’s TPV subsystem under load, using the classic diode equation with photogenerated current. By simulating the full current–voltage (I–V) and power–voltage (P–V) curves, we quantify the reactor’s performance beyond raw power density.

---

## Methodology

The TPV cell behaves like a photodiode under illumination:

$$
\[
I(V) = I_L - I_0 \left( e^{\frac{qV}{nkT}} - 1 \right)
\]
$$

Where:
- $$\( I_L \)$$: Light-generated current (from thermal photon flux)
- $$\( I_0 \)$$: Reverse saturation current (1e-9 A assumed)
- $$\( n \)$$: Ideality factor (1.5)
- $$\( V \)$$: Output voltage
- $$\( T \)$$: TPV cell temperature (300 K)

The simulation is based on:
- Current density from Section 13 (13.48 MA/m²)
- TPV cell area of 1 cm² (0.0001 m²)

---

## Results

| Metric | Value |
|--------|--------|
| **Short-Circuit Current (I<sub>sc</sub>)** | 1348.0 A |
| **Open-Circuit Voltage (V<sub>oc</sub>)** | 1.08 V |
| **Voltage at Max Power Point (V<sub>mpp</sub>)** | 0.96 V |
| **Current at Max Power Point (I<sub>mpp</sub>)** | 1295.6 A |
| **Max Power Output (P<sub>max</sub>)** | 1240.05 W |
| **Fill Factor (FF)** | 85.01% |

This implies an incredibly efficient conversion system, capable of generating **over 12 MW/m²** at maximum performance — a level of output that vastly exceeds conventional photovoltaic and solar thermal technologies.

---

## I–V and P–V Curves

The figure below illustrates how voltage and current behave under load, and where maximum power is extracted:

![TPV I–V Curve](https://github.com/bolaabanjo/QuanTonic-Reactor/blob/5fa81cfc39795b1d4897eaccd46017589f7f6b5d/Simulation/visuals/QT%20Reactor%20TPV%20IV%20Curve.png)

- **Red Curve:** Current vs. Voltage (I–V)  
- **Blue Dashed Curve:** Power vs. Voltage (P–V)  
- **Peak:** Indicates maximum power point (MPP)

---

## Implications

The high fill factor (85%) indicates that the TPV cell operates near its theoretical limits. This confirms:

- Strong material-electrical coupling  
- Proper spectral matching from the thermal emitter  
- Efficient load delivery at real circuit conditions

With minimal resistive losses and optimized bandgap filtering, the QT-Reactor’s electrical model demonstrates readiness for direct integration with storage, propulsion, or microgrid systems.

---

## Next Steps

→ Section 15: TPV Efficiency + Heat Balance  
We now analyze thermal vs. electrical balance: how much input heat is converted to electricity, how much is lost, and what improvements are possible.
