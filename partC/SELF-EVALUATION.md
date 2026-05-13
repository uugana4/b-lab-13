# SELF-EVALUATION.md

## 1) Хэрэв шалгалт өнөөдөр болбол би энэ кодыг өөрөө бичиж чадах уу?
**Хэсэгчлэн.**

Би дараах хэсгүүдийг өөрөө дахин бичиж чадна гэж үзэж байна:
- task CRUD logic
- input validation pattern
- edge case-д зориулсан unit test structure

Гэхдээ дараах зүйл дээр удаашрах магадлалтай:
- бүх documentation artifact-ийг нэг дор бүрэн бичих
- AI draft тусламжгүйгээр architecture/ADR wording-ийг ийм түвшинд polish хийх

## 2) Дахин хийнэ гэвэл юуг өөрөөр хийх вэ?
- Эхний өдрөөс requirements-to-tests matrix хөтөлнө.
- Hallucination/security incident-үүдийг дараа нь сэргээж бичих биш, тухайн үед нь тэмдэглэнэ.
- Traceability сайжруулахын тулд эхнээс нь бүр жижиг commit-үүд хийнэ.
- Manual exploratory testing хийхэд зориулж lightweight CLI interaction-ийг эрт нэмнэ.

## 3) Энэ туршлагаас юу сурсан бэ?
- AI нь draft generation болон option exploration-д хүчтэй боловч final truth биш.
- Verification буюу test + manual review нь professional skill-ийн гол хэсэг.
- Scope control маш чухал; over-engineering-д "үгүй" гэж хэлэх нь чанарыг сайжруулсан.
- Honest attribution болон AI usage transparency нь engineering ethics-ийн нэг хэсэг.
