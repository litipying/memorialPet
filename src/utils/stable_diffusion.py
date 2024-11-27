from config import STABILITY_API_KEY
import requests
import base64
from PIL import Image
import io

class StableDiffusionAPI:
    def __init__(self):
        self.api_key = STABILITY_API_KEY
        self.api_host = 'https://api.stability.ai'
        
    def image_to_image(self, init_image: bytes, prompt: str) -> bytes:
        """
        使用 Stable Diffusion 的 image-to-image API 生成新圖片
        Reference: https://platform.stability.ai/docs/api-reference#tag/SDXL-1.0-and-SD1.6/operation/imageToImage
        """
        engine_id = "stable-diffusion-v1-6"
        
        # 準備圖片數據
        image = Image.open(io.BytesIO(init_image))
        # 確保圖片是 RGB 模式
        if image.mode != "RGB":
            image = image.convert("RGB")
        # 調整圖片大小到 1024x1024
        image = image.resize((1024, 1024))
        # 轉換為 PNG 格式的字節數據
        buf = io.BytesIO()
        image.save(buf, format='PNG')
        init_image_data = buf.getvalue()
        
        response = requests.post(
            f"{self.api_host}/v1/generation/{engine_id}/image-to-image",
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            },
            files={
                "init_image": ("image.png", init_image_data, "image/png")
            },
            data={
                "init_image_mode": "IMAGE_STRENGTH",
                "image_strength": 0.35,
                "steps": 50,
                "seed": 0,
                "cfg_scale": 7,
                "samples": 1,
                "text_prompts[0][text]": prompt,
                "text_prompts[0][weight]": 1,
                "style_preset": "enhance",
            }
        )
        
        if response.status_code != 200:
            raise Exception(f"API 請求失敗: {response.text}")
            
        data = response.json()
        image_data = base64.b64decode(data["artifacts"][0]["base64"])
        return image_data

    def text_to_image(self, prompt: str) -> bytes:
        """
        使用 Stable Diffusion 的 text-to-image API 生成新圖片
        """
        engine_id = "stable-diffusion-v1-6"
        
        response = requests.post(
            f"{self.api_host}/v1/generation/{engine_id}/text-to-image",
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            },
            json={
                "text_prompts": [{"text": prompt}],
                "cfg_scale": 7,
                "height": 1024,
                "width": 1024,
                "samples": 1,
            },
        )
        
        if response.status_code != 200:
            raise Exception(f"API 請求失敗: {response.text}")
            
        data = response.json()
        image_data = base64.b64decode(data["artifacts"][0]["base64"])
        return image_data 