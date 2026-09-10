import os
import uuid
import requests
import urllib3
from dotenv import load_dotenv, find_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Ищем .env явно и печатаем путь
dotenv_path = find_dotenv()
print(f"🔍 Найден файл .env по пути: '{dotenv_path}'")

load_dotenv(dotenv_path)
key = os.getenv('key')
print(f"🔍 Ключ загружен: '{key[:10]}...' " if key else "❌ Ключ НЕ загружен (key = None)")

# Загружаем переменные из .env
load_dotenv()
key = os.getenv('key')

def get_token():
    if not key:
        raise ValueError("Ключ API не найден! Проверьте файл .env")
        
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": str(uuid.uuid4()),
        "Authorization": f"Basic {key.strip()}"
    }
    data = {"scope": "GIGACHAT_API_PERS"}
    
    response = requests.post(url, headers=headers, data=data, verify=False)
    
    if response.status_code != 200:
        raise Exception(f"Ошибка получения токена ({response.status_code}): {response.text}")
        
    return response.json()["access_token"]

def ask_gigachat(question, knowledge, token):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    
    system_prompt = f"""
    Ты — ИИ-консультант. Отвечай строго по документу.
    Если ответа нет — скажи "Я не знаю".
    
    ДОКУМЕНТ:
    {knowledge}
    """
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    data = {
        "model": "GigaChat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    }
    
    response = requests.post(url, headers=headers, json=data, verify=False)
    
    if response.status_code != 200:
        raise Exception(f"Ошибка генерации ответа ({response.status_code}): {response.text}")
        
    return response.json()

# ========== ОСНОВНАЯ ПРОГРАММА ==========
def main():
    print("🚀 Запуск ИИ-консультанта...")
    
    try:
        with open("knowledge.txt", "r", encoding="utf-8") as f:
            knowledge = f.read()
        print("📚 База знаний загружена успешно!")
    except FileNotFoundError:
        print("⚠️ Файл knowledge.txt не найден! Создан базовый контекст.")
        knowledge = "База знаний временно недоступна."
    
    try:
        token = get_token()
        print("✅ Подключение к GigaChat успешно!")
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return
    
    print("\n🤖 ИИ-консультант запущен!")
    print("Задайте вопрос или напишите 'выход' для завершения.\n")
    
    while True:
        q = input("👤 Вы: ")
        if q.strip().lower() in ["выход", "exit", "quit"]:
            print("👋 До свидания!")
            break
        
        if not q.strip():
            continue
        
        try:
            resp = ask_gigachat(q, knowledge, token)
            answer = resp["choices"][0]["message"]["content"]
            print(f"🤖: {answer}\n")
        except Exception as e:
            print(f"⚠️ Ошибка: {e}")

if __name__ == "__main__":
    main()