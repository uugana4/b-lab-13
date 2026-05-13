# /review

Холбогдох кодод security + robustness review хийнэ.

Анхаарах дараалал:
1. Security risk (OWASP mindset): input validation, injection-тэй төстэй pattern, data handling.
2. Behavioral regression: өмнөх behavior эвдэх боломжтой logic change.
3. Reliability: unhandled error, сул edge-case handling, brittle assumption.
4. Test gap: risky path дээр test дутуу эсэх.

Output format:
- Findings-ийг severity дарааллаар эхэнд нь бич.
- Finding бүрт: file, risk, impact, recommendation.
- Асуудал олдоогүй бол тодорхой хэлж, residual risk-ийг жагсаа.
