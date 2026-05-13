# ADR-0002: File/DB persistence-ийн оронд in-memory storage ашиглах

## Төлөв
Accepted

## Context
Part B implementation-ийн явцад JSON file persistence нэмэх боломжийг авч үзсэн.
Гэхдээ төслийн шаардлага дараах зүйлсийг илүү чухалчилсан:
- 3-5 working feature
- 10-аас дээш найдвартай unit test
- AI workflow traceability болон reflection-ийн чанар

Persistence нэмэх нь I/O failure, migration concern, state reset strategy зэрэг complexity нэмнэ.
Энэ нь reflection artifact болон verification-д зарцуулах цагийг багасгах эрсдэлтэй.

## Шийдвэр
Одоогийн assignment version-д **in-memory storage** ашиглана.

## Харгалзан үзсэн сонголтууд
1. Зөвхөн in-memory storage
2. JSON file persistence
3. SQLite persistence

## Үндэслэл
- In-memory approach нь business logic-ийг ойлгомжтой, test-friendly байлгана.
- Moving part цөөн байх нь feature/test threshold-ийг найдвартай хангахад тусална.
- Assignment grading нь deployment-grade persistence шаардаагүй.
- Reflection болон verification-ийн чанарт илүү цаг үлдээнэ.

## Үр дагавар
### Эерэг
- Implementation болон debugging хурдан.
- File cleanup complexity байхгүй тул deterministic test хийхэд амар.
- Санамсаргүй data corruption bug гарах эрсдэл бага.

### Сөрөг
- Process restart хийхэд data алдагдана.
- Real multi-session production usage-д тохиромжгүй.

## Follow-up
Lab 13-аас цааш өргөтгөвөл repository interface нэмээд, existing test-үүдийг хадгалан SQLite adapter нэмэх боломжтой.
