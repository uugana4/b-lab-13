# STACK-COMPARISON.md

## Зорилго
Personal Task Tracker төслийг богино хугацаанд, test хийхэд хялбар, ойлгомжтой байдлаар хэрэгжүүлэхийн тулд
3 боломжит stack-ийг харьцуулж нэгийг сонгох.

## Харьцуулсан stack-үүд

### Stack A: Python + Standard Library (`unittest`, in-memory model)
**Давуу тал**
- Setup хурдан, external dependency шаардлагагүй
- Built-in `unittest` ашиглан test хурдан бичих боломжтой
- Logic correctness-ийг хичээлийн хүрээнд харуулахад тохиромжтой

**Сул тал**
- Full framework-тэй харьцуулахад API scaffolding бага
- UI хэрэгтэй бол дараа нь нэмэлт ажил шаардана

**Тохирох байдал**
- AI workflow, test, documentation дээр төвлөрөх энэ бие даалтад хамгийн тохиромжтой.

---

### Stack B: Node.js + Express + Jest
**Давуу тал**
- REST API хөгжүүлэхэд түгээмэл, ecosystem өргөн
- Дараа нь web frontend рүү өргөтгөхөд амар

**Сул тал**
- Package config, lint, test tooling зэрэг setup арай их
- Богино хугацаанд dependency management цаг авах эрсдэлтэй

**Тохирох байдал**
- API/demo deployment гол зорилго бол сайн сонголт, гэхдээ энэ ажлын scope-д арай хүнд.

---

### Stack C: Java + Spring Boot + JUnit
**Давуу тал**
- Том системд тохирох хүчтэй architecture pattern-уудтай
- Enterprise service болон testing ecosystem тогтвортой

**Сул тал**
- Setup болон boilerplate хамгийн их
- Жижиг 2 долоо хоногийн бие даалтад iteration удаашрах магадлалтай

**Тохирох байдал**
- Урт хугацааны том төсөлд хүчтэй боловч энэ scope-д overkill.

## Шийдвэр
**Сонгосон stack: Stack A (Python + Standard Library).**

## Сонгосон үндэслэл
1. Setup friction багасгаж, Part C reflection-ийн чанарт цаг үлдээнэ.
2. 10+ unit test шаардлагыг хурдан, найдвартай биелүүлэх боломжтой.
3. Implementation ил тод тул AI review болон manual verification хийхэд хялбар.
4. Жижиг төсөлд dependency/security surface багатай.

## AI planning session-ы товч
- AI Node.js болон Python-ыг хамгийн боломжит сонголтууд гэж санал болгосон.
- Бид reproducible test болон бага setup overhead-ийг илүү чухал гэж үзсэн.
- Correctness, documentation, verifiable workflow дээр төвлөрөхийн тулд Python-ыг сонгосон.
