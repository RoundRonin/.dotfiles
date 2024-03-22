#
# This script is suitable for a case git email on the machine was wrong 
# And there were some commits in your OWN (single-contributor) repo under that wrong email
#
# In other words, github_reforestation for your activity field.
#
# Shamelessly stolen from https://medium.com/@gracet37/how-to-link-past-commits-to-the-correct-user-on-github-44a90533905a
#
#!/bin/sh
PROJECT="__________"
git clone --bare git@github.com:RoundRonin/${PROJECT}.git
cd ${PROJECT}.git

git filter-branch --env-filter '
OLD_EMAIL="_________"
CORRECT_NAME="________"
CORRECT_EMAIL="_________"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags

git push --force --tags origin 'refs/heads/*'

cd ..
rm -rf ${PROJECT}.git
