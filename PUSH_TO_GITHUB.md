# Instructions to Push to GitHub

Your files are already committed locally. Follow these steps to push to GitHub:

## Step 1: Create a New Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `emotion-detection-app` (or any name you prefer)
3. Description: "Flask emotion detection application using Watson NLP"
4. Choose **Public** or **Private**
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

## Step 2: Add Remote and Push

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add your GitHub repository as remote (replace YOUR_USERNAME with 'dietfizzy')
git remote add origin https://github.com/dietfizzy/emotion-detection-app.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**OR if you prefer SSH:**

```bash
git remote add origin git@github.com:dietfizzy/emotion-detection-app.git
git branch -M main
git push -u origin main
```

## Alternative: Using GitHub CLI (if you have it installed)

```bash
gh repo create emotion-detection-app --public --source=. --remote=origin --push
```

## After Pushing

Once pushed, you can clone it in your IBM IDE using:

```bash
git clone https://github.com/dietfizzy/emotion-detection-app.git
```

