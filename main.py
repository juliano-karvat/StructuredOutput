import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Resumo(BaseModel):
    titulo: str
    resumo: str
    palavras_chaves: list[str]

texto = """
Cartago foi uma cidade-estado da Antiguidade, localizada no norte da África.
Durante séculos, rivalizou com Roma pelo domínio do Mediterrâneo, até ser destruída na Terceira Guerra Púnica, em 146 a.C.
"""

response = client.chat.completions.parse(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "Você é um assistente que resume textos históricos."},
        {"role": "user", "content": f"Resuma o seguinte texto: {texto}"}
    ],
    response_format=Resumo
)

resumo: Resumo = response.choices[0].message.parsed

print("Titulo: ", resumo.titulo)
print("Resumo: ", resumo.resumo)
print("Palavras-chave: ", resumo.palavras_chaves)