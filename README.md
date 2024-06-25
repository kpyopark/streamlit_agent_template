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