from langchain_core.prompts import ChatPromptTemplate
# 프롬프트 템플릿을 생성하기 위해 불러옴

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "이 시스템은 추어탕과 관련된 질문에 답변할 수 있습니다."),
    ("user", "{user_input}"),
])
# 시스템 메시지와 사용자 입력을 포함한 프롬프트 템플릿 생성

messages = chat_prompt.format_messages(user_input="추어탕의 주요 재료는 무엇인가요?")
# 템플릿에 사용자 입력 값을 채워 메시지 리스트 생성
# print(messages)  # 출력 예상: [SystemMessage(content='이 시스템은 추어탕과 관련된 질문에 답변할 수 있습니다.'), HumanMessage(content='추어탕의 주요 재료는 무엇인가요?')]
# SystemMessage와 HumanMessage 객체로 구성된 메시지 리스트를 보여줌

from langchain_core.output_parsers import StrOutputParser
# 문자열 형식으로 출력을 변환하기 위한 파서 불러옴

from langchain_community.chat_models import ChatOllama
# ChatOllama 모델을 사용하기 위해 불러옴

llm = ChatOllama(model="llama3.2:1b")
# 모델을 llama3.2:1b로 설정하여 ChatOllama 인스턴스 생성

chain = chat_prompt | llm | StrOutputParser()
# chat_prompt와 llm, StrOutputParser를 결합하여 체인 생성

print(chain.invoke({"user_input": "추어탕의 주요 재료는 무엇인가요?"}))
# 체인을 통해 입력 값을 바탕으로 모델을 호출하여 응답 생성
# 출력 예상: "추어탕의 주요 재료는 미꾸라지와 다양한 채소입니다."
# 사용자 질문에 대한 모델의 응답을 보여줌
