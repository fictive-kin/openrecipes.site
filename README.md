# Open Recipes web site

This is the web site for the Open Recipes project. It uses Flask, Flask-FlatPages, and Frozen-Flask to generate static HTML content.

## Previewing during dev:

    python openrecipes.py

## Building the static site

    # this will output the site into the /build directory
    python openrecipes.py build

## Adding pages

Put a file in the `/pages` directory with a name like `file-name.md` extention. The page will be served as HTML from the path `/file-name/`

## Deploying the site

Make sure to regen the site:

	python openrecipes.py build

Then we deploy with the script in `deploy.example.sh`. You'll want to copy this to `deploy.sh` and modify the `STATICSITES_REPO_PATH` variable.
