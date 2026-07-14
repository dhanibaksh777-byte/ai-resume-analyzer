# 📄 AI Resume Analyzer

An AI-powered tool that analyzes resume text and returns structured, actionable feedback — summary, extracted skills, strengths, and areas for improvement — powered by Groq (Llama 3.3 70B) using structured output.

## 🔗 Live Demo

**Try it here:** [ai-resume-analyzer-frontend-five-chi.vercel.app](https://ai-resume-analyzer-frontend-five-chi.vercel.app/)

![image alt](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/73999cc6-f69c-47b1-b102-3689c32f8521" />
)

## Features

- **Structured Output**: The AI returns a clean, predictable JSON shape every time — no free-form rambling — parsed directly into a Pydantic model.
- **Instant feedback**: Paste raw resume text and get a breakdown in seconds:
  - Summary
  - Extracted skills (as tags)
  - Strengths
  - Areas to improve
- **Clean, minimal UI**: A simple dark-themed frontend — no unnecessary complexity, built to be functional and professional.

## Tech Stack

**Backend**
- FastAPI
- Groq API (Llama 3.3 70B)
- Pydantic (structured output validation)

**Frontend**
- Vanilla HTML/CSS/JS (no framework — kept simple and dependency-free)
- Deployed on Vercel

## Project Structure

```
ai-resume-analyzer/
├── main.py            # FastAPI app + /analyze-resume endpoint
├── llm_client.py        # Groq client setup + chat completion
├── schemas.py            # ResumeRequest and ResumeAnalysis Pydantic models
├── prompt.py              # System prompt instructing the model to return structured JSON
├── Frontend/
│   └── index.html          # Chat-free single-page UI: paste resume, get analysis
├── .env                   # API key (not committed)
├── requirements.txt
└── README.md
```

## Setup

### Backend

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file:
   ```
   groq_api_key=your_groq_api_key
   ```

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

4. API available at `/analyze-resume` (POST), docs at `/docs`.

### Frontend

Open `Frontend/index.html` in a browser, or deploy it as a static site (Vercel/Netlify). Update the `API_URL` constant in the script to point to your deployed backend.

## How It Works

1. The user pastes resume text into the frontend and hits **Analyze Resume**.
2. The text is sent to the `/analyze-resume` endpoint along with a system prompt instructing the model to return a specific JSON structure.
3. Groq generates the response as JSON; it's parsed and validated against the `ResumeAnalysis` Pydantic model.
4. The structured result is rendered into cards on the frontend — no manual text parsing needed anywhere in the pipeline.

## Notes

- CORS is enabled on the backend to allow requests from the deployed frontend.
- Hosted on Render's free tier — the first request after a period of inactivity may take 20–30 seconds due to cold start.
