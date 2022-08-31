#!/bin/bash

########################################
#   ETD SCRIPT                         #
########################################

# Getting path variables

ETD_PATH="$PWD"
ONTO_PATH="$(dirname "$SCRIPT_PATH")""ontology"

#TODO: TEST

echo "$SCRIPT_PATH"
echo "$ONTO_PATH"

# Create exported CSV from ontology

robot merge --input "$ONTO_PATH""oeo.omn" \
            --input "$ONTO_PATH""edits/oeo-model.omn" \
            --input "$ONTO_PATH""edits/oeo-physical.omn" \
            --input "$ONTO_PATH""edits/oeo-shared.omn" \
            --input "$ONTO_PATH""edits/oeo-social.omn" \
            --include-annotations true \
    export  --header "ID|LABEL|iao:definition" \
            --export "$ETD_PATH""etd.csv"

#TODO: TEST

# Create directory with markdown

STRING="|ID|Name|Definition|\n|:--|:---:|----:|"

if ! [ -e ETD.md ];
then
    cat > etd.md
fi




while IFS="," read -r rec1 rec2 rec3;
do
    STRING="\n$STRING|$rec1|$rec2|$rec3|"
    echo "$STRING" >> ETD.md
done < etd.csv

#TODO: TEST

echo "$STRING"