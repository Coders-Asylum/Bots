#!/bin/sh

baseDir="tests/results"

# list all directories and subdirectories
ls -R $baseDir

# Capture all directories.
dirs=$(ls -d $baseDir/*)

# Extract the latest directory using regex matching based on modification time
latestGuidDir=$(echo "$dirs" | sort -r | head -n1)

coverageFilePath="./$latestGuidDir/coverage.xml"

# set this as env var
export COVERAGE_FILE_PATH="$coverageFilePath"

# print the coverage file path
echo "Coverage file path:$COVERAGE_FILE_PATH"
