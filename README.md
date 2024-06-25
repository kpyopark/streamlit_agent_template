# streamlit_agent_template
Call Analysis Web App

This Streamlit web app utilizes Google Cloud's Vertex AI Gemini Pro model to analyze call transcripts and extract relevant information.

**Features:**

- Prompt Template: Define a template for the Gemini Pro model to understand the desired analysis.
- Function Management: Define a list of functions and their parameters.
- Conversation Analysis: Input a call transcript and the app will:
- Summarize the conversation.
- Select the most appropriate function from the list.
- Extract relevant parameters from the conversation.

**Requirements:**

- Google Cloud Platform account
- Vertex AI API enabled
- Gemini Pro model deployed and endpoint created
- Python 3.7 or higher
- Streamlit library installed (pip install streamlit)
- Google Cloud SDK installed (pip install google-cloud-sdk)

**Setup:**

- Create a Google Cloud Project:
- Go to the Google Cloud Console and create a new project.
- Enable Vertex AI API:
  - In the Google Cloud Console, navigate to the API Library and enable the Vertex AI API.
- Deploy Gemini Pro Model:
  - Follow the instructions in the Vertex AI documentation to deploy the Gemini Pro model.
- Set Environment Variables:
  - Set the PROJECT_ID and LOCATION variables in the main.py file.
  - Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of your service account key file.
- Run the App:
  - Run the following command in your terminal: streamlit run main.py

**Usage:**

- Input Prompt Template:
  - Enter a prompt template that describes the desired analysis.
- Manage Functions:
  - Define a list of functions and their parameters.
- Input Conversation Transcript:
  - Enter the call transcript you want to analyze.
- Click "분석" Button:
  - The app will analyze the conversation and display the results.

**Example:**

Prompt Template:

**Building Mechanism**

This app is made by Gen AI with the following prompts.
"

Streamlit-based Conversational Analysis App

"Streamlit을 이용하여, Web App을 하나 만들어줘. 왼쪽 패널은 위 아래 두개로 구성되어 있는데, 위에는 프롬프트 템플릿 그리고 하단에는 펑션에 대한 이름과 파라미터 스펙을 관리할 수 있는 기능. 그리고 오른쪽 패널에는 사용자 Dialog 입력창이 보이고, 사용자가 통화내용을 입력했을 경우에, Template을 이용하여 통화 내용을 분석하여 요약정보 제공 및 필요한 펑션을 선택하고 어떤 파라미터를 추출해야 하는지에 대한 내용을 보여주는 App."

"오 좋아. 여기 analyze_conversation 함수가 실제로 동작할 수 있게, VertexAI의 최신 언어모델인 gemin-pro-1.5를 이용하여 분석하는 함수를 보여줘."
