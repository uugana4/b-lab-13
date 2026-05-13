# Session 02 - Debug ба edge case review

## Зорилго
Input validation болон failure path-уудыг илүү найдвартай болгох.

## AI assistance
- Date format болон empty title handling дээр inconsistency гарах боломжийг анхааруулсан.
- Invalid priority болон байхгүй task ID дээр test нэмэхийг санал болгосон.

## Хүний verification
- Invalid due date format болон invalid priority-д test нэмсэн.
- `get_task`, `delete_task` дээр байхгүй ID ирэхэд `KeyError` гарахыг баталгаажуулсан.

## Үр дүн
- Error path-ууд тодорхой болж, test coverage-д орсон.
