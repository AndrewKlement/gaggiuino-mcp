# gaggiuino-mcp
Gaggiuino MCP Server
This is a lightweight Model Context Protocol (MCP) server built for [Gaggiuino](https://github.com/Zer0-bit/gaggiuino), the open-source espresso machine controller for the Gaggia Classic. It is designed to integrate easily AI clients that want to display or analyze data from the Gaggiuino system in real time.

## The MCP server exposes a simple HTTP API that allows connected clients to:

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

### Available Toolsets

| Toolset                 | Description                                                   |
| ----------------------- | ------------------------------------------------------------- |
| `getLatestShotId`       | Get latest espresso shot id                                   |
| `getShotData`           | Get espresso shot data for an id. Args: id: Shot id           |
| `getStatus`             | Get espresso machine status                                   |
