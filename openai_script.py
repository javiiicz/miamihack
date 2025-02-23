from openai import OpenAI
import cvlatex
from dotenv import load_dotenv
import os

load_dotenv(override=True)

key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=key
)

def generate_manim_script_with_openai(prompt):
    """
    Generates a Manim script using OpenAI's chat-based model.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",  #model
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates Manim scripts for animating mathematical equations."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,  
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

def main():
    cvlatex.main()
    question = cvlatex.latex_output
    print(f"trial: {question}") ##WORKS FINALLY
    #hardcoded prompt for OpenAI
    prompt = f"""
    
    Help me replace some of the important information in the following script, but do not reply sure I can help you or anything else just give me back the script THAT'S IT. Also write the script as text not with markdown because it will be used to write to a python script so do not include ```python. You will be given a python manim script and a string containing a math problem. If the problem a matches a calculating volume of function around the x axis problem then do the following: - identify the function thats being analyzed - Identify the range where the function is being analyzed - Change the RANGE_START and RANGE_END variables - Change the function in the code wherever you see m.exp(x) (this was a placeholder function) If the problem does not match reply the number -1.
from manim import *\nimport math as m\nimport random as r\nimport subprocess\n\n\nRANGE_START = 1\nRANGE_END = 2\nclass Rotating3DAxis(ThreeDScene):\n    def construct(self):\n        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)\n        \n        # Set the y_range and z_range to suit the new function\n        axes = ThreeDAxes(\n            x_range=[RANGE_START - 1, RANGE_END + 1],  \n            y_range=[-(m.exp(RANGE_END)), (m.exp(RANGE_END))],  \n            z_range=[-(m.exp(RANGE_END)), (m.exp(RANGE_END))],  \n        )\n        \n        self.add(axes)\n        \n        # Update the function being plotted\n        graph = axes.plot(lambda x: m.exp(x), x_range=[RANGE_START, RANGE_END], color=YELLOW)  \n        \n        self.play(Create(graph, run_time=3))\n        \n        # Update the surface equation for the function\n        surface = Surface(\n            lambda u, v: axes.c2p(u, (m.exp(u)) * np.cos(v), (m.exp(u) * np.sin(v))), \n            u_range=[RANGE_START + 0.01, RANGE_END], v_range=[0, TAU],\n            resolution=(20, 40),\n            fill_opacity=0.5, color=BLUE\n        )\n        \n        self.play(Create(surface, run_time=3))\n        \n        self.play(Rotate(VGroup(axes, graph, surface), angle=2 * PI, axis=OUT, run_time=7, rate_func=smooth))\n        \n        # After rotating, select a slice and show radius\n        self.wait()\n        \n        # Be careful to select a slice that is always within range\n        p = (RANGE_START + RANGE_END)/2\n        sliced_surface = Surface(\n            lambda u, v: axes.c2p(u, (m.exp(u)) * np.cos(v), (m.exp(u)) * np.sin(v)), \n            u_range=[p, p + 0.05], v_range=[0, TAU],\n            resolution=(20, 40),\n            fill_opacity=0.5, color=BLUE\n        )\n        \n        self.play(Transform(surface, sliced_surface))\n        \n        # Create the radius line\n        radius_line = Line(\n            start=axes.c2p(p, 0, 0),\n            end=axes.c2p(p, (m.exp(p)) * np.cos(0), (m.exp(p)) * np.sin(0)),  # End point on the surface\n            color=RED\n        )\n        \n        self.play(Create(radius_line, run_time=2))\n        \n        radius_label = MathTex("r = f(x)", color=RED).next_to(radius_line, RIGHT, buff=0.1)\n        \n        self.move_camera(phi = 0, theta = -90 * DEGREES)\n        self.play(Uncreate(surface, run_time=1))\n        self.play(Write(radius_label, run_time=1))\n        \n        self.wait()\n        self.clear()\n        \n        # Write the integral \n        # Change start and end with RANGE_START and RANGE_END\n        integral_label = MathTex(r"V = \int_1^2 \pi r^2 dx")\n        \n        self.play(Write(integral_label))\n        self.wait(2)\n        

def main():\n    #subprocess to call the manim command with the -p flag\n    command = [\n        "manim",\n        "-pql",  # -p: preview, -ql: low quality\n        #"-f",  ##full screen if needed\n        "generated_manim_script.py",  \n    ]\n    \n    # Run the command\n    subprocess.run(command)\n\nif __name__ == "__main__":\n    main()
\n\n\nProblem: {question}
    """

    #generate the manim script using OpenAI
    print(prompt)
    response = generate_manim_script_with_openai(prompt)
    if response == "-1":
        print("CANNOT ANALYZE YET")
        return
        
    manim_script = response
    print("Generated Manim Script:")
    print(manim_script)

    #save the generated Manim script to a file
    with open("generated_manim_script.py", "w") as f:
        f.write(manim_script)

    print("Manim script saved as 'generated_manim_script.py'.")
    
    import generated_manim_script

    generated_manim_script.main()

if __name__ == "__main__":
    main()




