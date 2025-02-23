import cv2
import requests
import json
import base64

latex_output = None
app_id = "visualize_me_f97908_b55e94"
app_key = "560f1a62008d03c970b565be9298bb462e57d596b95bcc140f8ed66d53a439bb"

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    print("Press 's' to take a photo or 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow("Webcam", frame)

       
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Press 's' to take a photo
            image_path = "math_problem.png"
            cv2.imwrite(image_path, frame)
            print(f"Image saved as {image_path}")
            break
        elif key == ord('q'):  # Press 'q' to quit
            print("Exiting without taking a photo.")
            return None

   
    cap.release()
    cv2.destroyAllWindows()
    return image_path


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

#function to send the image to Mathpix API and get LaTeX output
def mathpix_latex(image_base64):
    url = "https://api.mathpix.com/v3/text"
    headers = {
        "app_id": app_id,
        "app_key": app_key,
        "Content-type": "application/json"
    }
    data = {
        "src": f"data:image/png;base64,{image_base64}",
        "formats": ["latex_styled"]  
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()


def main():
    global latex_output
    image_path = capture_image()
    if not image_path:
        return

    image_base64 = encode_image_to_base64(image_path)

    
    result = mathpix_latex(image_base64)
    latex_output = result.get("latex_styled")
    if not latex_output:
        print("Error: Could not extract LaTeX from the image.")
        print("API Response:", result)  
        return

    print("LaTeX Output:")
    print(latex_output)




if __name__ == "__main__":
    main()