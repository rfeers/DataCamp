#!/usr/bin/env python3
"""
Streams a response and logs everything (messages, tool calls/results, errors)
to ~/.claude/logs/sdk-stream.jsonl using Claude Agent SDK's `query()` + options.
"""

import argparse, asyncio, datetime, json, os, sys
from typing import Any, Dict
from rich import print

# SDK imports (match your local version)
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ToolUseBlock

# ---- config ----
DEFAULT_MODEL = "haiku"
LOG_PATH = os.path.expanduser("/Users/josepferrersanchez/PRO/DataCamp/claude_agent_SDK/claude/logs/sdk-stream.jsonl")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

ALLOWED_TOOLS = [
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
        ]

def _utc_now() -> str:
    return datetime.datetime.utcnow().isoformat() + "Z"

def _safe_dump(obj: Any) -> Dict[str, Any]:
    try:
        if hasattr(obj, "model_dump"): return obj.model_dump()
        if hasattr(obj, "dict"): return obj.dict()
        return json.loads(json.dumps(obj, default=lambda x: getattr(x, "__dict__", str(x))))
    except Exception as e:
        return {"repr": repr(obj), "dump_error": repr(e)}

def log_event(kind: str, **payload: Any) -> None:
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": _utc_now(), "kind": kind, **payload}, ensure_ascii=False) + "\n")

def parse_args():
    p = argparse.ArgumentParser(description="Claude query + stream + logging")
    p.add_argument("--prompt", type=str, help="If omitted, you'll be asked interactively.")
    p.add_argument("--model", type=str, default=DEFAULT_MODEL)
    p.add_argument("--verbose", action="store_true", help="Print streamed messages")
    p.add_argument("--cwd", type=str, default=None, help="Working dir for tools (defaults to current dir)")
    p.add_argument("--permission-mode", type=str, default="acceptEdits",
                   choices=["acceptEdits","ask","autoDeny"])
    return p.parse_args()

async def run_once(prompt: str, model: str, verbose: bool, cwd: str | None, permission_mode: str):
    # Build options (this is where model & tool policy go)
    options = ClaudeAgentOptions(
        model=model,
        allowed_tools=ALLOWED_TOOLS,
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

    log_event("run_start", model=model, prompt_preview=prompt[:200], cwd=options.cwd)

    try:
        async for message in query(prompt=prompt, options=options):
            if verbose:
                print("—" * 80)
                print(message)

            log_event("sdk_message", payload=_safe_dump(message))

            if isinstance(message, AssistantMessage):
                for block in (getattr(message, "content", []) or []):
                    if isinstance(block, ToolUseBlock):
                        # Short console cue + structured log
                        print(f"🔧 Tool requested: {getattr(block, 'name', '<?>')}")
                        log_event(
                            "tool_use_request",
                            name=getattr(block, "name", None),
                            input=_safe_dump(getattr(block, "input", None)),
                            tool_use_id=getattr(block, "id", None),
                        )

        log_event("run_stop", ok=True)
    except Exception as e:
        log_event("run_error", error=repr(e), prompt_preview=prompt[:200])
        print(f"❌ Error while streaming response: {e}", file=sys.stderr)

async def main():
    args = parse_args()
    prompt = args.prompt or input("You: ").strip()
    await run_once(prompt, args.model, args.verbose, args.cwd, args.permission_mode)

if __name__ == "__main__":
    asyncio.run(main())
