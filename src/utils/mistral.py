from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from config import MISTRAL_API_KEY
import json

class MistralAPI:
    def __init__(self):
        self.client = MistralClient(api_key=MISTRAL_API_KEY)
        self.model = "mistral-large-latest"
    
    def generate_message(self, pet_name: str, comment: str) -> str:
        """Generate response message from pet"""
        messages = [
            ChatMessage(
                role="system",
                content="You are a beloved pet responding to your owner's message. Your response should be emotional, touching, and reference specific details from their message."
            ),
            ChatMessage(
                role="user",
                content=f"""As {pet_name}, write a heartwarming response (maximum 3 sentences) to this message from your owner:
                "{comment}"
                
                The response should:
                1. Be emotional and touching
                2. Reference specific details from their message
                3. Express love and gratitude
                4. Comfort them about your current state in heaven
                
                Write only the message, without any additional text or quotation marks."""
            )
        ]
        
        try:
            response = self.client.chat(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=150
            )
            return response.messages[0].content.strip()
        except Exception as e:
            return f"Dear owner, this is {pet_name}. Thank you for all the love you've given me. I'm happy and peaceful in heaven now."

    def analyze_pet_characteristics(self, comment: str) -> dict:
        """Analyze pet characteristics from owner's message"""
        messages = [
            ChatMessage(
                role="system",
                content="You are an AI that analyzes messages from pet owners to understand their pets' characteristics. Respond in JSON format."
            ),
            ChatMessage(
                role="user",
                content=f"""Based on this message from a pet owner:
                "{comment}"
                
                Create a JSON response with these fields:
                - pet_type: what kind of pet it might be
                - characteristics: physical characteristics that can be imagined
                - personality: personality traits that can be inferred
                
                Keep the response concise and focused on creating a new pet image."""
            )
        ]
        
        try:
            response = self.client.chat(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=200
            )
            response_text = response.messages[0].content
            
            # Parse JSON from response
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            json_str = response_text[start_idx:end_idx]
            return json.loads(json_str)
        except:
            return {
                "pet_type": "Lovely Pet",
                "characteristics": "Unique appearance with gentle features",
                "personality": "Kind and loving nature"
            } 