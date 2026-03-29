<!-- BANNER -->
<h1 align="center">🧠✨ AI Pokédex</h1>
<p align="center">
  <b>Production-grade AI-powered Pokédex</b><br/>
  Full-stack • Machine Learning • NLP • Scalable Systems
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Next.js-Frontend-black?style=for-the-badge&logo=next.js"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql"/>
  <img src="https://img.shields.io/badge/ML-scikit--learn-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Docker-DevOps-blue?style=for-the-badge&logo=docker"/>
</p>

---

## 🌟 Overview

AI Pokédex is a **smart Pokémon discovery engine** that combines:
- ⚡ High-performance backend APIs  
- 🎨 Modern UI  
- 🤖 Machine learning models  
- 🧠 Natural language understanding  

---

## 🚀 Features

### 🔍 Core
- Browse Pokémon with stats
- Search by name
- Filter by type and attributes

### 🤖 AI
- 🧬 Similarity search  
- 🎯 Type prediction  
- 💬 Natural language queries  
- 🖼️ (Optional) Image recognition  

---

## 🧱 Architecture
```
pokedex-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes.py        # Main API routes
│   │   │   └── deps.py          # Dependencies (DB, etc.)
│   │   │
│   │   ├── models/
│   │   │   └── pokemon_model.py # DB / ML models
│   │   │
│   │   ├── schemas/
│   │   │   └── pokemon_schema.py # Pydantic schemas
│   │   │
│   │   ├── services/
│   │   │   └── pokemon_service.py # Business logic
│   │   │
│   │   ├── core/
│   │   │   └── config.py        # App configuration
│   │   │
│   │   └── main.py              # FastAPI entry point
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx             # Home page
│   │   └── layout.tsx           # Layout
│   │
│   ├── components/
│   │   ├── PokemonCard.tsx
│   │   ├── Navbar.tsx
│   │   └── SearchBar.tsx
│   │
│   ├── lib/
│   │   └── api.ts               # API calls
│   │
│   ├── public/
│   │   └── logo.png
│   │
│   ├── styles/
│   │   └── globals.css
│   │
│   ├── types/
│   │   └── pokemon.ts           # Type definitions
│   │
│   ├── package.json
│   └── tsconfig.json
│
├── ml/
│   ├── data/
│   │   └── dataset.csv
│   │
│   ├── models/
│   │   └── model.pkl            # Trained ML model
│   │
│   ├── training/
│   │   └── train.py             # Training script
│   │
│   ├── inference/
│   │   └── predict.py           # Prediction logic
│   │
│   └── utils/
│       └── preprocess.py
│
├── infra/
│   ├── docker-compose.yml
│   └── nginx.conf
│
├── docs/
│   └── architecture.md
│
├── README.md
└── .gitignore
```
