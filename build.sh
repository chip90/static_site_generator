#!/bin/bash
# Build script for GitHub Pages deployment
echo "Building site into docs directory with basepath /chip90/static_site_generator/ ..."
python3 src/main.py "/chip90/static_site_generator/"
echo "Build complete. Output in docs/"
