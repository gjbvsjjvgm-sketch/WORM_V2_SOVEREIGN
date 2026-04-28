#!/bin/bash
export YOUSEF_SHTIWE_MODE="true"
export HERMES_HOME=$(pwd)/hermes_sovereign_data
export PYTHONPATH=$(pwd)/hermes-agent:$(pwd)
export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk 2>/dev/null || echo 30)"
source $(pwd)/venv/bin/activate
python3 -m yousef_shtiwe_cli.main "$@"
