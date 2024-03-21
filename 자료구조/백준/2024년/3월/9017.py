def cross_country_winner():
    T = int(input())  # 테스트 케이스 수
    results = []  # 각 테스트 케이스별 결과 저장 리스트

    for _ in range(T):
        N = int(input())  # 선수 수
        ranks = list(map(int, input().split()))  # 팀 번호 배열
        
        from collections import Counter

        # 6명 이상인 팀만 필터링
        tc = Counter(ranks)  # 각 팀별 선수 수
        qt = [t for t, c in tc.items() if c >= 6]
        
        # 6명 미만 팀 제외 후 순위 배열
        fr = [r for r in ranks if r in qt]
        
        # 각 팀별 상위 4명 점수 합산
        fs = {t: sum(sorted([i for i, rt in enumerate(fr, 1) if rt == t])[:4]) for t in qt}
        
        # 최저 점수 팀 찾기
        ms = min(fs.values())
        pw = [t for t, s in fs.items() if s == ms]
        
        # 동점 처리
        if len(pw) > 1:
            fp = {t: sorted([i for i, rt in enumerate(fr, 1) if rt == t])[4] for t in pw}
            winner = min(fp, key=fp.get)
        else:
            winner = pw[0]
            
        print(winner)

cross_country_winner()