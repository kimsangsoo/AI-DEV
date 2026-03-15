# AI-DEV

AI 에이전트 및 LLM 실험 프로젝트

## 프로젝트 구조

```
ai-dev/
├── crew/          # OpenAI API 기반 실험 (uv + Python 3.13)
│   ├── main.ipynb
│   ├── pyproject.toml
│   └── uv.lock
└── README.md
```

## crew

OpenAI Chat Completions API를 사용한 실험 노트북

### 설정

```bash
cd crew
uv sync
```

### 환경 변수

`crew/.env` 파일에 `OPENAI_API_KEY` 설정 (`.env.example` 참고)

## 요구사항

- [uv](https://docs.astral.sh/uv/) (Python 패키지 매니저)
- Python 3.13+
