#!/usr/bin/env python3
"""
Diagnostic script to troubleshoot GitHub repository connection issues
"""

import os
import sys
from github import Github
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_github_token():
    """Test if GitHub token is valid"""
    print("🔑 Testing GitHub token...")
    
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ No GITHUB_TOKEN found in .env file")
        return False
    
    if token == "your_github_token_here":
        print("❌ GITHUB_TOKEN is still set to placeholder value")
        print("💡 Please replace 'your_github_token_here' with your actual GitHub token")
        return False
    
    try:
        github = Github(token)
        user = github.get_user()
        print(f"✅ Token is valid! Connected as: {user.login}")
        return True
    except Exception as e:
        print(f"❌ Token is invalid: {e}")
        return False

def test_repository_access():
    """Test repository access"""
    print("\n🔍 Testing repository access...")
    
    token = os.getenv('GITHUB_TOKEN')
    username = os.getenv('GITHUB_USERNAME', 'nikhil-shr-23')
    repo_name = os.getenv('GITHUB_REPO', 'Gitgremlin')
    repo_owner = os.getenv('REPO_OWNER', 'nikhil-shr-23')
    
    print(f"Repository: {repo_owner}/{repo_name}")
    
    try:
        github = Github(token)
        repo = github.get_repo(f"{repo_owner}/{repo_name}")
        print(f"✅ Repository access successful!")
        print(f"   Full name: {repo.full_name}")
        print(f"   Private: {repo.private}")
        print(f"   URL: {repo.html_url}")
        
        # Check if repository is empty
        try:
            commits = list(repo.get_commits())
            if not commits:
                print("📝 Repository is empty (no commits yet)")
            else:
                print(f"📊 Repository has {len(commits)} commits")
        except Exception as e:
            print(f"📝 Repository appears to be empty: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Repository access failed: {e}")
        return False

def test_environment():
    """Test environment configuration"""
    print("\n⚙️  Testing environment configuration...")
    
    required_vars = ['GITHUB_TOKEN', 'GITHUB_USERNAME', 'GITHUB_REPO', 'REPO_OWNER']
    
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            print(f"❌ {var} is not set")
        elif value == "your_github_token_here" and var == "GITHUB_TOKEN":
            print(f"❌ {var} is still set to placeholder")
        else:
            print(f"✅ {var}: {value}")

def main():
    """Run all diagnostics"""
    print("🔧 GitHub Commit Bot - Diagnostic Tool")
    print("=" * 50)
    
    # Test environment
    test_environment()
    
    # Test token
    token_valid = test_github_token()
    
    # Test repository access
    if token_valid:
        repo_access = test_repository_access()
    else:
        repo_access = False
    
    print("\n" + "=" * 50)
    print("📊 Diagnostic Results:")
    
    if token_valid and repo_access:
        print("🎉 Everything looks good! The bot should work.")
        print("💡 Try running: python commit_bot.py --test")
    else:
        print("💥 Issues found. Please fix the problems above.")
        
        if not token_valid:
            print("\n🔧 To fix token issues:")
            print("1. Go to https://github.com/settings/tokens")
            print("2. Generate new token (classic)")
            print("3. Select 'repo' scope")
            print("4. Copy token and update .env file")
        
        if not repo_access and token_valid:
            print("\n🔧 To fix repository issues:")
            print("1. Make sure the repository exists")
            print("2. Check repository name and owner")
            print("3. Ensure your token has access to the repository")

if __name__ == "__main__":
    main()
