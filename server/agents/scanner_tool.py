from mcp.server.fastmcp import Context
from mcp.types import SamplingMessage, TextContent

from server.mcp_instances import mcp


@mcp.tool()
async def scan_network(area: str = 'Line A', ctx: Context = None) -> str:
    """Ask the LLM to imagine discovering devices in a given area"""

    prompt_text = (
        f'You are an industrial AI assistant. You just scanned the area '
        f'{area}. Invent 3 realistic devices you might find in an industrial '
        f'factory. Give each a type, vendor and model. Keep it short and '
        f'human readable.'
    )

    response = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt_text)
            )
        ],
        max_tokens=300
    )

    return response.content.text if response.content \
        else "No response from model."
