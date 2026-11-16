# Data Model - TaskMaster AI

## Entity-Relationship Diagram

```mermaid
erDiagram
    WORKSPACE ||--o{ TASK : contains
    WORKSPACE ||--o{ AI_GENERATION_LOG : tracks

    WORKSPACE {
        uuid id PK
        string name
        text description
        int max_tasks
        timestamp created_at
        timestamp updated_at
    }

    TASK {
        uuid id PK
        uuid workspace_id FK
        string title
        text description
        string status
        string priority
        float estimated_hours
        int position
        boolean is_ai_generated
        timestamp created_at
        timestamp updated_at
    }

    AI_GENERATION_LOG {
        uuid id PK
        uuid workspace_id FK
        text raw_prompt
        int generated_task_count
        string model_used
        timestamp created_at
    }
