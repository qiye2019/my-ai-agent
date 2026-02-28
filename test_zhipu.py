from zhipuai import ZhipuAI

# 初始化客户端
client = ZhipuAI(api_key="19e75692ed9a44b3b7d0639bf46e9c47.sX1uQYEo5uFyHA8N")

# 调用模型
response = client.chat.completions.create(
    model="glm-4.7",  # 免费模型
    messages=[
        {"role": "user", "content": "你好，请简单介绍你自己"}
    ],
    temperature=0.7,  # 控制随机性
)

# 打印回复
print(response.choices[0].message.content)
