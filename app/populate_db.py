# app/populate_db.py

from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

# Создаём все таблицы перед заполнением
models.Base.metadata.create_all(bind=engine)

# Определяем термины для заполнения
terms = [
    {
        "keyword": "Микросервис (Microservice)",
        "description": "Независимый попарно разрабатываемый, развертываемый и масштабируемый компонент, который выполняет конкретную бизнес-логику и взаимодействует с другими микросервисами через сети, обычно по API."
    },
    {
        "keyword": "Микросервисная архитектура (Microservices Architecture)",
        "description": "Архитектурный стиль, в котором приложение разделяется на несколько небольших, независимых сервисов, каждый из которых разрабатывается и развертывается отдельно."
    },
    {
        "keyword": "API (Application Programming Interface)",
        "description": "Набор правил и спецификаций, который позволяет различным программным компонентам взаимодействовать между собой."
    },
    {
        "keyword": "Контейнеризация (Containerization)",
        "description": "Процесс упаковки приложения и его зависимостей в контейнер, что обеспечивает единообразие среды исполнения. Инструменты, такие как Docker, широко используются для этой цели."
    },
    {
        "keyword": "Оркестрация (Orchestration)",
        "description": "Управление развертыванием, масштабированием и взаимодействием между микросервисами, часто с использованием платформ, таких как Kubernetes."
    },
    {
        "keyword": "Сервисное взаимодействие (Service Communication)",
        "description": "Способы, с помощью которых микросервисы взаимодействуют друг с другом, что может включать REST, gRPC, сообщения в очереди и т.д."
    },
    {
        "keyword": "Событийная архитектура (Event-Driven Architecture)",
        "description": "Архитектурный подход, при котором микросервисы обмениваются сообщениями и событиями через систему обмена сообщениями, что позволяет более свободное и асинхронное взаимодействие."
    },
    {
        "keyword": "API Gateway",
        "description": "Компонент, который действует как единственная точка входа для клиентских приложений, предоставляя маршрутизацию, агрегацию и управление вызовами к микросервисам."
    },
    {
        "keyword": "Состояние и управление состоянием (State and State Management)",
        "description": "Управление состоянием данных в распределённой системе. Микросервисы могут не хранить состояние, рассчитывая на внешние решения, такие как базы данных или кеши."
    },
    {
        "keyword": "Декларативные конфигурации (Declarative Configurations)",
        "description": "Подход, при котором настройки приложения описываются в виде декларативных файлов, которые затем используются для автоматизации процессов развертывания и управления."
    },
    {
        "keyword": "Службы обнаружения (Service Discovery)",
        "description": "Механизмы, позволяющие микросервисам находить и взаимодействовать друг с другом, что может быть реализовано через централизованный реестр или через 'клиентское обнаружение'."
    },
    {
        "keyword": "Централизованный логгинг (Centralized Logging)",
        "description": "Подход к сбору и хранению логов из различных микросервисов в одном месте для упрощения мониторинга и анализа."
    },
    {
        "keyword": "Мониторинг и алертинг (Monitoring and Alerting)",
        "description": "Процессы сбора метрик и данных производительности для оценки состояния микросервисов и настройки уведомлений о проблемах."
    },
    {
        "keyword": "Паттерн Circuit Breaker (Цепной ломатель)",
        "description": "Шаблон проектирования, который предотвращает повторные неудачные запросы к зависимым сервисам, если они находятся в состоянии сбоя, позволяя системе оставаться устойчивой."
    },
    {
        "keyword": "Паттерн Saga",
        "description": "Шаблон управления распределёнными транзакциями, позволяющий координировать и управлять длительными бизнес-процессами между микросервисами."
    },
    {
        "keyword": "Репликация данных (Data Replication)",
        "description": "Процесс копирования данных между микросервисами для обеспечения согласованности и доступности, часто используется в контексте микросервисов, которые нуждаются в доступе к одной и той же информации."
    },
    {
        "keyword": "CQRS (Command Query Responsibility Segregation)",
        "description": "Шаблон, который разделяет операции изменения состояния (команды) и операции чтения (запросы), позволяя оптимизировать архитектуру для этих различных сценариев."
    },
    {
        "keyword": "API First",
        "description": "Подход, при котором разработка API происходит до разработки самого приложения, что позволяет гибко проектировать и обрабатывать взаимодействия между различными микросервисами."
    },
    {
        "keyword": "Тестирование API (API Testing)",
        "description": "Процесс проверки функционирования API, чтобы гарантировать, что он работает корректно, включая тестирование безопасности, производительности и надёжности."
    },
    {
        "keyword": "Скалируемость (Scalability)",
        "description": "Способность системы обрабатывать увеличивающуюся нагрузку путем добавления ресурсов, таких как серверы или экземпляры микросервисов."
    }
]






def populate():
    db: Session = SessionLocal()
    try:
        existing_terms = db.query(models.Term).count()
        if existing_terms == 0:
            for term_data in terms:
                term = models.Term(**term_data)
                db.add(term)
            db.commit()
            print("База данных успешно заполнена начальными терминами.")
        else:
            print("База данных уже содержит данные. Пропуск заполнения.")
    except Exception as e:
        db.rollback()
        print(f"Ошибка при заполнении базы данных: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    populate()
