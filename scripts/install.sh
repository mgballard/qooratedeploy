#!/bin/bash
##
## This installs what is needed to run qoorateserver
## server on a production box
##
## Create a user first 
## $ sudo useradd deploy -m -s /bin/bash
## $ sudo passwd deploy
## 
## add them to sudo only for installation
## $ sudo adduser deploy sudo
##
## Should use virtualenv to sandbox the python packages needed
## Doesn't yet
##


###
### Settings
###

ZMQ_VERSION="zeromq-2.1.10"
MONGREL2_VERSION="mongrel2-1.7.5"
PREV_DIR=$PWD
SRC_DIR=$HOME/src


###
### Directory Structures
###

if [ ! -d $SRC_DIR ]; then
    mkdir $SRC_DIR 
fi


###
### This script must be run with sudo
###

###
### System Depenencies
###

apt-get -y install \
    python-dev \
    python-pip \
    libsqlite3-dev \
    sqlite3 \
    libevent-dev \
    libev4 \
    git \
    uuid-dev \
    libtool \
    autoconf \
    libzmq-dev \
    build-essential \
    ragel \
    redis-server \
    privbind \
    libjpeg8 \
    libjpeg62-dev \
    libfreetype6 \
    libfreetype6-dev
    

##
##Gave up on virtualenv for now
##wasn't playing nice with procer
##
## Set up out pip virtual env
##

sudo pip install virtualenv
sudo pip install virtualenvwrapper


mkdir /home/deploy/.virtualenvs

export WORKON_HOME="/home/deploy/.virtualenvs"
. $(which virtualenvwrapper.sh)

mkvirtualenv --no-site-packages qooratedeploy

workon qooratedeploy

## place them in .bashrc so they are always there
echo export WORKON_HOME="~/.virtualenvs" >> /home/deploy/.bashrc
echo source $(which virtualenvwrapper.sh) >> /home/deploy/.bashrc


###
### ZeroMQ
###

cd $SRC_DIR

if [ ! -d $ZMQ_VERSION ]; then
    wget http://download.zeromq.org/$ZMQ_VERSION.tar.gz 
    tar zxf $ZMQ_VERSION.tar.gz
    cd $ZMQ_VERSION
    ./autogen.sh
    ./configure && make && make install
fi

ldconfig # update library cache


###
### Mongrel2
###

cd $SRC_DIR
##if [ ! -d $MONGREL2_VERSION ]; then
if [ ! -d $MONGREL2_VERSION ]; then
    wget http://mongrel2.org/static/downloads/$MONGREL2_VERSION.tar.bz2
    tar jxf $MONGREL2_VERSION.tar.bz2
    cd $MONGREL2_VERSION
    make && make install
fi


###
### pip install gevent_zeromq==0.2.2
### at the moment we must build this from source for ubuntu 11.10
###

cd $SRC_DIR
if [ ! -d "gevent-zeromq" ]; then
    git clone https://github.com/traviscline/gevent-zeromq.git
    cd gevent-zeromq
    python ./setup.py install
fi

sudo ldconfig

##
## For now we need the bleeding edge Brubeck
##
## pip install brubeck==0.3.7

cd $SRC_DIR
if [ ! -d "brubeck" ]; then
    git clone https://github.com/j2labs/brubeck.git
    cd brubeck

    ### Install Brubeck's dependencies
    pip install -I -r envs/brubeck.reqs

    ### Concurrency already handled with gevent + zeromq

    ### Install Brubeck itself
    python ./setup.py install
    cd ../..
fi

##
## When procer is run securely root is used to start apps, 
## you need to activate the qooratedeploy virtualenv in the run file
##

pip install Cython==0.15.1
pip install Jinja2==2.6
pip install Mako==0.5.0
pip install dictshield==0.3.6
pip install py-bcrypt==0.2
pip install pymongo==2.1
pip install python-dateutil==2.0
pip install pyzmq==2.1.11
pip install ujson==1.15
pip install greenlet==0.3.2
pip install gevent==0.13.6
pip install gevent_zeromq==0.2.2
pip install brubeck==0.3.7
pip install BeautifulSoup==3.2.1
pip install requests==0.10.6
pip install boto==2.2.2
pip install redis==2.4.11
pip install PyMySQL==0.5
pip install python-magic==0.4.2

sudo ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib 
sudo ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/lib
sudo ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib

pip install PIL==1.1.7

###
### Brubeck Packages
###
pip install brubeck-oauth==0.0.9
pip install brubeck-uploader==0.0.9
pip install brubeck-mysql==0.0.9


