# PROJECT.md

## Төслийн нэр
Personal Task Tracker (сонголт 2)

## Товч танилцуулга
Энэ төсөл нь хувь хүн өдөр тутмын ажлаа бүртгэх, deadline хянах, priority/label оноох,
мөн task-уудаа хурдан хайж шүүхэд зориулсан жижиг task management систем юм.

## Асуудлын тодорхойлолт
Оюутан болон хувь хэрэглэгчид ажлаа олон өөр note, chat, reminder дээр тараан бичих нь элбэг.
Ингэснээр deadline мартах, чухал ажлыг ялгаж харахгүй байх, давтан шалгах явц алдагдах эрсдэлтэй.
Энэ систем task бүрийг нэг бүтэцтэйгээр хадгалж, priority, due date, label, search/filter-ээр ажлаа
илүү цэгцтэй удирдах боломж олгоно.

## Scope
### Хамрах үндсэн feature-үүд
1. Task CRUD (`create`, `read/list`, `update`, `delete`)
2. Due date дэмжих (`YYYY-MM-DD`)
3. Priority дэмжих (`low`, `medium`, `high`)
4. Label/tag оноох, label-аар filter хийх
5. Text search болон combined filtering (`status`/`priority`/`label`/`query`)

### Хамрахгүй зүйлс
- Олон хэрэглэгчийн authentication
- Cloud sync болон external integration
- Нарийн recurring schedule rule
- Web frontend UI (Part B нь backend logic + test дээр төвлөрнө)

## Амжилтын шалгуур
- 3-аас дээш core feature ажиллах хэмжээнд хэрэгжсэн байна.
- 10-аас дээш unit test pass болсон байна.
- Part A/B/C-ийн documentation ба AI collaboration evidence бүрэн байна.

## Эрсдэл ба бууруулах арга
- **Эрсдэл:** Буруу date/priority input нь data-г inconsistent болгох.  
  **Бууруулах арга:** strict validation ба тодорхой exception ашиглах.
- **Эрсдэл:** Search/filter logic хоёрдмол болж ойлгомжгүй үр дүн өгөх.  
  **Бууруулах арга:** deterministic filter order болон combined filter test нэмэх.
- **Эрсдэл:** AI suggestion-д хэт найдах.  
  **Бууруулах арга:** manual review, unit test, reflection log-оор заавал баталгаажуулах.
