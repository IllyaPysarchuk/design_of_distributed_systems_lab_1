# README: Dockerized NGINX with Service Provider and Consumer

## Опис проекту

Цей проект демонструє використання NGINX як реверс-проксі для маршрутизації HTTP-запитів між двома сервісами — **Постачальником Сервісу** (*Provider*) і **Споживачем Сервісу** (*Consumer*).

- **Provider**: Обчислює квадрат переданого числа.
- **Consumer**: Надсилає запит до **Provider**, отримує результат і повертає відповідь клієнту.

Проект використовує **Docker Compose** для контейнеризації сервісів.

---

## Структура проекту

```
.
├── nginx.conf            # Конфігурація NGINX
├── docker-compose.yml    # Docker Compose файл для запуску проекту
├── provider/             # Директория з кодом для сервісу Provider
│   ├── provider.py       # Код Flask-сервісу Provider
│   ├── Dockerfile        # Dockerfile для Provider
│   ├── requirements.txt  # Залежності для Python
│   └── start.sh          # Скрипт для запуску сервісу
├── consumer/             # Директория з кодом для сервісу Consumer
    ├── consumer.py       # Код Flask-сервісу Consumer
    ├── Dockerfile        # Dockerfile для Consumer
    ├── requirements.txt  # Залежності для Python
    └── start.sh          # Скрипт для запуску сервісу
```

---

## Як запустити проект

### Передумови
1. Встановіть Docker і Docker Compose на вашій машині.

### Кроки для запуску
1. **Клонування репозиторію**:
   ```bash
   git clone <URL вашого репозиторію>
   cd <назва папки з проектом>
   ```

2. **Створення Docker-образів і запуск сервісів**:
   ```bash
   docker-compose up --build
   ```

3. **Перевірка доступності сервісів**:
   - **Consumer**: [http://localhost:90/consumer/process](http://localhost:90/consumer/process)
   - **Provider**: [http://localhost:90/provider/calculate](http://localhost:90/provider/calculate)

> **Примітка:** NGINX маршрутизує запити через `/consumer/` та `/provider/` до відповідних бекендів.

---

## Як використовувати API

### Provider API
- **URL:** `http://localhost:90/provider/calculate`
- **Метод:** `POST`
- **Body (JSON):**
  ```json
  {
      "number": <число>
  }
  ```
- **Приклад відповіді:**
  ```json
  {
      "result": 16,
      "time_taken": 0.000123
  }
  ```

### Consumer API
- **URL:** `http://localhost:90/consumer/process`
- **Метод:** `POST`
- **Body (JSON):**
  ```json
  {
      "number": <число>
  }
  ```
- **Приклад відповіді:**
  ```json
  {
      "consumer_time_taken": 0.41684961318969727,
      "input": 4,
      "provider_result": {
          "result": 16,
          "time_taken": 7.939338684082031e-05
      }
  }
  ```

---

## Команди для Docker

### Запуск проекту
```bash
docker-compose up --build
```

### Зупинка проекту
```bash
docker-compose down
```

### Перевірка логів
- **Provider:**
  ```bash
  docker-compose logs provider
  ```
- **Consumer:**
  ```bash
  docker-compose logs consumer
  ```
- **NGINX:**
  ```bash
  docker-compose logs nginx
  ```

---

## Примітки

1. **Зміна портів**:
   - Якщо порт 90 зайнятий, змініть його в `docker-compose.yml` для сервісу NGINX.

