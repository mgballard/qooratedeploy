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

    create the user with bash as the default shell
        $ sudo useradd deploy -m -s /bin/bash

    give them a nice strong, but easy to remember, password (Don't use deploy ...)
        $ sudo passwd deploy
 
    add them to sudo (only needed for the installation)
        $ sudo adduser deploy sudo

# Installing dependancies
1. Login as `deploy`
2. Run the script [install.sh](https://github.com/qoorate/qoorateserver)
    $ sudo install.sh
3. Build `procer`
   Procer is a samll utility bundled, but not compiled, with Mongrel2.
   For more information on using `procer` and deployment of Mongrel2 see [Mongrel2 docs - Chapter 4](http://mongrel2.org/static/book-finalch5.html)
       $ cd ~/src/mongrel2-1.7.5/examples/procer
       $ make clean all && sudo make install
   Procer does one thing, and well, it makes sure the processes you need running stay up and running.
   
# Creating the deployment directory
    
# Starting the server