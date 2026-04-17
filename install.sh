#!/bin/bash
# 偵測並安裝 Skill 到對應平台
if [ -d "$HOME/.hermes" ]; then
    echo "安裝到 Hermes Agent..."
    mkdir -p "$HOME/.hermes/skills/save-your-token"
    cp -r . "$HOME/.hermes/skills/save-your-token/"
elif [ -d "$HOME/.openclaw" ]; then
    echo "安裝到 OpenClaw..."
    mkdir -p "$HOME/.openclaw/workspace/skills/save-your-token"
    cp -r . "$HOME/.openclaw/workspace/skills/save-your-token/"
else
    echo "找不到 Hermes 或 OpenClaw 目錄。"
fi
