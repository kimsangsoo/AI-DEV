from typing import List, Dict
from core import get_client, SYSTEM_PROMPT

def main() -> None:
    """
    사용자와 직접 대화하며 피드백을 주고받는 전문 AI 감독 챗봇입니다.
    대화 내역(Memory)을 유지하여 연속적인 상호작용이 가능합니다.
    """
    print("--- [🎬 대화형 전문 감독 시스템 시작] ---")
    print("(종료하려면 'exit', '종료'를 입력하세요.)\n")

    try:
        # 공통 모듈에서 클라이언트 가져오기
        client = get_client()

        # [참고] OpenAI의 3가지 핵심 역할(Role) 이해하기
        # ---------------------------------------------------------
        # 1. 'system': AI의 정체성과 행동 규칙을 정의 (가장 높은 권력)
        # 2. 'user': 실제로 질문을 던지는 사용자 (우리의 입력값)
        # 3. 'assistant': AI가 이전에 내뱉은 답변 (AI의 과거 기억)
        # ---------------------------------------------------------

        # [핵심] 대화 내역(Memory) 저장소 초기화
        # AI 모델은 기본적으로 이전 대화를 기억하지 못하는 '상태 비저장(Stateless)' 방식입니다.
        # 따라서 우리가 모든 대화 내용을 리스트에 담아 매 요청마다 AI에게 다시 보내줘야 합니다.
        messages: List[Dict[str, str]] = [
            # 1. 'system' 역할: AI에게 페르소나와 작업 규칙을 맨 처음에 한 번만 주입합니다.
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

        while True:
            # 2. 사용자로부터 새로운 입력을 받습니다.
            user_input: str = input("나 (아이디어/피드백): ").strip()

            # 종료 조건 처리
            if user_input.lower() in ["exit", "quit", "종료"]:
                print("멋진 영감이었습니다. 감독 시스템을 종료합니다!")
                break
            if not user_input:
                continue

            # 3. [기록 추가] 사용자가 한 말을 대화 내역(messages)에 추가합니다.
            # 'user' 역할: 말 그대로 사용자의 메시지임을 나타냅니다.
            messages.append({"role": "user", "content": user_input})

            print("\n[감독이 분석 중...]")

            # 4. [기억 전달] 지금까지 쌓인 모든 대화 내역(messages)을 API에 보냅니다.
            # AI는 이 리스트를 처음부터 끝까지 다 읽은 후 맥락을 파악하여 다음 말을 결정합니다.
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,  # 단일 질문이 아닌 '전체 리스트'를 전달함으로 기억력 구현
                temperature=0.7
            )

            # 5. AI의 응답을 추출합니다.
            ai_response: str = response.choices[0].message.content.strip()

            # 6. [기록 추가] AI가 한 말도 잊지 않도록 다시 대화 내역에 저장합니다.
            # 'assistant' 역할: AI(비서)가 한 대답임을 나타냅니다. 
            # 다음 턴에서 AI는 이 내용까지 포함해 읽게 되어 대화의 흐름을 유지합니다.
            messages.append({"role": "assistant", "content": ai_response})

            # 결과 출력
            print(f"\n{ai_response}\n")
            print("-" * 40)

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
