# Arquitectura del bot

## FileTree

```
.
├── src/
│   ├── cogs/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── moderation.py
|   |   ├── errorHandler.py
│   │   └── utility.py
│   ├── helpers/
│   │   │── __init__.py
│   │   └── database.py
│   ├── __init__.py
│   └── main.py
├── data/
│   |── schema.sql
│   └── database.sqlite
├── docs/
│   |── README.md
│   └── Arquitectura.md
├── .env.example
├── .gitignore
└── requirements.txt
```