# Используем образ Python
FROM python:3.9

# Устанавливаем зависимости
RUN pip install flask

# Копируем исходный код приложения в контейнер
COPY . /app
WORKDIR /app

# Задаем команду запуска приложения
CMD ["python", "app.py"]
