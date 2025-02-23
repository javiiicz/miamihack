import openai


import cvlatex
cvlatex.main()
question = cvlatex.latex_output
print(f"trial: {question}") ##WORKS FINALLY

openai.api_key = "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"

def generate_manim_script_with_openai(prompt):
    """
    Generates a Manim script using OpenAI's chat-based model.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  #model
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates Manim scripts for animating mathematical equations."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,  
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

def main():
    #hardcoded prompt for OpenAI
    prompt = f"""
    
    Help me replace some of the important information in the following script, but do not reply sure I can help you or anything else just give me back the script THAT'S IT. Also write the script as text not with markdown because it will be used to write to a python script so do not include ```python. Also please make sure to add "from manim import *\n
import numpy as np\n import subprocess\n" at the top. You will be given a python manim script and a string containing a math problem. If the problem a matches solids of revolution around the x axis problem then do the following: - identify the function thats being analyzed - Identify the range where the function is being analyzed - Change the RANGE_START and RANGE_END variables - Change the function in the code wherever you see x**2 (this was a placeholder function) If the problem does not match reply that you cannot analyze that problem yet.
class Rotating3DAxis(ThreeDScene):\n    def construct(self):\n        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)\n        \n        # Set the y_range and z_range to suit the new function\n        axes = ThreeDAxes(\n            x_range=[RANGE_START - 1, RANGE_END + 1],  \n            y_range=[-(RANGE_END**2 + 2), (RANGE_END**2 + 2)],  \n            z_range=[-(RANGE_END**2 + 2), (RANGE_END**2 + 2)],  \n        )\n        \n        self.add(axes)\n        \n        # Update the function being plotted\n        graph = axes.plot(lambda x: x**2 + 2, x_range=[RANGE_START, RANGE_END], color=YELLOW)  \n        \n        self.play(Create(graph, run_time=3))\n        \n        # Update the surface equation for the function\n        surface = Surface(\n            lambda u, v: axes.c2p(u, (u**2 + 2) * np.cos(v), (u**2 + 2) * np.sin(v)), \n            u_range=[RANGE_START + 0.01, RANGE_END], v_range=[0, TAU],\n            resolution=(20, 40),\n            fill_opacity=0.5, color=BLUE\n        )\n        \n        self.play(Create(surface, run_time=3))\n        \n        self.play(Rotate(VGroup(axes, graph, surface), angle=2 * PI, axis=OUT, run_time=7, rate_func=smooth))\n        \n        # After rotating, select a slice and show radius\n        self.wait()\n        \n        # Be careful to select a slice that is always within range\n        p = (RANGE_START + RANGE_END)/2\n        sliced_surface = Surface(\n            lambda u, v: axes.c2p(u, (u**2 + 2) * np.cos(v), (u**2 + 2) * np.sin(v)), \n            u_range=[p, p + 0.05], v_range=[0, TAU],\n            resolution=(20, 40),\n            fill_opacity=0.5, color=BLUE\n        )\n        \n        self.play(Transform(surface, sliced_surface))\n        \n        # Create the radius line\n        radius_line = Line(\n            start=axes.c2p(p, 0, 0),\n            end=axes.c2p(p, (p**2 + 2) * np.cos(0), (p**2 + 2) * np.sin(0)),  # End point on the surface\n            color=RED\n        )\n        \n        self.play(Create(radius_line, run_time=2))\n        \n        radius_label = MathTex("r = f(x)", color=RED).next_to(radius_line, RIGHT, buff=0.1)\n        \n        self.move_camera(phi = 0, theta = -90 * DEGREES)\n        self.play(Uncreate(surface, run_time=1))\n        self.play(Write(radius_label, run_time=1))\n        \n        self.wait()\n        self.clear()\n        \n        # Write the integral \n        # Change start and end with RANGE_START and RANGE_END\n        integral_label = MathTex(r"V = \int_1^2 \pi r^2 dx")\n        \n        self.play(Write(integral_label))\n        self.wait(2)\n

def main():\n    #subprocess to call the manim command with the -p flag\n    command = [\n        "manim",\n        "-pql",  # -p: preview, -ql: low quality\n        #"-f",  ##full screen if needed\n        "generated_manim_script.py",  \n    ]\n    \n    # Run the command\n    subprocess.run(command)\n\nif __name__ == "__main__":\n    main()
\n\n\nProblem: {question}
    """

    #generate the manim script using OpenAI
    manim_script = generate_manim_script_with_openai(prompt)
    print("Generated Manim Script:")
    print(manim_script)

    #save the generated Manim script to a file
    with open("generated_manim_script.py", "w") as f:
        f.write(manim_script)

    print("Manim script saved as 'generated_manim_script.py'.")

if __name__ == "__main__":
    main()


import generated_manim_script

generated_manim_script.main()

