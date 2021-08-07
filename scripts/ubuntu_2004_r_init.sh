#!/bin/bash
# Package setup for Ubuntu 20.04
# https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-20-04
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo apt install -y software-properties-common
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
sudo apt update
sudo apt install -y r-base libcurl4-openssl-dev libssl-dev libxml2-dev

# Update pandoc to recent, for Panflute
curl -L https://github.com/jgm/pandoc/releases/download/2.14.1/pandoc-2.14.1-1-amd64.deb -o pandoc.deb
sudo dpkg --install pandoc.deb
