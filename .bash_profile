d=$(date +%Y-%m-%d-%H:%M:%S)
echo "$d"
cd /Users/OwenPeng/nyc-ds-111819-lectures/
git fetch upstream
git merge upstream/master -m "$d"
git push

