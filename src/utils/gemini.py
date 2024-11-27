import google.generativeai as genai
from config import GEMINI_API_KEY
from PIL import Image
import io

class GeminiAPI:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')
        self.text_model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    def generate_message(self, pet_name: str, comment: str) -> str:
        """生成寵物的回應訊息"""
        prompt = f"""
        You are {pet_name}, a beloved pet. Your owner wrote you this message:
        "{comment}"
        
        Please write a heartwarming response message (maximum 3 sentences) to your owner.
        The message should:
        1. Be emotional and touching
        2. Reference specific details from their message
        3. Express love and gratitude
        4. Comfort them about your current state in heaven
        
        Write only the message, without any additional text or quotation marks.
        """
        
        try:
            response = self.text_model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Dear owner, this is {pet_name}. Thank you for all the love you've given me. I'm happy and peaceful in heaven now."

    def analyze_pet_characteristics(self, comment: str) -> dict:
        """分析寵物特徵（使用文本而不是圖片）"""
        prompt = f"""
        Based on this message from a pet owner:
        "{comment}"
        
        Please analyze and create a JSON response with the following fields:
        - pet_type: what kind of pet it might be
        - characteristics: physical characteristics that can be imagined
        - personality: personality traits that can be inferred
        
        Keep the response concise and focused on creating a new pet image.
        """
        
        try:
            response = self.text_model.generate_content(prompt)
            response_text = response.text
            
            # 解析 JSON
            import json
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            json_str = response_text[start_idx:end_idx]
            return json.loads(json_str)
        except:
            # 如果解析失敗，返回預設值
            return {
                "pet_type": "Lovely Pet",
                "characteristics": "Unique appearance with gentle features",
                "personality": "Kind and loving nature"
            }