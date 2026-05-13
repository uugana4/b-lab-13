# AI-USAGE-REPORT.md

## Оршил

Энэ тайлан нь F.CSM311 Lab 13 бие даалтыг AI-assisted workflow ашиглан хийсэн туршлагыг минь дүгнэж бичсэн reflection юм.  
Энэ бие даалтын зорилго нь зөвхөн код бичих биш, харин **Spec -> Generate -> Review -> Integrate** гэсэн зарчмыг бодит жижиг төсөл дээр хэрэгжүүлж, AI-аас гарсан output-ыг шууд итгэж авахгүйгээр шалгаж чаддаг гэдгээ харуулах явдал байсан.  
Би AI-г planning, implementation draft, review checklist, documentation structure гаргахад ашигласан. Гэхдээ эцсийн техникийн шийдвэр, correctness, test coverage, academic integrity зэрэгт өөрөө хариуцлага хүлээсэн.

Ажлыг гурван үндсэн үе шаттайгаар зохион байгуулсан:
1. **Plan (Part A)** - scope, architecture, stack, collaboration rule тодорхойлох.
2. **Build (Part B)** - core feature-үүд болон test-үүдийг iterative AI support-той хэрэгжүүлэх.
3. **Reflect (Part C)** - AI юуг сайн хийсэн, хаана алдсан, би эрсдэлийг хэрхэн удирдсан талаар дүгнэх.

Сонгосон төсөл нь **Personal Task Tracker** бөгөөд CRUD, due date, priority, label, search/filter feature-үүдтэй.  
Би зориуд жижиг боловч бүтэн core system хэлбэрээр scope-ийг барьсан. Ингэснээр хэт олон feature нэмж цаг алдахгүй, харин quality, verification, reflection дээр төвлөрөх боломжтой болсон.

---

## 1) AI юу хийсэн, би юу хийсэн бэ?

### Part A - Төлөвлөлт
**AI-ийн оролцоо**
- Боломжит project topic-уудыг санал болгож, stack сонголтын trade-off-уудыг харьцуулахад тусалсан.
- Architecture module boundary буюу model, service, validator, query/filter гэсэн хэсгүүдийн эхний draft-ыг гаргахад тусалсан.
- ADR template болон Mermaid diagram structure-ийг анхны хэлбэрээр зохион байгуулахад тусалсан.

**Миний оролцоо**
- Эцсийн project topic-ийг сонгож, аль feature scope-д орох, аль нь орохгүйг шийдсэн.
- 2 долоо хоногийн хугацаанд тохирохгүй over-engineered architecture suggestion-уудыг хассан.
- `CLAUDE.md` дотор quality rule, no-go zone, test expectation-ийг өөрийн project-д тааруулж бичсэн.

**Жишээ**
- AI эхний design дээр persistence/database нэмэхийг санал болгосон.
- Би үүнийг scope-оос хассан. Учир нь assignment-ийн pass criteria нь deployment-scale persistence шаардаагүй, харин test, documentation, reflection чанарыг илүү чухалчилсан.

### Part B - Хэрэгжилт
**AI-ийн оролцоо**
- Due date болон priority validation хийх helper function-уудын эхний draft-ыг санал болгосон.
- Invalid date, missing task id, combined filter зэрэг unit test case-үүдийг санал болгосон.
- Invalid input үед илүү ойлгомжтой error message ашиглах санаа өгсөн.

**Миний оролцоо**
- Code structure-ийг assignment-д тохируулж энгийн, уншихад ойлгомжтой байхаар өөрчилсөн.
- AI-аас гарсан method бүрийг гараар уншиж, logic зөрчилтэй эсэхийг шалгасан.
- Test-үүдийг бичиж/засаж, output нь intended behavior-тэй таарч байгаа эсэхийг баталгаажуулсан.

**Жишээ**
- AI search logic-ийн draft гаргасан. Би filter order-ийг илүү тодорхой болгож, due date дараа нь id-аар deterministic sort хийх болгосон.  
  Үүний зорилго нь test outcome тогтвортой, дахин ажиллуулахад ижил байх явдал байсан.

### Part C - Эргэцүүлэл
**AI-ийн оролцоо**
- Reflection prompt-уудыг structure-тэй болгох, required section-ууд дутуу эсэхийг шалгахад тусалсан.
- Hallucination болон security example бичих боломжит чиглэлүүдийг санал болгосон.

