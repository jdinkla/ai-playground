"""
Agent for Google Multi Agent.
"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from common import GOOGLE_MODEL

worker_agent = LlmAgent(
    name="worker_agent",
    model=GOOGLE_MODEL,
    description="Agent to execute tasks.",
    instruction="You are a worker agent. Your role is to execute the tasks given to you by the manager agent.",
)

manager_agent = LlmAgent(
    name="manager_agent",
    model=GOOGLE_MODEL,
    description="Agent to manage and delegate tasks to other agents.",
    instruction="You are the root agent. You have the first contact to the customer. You delegat",
    tools=[AgentTool(agent=worker_agent)],
)

root_agent = manager_agent
