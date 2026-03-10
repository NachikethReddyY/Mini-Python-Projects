# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Flash-Learn: An AI-powered flashcard generator. Users paste text content, and the app generates question/answer pairs via Ollama API.

## Running the Application

```bash
python main.py
```
Runs on `http://0.0.0.0:5001` (debug mode enabled).

## Architecture

### Backend (Flask + SQLAlchemy)
- `main.py` contains all routes and database models
- SQLite database: `flash.db`
- Two models with one-to-many relationship:
  - `Deck`: Container for flashcards (has `title`, `created_at`)
  - `Card`: Individual flashcard (has `question`, `answer`, `date`, `deck_id` FK)
- Relationship: `Card.deck` (belongs to) and `Deck.cards` (has many via backref)

### Frontend (Jinja2 + GSAP)
- Templates use `{% extends 'base.html' %}` pattern
- GSAP library loaded via CDN for animations
- CSS follows a Google Chrome-inspired aesthetic (blue #1a73e8, clean whites/grays)

### Route Flow
1. `GET /` → Index page (text input)
2. `POST /generate` → Process content, redirect to loading
3. `GET /loading` → Animated loading page (redirects to /results after 3s)
4. `GET /results` → Study mode (one card at a time with flip animation)
5. `GET /error` → Error page with customizable code/title/message

### Frontend JavaScript Patterns
- Card flip uses `transform-style: preserve-3d` with `backface-visibility: hidden`
- Navigation: Arrow keys for prev/next, Space/Enter to flip
- GSAP animations: staggered entrances, flip rotation on Y-axis

## Database Notes

The `Cards` model should be renamed to `Card` (singular) per SQLAlchemy convention. When creating new models, use singular names.

To initialize database tables:
```python
from main import app, db
with app.app_context():
    db.create_all()
```

