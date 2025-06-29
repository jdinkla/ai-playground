"""
Agent for Google Greeting Agent.
"""

from google.adk.agents import Agent
from common import GOOGLE_MODEL

root_agent = Agent(
    name="hello_world_agent",
    model=GOOGLE_MODEL,
    description=("Agent to greet the user and initiate some small talk."),
    instruction=(
        "You are a helpful agent who welcomes the users and initiate some small talk."
    ),
)
