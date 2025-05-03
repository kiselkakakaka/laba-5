# Лабораторная работа 5 — Docker и деплой FastAPI

## 📦 Что внутри

- `main.py` — минимальный FastAPI сервер
- `Dockerfile` — инструкция для контейнера
- `requirements.txt` — зависимости

## ▶ Как запустить

### 🔧 Вручную:

```
pip install -r requirements.txt
uvicorn main:app --reload
```

### 🐳 Через Docker:

1. Собрать образ:
```
docker build -t lab5-fastapi .
```

2. Запустить контейнер:
```
docker run -d -p 8000:80 lab5-fastapi
```

3. Перейти в браузере:
```
http://localhost:8000
```

## ✅ Как выложить на GitHub

```bash
git init
git add .
git commit -m "lab5 — Docker продакшн"
git branch -M main
git remote add origin https://github.com/ТВОЙ_ЛОГИН/lab5-docker.git
git push -u origin main
```
