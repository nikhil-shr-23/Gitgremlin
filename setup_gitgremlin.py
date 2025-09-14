#!/usr/bin/env python3
"""
Setup script specifically for Gitgremlin repository
This script sets up the bot for the nikhil-shr-23/Gitgremlin repository
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def setup_gitgremlin():
    """Setup specifically for Gitgremlin repository"""
    print("🚀 Setting up GitHub Commit Bot for Gitgremlin repository...")
    print("=" * 60)
    
    # Create .env file with correct values
    env_content = """GITHUB_TOKEN=your_github_token_here
GITHUB_USERNAME=nikhil-shr-23
GITHUB_REPO=Gitgremlin
REPO_OWNER=nikhil-shr-23"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env file with Gitgremlin repository settings")
    
    # Initialize git if not already done
    if not os.path.exists('.git'):
        commands = [
            ("git init", "Initializing git repository"),
            ("git branch -M main", "Setting default branch to main"),
        ]
        
        for command, description in commands:
            if not run_command(command, description):
                return False
    
    # Add remote origin
    remote_url = "https://github.com/nikhil-shr-23/Gitgremlin.git"
    run_command(f"git remote add origin {remote_url}", "Adding GitHub remote")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Setup completed for Gitgremlin repository!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your GitHub token")
    print("2. Test the bot: python commit_bot.py --test")
    print("3. Run the bot: python commit_bot.py")
    print("\n🔑 To get a GitHub token:")
    print("   - Go to GitHub Settings → Developer settings → Personal access tokens")
    print("   - Generate new token (classic) with 'repo' scope")
    print("   - Copy token and paste in .env file")
    
    return True

if __name__ == "__main__":
    setup_gitgremlin()
