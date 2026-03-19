import os
from typing import Optional

import openai
from dotenv import load_dotenv

def get_client() -> openai.OpenAI:
    """
    OpenAI 클라이언트를 초기화하여 반환합니다.
    .env 파일의 환경 변수를 로드하고, API 키를 검증합니다.
    """
    # .env 파일 로드
    load_dotenv(override=True)
    api_key: Optional[str] = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("Error: OPENAI_API_KEY를 찾을 수 없습니다. .env 파일을 확인해 주세요.")

    # OpenAI v1.x 클라이언트 생성
    return openai.OpenAI(api_key=api_key)

# 전문 AI 감독 페르소나 및 출력 규칙 (다양한 파일에서 재사용됨)
SYSTEM_PROMPT: str = """
당신은 "전문 멀티버스 콘텐츠 감독"입니다.
사용자의 아이디어를 듣고, 가장 적합한 콘텐츠 생산 라인을 결정하여 제안합니다.

생산 라인 목록:
- PRODUCE_SCENE(장르): 시나리오 오프닝 제작 (예: '사이버펑크')
- CRAFT_POEM(스타일): 시 창작 (예: '하이쿠')
- DESIGN_CHARACTER(능력): 영웅 특징 설계 (예: '시간여행')

규칙:
1. 사용자의 피드백을 반영하여 끊임없이 제안을 수정하거나 발전시킵니다.
2. 답변의 첫 줄에는 반드시 PRODUCTION_LINE('인자') 형식의 함수 호출을 포함하세요.
3. 그 아래는 감독으로서의 간결하고 전문적인 한국어 설명을 덧붙이세요.
""".strip()
