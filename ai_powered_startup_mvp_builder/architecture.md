# System Architecture - TaskMaster AI

## High-Level System Diagram

```mermaid
flowchart TD
    User([User / Browser]) -->|HTTPS| Frontend[Next.js + Tailwind CSS Frontend<br/>Hosted on Vercel]
    Frontend -->|REST API / JSON| Backend[FastAPI / Node.js Express Backend<br/>Hosted on Render]
    Backend -->|Prompt & Structured Output| AIService[OpenAI / LLM API<br/>Task Breakdown Engine]
    Backend -->|SQL Queries / ORM| DB[(PostgreSQL Database<br/>Hosted on Supabase)]
