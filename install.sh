#!/bin/bash

command -v uv &> /dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh
uv init .
