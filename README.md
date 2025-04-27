# Medical Report Simplifier

A Flask application that simplifies medical reports by converting technical medical terms into plain language explanations using Google's Gemini AI.

## Features

- Home page with a form to input medical reports
- AI-powered processing of medical reports using Google Gemini AI
- Interactive HTML output with medical terms highlighted and explained

## Setup

1. Create a virtual environment and activate it:

   ```
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up your Google Gemini API key:
   Create a `.env` file in the root directory and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Running the Application

1. Start the Flask application:

   ```
   python app.py
   ```

2. Open a web browser and navigate to:

   ```
   http://localhost:5000
   ```

3. Enter a medical report in the text area and click "Generate Simplified Report"

4. The processed report will open in a new browser tab with medical terms highlighted and explanations available on hover/click

## Project Structure

- `app.py` - Flask application with routes
- `prompt.py` - Contains the prompt for the AI model
- `gemini.py` - Contains the Gemini AI integration
- `report_template.html` - HTML template for the processed reports
- `templates/index.html` - Home page template
- `requirements.txt` - Python dependencies

## Technology Stack

- Flask (Python web framework)
- Google Gemini AI API
- HTML/CSS/JavaScript

## Note

This application requires a Google Gemini API key to function. Make sure to set up your API key in the `.env` file before running the application.
