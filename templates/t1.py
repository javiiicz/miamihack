from manim import *
import math as m

RANGE_START = 0;
RANGE_END = 2;

class Rotating3DAxis(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Set the y_range and z_range to suit the new function
        axes = ThreeDAxes(
            x_range=[RANGE_START, RANGE_END],  
            y_range=[-m.e**2, m.e**2],  
            z_range=[-9, 9],  
        )
        
        self.add(axes)
        
        # Update the function being plotted
        graph = axes.plot(lambda x: m.exp(x), x_range=[RANGE_START, RANGE_END], color=YELLOW)  
        
        self.play(Create(graph, run_time=3))
        
        # Update the surface equation for the function
        surface = Surface(
            lambda u, v: axes.c2p(u, m.exp(u) * np.cos(v), m.exp(u) * np.sin(v)), 
            u_range=[RANGE_START + 0.01, RANGE_END], v_range=[0, TAU],
            resolution=(20, 40),
            fill_opacity=0.5, color=BLUE
        )
        
        self.play(Create(surface, run_time=3))
        
        self.play(Rotate(VGroup(axes, graph, surface), angle=2 * PI, axis=OUT, run_time=7, rate_func=linear))
        
        # After rotating, select a slice and show radius
        self.wait()
        
        # Be careful to select a slice that is always within range
        sliced_surface = Surface(
            lambda u, v: axes.c2p(u, m.exp(u) * np.cos(v), m.exp(u) * np.sin(v)), 
            u_range=[1, 1.05], v_range=[0, TAU],
            resolution=(20, 40),
            fill_opacity=0.5, color=BLUE
        )
        
        self.play(Transform(surface, sliced_surface))
        
        # Create the radius line
        radius_line = Line(
            start=axes.c2p(1, 0, 0),  # Starting point at (1, 0, 0) on the slice
            end=axes.c2p(1, m.exp(1) * np.cos(0), m.exp(1) * np.sin(0)),  # End point on the surface
            color=RED
        )
        
        self.play(Create(radius_line, run_time=2))
        
        radius_label = MathTex("r = f(x)", color=RED).next_to(radius_line, RIGHT, buff=0.1)
        
        self.move_camera(phi = 0, theta = -90 * DEGREES)
        self.play(Uncreate(surface, run_time=1))
        self.play(Write(radius_label, run_time=1))
        
        self.wait()
        self.clear()
        
        # Write the integral 
        # Change start and end with RANGE_START and RANGE_END
        integral_label = MathTex(r"V = \int_0^2 \pi f(x)^2 dx")
        
        self.play(Write(integral_label))
        self.wait(2)