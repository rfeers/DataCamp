"""
************** 06 Agent with MCP *******************************************************
- MCP refers to the Model Context Protocol, an open standard that allows AI applications to 
reliably and securely connect to external tools and data sources like databases, 
search engines, and local files.
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
        allowed_tools=[
            'Read',
            'Write',
            'Edit',
            'MultiEdit',
            'Grep',
            'Glob',
            'TodoWrite',
            'WebSearch',
            'WebFetch',
            'mcp__Playwright__browser_navigate', 
            'mcp__Playwright__browser_type',
            'mcp__Playwright__browser_close',
            'mcp__Playwright__browser_resize',
            'mcp__Playwright__browser_console_messages',
            'mcp__Playwright__browser_handle_dialog',
            'mcp__Playwright__browser_evaluate',
            'mcp__Playwright__browser_file_upload',
            'mcp__Playwright__browser_fill_form',
            'mcp__Playwright__browser_install',
            'mcp__Playwright__browser_press_key',
            'mcp__Playwright__browser_type',
            'mcp__Playwright__browser_navigate',
            'mcp__Playwright__browser_navigate_back',
            'mcp__Playwright__browser_network_requests',
            'mcp__Playwright__browser_take_screenshot',
            'mcp__Playwright__browser_snapshot',
            'mcp__Playwright__browser_click',
            'mcp__Playwright__browser_drag',
            'mcp__Playwright__browser_hover',
            'mcp__Playwright__browser_select_option',
            'mcp__Playwright__browser_tabs',
            'mcp__Playwright__browser_wait_for',
        ],
        permission_mode="acceptEdits",
        setting_sources=["project"],
        cwd="/Users/josepferrersanchez/PRO/DataCamp/claude_agent_SDK",
        mcp_servers={
            "Playwright": {
                "command": "npx",
                "args": [
                    "-y",
                    "@playwright/mcp@latest"
                ]
            }
        }
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