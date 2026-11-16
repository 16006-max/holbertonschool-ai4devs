# Data Model - AI Sprint Retro & Blocker Analyzer

## Entity-Relationship Diagram

```mermaid
erDiagram
    TEAM_MEMBER ||--o{ CHECK_IN : submits
    CHECK_IN ||--o{ BLOCKER : generates
    TEAM_MEMBER ||--o{ BLOCKER : assigned_to

    TEAM_MEMBER {
        uuid id PK
        string name
        string role
        string email
        timestamp created_at
    }

    CHECK_IN {
        uuid id PK
        uuid member_id FK
        text yesterday_work
        text today_plan
        text raw_blockers
        date check_in_date
        timestamp created_at
    }

    BLOCKER {
        uuid id PK
        uuid check_in_id FK
        uuid owner_id FK
        string title
        string severity
        text ai_recommendation
        string status
        text resolution_note
        timestamp created_at
        timestamp resolved_at
    }
