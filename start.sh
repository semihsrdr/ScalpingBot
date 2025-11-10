#!/bin/bash
# This script is for LOCAL DEVELOPMENT only.
# For deployment, Coolify will use the 'Procfile' automatically.

echo "Starting application for local development using honcho..."
echo "Web server will be on http://localhost:3000"
echo "Press Ctrl+C to stop all processes."

# Use the .dev procfile for local execution
honcho -f Procfile.dev start
