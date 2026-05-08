# 集中实训代码仓库

本仓库为集中实训课程的全部实验代码与运行结果截图，涵盖从 Python 基础、前端开发、后端接口、大模型调用，到 LangChain 框架、RAG 检索增强生成、智能体（Agent）以及综合项目实战的完整学习路径。

## 目录结构

```
practical-training/
├── day01a ~ day01f     # Python 基础：流程控制与字符串处理
├── day02a ~ day02g     # Python 进阶：数据清洗与逻辑判断
├── day03a ~ day03c     # Python 面向对象初级：类与文件读写
├── day04a              # OOP 实战：人力资源管理系统
├── day05a ~ day05b     # OOP 高级 + HTML 表单
├── day06a              # CSS 页面排版设计
├── day07a ~ day07b     # HTML/CSS 静态布局 + JavaScript DOM 渲染
├── day08a              # 企业完整静态网站开发
├── day09a              # JavaScript 前端计算器
├── day10a ~ day10c     # JavaScript 动态表格、随机点名、多功能计算器
├── day11a ~ day11b     # JavaScript OOP + ES6 模块化（购物车）
├── day12a ~ day12b     # FastAPI 后端接口 + Ajax 跨域
├── day13a              # API 数据采集（天行新闻）→ Excel 持久化
├── day13c              # 阿里云通义千问大模型基础调用
├── day14a ~ day14b     # Few-Shot 情感分类 + 上下文记忆注入
├── day15a ~ day15c     # Streamlit 多页面架构 + 情感分析/文案助手
├── day16a ~ day16b     # Streamlit 聊天机器人 + 网页摘要生成
├── day17a ~ day17c     # LangChain 对话记忆 / Embeddings 向量化 / Prompt 模板
├── day18a ~ day18d     # Pydantic 结构化提取 / Ollama 本地部署 / 并发流水线 / 科普文生成
├── day19a ~ day19c     # 链式流水线 / 长篇创作 / 滑窗记忆聊天应用
├── day21a ~ day21c     # RAG 文档切分 / ChromaDB 向量检索 / 颐和园智能导游 Agent
├── day22a ~ day22b     # LangGraph 会话记忆追踪 / Deep Agent 本地技能推理
├── project1            # 综合项目：2020 年销售数据分析（Pandas）
├── project2            # 综合项目：AI 智能简历助手（Streamlit + OpenAI）
├── project3            # 综合项目：RAG + YOLO 融合系统导航（Streamlit）
└── project4            # 综合项目：专业领域大模型语料知识库（RAG + ChromaDB）
```

每个任务子目录均包含以下内容：
- `code/`：可执行的 Python / HTML / CSS / JS 代码文件
- `pictures/`：运行结果或页面渲染的截图

公共数据文件位于 `db/` 目录：
- `goods.txt`：商品信息 CSV 样例
- `students.csv`：学生信息 CSV 样例

## 课程体系概览

### 第一阶段：Python 编程基础（Day 01 ~ 03）

| 任务编号 | 任务名称 | 涉及知识点 |
|:---:|------|------|
| day01a | Craps 游戏 | `random`、条件分支、循环 |
| day01b | Craps 游戏 Plus 版 | 复杂游戏逻辑、金额管理 |
| day01c | 字符串清洗与格式化 | 字符串方法、正则 |
| day01d | 双色球随机选号 | 随机数、列表操作 |
| day01e | 城市区域字段拆分 | 字符串分割与提取 |
| day01f | 统计字符串字符个数 | 字典计数、字符分类 |
| day02a | 提取英文名 | 正则表达式匹配 |
| day02b | 含单位数值字段清洗 | 数据清洗、类型转换 |
| day02c | 敏感数据脱敏展示 | 字符串处理、隐私保护 |
| day02d | URL 参数提取 | URL 解析、参数拆分 |
| day02e | 复杂学校层级数据查询统计 | 嵌套字典遍历、聚合统计 |
| day02f | 检测密码强度 | 多条件判断、字符分类 |
| day02g | 统计元音字母数量 | 集合、循环遍历 |
| day03a | 商品信息管理系统 | 字典增删改查、CRUD |
| day03b | Txt 与 CSV 文件读写 | `csv` 模块、文件 I/O |
| day03c | 创建学生类对象 | 面向对象入门、`class` 定义 |

### 第二阶段：面向对象与前端基础（Day 04 ~ 11）

| 任务编号 | 任务名称 | 涉及知识点 |
|:---:|------|------|
| day04a | 人力资源管理系统 | 完整 OOP 设计、继承 |
| day05a | 多态与私有属性验证 | 多态、封装、`@property` |
| day05b | 真爱有缘网注册表单 | HTML 表单、Form 控件 |
| day06a | 欢迎注册页面排版设计 | CSS 选择器、盒模型、布局 |
| day07a | 淘宝链接区域静态布局 | HTML/CSS 综合布局 |
| day07b | 小米商品列表动态渲染 | JavaScript DOM 操作、模板字符串 |
| day08a | 企业完整静态网站 | HTML/CSS/JS 综合项目 |
| day09a | 简易前端计算器 v1 | JavaScript 事件处理 |
| day10a | 动态表格数据渲染 | JS 循环、表格 DOM 构建 |
| day10b | 网页随机点名系统 | 定时器、随机数、数组 |
| day10c | 多功能计算器升级版 | JS 综合逻辑、状态管理 |
| day11a | 面向对象版 Tab 切换 | JavaScript OOP、原型/类 |
| day11b | 购物车模块化 | ES6 Module、`import/export` |

