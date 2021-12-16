# the first argument to be passed is the commit msg
git add ${@:2}
git commit -m "$1"
git push
