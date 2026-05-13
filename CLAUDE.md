# CLAUDE.md

Төсөл: F.CSM311 Lab 13 - Personal Task Tracker

## Зорилго
Энэ файл нь AI assistant энэ repository дээр хэрхэн тогтвортой, аюулгүй, шалгаж болохуйц байдлаар хамтран ажиллах дүрмийг тодорхойлно.

## Build/Test командууд
- Тест ажиллуулах:
  - `cd partB && python3 -m unittest discover -s tests -p "test_*.py" -v`
- Module хурдан шалгах:
  - `cd partB && python3 -m py_compile src/task_tracker.py`
- Local demo ажиллуулах:
  - `cd partB && python3 src/task_tracker.py`

## Repository-ийн дүрэм
- Бие даалтын шаардсан бүтцийг өөрчлөхгүй:
  - `partA/`, `partB/`, `partC/`, `.claude/commands/`
- Part A нь зөвхөн төлөвлөлтийн баримт бичиг байна, production code оруулахгүй.
- Part C нь зөвхөн эргэцүүлэл ба нотолгооны материал байна.
- Бүх хэрэгжилтийн кодыг `partB/src/` дотор байрлуулна.
- Бүх тестийг `partB/tests/` дотор байрлуулна.
- Source code-ийн class/function/variable нэрийг ойлгомжтой English identifier-аар бичнэ.
- README, ADR, тайлан, session log зэрэг тайлбаруудыг Монгол хэлээр бичиж болно.

## Coding convention
- Filtering/search логикт жижиг, ойлгомжтой function ашиглана.
- Public API-д орж ирэх input-ыг validate хийнэ.
- Буруу task operation үед тодорхой exception (`ValueError`, `KeyError`) өгнө.
- Нууц side effect-ээс зайлсхийнэ.
- Огнооны format: ISO (`YYYY-MM-DD`).
- Priority зөвхөн `low`, `medium`, `high` байна.

## Testing convention
- Шинэ feature бүр дор хаяж нэг шууд unit test-тэй байна.
- Edge case-үүдийг заавал шалгана: буруу date, байхгүй task, хоосон title, filter-ийн хослол.
- Тестүүд deterministic, тусгаарлагдсан байна.

## Security ба robustness дүрэм
- User input-ыг code болгон ажиллуулахгүй.
- `eval`/`exec` огт ашиглахгүй.
- Store хийхээс өмнө бүх input-ыг validate/sanitize хийнэ.
- AI үүсгэсэн кодыг шууд итгэж авахгүй, тест ба review-ээр баталгаажуулна.
- User-facing output дээр internal stack trace задруулахгүй.

## Хориглох зүйлс
- Бие даалтын шаардсан folder/file нэрийг өөрчлөхгүй.
- AI usage evidence зохиож бичихгүй; log нь бодит session-ы товч байх ёстой.
- AI үүсгэсэн зүйлийг өөрөө гараар бичсэн гэж зарлахгүй.
- Унаж байгаа тестийг үндэслэлгүй устгахгүй.
- Шаардлагагүй dependency нэмэхгүй.

## Git/Commit зөвлөмж
- Conventional Commits ашиглана: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`.
- Commit бүр жижиг, нэг зорилготой байна.
- AI-assisted commit бүрийн body-д disclosure оруулна:
  - `Co-Authored-By: Claude <noreply@anthropic.com>`

## Энэ repo дахь slash command-ууд
- `/review`: security + robustness review (OWASP mindset)
- `/test`: edge case-тэй test нэмэх/сайжруулах
- `/docs`: docstring болон README хэсэг шинэчлэх
- `/commit`: Conventional Commit message санал болгох
- `/security`: гол эрсдэл ба mitigation тодорхойлох

## Эцсийн шалгах жагсаалт
- Шаардлагатай бүх файл байгаа.
- `python3 -m unittest ...` ажиллуулахад 10+ test pass болсон.
- Part A ба Part B-д AI session log байгаа.
- Part C нь 1500+ үгтэй, шаардсан evidence хэсгүүдтэй.
