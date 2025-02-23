from manim import *
import math as m
import random as r
import subprocess


RANGE_START = 0.5
RANGE_END = 2
class Rotating3DAxis(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Set the y_range and z_range to suit the new function
        axes = ThreeDAxes(
            x_range=[RANGE_START - 1, RANGE_END + 1],  
            y_range=[0, (m.sin(RANGE_END)**2 * m.exp(RANGE_END) + 1)],  
            z_range=[0, (m.sin(RANGE_END)**2 * m.exp(RANGE_END) + 1)],  
        )
        
        self.add(axes)
        
        # Update the function being plotted
        graph = axes.plot(lambda x: m.sin(x)**2 * m.exp(x) + 1, x_range=[RANGE_START, RANGE_END], color=YELLOW)  
        
        self.play(Create(graph, run_time=3))
        
        # Update the surface equation for the function
        surface = Surface(
            lambda u, v: axes.c2p(u, (m.sin(u)**2 * m.exp(u) + 1) * np.cos(v), (m.sin(u)**2 * m.exp(u) + 1) * np.sin(v)), 
            u_range=[RANGE_START + 0.01, RANGE_END], v_range=[0, TAU],
            resolution=(20, 40),
            fill_opacity=0.5, color=BLUE
        )
        
        self.play(Create(surface, run_time=3))
        
        self.play(Rotate(VGroup(axes, graph, surface), angle=2 * PI, axis=OUT, run_time=7, rate_func=smooth))
        
        # After rotating, select a slice and show radius
        self.wait()
        
        # Be careful to select a slice that is always within range
        p = (RANGE_START + RANGE_END)/2
        sliced_surface = Surface(
            lambda u, v: axes.c2p(u, (m.sin(u)**2 * m.exp(u) + 1) * np.cos(v), (m.sin(u)**2 * m.exp(u) + 1) * np.sin(v)), 
            u_range=[p, p + 0.05], v_range=[0, TAU],
            resolution=(20, 40),
            fill_opacity=0.5, color=BLUE
        )
        
        self.play(Transform(surface, sliced_surface))
        
        # Create the radius line
        radius_line = Line(
            start=axes.c2p(p, 0, 0),
            end=axes.c2p(p, (m.sin(p)**2 * m.exp(p) + 1) * np.cos(0), (m.sin(p)**2 * m.exp(p) + 1) * np.sin(0)),  # End point on the surface
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
        integral_label = MathTex(r"V = \int_{0.5}^{2} \pi r^2 dx")
        
        self.play(Write(integral_label))
        self.wait(2)
        

def main():
    #subprocess to call the manim command with the -p flag
    command = [
        "manim",
        "-pql",  # -p: preview, -ql: low quality
        #"-f",  ##full screen if needed
        "generated_manim_script.py",  
    ]
    
    # Run the command
    subprocess.run(command)

if __name__ == "__main__":
    main()