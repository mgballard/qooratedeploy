# Deploying the Brubeck Qoorate Server

This document cover deploying mongrel2 and the [qoorateserver](https://github.com/qoorate/qoorateserver) application.
The goal of the deployment directory is that once you have the requirements satisfied, you can drop and run it from anywhere 
It has been written and tested on Linodes Ubuntu-11.10 32-bit installation.

NOTE: This is a private repo and usernames and passwords are included in the configuration!

The following is assumed for the instructions and configuration to work:

*   MySQL is installed
*   The data for Qoorate is loaded in a database called `qoorate`
*   The username and password is qoorate:Q00rate
*   Apache (or any other web server) is installed and listening to port 8081
*   A user `deploy` exist with a default bash shell and sudoer capabilities
*   The server is named beta.qrate.co
create the user with bash as the default shell

    $ sudo useradd deploy -m -s /bin/bash

give them a nice strong, but easy to remember, password (Don't use deploy ...)

    $ sudo passwd deploy

add them to sudo (only needed for the installation)

    $ sudo adduser deploy sudo

# Installing dependancies

1.  Login as `deploy`

2.  Run the script [install.sh](https://github.com/qoorate/qooratedeploy/scripts/install.sh)

        $ sudo install.sh

3.  Build `procer`

    Procer is a samll utility bundled, but not compiled, with Mongrel2.
    For more information on using `procer` and deployment of Mongrel2 see [Mongrel2 docs - Chapter 4](http://mongrel2.org/static/book-finalch5.html)

        $ cd ~/src/mongrel2-1.7.5/examples/procer
        $ make clean all && sudo make install
        $ sudo chown -R deploy:deploy ~/

   Procer does one thing, and well, it makes sure the processes you need running stay up and running.

# Moving qoorateserver and qooratedeploy source to server
It is not recommended to have deploy pull code directly from github. Instead it is better to pull to the staging server, or your local machine, and rsynch the files to the production server.

I cloned the reposiories in the following manner:

    $ cd ~/src
    $ git clone git@github.com:qoorate/qoorateserver.git
    $ git clone git@github.com:qoorate/qooratedeploy.git

NOTE: This assumes git has been properly set up for your user and you have pull access to the private repositories.

So, once you have those repositories on another computer, perform the following from that computer.

    $ rsync -r ~/src/qooratedeploy deploy@beta.qrate.co:src
    $ rsync -r ~/src/qoorateserver deploy@beta.qrate.co:src

# Creating the deployment directory

The deployment directory will contain the static files to serve, settings and templates.

1.  Copy the deployment directory from qooratedeploy

        $ cp -R ~/src/qooratedeploy/deployment ~/

2.  Copy our static files from qoorateserver

        $ cp -R ~/src/qoorateserver/static ~/deployment/apps/qoorateserver

3.  Copy our template files from qoorateserver

        $ cp -R ~/src/qoorateserver/templates ~/deployment/apps/qoorateserver

# Cleaning up
1.  Make sure all files in `/home/deploy` are owned by deploy

        $ sudo chown -R deploy:deploy ~/

2.  Make sure one directoy is owned by root

        $ sudo chown -R root:root ~/deployment/profiles/mongrel2

    NOTE: This allows procer to `chown` to `/home/deploy/deployment`

# Starting the server
There are two scripts that have been written to start/stop the server:

        $ ~/deployment/qoorate-start
        $ ~/deployment/qoorate-kill
    
These scripts need to be run with `sudo`, but do not need to be run by `deploy`