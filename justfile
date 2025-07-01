set dotenv-load

run := 'PYTHONPATH=src uv run python'
openai-path := 'src/openai_examples'
langchain-path := 'src/langchain_examples'

# print this help test
help:
  @just --list

init:
    @uv sync

test:
	@PYTHONPATH=src uv run pytest

lint:
	@uv run pylint src tests

format:
	@uv run ruff format .

pylintrc:
	@pylint --generate-rcfile > .pylintrc

#
# OpenAI 
#

openai-chat:
    @{{run}} {{openai-path}}/openai_chat.py
    
openai-detective FILENAME:
    @{{run}} {{openai-path}}/openai_detective.py {{FILENAME}}

openai-dialogue FILENAME TURNS:
    @{{run}} {{openai-path}}/openai_dialogue.py {{FILENAME}} {{TURNS}}

openai-dialogue-generator DESCRIPTION:
    @{{run}} {{openai-path}}/openai_dialogue_generator.py "{{DESCRIPTION}}"

openai-image PROMPT:
    @{{run}} {{openai-path}}/openai_image.py "{{PROMPT}}"

openai-speak SOMETHING:
    @{{run}} {{openai-path}}/openai_speak.py "{{SOMETHING}}"

openai-speak2 SOMETHING VOICE:
    @{{run}} {{openai-path}}/openai_speak.py "{{SOMETHING}}" "{{VOICE}}"

openai-spoken-news URL:
    @{{run}} {{openai-path}}/openai_spoken_news.py "{{URL}}"

openai-spoken-news-infoq:
    @{{run}} {{openai-path}}/openai_spoken_news.py "https://feed.infoq.com/news/"

openai-better-filename FILENAME:
    @{{run}} {{openai-path}}/openai_better_filename.py "{{FILENAME}}"

#
# LangChain
#

langchain-chain:
    @{{run}} {{langchain-path}}/langchain_chain.py

langchain-conversation:
    @{{run}} {{langchain-path}}/langchain_conversation_chain.py

langchain-llm:
    @{{run}} {{langchain-path}}/langchain_llm.py

langchain-rag:
    @{{run}} {{langchain-path}}/langchain_rag.py

langchain-rag-extended FILENAME QUESTION:
    @{{run}} {{langchain-path}}/langchain_rag_extended.py "{{FILENAME}}" "{{QUESTION}}"

langchain-prompt-text2image DESCRIPTION:
    @{{run}} {{langchain-path}}/langchain_prompt_text2image.py "{{DESCRIPTION}}"

#
# Google ADK
#

adk-web:
    @cd src ; uv run adk web

adk-run AGENT:
    @cd src ; uv run adk run {{AGENT}}

google-greeting-agent:
    @{{run}} src/google_greeting_agent/runner.py

#
# Pydantic AI
#

pydantic-dice-game:
    @{{run}} src/pydantic_examples/dice_game.py
