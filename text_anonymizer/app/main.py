from fastapi import FastAPI, Request, Form, HTTPException, Body
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from logic import TextAnonymizer
from models import model_loader
from utils.logger import setup_logger

app = FastAPI(title="Конфиденциальный Анонимизатор Текстов")
current_dir = Path(__file__).parent
templates = Jinja2Templates(directory=str(current_dir / "templates"))
anonymizer = TextAnonymizer()
logger = setup_logger(__name__)

TEXTS = {
    "ru": {
        "title": "Конфиденциальный Анонимизатор Текстов",
        "description": "Введите текст на русском или английском языке для анонимизации личной информации.",
        "placeholder": "Введите ваш текст здесь...",
        "full_redaction": "Полное скрытие",
        "partial_redaction": "Частичное скрытие (с указанием типа)",
        "button_text": "Анонимизировать текст",
        "result": "Результат:",
        "footer": "Конфиденциальный Анонимизатор Текстов от Шифф Антал",
        "switch_to": "EN",
    },
    "en": {
        "title": "Privacy-Preserving Text Anonymizer",
        "description": "Enter text in Russian or English to anonymize personal information.",
        "placeholder": "Enter your text here...",
        "full_redaction": "Full redaction",
        "partial_redaction": "Partial redaction (with type indication)",
        "button_text": "Anonymize text",
        "result": "Result:",
        "footer": "Privacy-Preserving Text Anonymizer by Schiff Antal",
        "switch_to": "RU",
    },
}


@app.on_event("startup")
async def startup_event():
    try:
        model_loader.load_models()
        logger.info(
            "Все модели успешно загружены. Сервис готов к работе. \n All models have been successfully uploaded. The service is ready to work."
        )
    except Exception as e:
        logger.error(f"Ошибка при загрузке моделей: {e}")
        raise


def get_texts(lang: str = "ru"):
    return TEXTS.get(lang, TEXTS["ru"])


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request, lang: str = "ru"):
    if lang not in TEXTS:
        lang = "ru"

    texts = get_texts(lang)

    logger.info(f"Отображение страницы на языке: {lang}")

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "texts": texts, "current_lang": lang},
    )


@app.get("/switch_language")
async def switch_language(current_lang: str = "ru"):
    new_lang = "en" if current_lang == "ru" else "ru"
    logger.info(f"Переключение языка с {current_lang} на {new_lang}")
    return RedirectResponse(url=f"/?lang={new_lang}", status_code=303)


@app.post("/anonymize", response_class=HTMLResponse)
async def anonymize_via_web(
    request: Request,
    text: str = Form(...),
    mode: str = Form("full"),
    lang: str = "ru",
):
    if not text.strip():
        raise HTTPException(
            status_code=400, detail="Текст не может быть пустым."
        )

    if lang not in TEXTS:
        lang = "ru"

    texts = get_texts(lang)

    logger.info(
        f"Получен запрос на анонимизацию. Режим: {mode}, Язык: {lang}, Длина текста: {len(text)}"
    )
    try:
        anonymized_text = anonymizer.anonymize_text(text, mode)
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "texts": texts,
                "current_lang": lang,
                "original_text": text,
                "anonymized_text": anonymized_text,
                "selected_mode": mode,
            },
        )
    except Exception as e:
        logger.error(f"Ошибка при обработке текста: {e}")
        raise HTTPException(
            status_code=500, detail="Внутренняя ошибка сервера."
        )


@app.post("/api/anonymize")
async def anonymize_via_api(
    text: str = Body(..., embed=True), mode: str = Body("full", embed=True)
):
    if not text.strip():
        raise HTTPException(
            status_code=400, detail="Текст не может быть пустым."
        )
    try:
        anonymized_text = anonymizer.anonymize_text(text, mode)
        return {
            "original_text": text,
            "anonymized_text": anonymized_text,
            "mode": mode,
        }
    except Exception as e:
        logger.error(f"Ошибка API при обработке текста: {e}")
        raise HTTPException(
            status_code=500, detail="Внутренняя ошибка сервера."
        )
