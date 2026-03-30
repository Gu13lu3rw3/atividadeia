from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"), 
    tools=[TavilyTools()], 
    debug_mode=False
)

print("--- Agente de Clima (Digite 'sair' para encerrar) ---")

while True:
    pergunta = input("\nVocê: ")
    
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando...")
        break
        
    if not pergunta.strip():
        continue

    print("\nAgente: ", end="")
    agent.print_response(pergunta, stream=True)