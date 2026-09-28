from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_concept
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": None
        }
    )


@app.post("/process", response_class=HTMLResponse)
async def process(
    request: Request,
    task: str = Form(...),
    user_input: str = Form(...)
):

    result = ""

    try:

        if task == "qa":
            result = answer_question(user_input)

        elif task == "explain":
            result = explain_concept(user_input)

        elif task == "summarize":
            result = summarize_text(user_input)

        elif task == "learn":
            result = get_learning_recommendations(user_input)

        elif task == "quiz":
            result = generate_quiz(user_input)

        else:
            result = "Invalid task selected."

    except Exception as e:
        result = f"Error: {str(e)}"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )


@app.post("/qa")
async def qa_api(data: dict):

    question = data.get("question", "")

    answer = answer_question(question)

    return JSONResponse(
        {
            "answer": answer
        }
    )


@app.post("/explain")
async def explain_api(data: dict):

    topic = data.get("topic", "")

    explanation = explain_concept(topic)

    return JSONResponse(
        {
            "explanation": explanation
        }
    )


@app.post("/summarize")
async def summarize_api(data: dict):

    text = data.get("text", "")

    summary = summarize_text(text)

    return JSONResponse(
        {
            "summary": summary
        }
    )


@app.post("/quiz")
async def quiz_api(data: dict):

    topic = data.get("topic", "")

    quiz = generate_quiz(topic)

    return JSONResponse(
        {
            "quiz": quiz
        }
    )


@app.post("/learn/recommendations")
async def learn_api(data: dict):

    topic = data.get("topic", "")

    recommendations = get_learning_recommendations(topic)

    return JSONResponse(
        {
            "recommendations": recommendations
        }
    )


@app.get("/health")
async def health_check():

    return {
        "status": "running",
        "application": "EduGenie"
    }