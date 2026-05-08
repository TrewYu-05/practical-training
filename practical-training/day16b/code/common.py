import requests
from bs4 import BeautifulSoup
import json

def fetch_page(url):
    resp = requests.get(
        url=url,
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.3'
        }
    )
    resp.encoding = 'utf-8'
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        for elem in soup.body(['script', 'link', 'nav', 'header', 'footer', 'form', 'input', 'button', 'img', 'audio', 'video', 'area', 'canvas', 'map', 'object', 'embed']):
            elem.decompose()
        return soup.title.text if soup.title else "No Title", soup.body.get_text(separator='\n', strip=True) if soup.body else ""
    else:
        return "Error", f"HTTP Status Code: {resp.status_code}"

def get_llm_response(client, *, system_prompt='', few_shot_prompt='', user_prompt='', model='qwen3-max', stream=False):
    messages = []
    if system_prompt:
        messages.append({'role': 'system', 'content': system_prompt})
    if few_shot_prompt:
        messages += json.loads(few_shot_prompt)
    if user_prompt:
        messages.append({'role': 'user', 'content': user_prompt})

    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream
    )
    if not stream:
        return resp.choices[0].message.content
    return resp
