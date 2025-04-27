from flask import Flask, request, render_template, jsonify
import os
from prompt import prompt
from dotenv import load_dotenv
from gemini import GeminiProcessor

# Load environment variables from .env file
load_dotenv()

# Initialize Gemini processor
gemini_processor = GeminiProcessor()

app = Flask(__name__, template_folder='./templates', static_folder='./static')

# Ensure templates directory exists
os.makedirs('./templates', exist_ok=True)
os.makedirs('./static', exist_ok=True)

@app.route('/')
def home():
    """Render the home page with text input form"""
    return render_template('index.html')

@app.route('/process_report', methods=['POST'])
def process_report():
    """Process the medical report and return the formatted HTML"""
    if request.is_json:
        data = request.get_json()
        report_text = data.get('report_text', '')
    else:
        report_text = request.form.get('report_text', '')
    
    if not report_text:
        return jsonify({"error": "No report text provided"}), 400
    
    # Generate formatted report using AI
    try:
        # Process report using Gemini
        generated_html = gemini_processor.process_report(prompt, report_text)
        
        # Read the template file
        with open('./report_template.html', 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        # Replace the placeholder in the template
        final_html = template_content.replace(
            '<div id="report-container">\n    <!-- LLM-generated content goes here -->\n  </div>',
            f'<div id="report-container">\n    {generated_html}\n  </div>'
        )
        
        return final_html
        
    except Exception as e:
        return jsonify({"error": f"Error processing report: {str(e)}"}), 500

@app.route('/render_report', methods=['GET'])
def render_report():
    """Render the processed report template"""
    report_html = request.args.get('html', '')
    if not report_html:
        return "No report HTML provided", 400
    
    return report_html

if __name__ == '__main__':
    app.run(debug=True)
