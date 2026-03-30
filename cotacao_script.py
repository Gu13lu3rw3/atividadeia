from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    instructions="Use apenas tabelas para mostrar a informação final.",
    debug_mode=False
)

# aqui eu fiz uma adaptação, trocando as perguntas pra agora serem sobre a nvidia (espero que funcione)
print("--- Agente de Cotações Financeiras ---")
agent.print_response("Qual a cotação atual da NVIDIA (NVDA)?", stream=True)
