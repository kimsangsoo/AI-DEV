import random
from typing import List

from core import get_client, SYSTEM_PROMPT

def main() -> None:
    """
    미리 정의된 시나리오 중 하나를 랜덤으로 선택하여 테스트하는 샘플 테스트 스크립트입니다.
    이 파일은 core.py의 설정을 공유하여 핵심 로직에만 집중합니다.
    """
    print("--- [샘플 무작위 테스트 실행] ---")
    
    try:
        # 공통 모듈에서 클라이언트 가져오기
        client = get_client()

        # 테스트용 샘플 입력 리스트
        sample_inputs: List[str] = [
            "말하는 고양이가 유령과 대화하는 이야기를 보고 싶어",
            "22세기 미래 서울에서 인간과 사랑에 빠진 AI 로봇의 이야기",
            "중세 시대 마법사들이 모여서 요리 대회를 여는 코미디 설정",
            "우주 정거장에서 외계인 요리사들이 벌이는 서스펜스 미스터리",
            "꿈속에서만 만날 수 있는 두 연인의 애틋한 로맨스 시",
            "초능력을 가진 꼬마 아이가 지구를 지키는 웅장한 서사시",
            "디스토피아 미래 사회에서 버려진 도시를 탐험하는 탐험가",
            "지하철에서 옆자리에 앉은 사람이 사실은 미래에서 온 나였다는 사실"
        ]

        # 무작위 선택
        user_input: str = random.choice(sample_inputs)
        print(f"선택된 요청: {user_input}\n")

        # API 호출
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            n=1,
            temperature=0.8
        )

        # 결과 출력
        print(f"[감독의 제안]:\n{response.choices[0].message.content}")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()