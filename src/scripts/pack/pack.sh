#!/bin/bash

out=$1

if [[ -z $out ]]; then
    out="out"
fi

function convert {

    filepath=$1
    fullfilename=$(basename -- "$filepath")
    extension="${fullfilename##*.}"
    target_extension=$2
    filename="${fullfilename%.*}"
    mkdir -p $out/$filename 
    if [[ ! $extension == $target_extension ]]; then
        robot convert --input $filepath --output $out/$filename/$filename.$target_extension --format $target_extension
    else
        cp $filepath $out/$filename/$filename.$extension
    fi
}

function convert_all {

    echo $1 $2

}

cat pack.conf | while read -r line ; do
    linearr=($line)
    path=${linearr[0]}
    formats=${linearr[1]}
    if [[ ! $path == \#* ]] && [ ! -z "$line" ]; then
        IFS=','
        read -a formatarr <<< "$formats"
        for format in ${formats}; do
            convert ../../../$path $format
        done
        IFS=' '
    fi
done
