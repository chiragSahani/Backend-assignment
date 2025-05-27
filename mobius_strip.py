import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=200):
        """
        Initialization of Mobius strip parameters.
        R: The radius of the center to the strip
        w: Width of the strip
        n: Mesh resolution (number of points on u and v)
        """
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._generate_mesh()

    def _generate_mesh(self):
        """
        Produce meshgrid points with the parametric equations of the Möbius strip.
        Returns X, Y, Z as 2D arrays.
        """
        u, v = self.U, self.V
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def get_surface_area(self):
        """
        Estimate of cell surface area by numerical integration (trapezoidal rule).
        Area ≈ ∬ |∂r/∂u × ∂r/∂v| dudv
        """
        du = self.u[1] - self.u[0]
        dv = self.v[1] - self.v[0]

        # Compute partial derivatives
        Xu, Yu, Zu = np.gradient(self.X, du, axis=1), np.gradient(self.Y, du, axis=1), np.gradient(self.Z, du, axis=1)
        Xv, Yv, Zv = np.gradient(self.X, dv, axis=0), np.gradient(self.Y, dv, axis=0), np.gradient(self.Z, dv, axis=0)

        # Cross product ∂r/∂u × ∂r/∂v
        cross_x = Yu * Zv - Zu * Yv
        cross_y = Zu * Xv - Xu * Zv
        cross_z = Xu * Yv - Yu * Xv

        dA = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        area = np.sum(dA) * du * dv
        return area

    def calculate_edge_length(self):
        """
        Circumference of rounded v = ±w/2 2.
        """
        u = self.u
        edge_points = []
        for sign in [-1, 1]:
            v_edge = sign * self.w / 2
            x = (self.R + v_edge * np.cos(u / 2)) * np.cos(u)
            y = (self.R + v_edge * np.cos(u / 2)) * np.sin(u)
            z = v_edge * np.sin(u / 2)
            edge = np.stack((x, y, z), axis=-1)
            edge_points.append(edge)

        # Length is represented by the sum of the segment distances
        length = 0
        for edge in edge_points:
            diffs = np.diff(edge, axis=0)
            segment_lengths = np.linalg.norm(diffs, axis=1)
            length += np.sum(segment_lengths)
        return length

    def plot(self):
        """
        Plot the Möbius band in 3D with matplotlib.
        """
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=4, cstride=4, color='deepskyblue', edgecolor='k', linewidth=0.3, alpha=0.9)
        ax.set_title("Mobius Strip", fontsize=14)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()
        plt.show()

# Run and test
if __name__ == "__main__":
    mobius = MobiusStrip(R=1.0, w=0.2, n=300)
    area = mobius.get_surface_area()
    edge_length = mobius.calculate_edge_length()

    print(f"Surface Area ≈ {area:.5f}")
    print(f"Edge Length ≈ {edge_length:.5f}")
    mobius.plot()
