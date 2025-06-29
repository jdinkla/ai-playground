"""
Runner for Google Greeting Agent.
"""

import asyncio
from agent import root_agent
from google.adk.sessions import InMemorySessionService, Session
from google.adk.runners import Runner
from google.genai import types

import logging

logging.basicConfig(level=logging.DEBUG)

APP_NAME = "greeting_agent"
USER_ID = "user_1"
SESSION_ID = "session_001"

session_service = InMemorySessionService()


async def main():
    """Main function for Google Greeting Agent."""
    session = await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    async def prompt(session: Session, message: str):
        """Prompt the agent."""
        content = types.Content(role="user", parts=[types.Part(text=message)])
        async for event in runner.run_async(
            user_id=USER_ID, session_id=session.id, new_message=content
        ):
            if event.content and event.content.parts:
                print(event.content.parts[0].text)

    await prompt(session, "Hello, how are you?")
    await prompt(session, "I am feeling curious about the Google ADK")


if __name__ == "__main__":
    asyncio.run(main())