### 第三阶段：后端接口与大模型调用（Day 12 ~ 14）

| 任务编号 | 任务名称 | 涉及知识点 |
|:---:|------|------|
| day12a | FastAPI 后端 API 接口设计 | FastAPI、路由、CORS、Uvicorn |
| day12b | 前端 Ajax 跨域请求交互 | Ajax、跨域策略、前后端联调 |
| day13a | 天行 API 新闻数据网络采集 | `http.client`、`openpyxl`、API 调用 |
| day13c | 阿里云大模型基础对话 | OpenAI SDK、`requests`、流式输出 |
| day14a | Few-Shot 情感分类器 | Few-Shot Prompt、情感分析 |
| day14b | 上下文记忆注入实现 | 对话历史管理、记忆注入 |

### 第四阶段：Streamlit 应用与 AI 助手（Day 15 ~ 16）

| 任务编号 | 任务名称 | 涉及知识点 |
|:---:|------|------|
| day15a | Streamlit 多页面跳转架构 | `st.Page`、多页面路由、会话状态 |
| day15b | 用户情感分析助手 | Streamlit + LLM、Prompt 封装 |
| day15c | 小红书爆款文案助手 | 文案生成、Prompt 优化 |
| day16a | 自定义个人聊天机器人 | Streamlit Chat UI、会话状态 |
| day16b | 网页摘要生成助手 | `BeautifulSoup` 抓取、LLM 摘要 |

### 第五阶段：LangChain 框架与 RAG（Day 17 ~ 19）

| 任务编号 | 任务名称 | 涉及知识点 |
|:---:|------|------|
| day17a | ConversationBufferMemory 对话机器人 | LangChain 对话记忆、`ChatTongyi` |
| day17b | Embeddings 文本向量化距离测试 | `DashScopeEmbeddings`、文本相似度 |
| day17c | Prompt Template 提示词模板工程 | `PromptTemplate`、`FewShotPromptTemplate` |
| day18a | Pydantic 结构化个人信息提取器 | `with_structured_output`、数据模型 |
| day18b | Ollama 本地部署与联调 | Ollama、本地 LLM、OpenAI 兼容接口 |
| day18c | RunnableParallel 多任务并发流水线 | 并发链、`StrOutputParser` |
| day18d | LLMChain 定制科普文生成器 | Streamlit + LCEL 链 |
| day19a | SequentialChain 故事生成流水线 | 顺序链、`RunnablePassthrough` |
| day19b | 长链式文章创作流水线 | 多步骤链式创作 |
| day19c | 滑窗记忆聊天应用 | 短期/长期记忆、JSON 持久化 |

### 第六阶段：高级 Agent 与 RAG 实战（Day 21 ~ 22）

| 任务编号 | 任务名称 | 涉及知识点 |
|:---:|------|------|
| day21a | RAG 文档加载与文本递归切分 | `TextLoader`、`RecursiveCharacterTextSplitter` |
| day21b | ChromaDB 向量数据库构建与检索 | ChromaDB、Embeddings、相似度查询 |
| day21c | 颐和园智能导游（RAG + Tool Agent） | `create_agent`、自定义 Tool、RAG |
| day22a | 基于 InMemorySaver 的会话记忆追踪 | LangGraph、`StateGraph`、`MemorySaver` |
| day22b | Deep Agent 与本地技能推理 | Shell 后端、Agent 深度推理 |

### 第七阶段：综合项目（Project 1 ~ 4）

| 项目编号 | 项目名称 | 技术栈 |
|:---:|------|------|
| project1 | 2020 年销售数据分析 | `pandas`、数据透视、环比/毛利率计算 |
| project2 | AI 智能简历助手 | `streamlit`、OpenAI、STAR 法则、Markdown 导出 |
| project3 | RAG + YOLO 融合系统中控导航 | `streamlit`、系统架构设计 |
| project4 | 专业领域大模型语料知识库 | LangChain、ChromaDB、RAG、向量检索 |

## 环境配置

### 运行要求

- Python 3.10 及以上版本
- 操作系统：Windows / macOS / Linux

### 环境变量

部分任务（Day 13c 起及综合项目）依赖阿里云百炼或 OpenAI 兼容接口，需在项目根目录创建 `.env` 文件，配置以下环境变量：

```bash
# 阿里云百炼 API Key（通义千问大模型 + Embeddings）
DASHSCOPE_API_KEY=your_dashscope_api_key

# OpenAI 兼容 API Key（用于 langchain-openai 调用通义千问）
OPENAI_API_KEY=your_dashscope_api_key

# 天行数据 API Key（Day 13a 用）
TIANAPI_KEY=your_tianapi_key
```

> 实际使用中，`DASHSCOPE_API_KEY` 和 `OPENAI_API_KEY` 可填同一个阿里云百炼 API Key。项目通过 `https://dashscope.aliyuncs.com/compatible-mode/v1` 兼容端点访问通义千问模型。

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行方式

- **Python 脚本**：直接运行对应 `code/` 目录下的 `.py` 文件
- **Streamlit 应用**：`streamlit run <path_to_main.py>`
- **HTML/CSS/JS**：直接用浏览器打开 `.html` 文件

## 运行结果截图

所有任务的运行截图位于各自目录的 `pictures/` 文件夹内。
