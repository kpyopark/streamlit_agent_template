import streamlit as st
import json
from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel, ChatSession
import os

# Google Cloud 프로젝트 ID와 리전 설정
PROJECT_ID = "turnkey-charter-358922"  # 여기에 실제 프로젝트 ID를 입력하세요
LOCATION = "asia-northeast3"  # 또는 다른 적절한 리전

# Google Cloud 인증 설정 (환경 변수나 서비스 계정 키 파일 사용)
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-key.json"

aiplatform.init(project=PROJECT_ID, location=LOCATION)

def analyze_conversation(template, conversation, functions):
    model = GenerativeModel("gemini-1.5-flash-001")
    chat = model.start_chat()
    
    prompt = f"""
    템플릿: {template}
    
    대화 내용: {conversation}
    
    위의 템플릿과 대화 내용을 바탕으로 다음 작업을 수행해주세요:
    1. 대화 내용을 간단히 요약해주세요.
    2. 아래 함수 목록 중에서 이 대화에 가장 적합한 함수를 선택해주세요.
    3. 선택한 함수의 파라미터에 맞춰 대화에서 관련 정보를 추출해주세요.
    
    함수 목록:
    {json.dumps(functions, ensure_ascii=False, indent=2)}
    
    응답 형식:
    ```json
    {{
        "summary": "대화 요약",
        "selected_function": "선택된 함수 이름",
        "extracted_params": {{
            "파라미터1": "추출된 값1",
            "파라미터2": "추출된 값2"
        }}
    }}
    ```
    """
    
    response = chat.send_message(prompt)
    result = json.loads(response.text)
    
    return result["summary"], result["selected_function"], result["extracted_params"]

st.set_page_config(layout="wide")

# 왼쪽 패널
left_col = st.sidebar

# 프롬프트 템플릿
template = left_col.text_area("프롬프트 템플릿", height=200, value="""너는 사용자 통화 기록을 기반으로, 사용자에게 적절한 정보, 행위를 지원하는 통화 기록 도우미이다. 
사용자의 통화에서 중요하다고 판단되는 주제가 있다면, 주어진 함수 범위에서 어떻게 해당 함수를 호출할 수 있는지 정리해서 보여줘

Instruction :
1. 사용자의 대화에서 현재 진행되는 주요주제를 추출합니다. 
2. 사용자의 대화가 일반적인 경우 함수 호출을 자제합니다. 
3. 사용자의 대화에서 너가 도움이 될 수 있는 함수가 있다면 어떤 함수를 어떤 파라미터에 어떤 값으로 호출해야 하는지 알려줘
4. 함수 호출이 여러개일 수 있기 때문에 호출 함수에 대한 목록을 JSON Array형태로 보여줘

output example:
[
  { "target_function" : ... , 
    "selection_reason" : ... , 
    "parameters" : {
      "<param1>" : "<value1>" , 
      "<param2>" : "<value2>"
    "
  }
  , 
  ...
]
""")

# 함수 관리
left_col.subheader("함수 관리")
function_name = left_col.text_input("함수 이름", value="search_google")
function_params = left_col.text_area("함수 파라미터 (JSON 형식)", value="""[ 
{ "parameter_name" : "keyword" , 
    "description" : "사용자에게 필요한 검색 키워드" }
]
""")

if left_col.button("함수 추가"):
    functions = st.session_state.get('functions', [])
    functions.append({"name": function_name, "parameters": json.loads(function_params)})
    st.session_state['functions'] = functions

# 예시 함수 Remark로 처리
# retrieve_calendar
# [ 
# { "parameter_name" : "registered_datetime" , 
#     "description" : "조회하려는 캘린더 시간 정보 YYYY-MM-DD HH24:MI:SS 형태로 되어 있으며 특정. Prefix 매칭을 수행한다." }
# ]


# 저장된 함수 목록 표시
if 'functions' in st.session_state:
    for idx, func in enumerate(st.session_state['functions']):
        left_col.text(f"{idx + 1}. {func['name']}")

# 오른쪽 패널
right_col = st.container()

# 사용자 대화 입력
conversation = right_col.text_area("대화 내용을 입력하세요", height=200)

if right_col.button("분석"):
    if conversation and template:
        functions = st.session_state.get('functions', [])
        summary, selected_function, extracted_params = analyze_conversation(template, conversation, functions)
        
        right_col.subheader("분석 결과")
        right_col.write(f"요약: {summary}")
        
        if selected_function:
            right_col.write(f"선택된 함수: {selected_function['name']}")
            right_col.write("추출된 파라미터:")
            right_col.json(extracted_params)
    else:
        right_col.warning("템플릿과 대화 내용을 모두 입력해주세요.")