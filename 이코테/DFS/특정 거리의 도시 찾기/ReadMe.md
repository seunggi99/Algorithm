## 📌 문제: 특정 거리의 도시 찾기 (이코테)

### ✅ 문제 요약
- 단방향 그래프에서 거리 K만큼 떨어진 도시 찾기 (BFS 활용)

---

### ❌ 내 초기 풀이 (틀림 or 비효율)
- k만큼만 queue 순환시켜서 거리 판별
- 하지만 레벨 관리 정확히 안 돼서 오답 가능성있음

---

### ✅ 정답 풀이 (참고 + 개선)
- 거리 배열을 이용해 모든 거리 저장
- BFS 돌린 후 distance == k인 노드 출력

---

### 💡 배운 점
- BFS는 정답 보장 위해 distance 배열 쓰는 게 안정적
- "최단 거리" 키워드 → 무조건 BFS부터 고려할 것