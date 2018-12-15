# coding=utf-8
import requests

# 请求该接口
response = requests.get('http://localhost:5000/todos')

# 获取响应数据，并解析JSON，转化为python字典
result = response.json()

# 打印响应状态码
print(response.status_code)

# 打印result
print(result)

# 打印结果中的 ‘todo1’ 任务
print(result['todo1'])