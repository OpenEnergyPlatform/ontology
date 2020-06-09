#!/bin/bash

out=$1

OEO_VERSION=`cat ../../../VERSION`

if [[ -z $out ]]; then
    out="out"
fi

function convert {

    filepath=$1
    ontology=$2
    version=$3
    target_extension=$4
    primary=$5

    if [[ $version == OEO_VERSION ]] ; then
        version="$OEO_VERSION"
    fi

    fullfilename=$(basename -- "$filepath")
    extension="${fullfilename##*.}"
    filename="${fullfilename%.*}"
    
    target_path=$out/$ontology/$version
    if [[ $primary == n ]]; then
        target_path=$target_path/modules
    fi
    mkdir -p $target_path
    if [[ ! $extension == $target_extension ]]; then
        robot convert --input $filepath --output $target_path/$filename.$target_extension --format $target_extension
    else
        cp $filepath $target_path/$filename.$extension
    fi
}



cat pack.conf | while read -r line ; do
    linearr=($line)
    path=${linearr[0]}
    ontology=${linearr[1]}
    primary=${linearr[2]}
    version=${linearr[3]}
    formats=${linearr[4]}
    
    if [[ ! $path == \#* ]] && [ ! -z "$line" ]; then
        IFS=','
        read -a formatarr <<< "$formats"
        for format in ${formats}; do
            convert ../../../$path $ontology $version $format $primary
        done
        IFS=' '
    fi
done
