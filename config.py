"""
Configuration settings for GitHub Commit Bot
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the bot"""
    
    # GitHub settings
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
    GITHUB_REPO = os.getenv('GITHUB_REPO')
    REPO_OWNER = os.getenv('REPO_OWNER')
    
    # Default values for your repository
    if not GITHUB_USERNAME:
        GITHUB_USERNAME = 'nikhil-shr-23'
    if not REPO_OWNER:
        REPO_OWNER = 'nikhil-shr-23'
    if not GITHUB_REPO:
        GITHUB_REPO = 'Gitgremlin'
    
    # Commit settings
    COMMIT_TIMES = ['09:00', '15:30', '21:45']  # Times to create commits
    CONTRIBUTIONS_DIR = 'contributions'  # Directory for contribution files
    
    # Commit message templates
    COMMIT_MESSAGES = [
        "Update daily progress",
        "Add new feature implementation", 
        "Fix minor bugs",
        "Improve code structure",
        "Update documentation",
        "Refactor existing code",
        "Add new tests",
        "Optimize performance",
        "Update dependencies",
        "Clean up code",
        "Add error handling",
        "Improve user interface",
        "Update configuration",
        "Add new functionality",
        "Fix typos in comments",
        "Update README",
        "Add code examples",
        "Improve code readability",
        "Update project structure",
        "Add logging functionality"
    ]
    
    @classmethod
    def validate(cls):
        """Validate that all required configuration is present"""
        required_vars = [
            'GITHUB_TOKEN',
            'GITHUB_USERNAME', 
            'GITHUB_REPO',
            'REPO_OWNER'
        ]
        
        missing_vars = []
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True
