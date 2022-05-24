#!/bin/bash
. ./src/vars.py
hash_name=$($RANDOM | md5sum | head -c 5; echo;)
build_tag=test_$hash_name
docker build . -t hello:$build_tag
docker run --rm -d --name $build_tag -p $external_port:8000 hello:$build_tag
sleep 10s
url='http://localhost:'$external_port
if nc -z localhost 8000 ; then
    echo "Server is running [+]"
    content=$(curl -L localhost:8000)
    if [ "b$content" = "$http_message" ] ; then
        echo "Server prints right message [+]"
        echo "build is sucssessful"
        if [ -z "$1" ]
        then
            docker build . -t immushroom/hello
        else
            docker build . -t immushroom/hello:$1 -t immushroom/hello
        fi

    else
        echo "Server prints right message [-]"
        echo "Build is failed"
    fi
else
    echo "Server is running [-]"
    echo "Build is failed"
fi
docker stop $build_tag
docker image rmi hello:$build_tag