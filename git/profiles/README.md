# Git Profiles

If you want to have different account setup for e.x. Work and Personal projects you can do something like:

## SSH keys

- Generate keys like:

```bash
ssh-keygen -f ~/.ssh/id_rsa_<profile_name> -t ed25519 -C "email@example.com"
```

Remember to connect them with you Github account.

## Create Profiles

- Create directory (or choose where you want them to have), and create files:
- `~/.git_profiles/<profile_name>.gitconfig`:

```bash
[user]
  name = Github Account Name
  email = email@example.com
[core]
  sshCommand = ssh -i ~/.ssh/id_rsa_<profile_name> -F /dev/null
```

## Use Profiles

- Create `~/.gitconfig`
- Setup users like:

```bash
[includeIf "gitdir:~/Code/Personal/"]
  path = ~/.git_profiles/<profile_name>.gitconfig
[includeIf "gitdir:~/Code/Work/"]
  path = ~/.git_profiles/<another_profile_name>.gitconfig
```

It will use profile in all subdirectories
