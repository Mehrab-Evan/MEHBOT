import os
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatGooglePalm
from langchain.llms.google_palm import GooglePalm

import db
import pickle


def evanbot(question):
    palm_api = os.getenv('GOOGLE_PALM_API')
    llm = GooglePalm(google_api_key=palm_api, temperature=0.9)
    # chat = ChatGooglePalm(google_api_key=palm_api, temperature=0.9)


    knowledge = db.get_knowledge(29)
    knowledgebase = pickle.loads(knowledge)
    # retriever = knowledgebase.as_retriever(score_threshold=0.7)

    chain = load_qa_chain(llm, chain_type='stuff')

    docs = knowledgebase.similarity_search(question)
    # chain = load_qa_chain(llm, chain_type='stuff')
    # print(docs)
    response = chain.run(input_documents=docs, question=question)
    # print(response)
    return response

