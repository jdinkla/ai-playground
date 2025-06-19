
# print this help test
help:
  @just --list

init:
    uv sync

test:
	uv run pytest

lint:
	uv run pylint src

pylintrc:
	pylint --generate-rcfile > .pylintrc

#
# OpenAI 
#

openai-chat:
    uv run python src/openai_chat.py
    
openai-detective FILENAME:
    uv run python src/openai_detective.py {{FILENAME}}

openai-dialogue FILENAME TURNS:
    uv run python src/openai_dialogue.py {{FILENAME}} {{TURNS}}

openai-dialogue-generator DESCRIPTION:
    uv run python src/openai_dialogue_generator.py "{{DESCRIPTION}}"

openai-image PROMPT:
    uv run python src/openai_image.py "{{PROMPT}}"

openai-speak SOMETHING:
    uv run python src/openai_speak.py "{{SOMETHING}}"
    
#
# LangChain
#

langchain-chain:
    uv run python src/langchain_chain.py

langchain-conversation:
    uv run python src/langchain_conversation_chain.py

langchain-llm:
    uv run python src/langchain_llm.py

langchain-rag:
    uv run python src/langchain_rag.py

langchain-rag-extended FILENAME QUESTION:
    uv run python src/langchain_rag_extended.py "{{FILENAME}}" "{{QUESTION}}"

langchain-prompt-text2image DESCRIPTION:
    uv run python src/langchain_prompt_text2image.py "{{DESCRIPTION}}"
