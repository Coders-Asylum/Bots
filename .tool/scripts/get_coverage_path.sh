
cd ./tests/results
# List all directories within the base directory that match a GUID pattern
guidDirs=$(ls -d $baseDir/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})

# Extract the latest directory using regex matching based on modification time
latestGuidDir=$(echo "$guidDirs" | sort -r | head -n1)

coverageFilePath="./tests/results/$latestGuidDir/coverage.xml"

# print the coverage file path.
echo $coverageFilePath
# set this as env var
export COVERAGE_FILE_PATH=$coverageFilePath