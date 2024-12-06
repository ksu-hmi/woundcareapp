from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create folder for uploads

# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "No image file uploaded.", 400

        file = request.files["image"]
        if file.filename == "":
            return "No selected file.", 400

        # Save the uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Example wound stage and care recommendation logic
        wound_stage = "Stage 2"  # Placeholder for analysis
        care_recommendation = (
            "Clean the wound with saline, apply a hydrocolloid dressing, and monitor for infection."
        )

        # Simulated response
        response = {
            "filename": file.filename,
            "wound_stage": wound_stage,
            "care_recommendation": care_recommendation,
        }

        return jsonify(response)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
