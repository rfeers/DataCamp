"""
************** 03 AGENT WITH PROMPT USING QUERY() *******************************************************
Advanced example using the model with Query() and a specific tool. 
"""

from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ToolUseBlock
from rich import print
import asyncio

MODEL="haiku"

async def create_project():
    options = ClaudeAgentOptions(
        model = MODEL, # model to use
        allowed_tools=["Read", "Write", "Bash"], # allowed tools
        permission_mode='acceptEdits', # permissions for the model
        cwd="/Users/josepferrersanchez/PRO/DataCamp/claude_agent_SDK" # working directory
    )

    async for message in query(
        prompt="Create a Python project structure with setup.py contained in a dummy_project folder.",
        options=options
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, ToolUseBlock):
                    print(f"Using tool: {block.name}")

asyncio.run(create_project())