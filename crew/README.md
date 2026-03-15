# crew

OpenAI Chat Completions API 기반 실험 노트북

## 다른 PC에서 clone 후 실행하기

### 1. 사전 요구사항

- [uv](https://docs.astral.sh/uv/) 설치
- Python 3.13+ (uv가 자동 설치 가능)

```bash
# uv 설치 (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 프로젝트 clone

```bash
git clone https://github.com/kimsangsoo/AI-DEV.git
cd AI-DEV/crew
```

### 3. 의존성 설치

```bash
uv sync
```

`.venv` 가상환경과 의존성이 자동으로 생성됩니다.

### 4. 환경 변수 설정

`.env` 파일은 git에 포함되지 않으므로 **직접 생성**해야 합니다.

```bash
# crew/.env 파일 생성
echo 'OPENAI_API_KEY="your-api-key-here"' > .env
```

또는 `.env` 파일을 만들고 아래 내용 추가:

```
OPENAI_API_KEY=sk-proj-...
```

### 5. 실행

**Jupyter 노트북:**

```bash
uv run jupyter notebook main.ipynb
```

**Python REPL에서 테스트:**

```bash
uv run python
>>> import openai
>>> # ...
```

### 6. IDE에서 커널 선택

VS Code / Cursor에서 `main.ipynb`를 열었다면:

- 커널 선택 → `crew/.venv` (Python 3.13) 선택
- 또는 "Enter interpreter path" → `./crew/.venv/bin/python` 지정
