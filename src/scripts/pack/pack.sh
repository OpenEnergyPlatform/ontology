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

    if [[ $version == OEO_VERSION ]] ; then
        version="$OEO_VERSION"
    fi

    fullfilename=$(basename -- "$filepath")
    extension="${fullfilename##*.}"
    filename="${fullfilename%.*}"
    mkdir -p $out/$ontology/$version
    if [[ ! $extension == $target_extension ]]; then
        robot convert --input $filepath --output $out/$ontology/$version/$filename.$target_extension --format $target_extension
    else
        cp $filepath $out/$ontology/${version}/$filename.$extension
    fi
}



cat pack.conf | while read -r line ; do
    linearr=($line)
    path=${linearr[0]}
    ontology=${linearr[1]}
    version=${linearr[2]}
    formats=${linearr[3]}
    if [[ ! $path == \#* ]] && [ ! -z "$line" ]; then
        IFS=','
        read -a formatarr <<< "$formats"
        for format in ${formats}; do
            convert ../../../$path $ontology $version $format
        done
        IFS=' '
    fi
done
