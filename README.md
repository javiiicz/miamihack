# Customized Math Vizualizer

This project is an application that allows you to connect to you phone to analyze your math problem, and generate your very own Manim video, inspired by the goat 3b1b Grant Sanderson, to visualize complex concepts like the volume of a disk in calculus. We combined the following available technologies:

1. **Mathpix API**: For extracting LaTeX equations from images of math problems.
2. **OpenAI API**: For generating Manim script templates based on the extracted LaTeX equations.
3. **Manim Open Source Library**: For rendering the mathematical visualizations into high-quality videos.

---

## How It Works

### 1. **Capture and Analyze the Math Problem**
- The application uses your device's camera to capture an image of a math problem.
- The image is sent to the **Mathpix API**, which derives the LaTeX representation of the equation.

### 2. **Generate Manim Script**
- The derived LaTeX equation is passed to the **OpenAI API**, which adjusts parameters of a **Manim script** tailored to your personal question to visualize the concept (e.g., volume of a disk, surface area, etc.).
- The OpenAI API ensures the script is accurate and visually appealing.

### 3. **Render the Visualization**
- The generated Manim script is executed automatically using the **Manim library** to produce a high-quality video.
- The video visualizes the math problem, making it easier to understand complex concepts.

---

## Technologies Used

### **Mathpix API**
- **Purpose**: Extracts LaTeX equations from images of math problems.
- **How It Works**: The application captures an image of the math problem, encodes it in base64, and sends it to the Mathpix API. The API returns the LaTeX representation of the equation.

### **OpenAI API**
- **Purpose**: Generates a Manim script based on the extracted LaTeX equation.
- **How It Works**: The LaTeX equation is passed to the OpenAI API, which uses a prompt to generate a Manim script. The script is designed to visualize the math problem effectively.

### **Manim**
- **Purpose**: Renders the mathematical visualization into a video.
- **How It Works**: The generated Manim script is executed, producing a video that visualizes the math problem. The video can be previewed or saved for later use.

---

## Example: Volume of a Disk
For a calculus problem involving the **volume of a disk**, the application:
1. Captures an image of the equation (e.g., \( V = \int_{a}^{b} \pi r^2 \, dx \)).
2. Extracts the LaTeX equation using Mathpix.
3. Generates a Manim script using OpenAI to visualize the disk method.
4. Renders a video showing the disk being rotated and integrated to calculate the volume to help students excel in math :)

---

