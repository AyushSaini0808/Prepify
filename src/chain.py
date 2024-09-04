from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from prompt_template import memory_prompt_template


def create_prompt_template(prompt_template):
    return PromptTemplate.from_template(prompt_template)


def create_llm_chain(chat_prompt, memory):
    return LLMChain(
        llm=ChatOllama(model="llama3.1", temperature=0.2),
        prompt=chat_prompt,
        memory=memory
    )


def create_chat_memory(chat_history):
    return ConversationBufferMemory(memory_key="history", chat_memory=chat_history, k=3)


def load_normal_chain(chat_history):
    return ChatChain(chat_history)


class ChatChain:
    def __init__(self, chat_history):
        self.memory = create_chat_memory(chat_history=chat_history)
        chat_prompt = create_prompt_template(memory_prompt_template)
        self.llm_chain = create_llm_chain(chat_prompt=chat_prompt, memory=self.memory)

    def run(self, user_input, **kwargs):
        return self.llm_chain.run(human_input=user_input, history=self.memory.chat_memory.messages,)