**Миний оролцоо**
- Зөвхөн build явцад бодитоор гарсан incident-үүдийг сонгож бичсэн.
- Claim бүрийг code болон test behavior-тэй тулгаж шалгасны дараа тайланд оруулсан.
- AI-generated confidence language-д найдалгүй, өөрийн ойлголт дээр үндэслэн honest self-evaluation хийсэн.

---

## 2) Hallucination жишээнүүд: AI юуг буруу санал болгосон, би яаж зассан бэ?

### Hallucination жишээ 1: Python standard library-ийн буруу claim
**AI юу санал болгосон бэ?**
- Date validation хийхэд standard library дотор байдаггүй нэг convenience parser ашиглахыг санал болгосон.

**Яагаад буруу байсан бэ?**
- Тэр function/module path нь миний ашиглаж байсан Python version/environment-д огт байхгүй байсан.
- Хэрэв шууд хуулж ашигласан бол runtime import error гарах байсан.

**Би яаж илрүүлсэн бэ?**
- Official Python documentation шалгаж, local environment дээр import хийж үзсэн.
- Import fail болсон тул suggestion буруу гэдгийг баталгаажуулсан.

**Би яаж зассан бэ?**
- `datetime.strptime(..., "%Y-%m-%d")` дээр суурилсан validation болгож сольсон.
- `05/20/2026` гэх мэт invalid format ирэхэд `ValueError` гарах unit test нэмсэн.

**Сурсан зүйл**
- AI API нэр, module path-ийг маш итгэлтэй хэлж чаддаг ч заавал бодитоор import/test хийж шалгах хэрэгтэй.

### Hallucination жишээ 2: Filter ordering deterministic гэж хэт итгэлтэй таамагласан
**AI юу санал болгосон бэ?**
- Combined filter ашиглахад explicit sorting хийхгүй байсан ч result тогтвортой, deterministic байна гэсэн санаа гаргасан.

**Яагаад буруу байсан бэ?**
- In-memory dictionary/list iteration нь одоогийн run дээр stable харагдаж болох ч future refactor үед ordering assumption эвдрэх боломжтой.
- Нэг удаа stable харагдах нь test-д баталгаатай deterministic гэсэн үг биш.

**Би яаж илрүүлсэн бэ?**
- Logic-ийг review хийхэд filtered task буцаахаас өмнө explicit sort байхгүй байгааг анзаарсан.
- Энэ нь test outcome болон user-facing output-д subtle nondeterminism үүсгэж болзошгүй гэж үзсэн.

**Би яаж зассан бэ?**
- `list_tasks()` function-д `(due_date is None, due_date, id)` гэсэн sorting rule нэмсэн.
- `search_tasks()` нь `list_tasks()`-ийн output дээр ажиллахаар болгосон.
- Expected order шалгах unit test нэмсэн.

**Сурсан зүйл**
- AI ихэвчлэн plausible буюу боломжийн сонсогдох шийдэл санал болгодог. Харин инженерийн хувьд би guarantee, testability, reproducibility-г илүү чухалчлах ёстой.

### Hallucination жишээ 3: "Best practice" нэрээр scope томруулсан
**AI юу санал болгосон бэ?**
- Authentication, role-based access зэрэг feature-ийг "recommended architecture baseline" гэж санал болгосон.

**Яагаад буруу байсан бэ?**
- Энэ нь assignment scope-оос гадуур байсан.
- Single-user local tracker demo-д authentication шаардлагагүй.
- Нэмэлт feature нэмэх нь Part A/B/C-ийн required artifact-уудад зарцуулах цагийг багасгах байсан.

**Би яаж илрүүлсэн бэ?**
- AI suggestion-ийг assignment rubric болон `PROJECT.md` дээрх scope-той тулгаж харьцуулсан.

**Би яаж зассан бэ?**
- Authentication, cloud sync, external integration зэргийг out-of-scope гэж тодорхой бичсэн.
- Feature, test, AI log, ADR, reflection гэсэн required quality metric дээр төвлөрсөн.

**Сурсан зүйл**
- "Best practice" гэдэг нь context-оос хамаардаг. Scope control бол software engineering-ийн чухал чадвар.

---

## 3) Security/license анхаарах зүйл: AI-generated code эрсдэл үүсгэсэн үү?

Тийм, нэг чухал risk pattern гарсан.

### Security risk жишээ: unsafe dynamic execution санал болгосон
**AI юу санал болгосон бэ?**
- Exploratory step-ийн үед user input-оор filter expression хурдан үүсгэхийн тулд dynamic evaluation маягийн approach санал болгосон.

