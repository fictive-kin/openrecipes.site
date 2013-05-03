#!/usr/bin/env bash
# a simple, and kind of dumb, bash script to get the site deployed
#

# you probably want to change this
STATICSITES_REPO_PATH="/Users/foo/Sites/fk-staticsites"

# probably shouldn't change this
OR_PATH=$STATICSITES_REPO_PATH"/sites/openrecip.es/"

echo "> cd ./build"
cd ./build
echo "> cp -vR * $OR_PATH"
cp -vR * "$OR_PATH"
echo "> cd $OR_PATH"
cd "$OR_PATH"
echo "> git checkout master"
git checkout master
echo "> git commit -a -m \"new build\""
git commit -a -m "new build"
echo "> git push origin master"
git push origin master
echo "> git checkout production"
git checkout production
echo "> git merge master"
git merge master
echo "Now `git push origin production` to deploy"
