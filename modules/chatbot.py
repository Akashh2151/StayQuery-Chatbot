import pandas as pd
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts.prompt import PromptTemplate
from langchain.callbacks import get_openai_callback
# from pages.Chat import data


# #fix Error: module 'langchain' has no attribute 'verbose'
# import langchain
# langchain.verbose = False

# class Chatbot:

#     def __init__(self, model_name, temperature, vectors):
#         self.model_name = model_name
#         self.temperature = temperature
#         self.vectors = vectors

#     qa_template = """
#         You are a helpful AI assistant named  . The user gives you a file its content is represented by the following pieces of context, use them to answer the question at the end.
#         If you don't know the answer, just say you don't know. Do NOT try to make up an answer.
#         If the question is not related to the context, politely respond that you are tuned to only answer questions that are related to the context.
#         Use as much detail as possible when responding.

#         context: {context}
#         =========
#         question: {question}
#         ======
#         """

#     QA_PROMPT = PromptTemplate(template=qa_template, input_variables=["context","question" ])

#     def conversational_chat(self, query):
#         """
#         Start a conversational chat with a model via Langchain
#         """
#         llm = ChatOpenAI(model_name=self.model_name, temperature=self.temperature)

#         retriever = self.vectors.as_retriever()


#         chain = ConversationalRetrievalChain.from_llm(llm=llm,
#             retriever=retriever, verbose=True, return_source_documents=True, max_tokens_limit=4097, combine_docs_chain_kwargs={'prompt': self.QA_PROMPT})

#         chain_input = {"question": query, "chat_history": st.session_state["history"]}
#         result = chain(chain_input)

#         st.session_state["history"].append((query, result["answer"]))
#         #count_tokens_chain(chain, chain_input)
#         return result["answer"]


# def count_tokens_chain(chain, query):
#     with get_openai_callback() as cb:
#         result = chain.run(query)
#         st.write(f'###### Tokens used in this conversation : {cb.total_tokens} tokens')
#     return result 




from langchain.chat_models import ChatOpenAI

class Chatbot:
        def __init__(self, model_name, temperature):
            if not model_name:
                raise ValueError("A model name must be specified.")
            self.model_name = model_name
            self.temperature = temperature
            self.llm = ChatOpenAI(model_name=self.model_name, temperature=self.temperature)
            self.conversation_history = []  # Initialize an empty conversation history


        def conversational_chat(self, user_input):
            # Ensure a DataFrame is provided
            # if not isinstance(dataframe, pd.DataFrame):
                # return "Error: Input data is not a DataFrame."

            print("User Input:", user_input)
            # print("DataFrame Preview:", dataframe.head())

            try:
                # Create an agent that processes a DataFrame and user input
                # This agent may run queries or generate summaries based on the DataFrame
                # agent = create_pandas_dataframe_agent(dataframe, self.llm, user_input, verbose=True)
                # query_input = user_input
                # summary_response = agent.run(query_input)s
                return user_input

            except Exception as e:
                print(f"Error during response generation: {e}")
                return "Sorry, I encountered an error."
        
    # def conversational_chat(self, user_input):
    #     user_message = {'role': 'user', 'content': user_input}
    #     self.conversation_history.append(user_message)
    #     print(f"Updated conversation history with user input: {self.conversation_history}")

    #     try:
    #         response = self.llm.generate(messages=self.conversation_history, max_tokens=150)
    #         response_text = response['choices'][0]['text'].strip()

    #         assistant_message = {'role': 'assistant', 'content': response_text}
    #         self.conversation_history.append(assistant_message)
    #         print(f"Updated conversation history with assistant response: {self.conversation_history}")

    #         return response_text
    #     except Exception as e:
    #         print(f"Error during response generation: {e}")
    #         return "Sorry, I encountered an error."

    
