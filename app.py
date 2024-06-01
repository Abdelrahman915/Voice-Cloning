import os
import subprocess
from flask import Flask, request, redirect, url_for, render_template,flash, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flashing messages

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
MODEL_FOLDER = 'models'
ALLOWED_EXTENSIONS = {'wav'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MODEL_FOLDER'] = MODEL_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

if not os.path.exists(MODEL_FOLDER):
    os.makedirs(MODEL_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_models():
    models = [f for f in os.listdir(app.config['MODEL_FOLDER']) if os.path.isdir(os.path.join(app.config['MODEL_FOLDER'], f))]
    return models

def clear_uploads_and_outputs():
    for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER]:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error: {e}")

@app.route('/')
def upload_form():
    models = get_models()
    filename = request.args.get('filename')
    error = request.args.get('error')
    return render_template('upload.html', models=models, filename=filename, error=error)

@app.route('/upload', methods=['POST'])
def upload_file():
    clear_uploads_and_outputs()

    if 'file' not in request.files or 'model' not in request.form:
        flash("File or model part not in the request", 'error')
        return redirect(url_for('upload_form'))
    
    file = request.files['file']
    model = request.form['model']
    
    if file.filename == '':
        flash("No file selected", 'error')
        return redirect(url_for('upload_form'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Perform inference using the svc command
        model_path = os.path.join(app.config['MODEL_FOLDER'], model)
        output_filename = f"output_{filename.rsplit('.', 1)[0]}.wav"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

        config_path = os.path.join(model_path, 'config.json')
        model_files = [os.path.join(model_path, f) for f in os.listdir(model_path) if f.endswith('.pth')]
        if not model_files:
            flash("Model files not found in the selected model directory", 'error')
            return redirect(url_for('upload_form'))

        flash("File uploaded successfully. Voice cloning in progress...", 'info')
        command = [
            'svc', 'infer',
            '-na', file_path,
            '-m', model_path,
            '-c', config_path,
            '-o', output_path  # Specify the output file path
        ]
        
        try:
            subprocess.run(command, check=True)
            if not os.path.exists(output_path):
                raise FileNotFoundError(f"Inferred output file not found: {output_path}")
            
            # Delete the input file after inference
            os.remove(file_path)
        except subprocess.CalledProcessError as e:
            print(f"Inference command failed with error: {e}")
            flash("Inference command failed", 'error')
            return redirect(url_for('upload_form'))

        #flash("Voice cloning completed successfully!", 'success')
        return redirect(url_for('upload_form', filename=output_filename))
    
    flash("File type not allowed", 'error')
    return redirect(url_for('upload_form'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/outputs/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)