**Эрсдэл**
- `eval`-тэй төстэй behavior нь энэ төсөлд огт шаардлагагүй бөгөөд аюултай.
- Local app байсан ч ийм pattern ашиглах нь буруу coding habit-ийг хэвшүүлнэ.
- User-provided string code шиг ажиллах боломжтой бол injection төрлийн эрсдэл үүснэ.

**Би яаж шийдсэн бэ?**
- Тэр approach-ийг шууд reject хийсэн.
- Filtering logic-ийг explicit `if` check дээр суурилсан хэвээр үлдээсэн.
- `CLAUDE.md` дотор `eval`/`exec` огт ашиглахгүй гэсэн no-go rule нэмсэн.

**Яагаад чухал вэ?**
- OWASP mindset нь default байдлаар defensive байхыг шаарддаг.
- Security гэдэг зөвхөн internet-facing app-д хамаарахгүй; жижиг local project дээр ч unsafe pattern-ээс зайлсхийх ёстой.

### License/attribution анхаарах зүйл
AI-generated text болон code нь authorship boundary-г бүдгэрүүлэх эрсдэлтэй.

**Боломжит асуудал**
- AI-assisted commit болон document-ийг disclosure хийхгүй бол assignment integrity requirement зөрчигдөнө.
- AI үүсгэсэн зүйлийг өөрөө бүрэн бичсэн мэтээр зарлах нь academic honesty-д нийцэхгүй.

**Бууруулах арга**
- AI session log-уудыг хадгалсан.
- Commit message policy-д AI attribution footer оруулах дүрэм бичсэн.
- Reflection дээр AI юу санал болгосон, би юуг өөрчилж баталгаажуулсан гэдгийг ялгаж бичсэн.

**Үр дүн**
- Technical output болон academic integrity хоёулаа traceable болсон.

---

## 4) AI юуг хурдан хийхэд тусалсан бэ? (production benefit)

AI хэд хэдэн бодит хэсэг дээр хурдыг нэмэгдүүлсэн.

1. **Boilerplate хурдан гаргах**
   - Class/method signature, validation scaffolding, test skeleton-ийн эхний draft-ыг хурдан гаргасан.
   - Хоосон file дээрээс эхлэх blank-page time мэдэгдэхүйц багассан.

2. **Test idea brainstorm хийх**
   - Invalid input, missing ID, combined filter, sorted listing зэрэг олон candidate test scenario санал болгосон.
   - Edge-case coverage-ийг илүү хурдан өргөн хүрээтэй болгоход тусалсан.

3. **Documentation scaffolding**
   - ADR, architecture, AI session log зэрэг document-ийн эхний structure гаргахад тусалсан.
   - Assignment-ийн required section-уудыг алгасахгүй байхад дэмжлэг болсон.

4. **Review framing**
   - Security, robustness, regression risk гэсэн review lens-үүд өгсөн.
   - Final quality check хийхдээ юуг эхэлж харах вэ гэдгийг илүү тодорхой болгосон.

5. **Iteration loop хурд**
   - Propose -> inspect -> edit -> retest гэсэн цикл хурдан болсон.
   - Давтагдсан typing ажил багасаж, би verification болон reasoning дээр илүү цаг зарцуулсан.

Нийт дүгнэлтээр AI нь draft generation болон idea expansion хийх өндөр хурдтай junior collaborator шиг ажилласан. Харин reviewer/architect-ийн үүргийг би өөрөө гүйцэтгэсэн. Энэ нь AI-г "орлох хүн" биш, харин зөв ашиглавал productivity multiplier байж болохыг харуулсан.

---

## 5) AI юуг удаашруулсан бэ? (бэрхшээл, anti-pattern)

AI үргэлж хурд нэмээгүй. Зарим үед дараах шалтгаанаар ажил удааширсан.

1. **Үнэмшилтэй боловч буруу suggestion**
   - Hallucination засахад цаг ордог, учир нь AI ихэвчлэн итгэлтэй tone-оор хариулдаг.
   - Evidence сул үед verification overhead зайлшгүй хэрэгтэй болдог.

2. **Over-engineering pressure**
   - Зарим suggestion нь шаардлагагүй architecture complexity рүү түлхсэн.
   - Assignment-fit implementation рүү scope буцааж багасгахад цаг зарцуулсан.

3. **Style drift**
   - AI output заримдаа naming convention, error handling style-ийг хольж өгсөн.
   - Readability болон maintainability хадгалахын тулд style normalize хийх шаардлагатай болсон.

