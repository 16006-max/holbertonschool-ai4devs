# Team Ideation

## Brainstormed Ideas
1. **AI Meeting Action-Item Extractor** — Transcribes team standups and automatically assigns tasks.
2. **Smart Code Snippet Organizer** — Tag, search, and explain reusable code blocks using AI.
3. **AI Sprint Retro & Blocker Analyzer** ✅ *(chosen)* — Analyzes team daily check-ins to detect sprint bottlenecks and suggest actionable resolutions.

## Problem Statement
During fast-paced hackathons and agile sprints, engineering teams lose visibility into emerging blockers and miscommunications until deadlines are already missed. An AI-powered retro and blocker analyzer synthesizes short team updates in real time, highlights critical risks, and recommends immediate next steps.

## MVP Features
- **Quick Check-In Form:** Team members submit a brief update (Yesterday, Today, Blockers) in under 30 seconds.
- **AI Blocker & Risk Detection:** Automatically scans submitted updates to flag dependencies, repeated delays, and high-risk bottlenecks.
- **Actionable Resolution Suggestions:** Generates concrete recommendations and task reassignments for each detected blocker.
- **Live Team Health Dashboard:** Displays sprint momentum, active blockers, and resolved issues in a clean summary view.
- **Markdown Sprint Report Export:** One-click export of the daily summary for sharing in Slack, Discord, or GitHub.

## Team Roles

| Member | Role | Responsibilities |
| :--- | :--- | :--- |
| Alice | AI Prompt Strategist | Designs prompts for blocker detection, risk scoring, and structured JSON output |
| Bob | Frontend Developer | Builds the check-in form, live dashboard UI, and responsive layout |
| Carol | Backend / API Developer | Implements REST endpoints, database schema, and LLM API integration |
| Dave | UI/UX & Testing Lead | Creates wireframes, writes automated tests, and manages live deployment |
