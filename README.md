# GitHub Daily Commit Bot 🤖

An automated Python bot that creates daily commits to maintain your GitHub contribution streak. This bot helps you maintain a consistent presence on GitHub by automatically generating meaningful commits.

## Features ✨

- 🕒 **Automated Scheduling**: Runs commits at multiple times throughout the day
- 🎲 **Random Content**: Generates varied commit messages and content
- 🔍 **Smart Detection**: Avoids duplicate commits on the same day
- 🔐 **Secure**: Uses GitHub tokens for authentication
- 🧪 **Test Mode**: Allows immediate testing before scheduling
- 📁 **Organized**: Creates structured contribution files

## Setup Instructions 🚀

### Prerequisites

- Python 3.6 or higher
- Git installed on your system
- A GitHub account with a personal access token

### 1. Clone or Download

```bash
git clone <your-repo-url>
cd commit-creator
```

### 2. Run Setup Script

```bash
python setup.py
```

This will:
- Install required dependencies
- Create a `.env` file from the template
- Initialize a git repository
- Create an initial commit

### 3. Configure GitHub Credentials

Edit the `.env` file with your GitHub information:

```env
GITHUB_TOKEN=your_personal_access_token_here
GITHUB_USERNAME=your_github_username
GITHUB_REPO=your_repo_name
REPO_OWNER=your_username_or_org_name
```

#### Getting a GitHub Token:

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name like "Commit Bot"
4. Select scopes: `repo` (full control of private repositories)
5. Click "Generate token"
6. Copy the token and paste it in your `.env` file

### 4. Create GitHub Repository

1. Create a new repository on GitHub
2. Add it as a remote:

```bash
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
```

### 5. Test the Bot

```bash
python commit_bot.py --test
```

This will create a test commit immediately to verify everything works.

### 6. Run the Bot

```bash
python commit_bot.py
```

The bot will now run continuously and create commits at:
- 9:00 AM
- 3:30 PM
- 9:45 PM

## Usage 📖

### Running the Bot

```bash
# Run normally (scheduled commits)
python commit_bot.py

# Test mode (immediate commit)
python commit_bot.py --test
```

### Stopping the Bot

Press `Ctrl+C` to stop the bot gracefully.

## Configuration ⚙️

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GITHUB_TOKEN` | Your GitHub personal access token | `ghp_xxxxxxxxxxxx` |
| `GITHUB_USERNAME` | Your GitHub username | `johndoe` |
| `GITHUB_REPO` | Repository name | `my-commit-bot` |
| `REPO_OWNER` | Repository owner (username or org) | `johndoe` |

### Scheduling

The bot creates commits at three different times during the day:
- **9:00 AM**: Morning commit
- **3:30 PM**: Afternoon commit  
- **9:45 PM**: Evening commit

This ensures you have contributions throughout the day and helps maintain your streak even if you miss a day.

## How It Works 🔧

1. **Smart Detection**: The bot checks if you already have commits today to avoid duplicates
2. **Content Generation**: Creates unique markdown files with timestamps and random content
3. **Git Operations**: Adds, commits, and pushes changes to your repository
4. **Error Handling**: Gracefully handles network issues and git errors

## File Structure 📁

```
commit-creator/
├── commit_bot.py          # Main bot script
├── setup.py              # Setup script
├── requirements.txt      # Python dependencies
├── .env.example         # Environment template
├── .env                 # Your configuration (create this)
├── contributions/       # Generated contribution files
└── README.md           # This file
```

## Troubleshooting 🔧

### Common Issues

**"Missing required environment variables"**
- Make sure your `.env` file exists and has all required variables
- Check that variable names match exactly

**"Failed to push to GitHub"**
- Verify your GitHub token has the correct permissions
- Check that the repository exists and you have push access
- Ensure your internet connection is stable

**"Could not check today's commits"**
- This is usually a network issue
- The bot will still try to create commits, but may create duplicates

**Bot stops unexpectedly**
- Check the console output for error messages
- Verify all dependencies are installed correctly
- Make sure your `.env` file is properly configured

### Getting Help

If you encounter issues:

1. Check the console output for error messages
2. Verify your `.env` configuration
3. Test with `--test` flag first
4. Check GitHub repository permissions

## Security Notes 🔒

- **Never commit your `.env` file** - it contains sensitive information
- Keep your GitHub token secure and don't share it
- Consider using environment variables in production
- Regularly rotate your GitHub tokens

## Legal Notice ⚖️

This bot is for educational and personal use. Make sure you comply with:
- GitHub's Terms of Service
- Your local laws and regulations
- Your organization's policies (if applicable)

## Contributing 🤝

Feel free to submit issues and enhancement requests!

## License 📄

This project is open source and available under the [MIT License](LICENSE).
