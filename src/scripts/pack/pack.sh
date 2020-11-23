#!/bin/bash

out=$1

OEO_VERSION=`cat ../../../VERSION`

if [[ -z $out ]]; then
    out="out"
fi

function convert {

    filepath=$1
    type=$2
    target_extension=$3

    fullfilename=$(basename -- "$filepath")
    extension="${fullfilename##*.}"
    filename="${fullfilename%.*}"
    
    target_path=$out/oeo/$OEO_VERSION
    if [[ ! $type == main ]]; then
        target_path=$target_path/$type
    fi
    mkdir -p $target_path
    if [[ ! $extension == $target_extension ]]; then
        echo "robot convert --input $filepath --output $target_path/$filename.$target_extension --format $target_extension"
        robot convert --input $filepath --output $target_path/$filename.$target_extension --format $target_extension
        if [[ $extension == omn && $target_extension == owl ]]; then
            sed -i -E "s/(http:\/\/openenergy-platform\.org\/ontology\/oeo\/releases\/(v[0-9]+\.[0-9]+\.[0-9]+)\/([A-z-]+)\.)omn/\1owl/m" $target_path/$filename.owl
        fi
    else
        cp $filepath $target_path/$filename.$extension
    fi
}



cat pack.conf | while read -r line ; do
    linearr=($line)
    path=${linearr[0]}
    type=${linearr[1]}
    formats=${linearr[2]}
    
    if [[ ! $path == \#* ]] && [ ! -z "$line" ]; then
        IFS=','
        read -a formatarr <<< "$formats"
        for format in ${formats}; do
            convert ../../../$path $type $format
        done
        IFS=' '
    fi
done
