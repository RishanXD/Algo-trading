import requests
def telegram_send(message):
    """used to send telegram notification"""
    base_url = rf"https://api.telegram.org/bot6278715208:AAHuQBLJUWxOILF0MJyqToslQIr2LhXoG2k/sendMessage?chat_id=-903007971&text={message}"
    requests.get(base_url)
    print(f"Sent telegram message: {message}")
    return None