from langgraph.graph import StateGraph,START,END
from langchain_core.messages import BaseMessage,HumanMessage,AIMessage
from typing import TypedDict,Annotated
from langchain_groq import ChatGroq
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3


class chatstate(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]

conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(chatstate)

def chat_node(state:chatstate):
    llm = ChatGroq(
    api_key="your api key", # don't hardcode api key,store it in env variables
    model="openai/gpt-oss-20b",  # Or another Groq model like "llama2-70b-4096"
    temperature=0.7,  # Controls randomness (0.0 = deterministic, 1.0 = creative)
    max_tokens=1024,  # Maximum response length
)
    question = state['messages']
    ans = llm.invoke(question)
    return {
        'messages':[ans]
    }

graph.add_node('chat_node',chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpointer)


'''response = chatbot.invoke({'messages':[HumanMessage(content='what is my name')]},config = {'configurable':{'thread_id':'thread-1'}})
print(response)'''

def retrive_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)
