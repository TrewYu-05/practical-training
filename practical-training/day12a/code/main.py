import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)

@app.get('/')
def test_demo():
    return '欢迎来到服务器！'

@app.get('/shop/{product_id}')
def shop(product_id: str):
    if product_id == '100':
        return f'这是A商品，id编号：{product_id}'
    elif product_id == '200':
        return f'这是B商品，id编号：{product_id}'
    else:
        return f'这是商品接口，{product_id}'

fake_item_db = [
    {"id": 0, "name": "商品A"},
    {"id": 1, "name": "商品B"},
    {"id": 2, "name": "商品C"},
    {"id": 3, "name": "商品D"},
    {"id": 4, "name": "商品E"}
]

@app.get('/pages/data')
def data_page(skip: int = 0, limit: int = 10):
    return fake_item_db[skip: skip + limit]

@app.post('/register')
def register_fn(username: str = Form(...), password: str = Form(...)):
    print(username, password)
    return {"code": 1, "msg": '注册成功'}

@app.get('/demo2')
def demo2(user: str):
    if user == 'admin':
        return {"code": 1, "msg": '登录成功'}
    else:
        return {"code": 0, "msg": '用户名或者密码错误'}

@app.get('/demo3', response_class=HTMLResponse)
def demo3():
    return '<h1>hello 美女帅哥！</h1>'

@app.get('/dzy')
def dzy():
    return "欢迎来到丁致宇真爱有缘网"

@app.get('/item')
def item():
    return RedirectResponse(url='/dzy')

@app.get('/home')
def home(a: int = 0, b: int = 0):
    return f'首页数据: a={a}, b={b}'

@app.get('/category')
def category():
    return '分类页面数据'

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080)
