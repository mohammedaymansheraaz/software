# Junior Pioneers (Mubarmij Al Emarat) Systems Engineering Manual
**A Comprehensive Guide to Mechatronics, Physics, Mathematics, Chemistry, and Autonomous Design**

---

## 1. Classical Mechanics & Kinematics of Mobile Robots

### 1.1 Differential & Four-Wheel Drive Kinematics
For a robot operating on a 2D plane (the competition mat), its pose is defined as:

$$
q = \begin{bmatrix} x \\ y \\ \theta \end{bmatrix}
$$

Where $(x, y)$ represents position in the global coordinate frame and $\theta$ is the heading angle relative to the X-axis.

When using DC encoder motors with wheel radius $r$ and track width $L$ (distance between left and right wheel midpoints), the linear velocities of the left and right sides ($v_L, v_R$) are derived from angular motor speeds ($\omega_L, \omega_R$):

$$
v_L = r \cdot \omega_L, \quad v_R = r \cdot \omega_R
$$

The robot's net linear velocity $v$ and rotational velocity $\omega$ (yaw rate) about its Instantaneous Center of Rotation (ICR) are given by:

$$
v = \frac{v_R + v_L}{2} = \frac{r(\omega_R + \omega_L)}{2}
$$

$$
\omega = \frac{v_R - v_L}{L} = \frac{r(\omega_R - \omega_L)}{L}
$$

#### Kinematic Forward Equation (Odometry Integration)
To track the robot's coordinates over time step $\Delta t$:

$$
x_{t+\Delta t} = x_t + v \cdot \cos(\theta_t) \cdot \Delta t
$$

$$
y_{t+\Delta t} = y_t + v \cdot \sin(\theta_t) \cdot \Delta t
$$

$$
\theta_{t+\Delta t} = \theta_t + \omega \cdot \Delta t
$$

---

### 1.2 Dynamics, Torque, & Friction Analysis
To achieve rapid acceleration without wheel slip, you must calculate maximum tractive force based on static friction ($\mu_s$) between rubber tires and the vinyl mat.

#### Friction Limited Force
$$
F_{\text{max}} = \mu_s \cdot N = \mu_s \cdot (m \cdot g)
$$

Where:
* $m$: Total robot mass ($\approx 2.4\text{ kg}$)
* $g$: Acceleration due to gravity ($9.81\text{ m/s}^2$)
* $\mu_s$: Static friction coefficient of rubber on vinyl ($\approx 0.85 - 0.95$)

#### Required Motor Torque calculation
For a 4WD chassis with 4 motors driving wheels of radius $r = 0.032\text{ m}$:

$$
T_{\text{wheel}} = \frac{F_{\text{total}} \cdot r}{4} = \frac{(m \cdot a) \cdot r}{4}
$$

If maximum desired acceleration $a = 2.5\text{ m/s}^2$:

$$
T_{\text{wheel}} = \frac{2.4\text{ kg} \times 2.5\text{ m/s}^2 \times 0.032\text{ m}}{4} = 0.048\text{ N}\cdot\text{m} = 0.49\text{ kg}\cdot\text{cm per motor}
$$

#### Center of Gravity (CoG) & Tipping Prevention
During max deceleration $a_{\text{decel}}$, tipping occurs if the net moment around the front axle becomes positive:

$$
\sum M_{\text{front}} = N_{\text{rear}} \cdot L_{\text{wheelbase}} - m \cdot g \cdot d_{\text{front}} + m \cdot a_{\text{decel}} \cdot h_{\text{CoG}} = 0
$$

To eliminate forward tipping during aggressive braking, keep $h_{\text{CoG}}$ (height of center of mass) as low as possible:

$$
h_{\text{CoG}} < \frac{g \cdot d_{\text{front}}}{a_{\text{decel}}}
$$

---

## 2. Structural Architecture & Mechanical Design

### 2.1 Dual-Kit Chassis Stiffening
Merging two MC 4.0 kits allows you to create a **box truss arrangement**:
1. **Lower Structural Deck:** Absorbs high shearing forces during acceleration and turning.
2. **Upper Payload Deck:** Acts as a tension/compression member, preventing frame torsion.
3. **Vertical Standoff Pillars:** Four dual-plate standoff points form a closed structural cage, increasing torsional rigidity ($\kappa$) governed by:

$$
\kappa = \frac{G \cdot J}{L_{\text{cage}}}
$$

Where $G$ is shear modulus, $J$ is torsional constant, and $L_{\text{cage}}$ is pillar height.

```
+-------------------------------------------------------------+
|                  UPPER DECK: CONTROLLER & HOPPER            |
+-------------------------------------------------------------+
   |   [Standoff Pillar]                       | [Standoff Pillar]
   |                                           |
+-------------------------------------------------------------+
|                  LOWER DECK: MOTORS & LINE ARRAY            |
+-------------------------------------------------------------+
      (Wheel L1)                             (Wheel R1)
      (Wheel L2)                             (Wheel R2)
```

### 2.2 Elevator Subsystem Mechanics (Rack & Pinion)
To raise soil cylinders vertically without jamming:
* **Rack and Pinion Gear Ratio:** Direct displacement $x_{\text{lift}} = r_{\text{pitch}} \cdot \theta_{\text{servo}}$.
* **Mechanical Advantage (MA):**

$$
\text{MA} = \frac{F_{\text{load}}}{F_{\text{input}}} = \frac{r_{\text{arm}}}{r_{\text{pitch}}}
$$

