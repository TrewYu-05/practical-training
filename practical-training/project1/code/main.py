import pandas as pd
import os

data_path = os.path.join(os.path.dirname(__file__), "2020年销售数据.xlsx")
df = pd.read_excel(data_path, sheet_name='data')

df.columns = df.columns.str.strip()

df['售价'] = pd.to_numeric(df['售价'], errors='coerce')
df['销售数量'] = pd.to_numeric(df['销售数量'], errors='coerce')
df['直接成本'] = pd.to_numeric(df['直接成本'], errors='coerce')
df['销售日期'] = pd.to_datetime(df['销售日期'], errors='coerce')

df['销售额'] = df['售价'] * df['销售数量']
df['月份'] = df['销售日期'].dt.month

print("=== 2020年销售数据分析业务指标统计 ===\n")

# 1. 统计销售额、毛利润、毛利率
total_sales = df['销售额'].sum()
total_cost = df['直接成本'].sum()
gross_profit = total_sales - total_cost
gross_margin = (gross_profit / total_sales) * 100 if total_sales > 0 else 0

print(f"总销售额: {total_sales:.2f} 元")
print(f"总直接成本: {total_cost:.2f} 元")
print(f"总毛利润: {gross_profit:.2f} 元")
print(f"整体毛利率: {gross_margin:.2f}%\n")

# 2. 月度销售及环比
monthly_sales = df.groupby('月份')['销售额'].sum().reset_index()
monthly_sales['环比增长率(%)'] = monthly_sales['销售额'].pct_change() * 100

print("--- 月度销售及环比 ---")
for index, row in monthly_sales.iterrows():
    month = int(row['月份'])
    sales = row['销售额']
    mom = row['环比增长率(%)']
    mom_str = f"{mom:.2f}%" if pd.notna(mom) else "N/A"
    print(f"{month}月: 销售额 {sales:.2f}元, 环比 {mom_str}")
print()

# 3. 品牌贡献占比
brand_sales = df.groupby('品牌')['销售额'].sum().reset_index()
brand_sales['占比(%)'] = (brand_sales['销售额'] / total_sales) * 100
brand_sales = brand_sales.sort_values(by='销售额', ascending=False)

print("--- 品牌贡献占比 ---")
for index, row in brand_sales.iterrows():
    print(f"品牌: {row['品牌']}, 销售额: {row['销售额']:.2f}元, 占比: {row['占比(%)']:.2f}%")
print()

# 4. 渠道贡献占比
channel_sales = df.groupby('销售渠道')['销售额'].sum().reset_index()
channel_sales['占比(%)'] = (channel_sales['销售额'] / total_sales) * 100
channel_sales = channel_sales.sort_values(by='销售额', ascending=False)

print("--- 渠道贡献占比 ---")
for index, row in channel_sales.iterrows():
    print(f"渠道: {row['销售渠道']}, 销售额: {row['销售额']:.2f}元, 占比: {row['占比(%)']:.2f}%")
