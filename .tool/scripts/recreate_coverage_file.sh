#!/bin/sh

# This script is used to recreate the coverage file from the latest test run, 
# so that it can be uploaded to codecov.io for code coverage analysis.

# to enable unicode characters in bash
locale-gen C.UTF-8 || true
export LANG=C.UTF-8
export LC_ALL=C.UTF-8

baseDir="tests/results"
printf "\U2603 Looking for coverage file in $baseDir \n"
# Capture all directories.
dirs=$(ls -d $baseDir/*)

# Extract the latest directory using regex matching based on modification time
latestGuidDir=$(echo "$dirs" | sort -r | head -n1)

coverageFilePath="./$latestGuidDir/coverage.xml"
printf "\U2603 Found Coverage file at: $coverageFilePath \n"

printf "\U2603 Copying contents from $coverageFilePath \U27A0 $baseDir/coverage.xml \n"
# create the file outside of results directory by coping contents of coverage.xml
cp "$coverageFilePath" "$baseDir/coverage.xml"

printf "\U2603 Coverage file ready at $baseDir/coverage.xml. \n"
