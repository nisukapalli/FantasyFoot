#!/bin/bash

# Exit on error
set -e

# 1. Clone the repository
REPO_URL='https://github.com/nisukapalli/FantasyFoot.git'
PROJECT_DIR='FantasyFoot'
if [ ! -d "$PROJECT_DIR" ]; then
    echo "Cloning repository..."
    git clone $REPO_URL
fi
cd $PROJECT_DIR

# 2. Set up Python virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
echo "Activating virtual environment..."
source venv/bin/activate

# 3. Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Run the test script
echo "Running test_db.py..."
python -m app.test_db