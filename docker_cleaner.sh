#!/bin/sh

usage () {
    echo "Usage:\n\t sh docker_cleaner.sh <option>\n"
    echo "Options: \n"
    echo "\t-S, --soft\tSoft docker cleanup. Stopped containers, unused images, volumes \n\t\t\tand networks not related to running containers will be deleted.\n"
    echo "\t-H, --hard\tHard docker cleanup. All containers will be stopped. \n\t\t\tAll containers, volumes and networks will be deleted.\n"
    echo "\t-h, --help\tThis help.\n"
}

soft_cleanup() {
    echo "Soft cleanup selected!\n"
    echo "Stopped containers, unused images, volumes \nand networks not related to running containers will be deleted.\n"
    read -p "Are you sure? (y/N) " yn
    case "$yn" in
        y|Y )
            echo "Start soft cleanup!"
            docker system prune -a -f 2> /dev/null
            echo "Soft cleanup finished!"
            ;;
        * ) 
            echo "Soft cleanup canceled!"
            ;;
    esac
}

hard_cleanup() {
    echo "Hard cleanup selected!\n"
    echo "All containers will be stopped. \nAll containers, volumes and networks will be deleted.\n"
    read -p "Are you sure? (y/N) " yn
    case "$yn" in
        y|Y )
            echo "Start hard cleanup!"
            docker stop $(docker ps -a -q) 2> /dev/null
            docker rm $(docker ps -a -q) 2> /dev/null
            docker rmi --force $(docker images -a -q) 2> /dev/null
            docker volume rm $(docker volume ls -q) 2> /dev/null
            docker network rm $(docker network ls -q) 2> /dev/null
            echo "Hard cleanup finished!"
            ;;
        * ) 
            echo "Hard cleanup canceled!"
            ;;
    esac
}

case "$1" in
    -S|--soft ) soft_cleanup ;;
    -H|--hard ) hard_cleanup ;;
    * ) usage ;;
esac