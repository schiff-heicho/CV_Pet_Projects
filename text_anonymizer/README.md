# Конфиденциальный Анонимизатор Текстов / Privacy-Preserving Text Anonymizer

## Русская Версия

### О проекте

Веб-приложения для автоматического обнаружения и анонимизации чувствительной информации в текстах на русском и английском языках. 

Основная цель этого проекта соединить знание по MLOps, NLP и MLSec для построения инструмента для защиты приватности.

**Ключевые технологии:** Python, FastAPI, spaCy, Docker, NER.

### Основные функции

-   **Обнаружение сущностей:** Автоматическое нахождение в тексте имён, названий организаций, локаций и других объектов.
-   **Режимы анонимизации:**
    -   **Полное скрытие:** Замена сущностей на `[REDACTED]`.
    -   **Частичное скрытие:** Замена сущностей на `[ТИП_СУЩНОСТИ]` (например, `[PER]`).
-   **Мультиязычность:** Поддержка русского и английского языков.

### ⚠️ Ограничения и рекомендации

- **Текст должен быть написан строго на одном языке** так как смешанные тексты может иногда неправильно обнаружить сущностей и / или тип сущности.
- Названия компаний на русском языке (особенно транслитерированные) могут иногда распознаваться как локации (LOC)
- Номера телефонов в нестандартных форматах могут не распознаваться

#### Типы сущностей в частичном режиме

| Метка | Описание | Примеры |
|-------|----------|---------|
| **PER** | Имя человека | Иван, Аня, John |
| **ORG** | Организация, компания | Яндекс, Google, Сбербанк |
| **GPE** | Геополитическая единица | Россия, Москва, London |
| **LOC** | Локация (не-GPE) | Красная площадь, Уральские горы |
| **FAC** | Объект инфраструктуры | аэропорт, вокзал, больница |
| **EMAIL** | Email адрес | user@example.com |
| **PHONE** | Номер телефона | +79161234567 |
| **DATE** | Дата (потенциально персональная) | 01.01.1990, 1990-01-01 |
| **CREDIT_CARD** | Номер кредитной карты | 4111 1111 1111 1111 |
| **IP_ADDRESS** | IP-адрес | 192.168.1.1, 8.8.8.8 |

### Запуск веб-приложения

1.  **Клонируйте репозиторий и перейдите в папку проекта:**
    ```bash
    git clone <ваш-репозиторий>
    cd text-anonymizer-mvp
    ```

2.  **Запустите сервис с помощью Docker Compose:**
    ```bash
    docker-compose up --build
    ```

3.  **Откройте браузер и перейдите по адресу:**
    [http://localhost:8000](http://localhost:8000)

### Отправить запросы через терминал

Отправьте POST-запрос на эндпоинт `/api/anonymize`:

```bash
curl -X 'POST' \
  'http://localhost:8000/api/anonymize' \
  -H 'Content-Type: application/json' \
  -d '{"text":"Меня зовут Алексей. Моя карта 4111 1111 1111 1111, дата рождение 15.05.1985., IP сервера: 192.168.1.1", "mode":"partial
"}'

```


Ответ:

```json
{
  "original_text": "Меня зовут Алексей. Моя карта 4111 1111 1111 1111, дата рождение 15.05.1985., IP сервера: 192.168.1.1",
  "anonymized_text": "Меня зовут [PER]. Моя карта [CREDIT_CARD], дата рождение [DATE]., IP сервера: [IP_ADDRESS]",
  "mode":"partial"
}
```

### Структура проекта

```bash
text-anonymizer-mvp/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── anonymizer.py
│   ├── models.py
│   ├── utils/
│   │   └── logger.py
│   └── templates/
│       ├── base.html
│       └── index.html
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

---

## English Version

### About The Project

A web application for automatic detection and anonymization of personal / sensitive information in texts in Russian and English. 

The goal of this project is to combine knowledge of MLOps, NLP, and MLSec to build a privacy-preserving tool.

**Core Technologies:**  Python, FastAPI, spaCy, Docker, NER

### Features

-   **Entity Recognition:** Automatically find names, organization names, locations, and other objects in text.
-   **Anonymization Modes:**
    -   **Full Redaction:** Replace entities with `[REDACTED]`.
    -   **Partial Redaction:** Replace entities with `[ТИП_СУЩНОСТИ]` (for example, `[PER]`).
-   **Multilingual:** Support for Russian and English languages.

### Limitations and recommendations
- **Text must be strictly in one language** because mixed langugage texts may lead to incorrect anonymization
- Company names in Russian may sometimes be recognized as locations (LOC)
- Phone numbers in non-standard formats might not be recognized

#### Entity Types in Partial Mode

| Label | Description | Examples |
|-------|-------------|----------|
| **PER** | Person name | Ivan, Anna, Smith |
| **ORG** | Organization, company | Yandex, Google, Sberbank |
| **GPE** | Geopolitical entity | Russia, Moscow, London |
| **LOC** | Location (non-GPE) | Red Square, Ural Mountains |
| **FAC** | Infrastructure object | airport, railway station, hospital |
| **EMAIL** | Email address | user@example.com |
| **PHONE** | Phone number | +79161234567 |
| **DATE** | Date (potentially personal) | 01.01.1990, 1990-01-01 |
| **CREDIT_CARD** | Credit card number | 4111 1111 1111 1111 |
| **IP_ADDRESS** | IP address | 192.168.1.1, 8.8.8.8 |

### How to launch web app

1.  **Clone the repo and navigate to the projects folder::**
    ```bash
    git clone <ваш-репозиторий>
    cd text-anonymizer-mvp
    ```

2.  **Run the service using Docker Compose:**
    ```bash
    docker-compose up --build
    ```

3.  **Open your browser and go to:**
    [http://localhost:8000](http://localhost:8000)

### How to send request from terminal

Send a POST request to the /api/anonymize endpoint - Example:

```bash
curl -X 'POST' \
  'http://localhost:8000/api/anonymize' \
  -H 'Content-Type: application/json' \
  -d '{"text":"My name is Alexey. My card number is 4111 1111 1111 1111, my date of birth is May 15, 1985. Server IP: 192.168.1.1.", "mode":"full"}'
```


Example Response:

```json
{
  "original_text": "My name is Alexey. My card number is 4111 1111 1111 1111, my date of birth is May 15, 1985. Server IP: 192.168.1.1.",
  "anonymized_text": "My name is [PER]. My card number is [CREDIT_CARD], my data of birth is [DATE]., Server IP: [IP_ADDRESS].",
  "mode": "full"
}
```

### Project Structure

```bash
text-anonymizer-mvp/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── anonymizer.py
│   ├── models.py
│   ├── utils/
│   │   └── logger.py
│   └── templates/
│       ├── base.html
│       └── index.html
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```
