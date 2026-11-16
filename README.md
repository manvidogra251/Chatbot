# EDU Revolution Chatbot — Streamlit

A Streamlit web app version of the supplied EDU Revolution manual chatbot.

## 1. Install Python
Use Python 3.10 or newer.

## 2. Open the project folder in a terminal
(Optional but recommended) create and activate a virtual environment.

Windows:
```powershell
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Add your API key
Open `.streamlit/secrets.toml` and replace:
```toml
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
```
with your Google AI Studio API key. Keep the quotation marks.

The file already includes a configurable `GEMINI_MODEL` setting. The default is `gemini-2.5-flash`; change it only if you have access to another supported model.

## 5. Run the app
```bash
streamlit run app.py
```
Streamlit will open the chatbot in your browser.

## Security note
Do not share your API key or commit `.streamlit/secrets.toml` to a public repository. The `.gitignore` file excludes it from Git.

## Important
The chatbot answers only from the manual embedded in `app.py`. Academic benefits and eligibility are subject to the latest official LPU policy, criteria sheet, and approval.
