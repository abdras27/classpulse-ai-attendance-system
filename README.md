# ai-attendance-project-app

## Run locally

1. Create and activate a Python 3.12 virtual environment in the repo root.
2. Install dependencies:

```powershell
.\.venv312\Scripts\python.exe -m pip install -r ai-attendance-project-app\requirements.txt
```

3. Fill in `ai-attendance-project-app/.env` with your Supabase project URL and key.
4. In Supabase, run `ai-attendance-project-app/supabase_schema.sql` to create the required tables.
5. Start the app:

```powershell
cd ai-attendance-project-app
..\..\.venv312\Scripts\streamlit.exe run app.py
```

## Required tables

- `teachers`
- `students`
- `subjects`
- `subject_students`
- `attendance_logs`
