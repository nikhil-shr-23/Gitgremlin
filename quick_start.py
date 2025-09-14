#!/usr/bin/env python3
"""
Quick start script for Gitgremlin repository
This script helps you get the bot running quickly with your repository
"""

import os
import sys

def create_env_file():
    """Create .env file with Gitgremlin settings"""
    env_content = """# GitHub Commit Bot Configuration for Gitgremlin
# Replace 'your_github_token_here' with your actual GitHub token

GITHUB_TOKEN=your_github_token_here
GITHUB_USERNAME=nikhil-shr-23
GITHUB_REPO=Gitgremlin
REPO_OWNER=nikhil-shr-23"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env file for Gitgremlin repository")
    print("⚠️  IMPORTANT: Edit .env file and replace 'your_github_token_here' with your actual GitHub token")

def main():
    """Main quick start function"""
    print("🚀 Quick Start for Gitgremlin GitHub Commit Bot")
    print("=" * 50)
    
    # Create .env file
    create_env_file()
    
    print("\n📋 Next Steps:")
    print("1. Get a GitHub token:")
    print("   - Go to: https://github.com/settings/tokens")
    print("   - Click 'Generate new token (classic)'")
    print("   - Select 'repo' scope")
    print("   - Copy the token")
    print()
    print("2. Edit .env file:")
    print("   - Open .env file in a text editor")
    print("   - Replace 'your_github_token_here' with your actual token")
    print()
    print("3. Test the bot:")
    print("   - Run: python test_bot.py")
    print("   - Then: python commit_bot.py --test")
    print()
    print("4. Run the bot:")
    print("   - Run: python commit_bot.py")
    print()
    print("🔗 Your repository: https://github.com/nikhil-shr-23/Gitgremlin")
    print("💡 The bot will create commits at 9:00 AM, 3:30 PM, and 9:45 PM daily")

if __name__ == "__main__":
    main()
