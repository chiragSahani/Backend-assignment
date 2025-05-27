

<h1 align="center">🌀 Möbius Strip Visualizer & Geometry Analyzer</h1>
<p align="center">
  <img src="https://res.cloudinary.com/dlyctssmy/image/upload/v1748324730/2012_10_31-mobifab_e2n7fg.gif" alt="Mobius Strip" width="220"/>
</p>
<p align="center">
  <b>🎲 An elegant fusion of mathematics, geometry, and interactive visualization. Explore the Möbius world with Python. 🧑‍💻🌀</b>
</p>

---

## 📦 Project Overview

This repository provides a Python-based **3D visualizer and geometry analyzer** for the Möbius strip—one of the most iconic non-orientable surfaces in topology. Through parametric equations, the project enables:

* ✨ Interactive 3D plotting via `matplotlib`
* 📐 Surface area approximation using numerical integration
* 🧮 Edge length calculations through arc-length integration
* 🔧 Parameter customization for shape manipulation and experimentation

---

## 📌 Key Features

* 🎨 **3D Visualization** — Spin, zoom, and admire the Möbius strip in action
* 🧠 **Numerical Computations** — Surface area and edge length estimated using fast, vectorized NumPy routines
* ⚙️ **Customizable Geometry** — Play with radius (`R`), strip width (`w`), and mesh density (`n`)
* 🧩 **Modular Code** — Easily extendable for animations, exports, or new geometrical constructs

---

## 🧑‍💻 Code Structure

```bash
mobius/
├── mobius.py         # Contains the MobiusStrip class and geometry methods        
└── README.md         # Project documentation
```

### ✳️ Core Class: `MobiusStrip`

```python
class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=200):
        # Parameters: Radius (R), Width (w), Mesh Density (n)
        
    def _generate_mesh(self):
        # Creates (x, y, z) meshgrid using parametric equations
        
    def get_surface_area(self):
        # Approximates surface area via vectorized cross product integration
        
    def calculate_edge_length(self):
        # Computes edge length via arc-length approximation of boundary curves
        
    def plot(self):
        # Interactive 3D rendering using matplotlib
```

---

## 📊 Mathematical Foundation

### 🔁 Parametric Representation

$$
\begin{align*}
x(u,v) &= (R + v \cdot \cos(u/2)) \cos(u) \\
y(u,v) &= (R + v \cdot \cos(u/2)) \sin(u) \\
z(u,v) &= v \cdot \sin(u/2)
\end{align*}
$$

* $u \in [0, 2\pi], \quad v \in [-w/2, w/2]$

---

## 🧮 Surface Area Approximation

We use the standard surface integral:

$$
A = \iint \left\| \frac{\partial \vec{r}}{\partial u} \times \frac{\partial \vec{r}}{\partial v} \right\| du\,dv
$$

Implemented using finite difference approximations and NumPy’s broadcasting for high performance. No external libraries—just pure Python + math!

---

## 📏 Edge Length Calculation

Both boundary edges are computed separately by:

* Sampling boundary points ($v = \pm w/2$)
* Approximating length by summing Euclidean distances between consecutive mesh points

---

## 🧗 Challenges Faced

* ⚖️ **Balancing Accuracy and Performance**: Increasing mesh density (`n`) improves precision but slows computation. A reasonable default of 200 strikes a good balance.
* 🧮 **Numerical Integration Edge Cases**: Ensured robustness when handling discontinuities due to Möbius twist.
* 🎨 **3D Plotting with Non-Orientable Surfaces**: Rendering Möbius twists while maintaining a coherent mesh without visual artifacts.
* 🔁 **Modular Refactoring**: Making the code extensible for future additions like STL exports, color mappings, or animations.

---

## 🚀 Try It Yourself

```python
from mobius import MobiusStrip

strip = MobiusStrip(R=1.5, w=0.4, n=300)
strip.plot()

print("Surface Area:", strip.get_surface_area())
print("Edge Length:", strip.calculate_edge_length())
```

---

## 🌈 Customize & Extend

* 🎨 Add textures, lighting, or themes
* 🔁 Animate twists or shape transformations
* 🖨 Export mesh for 3D printing (e.g. STL format)
* 🧪 Extend to other non-orientable surfaces (Klein bottle, etc.)

---

## 🤝 Contributions Welcome

Whether you're here to experiment, extend, or simply marvel at Möbius geometry—your feedback and ideas are valuable. PRs are open!

---

<p align="center">
  <i>Crafted with precision and a twist 🌀 by <b>ChiragSahani</b></i>
</p>

