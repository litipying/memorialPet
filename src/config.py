import os
from dotenv import load_dotenv

# 載入 .env 文件
load_dotenv()

# API Keys
STABILITY_API_KEY = os.getenv('STABILITY_API_KEY')
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')

# 檢查必要的環境變數
def check_env_variables():
    missing_vars = []
    if not STABILITY_API_KEY:
        missing_vars.append('STABILITY_API_KEY')
    if not MISTRAL_API_KEY:
        missing_vars.append('MISTRAL_API_KEY')
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}. "
            "Please make sure these variables are set in your .env file."
        ) 