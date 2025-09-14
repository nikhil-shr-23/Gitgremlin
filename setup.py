#!/usr/bin/env python3
"""
Setup script for GitHub Commit Bot
This script helps initialize the repository and set up the environment.
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

def setup_git_repo():
    """Initialize git repository if not already initialized"""
    if os.path.exists('.git'):
        print("✅ Git repository already initialized")
        return True
    
    commands = [
        ("git init", "Initializing git repository"),
        ("git add .", "Adding files to git"),
        ("git commit -m 'Initial commit: GitHub Commit Bot setup'", "Creating initial commit")
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    return True

def create_env_file():
    """Create .env file from template"""
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return True
    
    if not os.path.exists('env_example.txt'):
        print("❌ env_example.txt file not found")
        return False
    
    # Copy env_example.txt to .env
    with open('env_example.txt', 'r') as f:
        content = f.read()
    
    with open('.env', 'w') as f:
        f.write(content)
    
    print("✅ Created .env file from template")
    print("⚠️  Please edit .env file with your GitHub credentials")
    return True

def install_dependencies():
    """Install Python dependencies"""
    return run_command("pip install -r requirements.txt", "Installing Python dependencies")

def main():
    """Main setup function"""
    print("🚀 Setting up GitHub Commit Bot...")
    print("=" * 50)
    
    # Check if Python 3 is available
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        print("❌ Failed to create .env file")
        sys.exit(1)
    
    # Setup git repository
    if not setup_git_repo():
        print("❌ Failed to setup git repository")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file with your GitHub credentials")
    print("2. Create a GitHub repository")
    print("3. Add the repository as remote: git remote add origin <your-repo-url>")
    print("4. Test the bot: python commit_bot.py --test")
    print("5. Run the bot: python commit_bot.py")
    print("\n💡 Make sure to keep your GitHub token secure!")

if __name__ == "__main__":
    main()
