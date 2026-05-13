# bie-daalt-13

F.CSM311 хичээлийн "Бие даалт 13: AI-Assisted Software Construction" ажлын repository.

Энэ repo нь 3 хэсгээс бүрдэнэ:
- `partA/` - Plan (төлөвлөлт, архитектур, ADR, AI planning log)
- `partB/` - Build (эх код, тест, slash commands ашиглалт, AI build logs)
- `partC/` - Reflect (AI usage report, ADR-002, self-evaluation)

## Сонгосон төсөл
**Personal Task Tracker** (Option 2): task CRUD, due date, priority, label, search/filter.

## Repo бүтэц
- `CLAUDE.md` - build/test command, conventions, no-go zones
- `.claude/commands/` - custom slash commands (`review`, `test`, `docs`, `commit`, `security`)
- `partA/` - төлөвлөлтийн материал
- `partB/` - хэрэгжилт ба тест
- `partC/` - эргэцүүлэл, нотолгоо

## Хурдан эхлүүлэх
```bash
cd partB
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## Үнэлгээний шалгууртай уялдуулалт
- Part A: шаардлагатай бүх файл бэлэн
- Part B: 3+ feature, 10+ unit test, slash commands, AI logs
- Part C: 1500+ үгийн тайлан, hallucination/security жишээ, ADR-002, self-evaluation
