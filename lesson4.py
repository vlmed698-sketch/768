# импортирую либы тут
import os
import sys
from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv()
api_key = os.getenv("GIGACHAT_CREDENTIALS")
# тута считывается и проверяется мой апишка который впащен в .env
if not api_key:
    sys.exit(1)
#функция для отправкизапросика в тупейший гигачат (ask_llm)
def ask_llm(prompt):
    with GigaChat(credentials=api_key, scope="GIGACHAT_API_PERS", verify_ssl_certs=False) as client:
        models = client.get_models()
        model_name = getattr(models.data[0], "id_", "GigaChat")
        response = client.chat({
            "model": model_name,
            "messages": [{"role": "user", "content": prompt}]
        })
        return response.choices[0].message.content

def main():
    while True:
        try:
            q = input("vopros: ").strip()
            if not q:
                continue
            if q.lower() in ["выход", "exit"]:
                break
            print(ask_llm(q))
        except Exception as e:
            print("err:", e)

if __name__ == "__main__":
    main()