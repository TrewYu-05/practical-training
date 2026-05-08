import http.client
import urllib.parse
import json
import openpyxl
import os
from dotenv import load_dotenv

# Load environment variables (from repo root)
load_dotenv(os.path.join(os.path.dirname(__file__), '../../../../.env'))
load_dotenv('../../../../.env')
load_dotenv() # It will find .env in root if run from root

# Get the TianAPI key
tianapi_key = os.getenv('TIANAPI_KEY', '')

# Fetch news data
conn = http.client.HTTPSConnection('apis.tianapi.com')
params = urllib.parse.urlencode({'key': tianapi_key, 'num': '5'})
headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/huanbao/index', params, headers)
tianapi = conn.getresponse()
result = tianapi.read()
data = result.decode('utf-8')
dict_data = json.loads(data)

print(f"API Code: {dict_data.get('code')}, Message: {dict_data.get('msg')}")

# Save to Excel
news_list = dict_data.get('result', {}).get('newslist', [])

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "环保新闻"
ws.append(["编号", "标题", "来源", "链接"])

for i, news in enumerate(news_list, 1):
    ws.append([i, news.get('title'), news.get('source'), news.get('url')])

excel_path = os.path.join(os.path.dirname(__file__), "news_data.xlsx")
wb.save(excel_path)
print(f"Data saved to {excel_path}")
