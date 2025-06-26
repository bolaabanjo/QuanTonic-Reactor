# 10. Physical Design — CAD Blueprint of the QuanTonic Reactor Core

This section converts the QuanTonic Reactor’s optical–thermal stack into a dimensioned mechanical model that can be imported into any CAD package (Onshape, Fusion 360, Shapr3D, SolidWorks, or Blender for visuals).  
The goal is to deliver a single, modular “reactor puck” that integrates:

1. High-temperature emitter  
2. Wavelength-selective filter (ε(λ))  
3. Thermophotovoltaic (TPV) receiver  
4. Photon-recycling mirror  
5. Vacuum containment & support shell  

All dimensions are parametric. Update one variable and the entire assembly scales in CAD.

---

## 10.1 Global Parameters (Prefix **P\_**)

| Parameter | Symbol | Default | Notes |
|-----------|--------|---------|-------|
| Outer diameter | P_D | 100 mm | Full disc size |
| Core thickness | P_T | 25 mm | Overall stack height |
| Emitter radius | P_Re | 45 mm | Radius of tungsten/SiC emitter |
| Filter gap | P_Gf | 1.0 mm | Vacuum gap between emitter & filter |
| Filter thickness | P_Tf | 0.25 mm | Dielectric stack |
| TPV thickness | P_Tp | 0.40 mm | GaSb multijunction |
| Mirror thickness | P_Tm | 0.50 mm | Silvered quartz disc |
| Shell wall | P_Ts | 2.0 mm  | Stainless or titanium |
| Electrical port dia. | P_De | 4 mm | Feed-through for PV leads |
| Heat sink boss dia. | P_Dh | 12 mm | Mount for optional cooling block |

---

## 10.2 Layer-by-Layer Specification

| ID | Layer | Material | Dia / Radius | Thickness | Key Features |
|----|-------|----------|--------------|-----------|--------------|
| L1 | **Emitter Disc** | Tungsten (99.9 %) or SiC | P_Re × 2 | 3 mm | Nanostructured surface, central thermocouple well Ø 3 mm |
| L2 | **Spectral Filter** | 20-layer HfO₂/SiO₂ stack | ≈ P_Re × 2 | P_Tf | Mounted on alumina spacer ring; ε(λ)=1 from 0.4–1.1 µm |
| L3 | **TPV Cell** | GaSb multijunction array | P_Re × 2 | P_Tp | Back-contact busbars to two M3 feed-through studs |
| L4 | **Photon Mirror** | Silvered quartz or Au film | P_Re × 2 | P_Tm | ≥ 96 % reflectivity for λ > 1.1 µm |
| L5 | **Vacuum Shell** | Ti-6Al-4V (Grade 5) | P_D | P_Ts | Cylindrical cup + lid, knife-edge CF seal, KF16 vacuum port |

Gap between L1 and L2 set by **P_Gf** spacers (macor or sapphire posts).

---

## 10.3 Exploded Assembly Order (Z-axis)

1. Mirror (L4) seats inside shell bottom.  
2. TPV cell (L3) bonded to mirror via indium solder preform.  
3. Alumina spacer ring creates **P_Gf** gap.  
4. Filter disc (L2) rests on spacer ring.  
5. Precision posts set emitter height; emitter disc (L1) placed on posts.  
6. Shell lid clamps with CF knife-edge, compressing copper gasket.  
7. Vacuum port evacuated to ≤ 10⁻⁵ mbar; getter pump optional.  

---

## 10.4 Material & Manufacturing Notes

* **Emitter (L1)**  
  * EDM-cut tungsten or hot-pressed SiC.  
  * Nanostructured by femtosecond laser texturing or e-beam lithography.  

* **Filter (L2)**  
  * Alternating HfO₂ (n≈1.9) / SiO₂ (n≈1.45) quarter-wave stack, 20 layers.  
  * Deposition via ion-beam sputtering, thickness tolerance ±2 nm.

* **TPV Cell (L3)**  
  * GaSb wafer diced to disc; backside busbar pattern via photolithography.  
  * Cell soldered to mirror with 80 In / 15 Ag solder; melting 230 °C.

* **Mirror (L4)**  
  * 2 µm silver coating on fused silica; AR-coated front face.  
  * Surface roughness < 5 nm RMS.

* **Shell (L5)**  
  * Turned Ti Grade 5 cup + lid.  
  * Knife-edge conforms to Conflat CF63 standard (miniaturised).  

---

## 10.5 CAD Workflow (Suggested)

1. **Onshape** (cloud, free for open projects)  
   * Create a new document “QT_Reactor_Core”  
   * Set global variables: `P_D`, `P_T`, etc.  
   * Sketch top-down disc profiles.  
   * Revolve or extrude each layer.  
   * Use `Mate` connectors for stack alignment.

2. **Fusion 360**  
   * Import Onshape STEP if preferred.  
   * Assign materials (Appearance → Physical).  
   * Run thermal study (Static > Thermal) with 1800 K boundary on emitter face and radiation surfaces for rest.  

3. **Blender** (visual only)  
   * Import STEP/IGES.  
   * Apply emissive shader to emitter, transparent shader to filter.  
   * Render cut-away for publication.  

---

## 10.6 Parametric Scaling Rules

To miniaturise:  
* Decrease `P_D` to 40 mm; maintain aspect ratio `P_T : P_D ≈ 0.25`.  
* Reduce layer thicknesses proportionally except filter (optical thickness fixed by wavelength).  
* Vacuum shell wall can drop to 1 mm if diameter < 60 mm.

To up-scale:  
* Increase `P_D`; leave `P_T` constant until emitter surface becomes area-limited.  
* Add radial heat-sink fins to outer shell.  

---

## 10.7 Next Actions

1. **CAD Draft** — Build parametric model with variables listed.  
2. **Thermal FEA** — Validate stress and temperature gradients at 1800 K.  
3. **Optical Ray-Trace** — Simulate photon paths (Zemax or open-source Raysect).  
4. **BOM & Costing** — Estimate fabrication cost for one 100 mm unit.  

Upon completion, Section 11 will document simulation results of optical ray-tracing and thermal finite-element analysis.
