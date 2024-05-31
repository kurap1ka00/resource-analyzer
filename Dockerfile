# Используем базовый образ Python
FROM python:3.9

# Устанавливаем git
RUN apt-get update
RUN apt-get install -y git

# Клонируем репозиторий
RUN git clone https://github.com/kurap1ka00/resource-analyzer.git

# Переходим в директорию resource-analyzer
WORKDIR /resource-analyzer

# Устанавливаем зависимости из requirements.txt
RUN pip install -r requirements.txt

# Запускаем main.py
CMD ["python3", "./main.py"]
