# GitHub Publish Notes

Recommended repository name:

`upwork-automation-portfolio`

Recommended visibility:

Public, because this is meant to be shown to Upwork clients.

Recommended description:

`Portfolio samples for Python automation, public web data extraction, CSV cleanup, and AI workflow design.`

Current local repository state:

- Local path: `E:\codexwork\upwork-automation-portfolio`
- Branch: `master`
- Latest commits:
  - `d45b7f8 Add GitHub publishing notes`
  - `de5de9b Add Upwork automation portfolio samples`

After publishing, add the GitHub link to:

- Upwork profile linked accounts
- proposal messages for scraping / CSV / automation jobs
- follow-up messages when clients ask for examples

Suggested proposal line:

`I also have a small portfolio sample showing a public website to CSV workflow with source code and setup notes.`

Before publishing, confirm that the email/name in Git history are acceptable:

- Name: `Herry Fu`
- Email: `zhuzhu21210@gmail.com`

## Manual GitHub Publish Steps

1. Open GitHub and create a new empty repository.
2. Repository name: `upwork-automation-portfolio`
3. Visibility: Public
4. Do not initialize with README, `.gitignore`, or license because the local repo already has files.
5. After GitHub shows the new repository URL, run these commands locally:

```powershell
cd E:\codexwork\upwork-automation-portfolio
git remote add origin https://github.com/YOUR_USERNAME/upwork-automation-portfolio.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## If Codex Controls Chrome

If you explicitly confirm that Codex may create a public GitHub repository in
your logged-in GitHub account, Codex can use Chrome to create the empty repo
through the GitHub website. After that, Codex can add the remote and push from
the local repository.

## Current Publish Status

The public GitHub repository has been created:

`https://github.com/zhuzhu21210-commits/upwork-automation-portfolio`

The local remote has been configured:

```powershell
origin https://github.com/zhuzhu21210-commits/upwork-automation-portfolio.git
```

The local branch has been renamed to:

`main`

Remaining step:

GitHub push requires local Git authentication. Running `git push -u origin main`
without credentials currently fails with:

```text
fatal: could not read Username for 'https://github.com': terminal prompts disabled
```

The helper script at `E:\codexwork\publish_github_portfolio.ps1` can be used
after GitHub authentication is completed.
