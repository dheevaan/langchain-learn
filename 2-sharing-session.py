from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_ebdesk import EBWhale


prompt = ChatPromptTemplate.from_messages([("system", "As an experienced back-end developer, your task is to describe the process and steps required to become a professional back-end developer who excels in problem-solving and finding solutions.Include essential skills, best practices, relevant technologies, and any recommended learning paths.Consider the following specifics with placeholders for any necessary details"),
                                                    ("human", "{user_input}"),
                                                    ])

llm = EBWhale(model='ebOpenwhalev2-78-GPTQ', api_key='pr-_Kje9WhSiwKYNsTeVStDtqb0-vmAI3L35n_3W0zOESk')
chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

chain.run(
    {
        'user_input': ''
    }
)