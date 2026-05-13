# Part B - Build

## Хэрэгжүүлсэн feature-үүд
1. Task CRUD (`create_task`, `get_task`, `update_task`, `delete_task`)
2. Due date validation (`YYYY-MM-DD`)
3. Priority validation (`low|medium|high`)
4. Label normalization + filtering
5. Text search + combined filter (`query`, `priority`, `label`, `status`)
6. Task-ийг completed болгох

## Тест ажиллуулах
```bash
cd partB
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## Source structure
- `src/task_tracker.py`: үндсэн domain/service logic
- `tests/test_task_tracker.py`: happy path болон edge case unit test-үүд
- `ai-sessions/`: AI-assisted build session-ы товч log

## Чанарын тэмдэглэл
- Strict validation болон тодорхой exception ашигласан.
- Аюултай dynamic execution pattern ашиглаагүй.
- Predictable behavior гаргахын тулд deterministic list ordering хийсэн.
