from google.adk.agents import Agent

root_agent = Agent(
    name="hello_world_agent",
    model="gemini-2.5-flash",
    description=("Agent to greet the user and initiate some small talk."),
    instruction=(
        "You are a helpful agent who welcomes the users and initiate some small talk."
    ),
)
