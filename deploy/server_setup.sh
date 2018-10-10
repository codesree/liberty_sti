#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/codesree/liberty_sti.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git


mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/liberty_sti

mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/tag_env

$VIRTUALENV_BASE_PATH/tag_env/bin/pip install -r $PROJECT_BASE_PATH/liberty_sti/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/liberty_sti

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/liberty_sti/deploy/supervisor_api_tag.conf /etc/supervisor/conf.d/api_tag.conf
supervisorctl reread
supervisorctl update
supervisorctl restart api_tag

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/liberty_sti/deploy/nginx_api_tag.conf /etc/nginx/sites-available/api_tag.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/api_tag.conf /etc/nginx/sites-enabled/api_tag.conf
systemctl restart nginx.service

echo "DONE! :)"