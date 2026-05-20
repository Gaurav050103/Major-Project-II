from flask import Flask, request, render_template, send_from_directory, jsonify
import os
from services.pipeline import run_autodub_pipeline

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_video():
    if 'video' not in request.files:
        return jsonify({"error": "No incoming video payload identified."}), 400
        
    video_file = request.files['video']
    target_lang = request.form.get('target_lang', 'hi')
    voice_profile = request.form.get('voice_profile', 'female') # Capture Voice Selection
    
    if video_file.filename == '':
        return jsonify({"error": "Empty filename header returned."}), 400
        
    source_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
    video_file.save(source_path)
    
    try:
        # Route voice parameters directly through to backend manager
        output_path, filename = run_autodub_pipeline(source_path, target_lang, voice_profile)
        return jsonify({
            "success": True, 
            "message": "Video tracking and localization finished successfully.",
            "video_url": f"/download/{filename}"
        })
    except Exception as e:
        print(f"[Core Pipeline Failure] Stack: {str(e)}")
        return jsonify({"error": f"Execution sequence halted: {str(e)}"}), 500

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)