# Telegram Bot для управления каталогом товаров

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)

Бот для управления каталогом товаров с системой учета пользователей, их рейтинга и товаров. Проект построен на aiogram 3.x с использованием SQLite.

## 📌 Основные возможности

- Регистрация пользователей при первом запуске
- Управление товарами пользователей
- Система рейтинга пользователей
- Гибкая система клавиатур и команд
- Логирование всех действий
- Обработка ошибок с уведомлением пользователя

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.9+
- Аккаунт Telegram и токен бота от [@BotFather](https://t.me/BotFather)

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/telegram-catalog-bot.git
cd telegram-catalog-bot
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` в корне проекта:
```env
BOT_TOKEN=your_bot_token_here
```

4. Запустите бота:
```bash
python run.py
```

## 🛠 Структура проекта

```
app/
├── src/               # Исходный код
│   ├── bot/           # Основной код бота
│   ├── middlewares/   # Промежуточное ПО
│   └── models.py      # Модели базы данных
├── tests/             # Тесты
├── .env.example       # Пример конфигурации
└── run.py             # Точка входа
```

## 🔧 Команды бота

- `/start` - Начало работы, регистрация
- `/help` - Получить помощь
- `/catalog` - Просмотреть каталог
- `/add_product` - Добавить товар
- "Мои товары" - Просмотреть свои товары (через кнопку)

## 🤝 Участие в разработке

Приветствуются pull requests. Основные шаги:

1. Форкните репозиторий
2. Создайте ветку для своей фичи (`git checkout -b feature/amazing-feature`)
3. Сделайте коммит изменений (`git commit -m 'Add some amazing feature'`)
4. Запушьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте pull request