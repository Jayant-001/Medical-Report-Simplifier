from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GeminiProcessor:
    def __init__(self, api_key=None):
        # Use API key from environment variable if not provided
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.0-flash"  # Default model
    
    def set_model(self, model_name):
        """Update the model to use"""
        self.model = model_name
        return self
    
    def process_report(self, system_prompt, report_text):
        """
        Process a medical report using Gemini AI.
        
        Args:
            system_prompt (str): The system prompt from prompt.py
            report_text (str): The user's medical report text
            
        Returns:
            str: The generated HTML content
        """
        try:
            response = self.client.models.generate_content(
                model=self.model,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt),
                contents=[report_text]
            )
            
            content = response.text
            
            # Clean up the markdown code block markers
            content = content.replace("```html", "")
            content = content.replace("```", "")
            content = content.strip()
            
            return content
            
        except Exception as e:
            raise Exception(f"Error processing with Gemini: {str(e)}")

# Example usage
if __name__ == "__main__":
    from prompt import prompt as system_prompt
    
    user_prompt = """
    History
    Patient has a history of heart failure and chronic obstructive pulmonary disease (COPD).

    Diagnosis
    Recent tests indicate pulmonary edema and atrial fibrillation.

    Treatment Plan
    Start digoxin to manage heart failure symptoms.
    Prescribe enalapril to lower blood pressure and prevent further damage to the heart.
    Initiate warfarin therapy for atrial fibrillation.
    
    Follow-Up
    The patient is scheduled for a follow-up visit in two weeks for further evaluation and to monitor the effectiveness of prescribed medications.
    """
    
    processor = GeminiProcessor()
    result = processor.process_report(system_prompt, user_prompt)
    print(result)