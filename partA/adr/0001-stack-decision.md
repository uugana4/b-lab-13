# ADR-0001: Python Standard Library stack сонгох

## Төлөв
Accepted

## Context
Lab 13 дараах зүйлсийг шаардсан:
- 3+ working feature
- 10-аас дээш unit test
- documentation болон AI collaboration evidence
- хязгаарлагдмал хугацаа (2 долоо хоног)

Иймээс setup багатай, хурдан iteration хийх боломжтой, тест бичихэд найдвартай stack хэрэгтэй.

## Харгалзан үзсэн сонголтууд
1. Python + standard library (`unittest`)
2. Node.js + Express + Jest
3. Java + Spring Boot + JUnit

## Шийдвэр
Part B implementation-д **Python + standard library** ашиглана.

## Үндэслэл
- Setup complexity болон dependency overhead хамгийн бага.
- Чанартай unit test бичих хамгийн хурдан зам.
- Assignment-ийн гол зорилго болох workflow, verification, reflection дээр төвлөрөх боломж өгнө.
- Deterministic logic болон edge-case coverage хийхэд ойлгомжтой.

## Үр дагавар
### Эерэг
- Development болон testing хурдан.
- Environment/dependency алдаа гарах эрсдэл бага.
- AI-assisted development-ийн audit trail илүү цэвэр.

### Сөрөг
- Default байдлаар бүрэн production web stack биш.
- Дараа нь API surface хэрэгтэй бол нэмэлт tooling шаардагдана.
