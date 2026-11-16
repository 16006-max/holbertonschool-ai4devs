# High-Level Architecture Plan - AI Sprint Retro & Blocker Analyzer

## System Architecture Diagram

```mermaid
flowchart TD
    Client([Team Member Browser]) -->|HTTPS| Frontend[Next.js + Tailwind CSS UI<br/>Deployed on Vercel]
    Frontend -->|REST API / JSON| Backend[FastAPI / Node.js Backend<br/>Deployed on Render]
    Backend -->|Structured Prompt| LLM[OpenAI / LLM API<br/>Blocker & Risk Analyzer]
    Backend -->|SQL / ORM| DB[(PostgreSQL Database<br/>Deployed on Supabase)]
