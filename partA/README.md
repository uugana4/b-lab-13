# partA README (Draft)

## Зорилго
Код бичиж эхлэхээс өмнө төслийн үндсэн төлөвлөгөөг тодорхойлох:
- scope болон feature boundary
- архитектур ба data flow
- stack сонголт, үндэслэл
- AI-тай хамтран ажиллах дүрэм (`CLAUDE.md`)

## Part B-д төлөвлөсөн build/run/test
- Тест ажиллуулах:
  - `cd partB && python3 -m unittest discover -s tests -p "test_*.py" -v`
- Local script ажиллуулах:
  - `cd partB && python3 src/task_tracker.py`

## Төлөвлөсөн directory map
- `partB/src/` - эх код
- `partB/tests/` - unit test-үүд
- `partB/ai-sessions/` - build session-ы товч log-ууд

## Төлөвлөсөн feature-үүд
1. CRUD
2. Due date + priority + label
3. Search/filter
4. Task complete болгох
5. Deterministic listing/sorting
