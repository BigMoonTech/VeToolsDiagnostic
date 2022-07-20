#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/VeTools.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/VeTools.dmg" && rm "dist/VeTools.dmg"
create-dmg \
  --volname "VeTools" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --hide-extension "VeTools.app" \
  --icon "VeTools.app" 175 120 \
  --app-drop-link 425 120 \
  "dist/VeTools.dmg" \
  "dist/dmg/"