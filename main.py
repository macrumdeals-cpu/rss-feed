import base64
import requests

def update_github_rss(xml_content):
    # بيانات حسابك في جيت هاب
    GITHUB_TOKEN = "your_github_token_here"  # قم بإنشاء Personal Access Token
    REPO_NAME = "your_username/rss-feed"
    FILE_PATH = "rss.xml"
    
    url = f"https://api.github.io/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # الحصول على sha للملف إذا كان موجوداً مسبقاً للتحديث عليه
    res = requests.get(url, headers=headers)
    sha = res.json().get('sha') if res.status_code == 200 else None
    
    # تشفير محتوى الـ XML إلى Base64
    encoded_content = base64.b64encode(xml_content.encode('utf-8')).decode('utf-8')
    
    data = {
        "message": "Update RSS Feed",
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha
        
    requests.put(url, json=data, headers=headers)
