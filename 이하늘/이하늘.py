import json
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage

# 1. Pydantic을 사용하여 자료구조 정의
class SongRecommendation(BaseModel):
    title: str = Field(description="추천 곡의 제목")
    artist: str = Field(description="추천 곡의 아티스트")

# 2. JsonOutputParser 설정 (필요 없더라도 유지)
output_parser = JsonOutputParser(pydantic_object=SongRecommendation)
format_instructions = output_parser.get_format_instructions()

# 3. 한글 프롬프트 템플릿 구성
prompt_template = PromptTemplate(
    template="다음 곡들을 기반으로 비슷한 스타일의 곡 3개를 추천해 주세요:\n{song_list}\n추천곡은 '1. 아티스트 - 곡 제목' 형식으로 작성해 주세요.",
    input_variables=["song_list"]
)

# 4. JSON 파일 읽기
def load_song_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)  # JSON 파일을 딕셔너리 리스트로 변환
    return data

# 5. JSON 파일에서 입력받아 곡 정보를 분석하여 3곡 추천
file_path = "song_list.txt"  # JSON 파일 경로
song_data = load_song_data(file_path)

# 6. 곡 목록을 하나의 문자열로 구성
song_list = "\n".join([f"{song['artist']} - {song['title']}" for song in song_data])

# 7. 포맷된 프롬프트 생성
formatted_prompt = prompt_template.format(song_list=song_list)
print("Formatted Prompt:\n", formatted_prompt)

# 8. ChatOllama 사용하여 추천곡 생성
llm = ChatOllama(model="llama3.2:1b")  # ChatOllama 모델 설정
message = HumanMessage(content=formatted_prompt)
response = llm.invoke([message])  # `invoke` 메서드 사용

# 9. 추천곡 출력 (텍스트 형식)
print("추천곡:\n", response.content)

