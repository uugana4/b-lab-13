# bie-daalt-13

F.CSM311 хичээлийн "Бие даалт 13: AI-Assisted Software Construction" ажлын repository.

Энэ repository нь 3 хэсгээс бүрдэнэ:
- `partA/` - Төлөвлөлт: архитектур, stack сонголт, ADR, AI planning log
- `partB/` - Хэрэгжилт: эх код, unit test, slash command ашиглалт, AI build log
- `partC/` - Эргэцүүлэл: AI usage report, ADR-002, self-evaluation

## Сонгосон төсөл
**Personal Task Tracker** (сонголт 2): task CRUD, due date, priority, label, search/filter.

## Repository бүтэц
- `CLAUDE.md` - build/test команд, coding convention, no-go zone
- `.claude/commands/` - custom slash command-ууд (`review`, `test`, `docs`, `commit`, `security`)
- `partA/` - төлөвлөлтийн материал
- `partB/` - хэрэгжилт ба тест
- `partC/` - эргэцүүлэл ба нотолгоо

## Хурдан ажиллуулах
```bash
cd partB
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## Үнэлгээний шалгууртай уялдуулалт
- Part A: шаардлагатай бүх файл бэлэн
- Part B: 3+ feature, 10+ unit test, slash command, AI log
- Part C: 1500+ үгийн тайлан, hallucination/security жишээ, ADR-002, self-evaluation
