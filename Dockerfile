# Stage 1: Build the React frontend
FROM node:14 AS frontend

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# Stage 2: Build the FastAPI backend
FROM python:3.9 AS backend

WORKDIR /app

RUN pip install fastapi uvicorn

COPY backend/requirements.txt ./
RUN pip install -r requirements.txt

COPY backend/ ./
COPY --from=frontend /app/build ./frontend

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
