# Project Analysis: ai-playground

This is a Python project designed as a playground for experimenting with various AI APIs. It is well-structured and provides numerous examples for interacting with different services.

## Key Technologies & Dependencies

- **AI Libraries:** OpenAI, Langchain, Google ADK
- **Package Management:** `uv`
- **Task Runner:** `just`
- **Core Dependencies:** `openai`, `langchain`, `google-adk`, `pydantic`, `pyyaml`
- **Testing & Linting:** `pytest`, `pylint`, `ruff`

## Project Structure

The source code is located in the `src/` directory and is organized by functionality:

- `src/openai_examples/`: Contains scripts demonstrating various OpenAI API features like chat, image generation, and dialogue creation.
- `src/langchain_examples/`: Includes examples for LangChain concepts such as chains, RAG (Retrieval-Augmented Generation), and conversational AI.
- `src/google_greeting_agent/`: An example implementation of a Google ADK agent.
- `src/`: Contains shared domain models (`domain.py`), dialogue management (`dialogue.py`), and other utilities.
- `examples/`: Contains `yaml` and `json` configuration files for the dialogue generation scripts.

## Available Commands

The `justfile` provides convenient commands to manage and run the project:

- `just init`: Installs or syncs project dependencies using `uv`.
- `just test`: Runs the test suite using `pytest`.
- `just lint`: Lints the code with `pylint`.
- `just format`: Formats the code with `ruff`.
- **OpenAI Examples:**
    - `just openai-chat`
    - `just openai-dialogue <FILENAME> <TURNS>`
    - `just openai-image <PROMPT>`
- **LangChain Examples:**
    - `just langchain-chain`
    - `just langchain-rag`
    - `just langchain-rag-extended <FILENAME> <QUESTION>`
- **Google ADK Examples:**
    - `just adk-web`
    - `just google-greeting-agent`

This project serves as a comprehensive collection of examples for developers working with modern AI tools.
