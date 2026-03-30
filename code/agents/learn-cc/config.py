import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

# LLM 配置
LLM_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
LLM_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_BASE_URL = os.getenv("OPENAI_BASE_URL")
LLM_PROVIDER = os.getenv("OPENAI_PROVIDER") or os.getenv("LLM_PROVIDER")
LLM_TEMPERATURE = os.getenv("OPENAI_TEMPERATURE", 0.5)
LLM_TIMEOUT = os.getenv("OPENAI_TIMEOUT", 20)

# 路径配置
WORKDIR = Path.cwd()
SKILLS_DIR = WORKDIR / "skills"

THRESHOLD = 50000
TRANSCRIPT_DIR = WORKDIR / ".transcripts"
KEEP_RECENT = 3
PRESERVE_RESULT_TOOLS = {"read_file"}

TASKS_DIR = WORKDIR / ".tasks"

TEAM_DIR = WORKDIR / ".team"
INBOX_DIR = TEAM_DIR / "inbox"
MAX_TEAMMATE_TURNS = 50

VALID_MSG_TYPES = {
    "message",
    "broadcast",
    "shutdown_request",
    "shutdown_response",
    "plan_approval_response",
}


POLL_INTERVAL = 5
IDLE_TIMEOUT = 120
