#!/bin/bash
# Script to generate the dayXX folder structure and basic files

# List of all tasks provided by the user
declare -a tasks=(
  # day01
  "day01a:Craps游戏"
  "day01b:Craps游戏Plus版"
  "day01c:字符串清洗与格式化作业"
  "day01d:双色球随机选号作业"
  "day01e:城市区域字段拆分作业"
  "day01f:统计字符串字符个数作业"

  # day02
  "day02a:提取英文名作业"
  "day02b:含单位数值字段清洗作业"
  "day02c:敏感数据脱敏展示作业"
  "day02d:URL参数提取作业"
  "day02e:复杂学校层级数据查询统计作业"
  "day02f:检测密码强度作业"
  "day02g:统计元音字母数量作业"

  # day03
  "day03a:商品信息管理系统"
  "day03b:Txt与CSV文件读写持久化"
  "day03c:创建学生类对象作业"

  # day04
  "day04a:人力系统面向对象作业"

  # day05
  "day05a:多态与私有属性验证代码"
  "day05b:丁致宇真爱有缘网注册表单"

  # day06
  "day06a:欢迎注册页面排版设计"

  # day07
  "day07a:淘宝链接区域网页静态布局"
  "day07b:小米商品列表动态渲染"

  # day08
  "day08a:企业完整静态网站开发"

  # day09
  "day09a:简易前端计算器v1"

  # day10
  "day10a:基于JS循环的动态表格数据渲染"
  "day10b:网页随机点名系统"
  "day10c:多功能前端计算器升级版"

  # day11
  "day11a:面向对象版选项卡(Tab)切换"
  "day11b:购物车模块化(ES6 Module)"

  # day12
  "day12a:FastAPI后端API接口设计"
  "day12b:前端Ajax跨域请求交互"

  # day13
  "day13a:天行API新闻数据网络采集"
  "day13b:新闻数据Excel持久化项目"
  "day13c:调用阿里云大模型基础对话"

  # day14
  "day14a:大模型Few-Shot情感分类器"
  "day14b:大模型上下文记忆注入实现"

  # day15
  "day15a:Streamlit带状态的多页面跳转架构"
  "day15b:用户情感分析助手"
  "day15c:小红书爆款文案助手"

  # day16
  "day16a:自定义个人聊天机器人"
  "day16b:网页摘要生成助手"

  # day17
  "day17a:ConversationBufferMemory对话机器人"
  "day17b:DashScope Embeddings文本向量化距离测试"
  "day17c:Prompt Template提示词模板工程"

  # day18
  "day18a:Pydantic结构化个人信息提取器"
  "day18b:Ollama开源大模型本地部署与联调"
  "day18c:RunnableParallel多任务并发流水线"
  "day18d:LLMChain定制科普文生成器"

  # day19
  "day19a:SequentialChain故事生成流水线"
  "day19b:长链式文章创作流水线"
  "day19c:滑窗短期与Json持久化长期记忆聊天应用"

  # day21
  "day21a:RAG文档加载与文本递归切分处理"
  "day21b:ChromaDB向量数据库构建与相似度检索"
  "day21c:颐和园智能导游（RAG与Tool Agent综合实战）"

  # day22
  "day22a:基于InMemorySaver的智能体会话记忆追踪"
  "day22b:Deep Agent与本地技能（Skills）深度推理智能体"

  # 综合项目
  "project1:2020年销售数据分析业务指标统计"
  "project2:AI智能简历助手（Web工具开发）"
  "project3:RAG_YOLO融合应用（系统构架）"
  "project4:专业领域大模型语料知识库研发"
)

mkdir -p practical-training
for task in "${tasks[@]}"; do
  # Extract folder name
  folder="${task%%:*}"
  name="${task#*:}"

  mkdir -p "practical-training/$folder/code"
  mkdir -p "practical-training/$folder/pictures"

  echo "# $name" > "practical-training/$folder/code/README.md"
done
