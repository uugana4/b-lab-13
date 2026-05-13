# Part B - Build

## Implemented Features
1. Task CRUD (`create_task`, `get_task`, `update_task`, `delete_task`)
2. Due date validation (`YYYY-MM-DD`)
3. Priority validation (`low|medium|high`)
4. Label normalization + filtering
5. Text search + combined filters (query, priority, label, status)
6. Mark task as completed

## Run Tests
```bash
cd partB
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## Source Structure
- `src/task_tracker.py`: core domain/service logic
- `tests/test_task_tracker.py`: unit tests for happy paths + edge cases
- `ai-sessions/`: summarized AI-assisted build sessions

## Quality Notes
- Uses strict validation and explicit exceptions.
- Avoids dangerous dynamic execution patterns.
- Includes deterministic list ordering for predictable behavior.
