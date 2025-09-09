# Real-Time Collaborative Kanban Board

A web app to create and manage Kanban boards with live real-time collaboration.  
Built with Django (backend) and React (frontend) using WebSockets for instant updates.

## How It Works

- Users can create boards with multiple columns (e.g., Todo, In Progress, Done).
- Cards can be added, edited, and dragged between columns.
- Changes sync live for all users viewing the same board using WebSockets powered by Django Channels and Redis.
- Presence indicators show who is online on a board.
- In-app notifications alert users about assignments and mentions.
- Backend provides APIs for CRUD operations and manages real-time messaging.
- Frontend handles UI, drag-and-drop interactions, and WebSocket connections.

## Tech Stack

- Backend: Django, Django Channels, Redis
- Frontend: React, @dnd-kit (drag & drop)
- Database: PostgreSQL (Supabase)
- Real-time: WebSockets

## Running Locally

1. Start Redis server locally or connect to a remote Redis.
2. Run backend Django server with channels support.
3. Run React frontend development server.
4. Open browser at `http://localhost:3000` to use the app.

---

