#!/bin/bash

function capturar_noticias() {
    cd /home/wesley/Myprojects/blogscraper/scraperNews/spiders/
    scrapy runspider tecmundo.py --nolog
    cd /home/wesley/Myprojects/blogscraper
    django 
    git init
    git remote add origin git@github.com:wesleyolvr/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}