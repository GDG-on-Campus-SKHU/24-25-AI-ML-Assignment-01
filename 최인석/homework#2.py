from langchain_community.document_loaders import TextLoader
# 텍스트 파일을 로드하고 문서화하기 위한 TextLoader 불러옴

loader = TextLoader('review.txt', encoding='utf-8')
# 'history.txt' 파일을 UTF-8 인코딩으로 로드할 TextLoader 인스턴스 생성
# encoding='utf-8'을 통해 파일을 UTF-8 인코딩으로 읽도록 지정하여 인코딩 오류 방지

data = loader.load()
# 지정된 파일에서 데이터를 로드하고 data 변수에 저장

print(data[0])