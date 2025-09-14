#!/usr/bin/env python3
"""
Test script for GitHub Commit Bot
This script helps test the bot functionality without making actual commits.
"""

import os
import sys
from datetime import datetime

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config

def test_configuration():
    """Test if configuration is properly set up"""
    print("🧪 Testing configuration...")
    
    try:
        Config.validate()
        print("✅ Configuration is valid")
        print(f"   Username: {Config.GITHUB_USERNAME}")
        print(f"   Repository: {Config.REPO_OWNER}/{Config.GITHUB_REPO}")
        print(f"   Commit times: {Config.COMMIT_TIMES}")
        return True
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("💡 Make sure your .env file is properly configured")
        return False

def test_dependencies():
    """Test if all required dependencies are installed"""
    print("\n🧪 Testing dependencies...")
    
    dependencies = [
        ('github', 'PyGithub'),
        ('schedule', 'schedule'),
        ('dotenv', 'python-dotenv')
    ]
    
    all_good = True
    for module, package in dependencies:
        try:
            __import__(module)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is not installed")
            all_good = False
    
    if not all_good:
        print("💡 Run: pip install -r requirements.txt")
    
    return all_good

def test_git_setup():
    """Test if git repository is properly set up"""
    print("\n🧪 Testing git setup...")
    
    # Check if git is initialized
    if not os.path.exists('.git'):
        print("❌ Git repository not initialized")
        print("💡 Run: git init")
        return False
    
    print("✅ Git repository is initialized")
    
    # Check if we have commits
    try:
        result = os.popen('git log --oneline -1').read().strip()
        if result:
            print(f"✅ Latest commit: {result}")
        else:
            print("⚠️  No commits found")
        return True
    except Exception as e:
        print(f"❌ Git error: {e}")
        return False

def test_github_connection():
    """Test GitHub API connection"""
    print("\n🧪 Testing GitHub connection...")
    
    try:
        from github import Github
        
        # Test token validity
        github = Github(Config.GITHUB_TOKEN)
        user = github.get_user()
        print(f"✅ Connected as: {user.login}")
        
        # Test repository access
        try:
            repo = github.get_repo(f"{Config.REPO_OWNER}/{Config.GITHUB_REPO}")
            print(f"✅ Repository access confirmed: {repo.full_name}")
            return True
        except Exception as e:
            print(f"❌ Repository access failed: {e}")
            print("💡 Check repository name and permissions")
            return False
            
    except Exception as e:
        print(f"❌ GitHub connection failed: {e}")
        print("💡 Check your GitHub token and network connection")
        return False

def main():
    """Run all tests"""
    print("🚀 GitHub Commit Bot - Test Suite")
    print("=" * 50)
    
    tests = [
        ("Configuration", test_configuration),
        ("Dependencies", test_dependencies),
        ("Git Setup", test_git_setup),
        ("GitHub Connection", test_github_connection)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test failed with error: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Your bot is ready to run.")
        print("💡 Run 'python commit_bot.py --test' to create a test commit")
    else:
        print("💥 Some tests failed. Please fix the issues above.")
        print("💡 Run 'python setup.py' to help with initial setup")

if __name__ == "__main__":
    main()
