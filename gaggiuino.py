from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import json

# Initialize FastMCP server
mcp = FastMCP("gaggiuino")

# Constants
API_BASE = "http://gaggiuino.local"


async def make_gg_request(url: str) -> dict[str, Any] | None:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
        

def format_datapoints(obj):
    if not isinstance(obj, dict):
        return obj

    result = {}
    for key, value in obj.items():
        if key == "datapoints" and isinstance(value, dict):
            # Scale & format all numeric values in datapoints
            result[key] = {
                k: [float(f"{v / 10:.1f}") for v in v_list]
                for k, v_list in value.items()
                if isinstance(v_list, list)
            }
        else:
            # Recurse normally
            result[key] = format_datapoints(value)
    return result



def format_status(status: dict) -> str:
    """Format machine telemetry into a human-readable status."""
    temp = float(status.get("temperature", 0))
    pressure = float(status.get("pressure", 0))
    steam_on = status.get("steamSwitchState", "False") == "true"
    brew_on = status.get("brewSwitchState", "False") == "true"

    # Determine state based on brew/steam switches
    if brew_on:
        state = "brewing"
    elif steam_on:
        state = "steaming"
    else:
        state = "idle"

    return f"""Your espresso machine is currently:
- Temperature: {temp:.1f}°C
- Pressure: {pressure:.1f} bar
- State: {state}
- Steam mode: {"on" if steam_on else "off"}"""

def format_shot(shot: dict) -> str:
    formated = format_datapoints(shot)
    return json.dumps(formated, indent=2)

@mcp.tool()
async def getStatus() -> str:
    """Get espresso machine status.
    """
    url = f"{API_BASE}/api/system/status"
    data = await make_gg_request(url)

    if not data:
        return "Unable to fetch your espresso machine status."

    status = format_status(data[0])
    return status 

@mcp.tool()
async def getLatestShotId() -> str:
    """Get latest espresso shot id.
    """
    url = f"{API_BASE}/api/shots/latest"
    data = await make_gg_request(url)

    if not data:
        return "Unable to fetch shot or no shot found."

    id = data[0]
    return id

@mcp.tool()
async def getShotData(id: str) -> str:
    """Get espresso shot data for an id.

    Args:
        id: Shot id
    """
    url = f"{API_BASE}/api/shots/{id}"
    data = await make_gg_request(url)

    if not data:
        return "Unable to fetch shot or no shot found."

    shot = format_shot(data)
    return shot

if __name__ == "__main__":
    mcp.run(transport='stdio')