* **Buckling Force (Euler's Critical Load for Vertical Rails):**

$$
P_{\text{cr}} = \frac{\pi^2 \cdot E \cdot I}{(K \cdot L)^2}
$$

Where $E$ is Young's Modulus of PETG/Aluminum, $I$ is second moment of area, and $L$ is lift column length.

---

## 3. Materials Science & 3D Printing Engineering

### 3.1 Material Selection Matrix

| Property | PLA (Polylactic Acid) | PETG (Polyethylene Terephthalate Glycol) | ABS / ASA |
| :--- | :--- | :--- | :--- |
| **Flexural Modulus** | High ($3.8\text{ GPa}$) | Medium ($2.1\text{ GPa}$) | Medium ($2.3\text{ GPa}$) |
| **Impact Strength** | Low ($2.5\text{ kJ/m}^2$) | High ($7.9\text{ kJ/m}^2$) | Very High ($15\text{ kJ/m}^2$) |
| **Thermal Deflection**| $55^\circ\text{C}$ | $73^\circ\text{C}$ | $95^\circ\text{C}$ |
| **Ease of Printing** | Extremely High | High | Medium (Requires Enclosure) |
| **Recommended Use**| Static Structural Plates | Grippers, Rack gears, Mounts | High-Stress Gears |

### 3.2 Print Parameters for Mechanical Load-Bearing Parts
* **Anisotropy Mitigation:** 3D prints are weakest along the Z-axis (layer lines). Orient structural bracket load vectors parallel to the print bed ($X/Y$ axis).
* **Infill Pattern:** Use **Gyroid** or **3D Honeycomb** at $35\% - 45\%$ infill density. Gyroid infill provides isotropic shear resistance in all three spatial planes.
* **Wall Perimeters:** Increase perimeter wall count to **4 or 5 perimeter loops** (minimum $1.6\text{ mm}$ wall thickness). Shell thickness contributes significantly more to bending resistance than internal infill percentage.

---

## 4. Control Systems & Signal Mathematics

### 4.1 PID Line Following Algorithm
Line tracking uses closed-loop feedback based on error $e(t)$ from the multi-sensor line array.

$$
e(t) = \text{Target\_Position} - \text{Current\_Sensor\_Center\_of\_Gravity}
$$

$$
\text{Center of Gravity} = \frac{\sum_{i=1}^{N} (i \cdot S_i)}{\sum_{i=1}^{N} S_i}
$$

Where $S_i$ is the analog/digital reflectance value of sensor $i$.

#### Continuous Control Output:
$$
u(t) = K_p \cdot e(t) + K_i \int_{0}^{t} e(\tau) \, d\tau + K_d \cdot \frac{de(t)}{dt}
$$

#### Discrete MicroPython Implementation:
$$
P = K_p \cdot e_k
$$

$$
I = I_{\text{prev}} + K_i \cdot e_k \cdot \Delta t
$$

$$
D = K_d \cdot \frac{e_k - e_{k-1}}{\Delta t}
$$

$$
\text{Motor Output}_{L} = V_{\text{base}} + (P + I + D)
$$

$$
\text{Motor Output}_{R} = V_{\text{base}} - (P + I + D)
$$

```
               +-----------------------------------+
               | Calculate Line Error e(k)         |
               +-----------------------------------+
                                 |
                                 v
               +-----------------------------------+
               | PID Computation (P + I + D)       |
               +-----------------------------------+
                                 |
         +-----------------------+-----------------------+
         |                                               |
         v                                               v
+------------------+                           +------------------+
| Motor Left PWM   |                           | Motor Right PWM  |
| V_base + u(k)    |                           | V_base - u(k)    |
+------------------+                           +------------------+
```

---

## 5. Electronics, Power, & Sensor Integration

### 5.1 Power Budgeting & Voltage Regulation
The MC 4.0 system operates off an internal lithium power module supplying nominal voltage $V_{\text{bat}} = 7.4\text{V}$.

#### Power Draw Calculations:
* 4x DC Encoder Motors at full load: $4 \times 0.8\text{A} = 3.2\text{A}$
* 3x High-Torque Servos (Peak stall): $3 \times 1.2\text{A} = 3.6\text{A}$
* Controller, Camera & Sensor Modules: $\approx 0.8\text{A}$
* **Total Peak Current ($I_{\text{peak}}$):** $7.6\text{A}$

To prevent controller brownouts when servos engage, isolate servo power rails using an external High-Current Step-Down Buck Converter ($7.4\text{V} \rightarrow 6.0\text{V}$ @ $5\text{A}$ continuous).

---

## 6. Engineering Mindset & Design Workflow

### The 5-Step Iterative Engineering Process
1. **Deconstruct the Rulebook:** Map out point values per second of execution time. Prioritize missions with highest points-to-risk ratio.
2. **CAD Modeling (First Principles):** Model every bracket, structural plate, and sensor payload in CAD before physical assembly to check clearance and box constraints ($320\times 320\times 450\text{ mm}$).
3. **Mass & Center of Mass Budgeting:** Keep heaviest components (battery, lower chassis plates) close to drive axles.
4. **Failsafe Design (Defensive Engineering):**
   * Use physical endstops/switches alongside optical/encoder readings.
   * Add sensor shrouds to eliminate ambient light variance on RGB/Vision sensors.
5. **Data-Driven Tuning:** Log encoder ticks and IMU telemetry via MQTT to diagnose trajectory errors quantitatively rather than guessing.