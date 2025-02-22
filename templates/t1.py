from manim import *
import math as m

class Rotating3DAxis(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Set the x_range and y_range to suit the new function
        axes = ThreeDAxes(
            x_range=[0, 2],  # Range for x from 0 to 2
            y_range=[-m.e**2, m.e**2],  # Range for y based on f(x) = e^x at x=2
            z_range=[-9, 9],  # z-range remains unchanged
        )
        
        x_label = Tex("x").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Tex("f(x)").next_to(axes.y_axis.get_end(), UP)
        z_label = Tex("z").next_to(axes.z_axis.get_end(), OUT)
        x_label.look_at(self.camera.position)
        y_label.look_at(self.camera.position)
        z_label.look_at(self.camera.position)
        self.add(axes, x_label, y_label, z_label)
        
        # Update the function being plotted: f(x) = e^x
        graph = axes.plot(lambda x: m.exp(x), x_range=[0, 2], color=YELLOW)  # Plot e^x from 0 to 2
        
        self.play(Create(graph, run_time=3))
        
        # Update the surface equation for the function e^x
        surface = Surface(
            lambda u, v: axes.c2p(u, m.exp(u) * np.cos(v), m.exp(u) * np.sin(v)),  # Surface for e^x in 3D
            u_range=[0.05, 2], v_range=[0, TAU],
            resolution=(20, 40),
            fill_opacity=0.5, color=BLUE
        )
        
        self.play(Create(surface, run_time=3))
        
        self.play(Rotate(VGroup(axes, x_label, y_label, z_label, graph, surface), angle=2 * PI, axis=OUT, run_time=15, rate_func=linear))
        
        self.wait()
