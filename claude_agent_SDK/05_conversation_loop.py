"""
************** 05 CONVERSATION LOOP *******************************************************
Let's define a loop to keep having a conversation with our model. 
"""

from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, ToolUseBlock

from rich.console import Console
from rich.prompt import Prompt
from rich import print

import asyncio
import argparse

MODEL="haiku"

# --------------------------------
# Parse runtime args from CLI
# --------------------------------
parser = argparse.ArgumentParser()

# --------------------------------
# Define get_user_input function 
# --------------------------------
def get_user_input(console: Console) -> str:
    """
    Get user input and display it in a rich panel in one step.
    Returns the user input string.
    """
    user_input = Prompt.ask("\n[bold yellow]You[/bold yellow]", console=console)
    print()
    return user_input

async def main():
    console = Console()
    args = parser.parse_args()

    
    options = ClaudeAgentOptions(
        model=MODEL,
        allowed_tools=["Read", "Write", "WebSearch", "WebFetch"],
        permission_mode="acceptEdits",
        setting_sources=["project"],
        cwd="/Users/josepferrersanchez/PRO/DataCamp/claude_agent_SDK"
    )

    print(
        "system",
        f"Welcome to your personal assistant!\n\nSelected model: {MODEL}",
        console
        )

    async with ClaudeSDKClient(options=options) as client:
        # we loop the messages so we can have a conversation
        while True:
            input_prompt = get_user_input(console)
            if input_prompt == "exit":
                break

            await client.query(input_prompt)

            async for message in client.receive_response():
                # Uncomment to print raw messages for debugging
                # print(message)
                print(message, console)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())