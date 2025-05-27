# gaggiuino-mcp
[![smithery badge](https://smithery.ai/badge/@AndrewKlement/gaggiuino-mcp)](https://smithery.ai/server/@AndrewKlement/gaggiuino-mcp)

Gaggiuino MCP Server
This is a lightweight Model Context Protocol (MCP) server built for [Gaggiuino](https://github.com/Zer0-bit/gaggiuino), the open-source espresso machine controller for the Gaggia Classic. It is designed to integrate easily AI clients that want to display or analyze data from the Gaggiuino system in real time.

This is an article I wrote about this project https://medium.com/@a.klement.w/dialing-in-espresso-using-mcp-server-0207819fe93a

<a href="https://glama.ai/mcp/servers/@AndrewKlement/gaggiuino-mcp">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@AndrewKlement/gaggiuino-mcp/badge" alt="Gaggiuino Server MCP server" />
</a>

## Allows connected clients to:

- Retrieve the current machine status

- Access the latest shot ID

- Fetch shot data for a specified id 

## Features
📊 Real-time access to shot telemetry

🌐 Designed for local network access

## How to use

### Using Claude Desktop
```json
{
  "mcpServers": {
      "gaggiuino": {
          "command": "uv",
          "args": [
              "--directory",
              "/ABSOLUTE/PATH/TO/PARENT/FOLDER/gaggiuino-mcp",
              "run",
              "gaggiuino.py"
          ]
      }
  }
}
```

### Installing via Smithery

To install Gaggiuino Espresso Machine Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@AndrewKlement/gaggiuino-mcp):

```bash
npx -y @smithery/cli install @AndrewKlement/gaggiuino-mcp --client claude
```

### Available Toolsets

| Toolset                 | Description                                                   |
| ----------------------- | ------------------------------------------------------------- |
| `getLatestShotId`       | Get latest espresso shot id                                   |
| `getShotData`           | Get espresso shot data for an id. Args: id: Shot id           |
| `getStatus`             | Get espresso machine status                                   |


### Example
#### User: 
analyze the latest espresso shot data

#### Claude:
I'll retrieve and analyze the latest espresso shot data for you. Let me first check the status of your espresso machine and then get the latest shot information.
`getStatus`
Now I'll get the ID of the latest espresso shot:
`getLatestShotId`
Let me retrieve the data for shot #188:
`getShotData`
Based on the data retrieved, I'll now analyze your latest espresso shot (ID #188). Here's my analysis:

Machine Status and Shot Overview
Your machine is currently idle at 57.2°C with -0.1 bar pressure. The shot analyzed was taken on April 19, 2025 (based on the timestamp), with a total duration of 
26.5 seconds (265 datapoints at 0.1s intervals).

Profile Information
You used the "Leva 9 LR v0.5" profile, which is a multi-phase profile with declining pressure targeting 40g of output. The profile has
1. A flow-control preinfusion at 7 ml/s
2. Step-down to 3.5 ml/s flow
3. Pre-extraction at 1.5 ml/s flow with 3 bar pressure restriction
4. Pressure ramp to 9 bar over 2 seconds
5. A series of gradually declining pressure steps (8.8→6.0 bar)

Shot Analysis
Preinfusion and Extraction Phases
- Preinfusion (0-5s): Started with a high flow rate (6-7 ml/s) with minimal pressure (0.3-0.6 bar), allowing the puck to saturate.
- First Pressure Rise (5-10s): Pressure gradually built to ~2.5 bar while flow decreased to ~1.5 ml/s.
- Pressure Profile Phase (10-15s): Pressure held around 3 bar with flow reduced to ~0.8 ml/s.
- Pressure Ramp (15-20s): Pressure increased from 3 to 8.9 bar over ~5 seconds following the programmed profile.
- Declining Pressure Phase (20-26.5s): Pressure gradually declined from ~8.5 to 6.4 bar following the profile steps.

Key Measurements
- Final Yield: 38g (based on final shot weight)
- Brew Ratio: Unable to determine (coffee dose not provided)
- Temperature Stability: Excellent - maintained at 92.8-94.1°C throughout extraction
- First Drops: Appeared around 11-12 seconds (~75% into preinfusion)
- Peak Flow Rate: 7.2 ml/s (at the beginning)
- Peak Pressure: 8.9 bar (at ~20 seconds)

Extraction Dynamics
1. Flow Rate: Started high (7 ml/s), stepped down to 3.5 ml/s then 1.5 ml/s during preinfusion as programmed, then stabilized at ~2.8 ml/s during extraction.
2. Water Delivery: Total water pumped was 87.7 ml, with 38g in the cup, suggesting significant water retention in the puck.
3. Pressure Profile: The pressure curve shows excellent progression from preinfusion through extraction, with a smooth transition to declining pressure.

Performance Assessment
This appears to be a technically well-executed shot with good adherence to the programmed profile:
- Temperature Control: Excellent stability around 93-94°C
- Pressure Curve: Follows the programmed profile with smooth transitions
- Extraction Flow: Consistent during main extraction phase
- Weight Output: Achieved 38g (close to the 40g target)

Would you like me to provide more specific recommendations about any aspect of this shot, or is there a particular parameter you'd like me to analyze in more detail?
