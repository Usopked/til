pandas 라이브러리 함수 정리
============

- **1. read_csv() / to_csv()**
    - csv 파일을 읽어오거나, csv 파일을 저장하는 함수.
    - 사용 예시:
        ```
        pd.read_csv('train.csv')
        df.to_csv('submission.csv')
        ```
- **2. head() / tail()**
    - 데이터프라임의 상위/하위 n행을 반환함.
    - 사용 예시:
        ```
        df.head()
        df.tail()
        ```
- **3. describe()**
    - 데이터프라임의 칼럼별 요약 통계(평균, 표편, 최솟값/최댓값) 반환.
    - 사용 예시:
        ```
        df.describe()
        ```
- **4. info()**
    - 데이터프레임의 기본 정보 출력. **누락된 값의 여부** 확인 가능
    - 사용 예시:
        ```
        df.info()
        ```