#!/bin/bash
if [ -e ETD.md ]
then
    rm ETD.md
fi
SCRIPT_PATH="$PWD"
ONTO_PATH="$(dirname "$(dirname "$SCRIPT_PATH")")""/ontology/"
robot merge --input "$ONTO_PATH""oeo.omn" \
            --input "$ONTO_PATH""edits/oeo-model.omn" \
            --input "$ONTO_PATH""edits/oeo-physical.omn" \
            --input "$ONTO_PATH""edits/oeo-shared.omn" \
            --input "$ONTO_PATH""edits/oeo-social.omn" \
            --include-annotations true \
    export  --header "ID|LABEL|definition" \
            --prefix "OEO: http://openenergy-platform.org/ontology/oeo/OEO_" \
            --sort "LABEL" \
            --export "$ETD_PATH""etd.csv"
LINE1="|PREFIX:ID|Name|Definition|"
LINE2="|:--------|:---|:---------|"
echo $LINE1 >> ETD.md
echo $LINE2 >> ETD.md
while read -r line
do
    STRING="|"
    j=true
    for (( i=0; i<${#line}; i++ )); do
        CHAR="${line:$i:1}"
        if [ "$CHAR" = "\"" ]
        then
            # negate j
            if $j
            then
                j=false
            else
                j=true
            fi
            echo "$STRING"
            echo $j
        fi
        if [ "$CHAR" = "," ] && $j
        then
            STRING="$STRING""|"
        else   
            STRING="$STRING""$CHAR"
        fi
    done
    echo "$STRING""|" >> ETD.md
done < <(tail -n +2 etd.csv)
rm etd.csv