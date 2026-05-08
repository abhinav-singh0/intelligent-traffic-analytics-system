from flask import Flask, render_template, request
import os

from utils.detector import detect_vehicles

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():

    output_image = None
    analytics = None

    if request.method == "POST":

        if "image" not in request.files:
            return "No file uploaded"

        file = request.files["image"]

        if file.filename == "":
            return "No selected file"

        # Save uploaded image
        image_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(image_path)

        # Run detection
        output_image, analytics = detect_vehicles(image_path)

    return render_template(
        "index.html",
        output_image=output_image,
        analytics=analytics
    )


if __name__ == "__main__":
    app.run(debug=True)