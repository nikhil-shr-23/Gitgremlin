#!/usr/bin/env python3
"""
Initialize the Gitgremlin repository with the first commit
This script helps set up the repository for the commit bot
"""

import os
import subprocess
import sys
from datetime import datetime

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        if result.stdout:
            print(f"   Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr.strip()}")
        return False

def initialize_repository():
    """Initialize the local repository"""
    print("🚀 Initializing Gitgremlin repository...")
    print("=" * 50)
    
    # Create initial README
    readme_content = f"""# Gitgremlin

GitHub Daily Commit Bot Repository

This repository is managed by an automated commit bot that creates daily contributions to maintain GitHub activity.

## Setup Date
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Bot Information
- **Purpose**: Daily GitHub contributions
- **Schedule**: 9:00 AM, 3:30 PM, 9:45 PM daily
- **Owner**: nikhil-shr-23

## Files
- Contributions are stored in the `contributions/` directory
- Each contribution is a markdown file with timestamp

---
*This repository is automatically maintained by GitHub Commit Bot*
"""
    
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print("✅ Created README.md")
    
    # Initialize git repository
    commands = [
        ("git init", "Initializing git repository"),
        ("git add README.md", "Adding README to git"),
        ("git commit -m 'Initial commit: Setup Gitgremlin repository'", "Creating initial commit"),
        ("git branch -M main", "Setting default branch to main"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    # Add remote origin
    remote_url = "https://github.com/nikhil-shr-23/Gitgremlin.git"
    
    # Remove existing remote if it exists
    run_command("git remote remove origin", "Removing existing remote (if any)")
    
    # Add new remote
    if not run_command(f"git remote add origin {remote_url}", "Adding GitHub remote"):
        return False
    
    print("\n" + "=" * 50)
    print("🎉 Repository initialization completed!")
    print("\n📋 Next steps:")
    print("1. Make sure your .env file has the correct GitHub token")
    print("2. Run: python diagnose.py (to test connection)")
    print("3. Run: python commit_bot.py --test (to create first bot commit)")
    
    return True

if __name__ == "__main__":
    initialize_repository()
