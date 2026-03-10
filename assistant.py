from openai import OpenAI


class ChatAssistant:
    def __init__(self):
        self.client = OpenAI()
        self.system_prompt = (
            "Você é um assistente virtual pessoal chamado Josué. "
            "Fale sempre em português brasileiro, de forma clara e objetiva. "
            "Você está rodando em um computador do usuário e pode apenas responder "
            "com texto (sem executar comandos de sistema por conta própria). "
            "Se o usuário pedir para executar algo no computador, explique "
            "os passos que ele deve seguir."
            "Dê todas as respostas de forma curta e objetiva."
        )

    def respond(self, user_text: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_text},
            ],
        )

        return response.choices[0].message.content

