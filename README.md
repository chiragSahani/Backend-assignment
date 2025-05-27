
# 🌀 Möbius Strip Visualizer & Geometry Analyzer

> A Python project that models the mysterious Möbius strip using parametric equations, visualizes it in 3D, and calculates its **surface area** and **edge length** numerically.

![Mobius Strip](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Mobius_strip.jpg/320px-Mobius_strip.jpg)

---

## 📐 What is a Möbius Strip?

A **Möbius strip** is a surface with only one side and one boundary. It's a mind-bending topological object that has fascinated mathematicians, artists, and engineers alike.

This project turns equations into 3D visualizations and concrete geometry computations using Python.

---

## 🛠️ Features

- 📊 **3D Parametric Modeling** using NumPy and Matplotlib
- 📐 **Surface Area Approximation** via numerical integration
- 📏 **Edge Length Computation** along the boundary
- 🧪 Fully modular class structure for customization
- 💡 Ideal for math visualization, topology teaching, and computational geometry

---

## 📦 Requirements

```bash
pip install numpy matplotlib
````

---

## 🧠 Code Structure

```python
class MobiusStrip:
    ├── __init__(R, w, n)            # Initialize radius, width, resolution
    ├── generate_mesh()              # Create the mesh grid using parametric equations
    ├── compute_surface_area()       # Numerical integration of surface area using vector cross products
    ├── compute_edge_length()        # Approximate the edge length along boundary
    └── plot_3d()                    # 3D plot using matplotlib
```

### 🔣 Parametric Equations Used:

$$
\begin{align*}
x(u,v) &= (R + v \cdot \cos(u/2)) \cdot \cos(u) \\
y(u,v) &= (R + v \cdot \cos(u/2)) \cdot \sin(u) \\
z(u,v) &= v \cdot \sin(u/2)
\end{align*}
$$

Where:

* $u \in [0, 2\pi]$
* $v \in [-w/2, w/2]$

---

## 🔬 Surface Area Approximation

Surface area is computed using **numerical integration** based on the formula:

$$
A = \iint \left| \frac{\partial \vec{r}}{\partial u} \times \frac{\partial \vec{r}}{\partial v} \right| \, du\, dv
$$

This is discretized using finite differences over the mesh grid.

---

## 📏 Edge Length Approximation

Edge length is calculated by:

* Sampling points along $v = w/2$ (outer edge)
* Using Euclidean distances between successive points
* Summing to approximate the boundary’s total length

---

## 📸 Sample Output (3D Plot)

```python
strip = MobiusStrip(R=5, w=1, n=200)
strip.plot_3d()
```

Output:

![3D Mobius Plot](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/M%C3%B6bius_strip_2.png/640px-M%C3%B6bius_strip_2.png)

---

## 🧩 Challenges Faced

* 🔄 **Orientation Flip**: One challenge was handling the twisting nature of the Möbius strip while computing surface normals.
* 📈 **Numerical Stability**: Getting smooth approximations without increasing computational load required tuning `n` and applying proper vector calculus.
* 🧮 **Cross-Product Logic**: Deriving accurate partial derivatives in discrete form was non-trivial.

---

## 🚀 Future Improvements

* Add texture support to the strip
* Animate rotation of the Möbius in 3D
* Extend to Klein bottle and other non-orientable surfaces
* Export as STL/OBJ for 3D printing

---

## 🤝 Contributing

Pull requests and issues are welcome! Let’s bend space together!




> Made with 🧠 and 🌀 by ChiragSahani

