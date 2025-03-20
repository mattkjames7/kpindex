#!/bin/bash

python -c "import kpindex; kpindex.UpdateLocalData()"
if [ $? -ne 0 ]; then
  echo "UpdateLocalData() failed, exiting."
  exit 1
fi

echo "UpdateLocalData() succeeded."


# Check if there are files in $HOME/kpdata/bin
# This is obviously not foolproof, but better than nothing
if [ -z "$(ls -A "$HOME/kpdata/bin" 2>/dev/null)" ]; then
  echo "No files found in $HOME/kpdata/bin. Exiting."
  exit 1
fi

echo "Files found in $HOME/kpdata/bin."
