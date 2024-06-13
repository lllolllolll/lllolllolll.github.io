import openai

openai.api_key = "sk-VdYpVgHEHGTd9NDnV7CCd0F4LMxE7mbuJuEhrhx6sMwHS8cF"
openai.api_base = "https://api.chatanywhere.com.cn"
# # 非流式响应
# # messages = [{'role': 'user','content': '鲁迅和周树人的关系'},]
# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
# print(completion.choices[0].message.content)

import tkinter as tk
from tt import gpt_35_api_stream

def send_message():
    message = entry.get()
    # 在这里添加处理消息的代码，可以调用AI模型生成回复
    # reply = generate_reply(message)
    # 在这里将回复添加到聊天记录中
    chat_log.insert(tk.END, "You: " + message + "\n")
    messages = [{'role': 'user','content': message},]
    com = gpt_35_api_stream(messages)
    if com[0] == False:
       chat_log.insert(tk.END, "Bot: " + '连接错误' + "\n") 
    #    return 0 
    print(messages[0]['content'])
    chat_log.insert(tk.END, "Bot: " + messages[1]['content'] + "\n")
    entry.delete(0, tk.END)  # 清空输入框

# 创建主窗口
window = tk.Tk()
window.title("Chat Interface")

# 创建聊天记录显示区域
chat_log = tk.Text(window)
chat_log.pack(fill=tk.BOTH, expand=True)
chat_log.pack_propagate(False)  # 禁止聊天记录区域自动调整大小

# 创建输入框和发送按钮
entry = tk.Entry(window)
entry.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10)

# 运行主循环
window.mainloop()