4. **False completeness feeling**
   - AI-generated document гаднаасаа бүрэн харагдаж болох ч subtle requirement gap үлдэх боломжтой.
   - Rubric miss хийхгүйн тулд manual checklist audit хийх шаардлагатай байсан.

5. **Context reset friction**
   - Урт interaction үед AI өмнө reject хийсэн санааг дахин санал болгох тохиолдол гарсан.
   - Үүнийг багасгахын тулд concise session log болон explicit constraint ашигласан.

Миний ажигласан гол anti-pattern бол хэт өргөн, constraint багатай prompt өгөх явдал. Ийм үед output нь өргөн боловч noisy, заримдаа хэрэггүй complexity-тэй гардаг. Харин strict scope, expected format, verification target-тай prompt өгөхөд чанар илүү сайжирсан.

---

## 6) Skill atrophy эрсдэлийг яаж зохицуулсан бэ? ("AI-free" practice)

AI-д хэт хамааралтай болохоос зайлсхийхийн тулд би санаатайгаар дараах стратегиудыг ашигласан.

1. **AI-free checkpoint**
   - Гол function-ууд дээр AI-аас дахин асуухаасаа өмнө өөрөө expected behavior-ийг бодож бичсэн.
   - Зарим test assertion-ийг эхлээд өөрийн логикоор бичээд, дараа нь AI suggestion-тэй харьцуулсан.

2. **Explain-before-accept**
   - Хүлээж авах code block бүрийг энгийн үгээр өөртөө тайлбарлаж чаддаг байх шаардлага тавьсан.
   - Хэрэв тайлбарлаж чадахгүй бол тэр code-ийг trusted гэж үзээгүй, дахин review хийж зассан.

3. **Manual bug tracing**
   - Сэжигтэй behavior гарахад шууд AI-аас fix асуухын оронд code path-ийг өөрөө trace хийсэн.
   - Энэ нь debugging skill-ээ идэвхтэй байлгахад тусалсан.

4. **Structured validation**
   - Test-ийг зөвхөн pass condition биш, skill-preserving tool гэж ашигласан.
   - Test бичихийн тулд contract behavior, edge case, expected failure mode-ийг ойлгох шаардлагатай болсон.

5. **Reflective logging**
   - Session summary бүрт AI юу санал болгосон, би юуг accept/reject хийсэн гэдгийг тэмдэглэсэн.
   - Энэ нь passive acceptance буюу AI output-ыг бодолгүй авах эрсдэлийг бууруулсан.

Skill atrophy-ийн талаар миний дүгнэлт:  
AI typing effort-ийг багасгаж болно, гэхдээ thinking effort-ийг заавал багасгах ёсгүй.  
Хэрэв verification, test design, architecture decision дээр ownership-оо хадгалбал AI нь crutch биш, харин multiplier болж чадна.

---

## Ерөнхий дүгнэлт

Энэ бие даалт AI-assisted development хамгийн үр дүнтэй байх нөхцөл нь strict verification discipline-тэй хамт хэрэгжих явдал гэдгийг харуулсан.  
Миний хувьд хамгийн сайн workflow дараах байдалтай байсан:
1. Constraint болон expected output-ыг эхлээд тодорхой болгох.
2. AI-аар fast draft гаргуулах.
3. Чухал claim бүрийг test, document, spec-тэй тулгаж шалгах.
4. Зөвхөн өөрөө тайлбарлаж, defend хийж чадах зүйлийг integrate хийх.

Хамгийн том takeaway нь "AI код хурдан бичдэг" гэсэн энгийн санаа биш. Илүү чухал сургамж нь software quality нь **human judgment** дээр тогтдог явдал юм. Үүнд scope control, risk awareness, test quality, authorship-ийн талаар honest байх зэрэг багтана.

Дараагийн project дээр би verify-first collaboration style-ийг үргэлжлүүлэн ашиглана. Гэхдээ дараах зүйлсийг сайжруулна:
- Security threat-model note-ийг илүү эрт эхлүүлэх.
- Day one-оос requirement-to-test traceability хөтлөх.
- Noisy suggestion багасгахын тулд strict prompt template ашиглах.
- AI session log-ийг real time-д илүү тогтмол хадгалах.

Энэ lab миний mindset-ийг "autocomplete ашиглан код бичих" түвшнээс "accountable AI collaboration ашиглан engineering хийх" түвшин рүү шилжүүлсэн. AI-г ашиглаж болно, бүр ашиглах ёстой ч эцсийн ойлголт, тайлбарлах чадвар, баталгаажуулалт нь хүний өөрийн хариуцлага хэвээр үлддэг.
