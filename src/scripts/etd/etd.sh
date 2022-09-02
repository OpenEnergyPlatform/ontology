#!/bin/bash
SCRIPT_PATH="$PWD"
ONTO_PATH="$(dirname "$(dirname "$SCRIPT_PATH")")""/ontology/"
robot merge --input "$ONTO_PATH""edits/oeo-model.omn" \
            --input "$ONTO_PATH""edits/oeo-physical.omn" \
            --input "$ONTO_PATH""edits/oeo-shared.omn" \
            --input "$ONTO_PATH""edits/oeo-social.omn" \
            --include-annotations true \
    export  --header "ID|LABEL|definition" \
            --prefix "OEO: http://openenergy-platform.org/ontology/oeo/OEO_" \
            --sort "LABEL" \
            --export "$ETD_PATH""etd.csv"
LINE1="|ID|Name|Definition|"
LINE2="|:-|:---|:-------|"
echo $LINE1 >> ETD.md
echo $LINE2 >> ETD.md
while IFS=, read -r rec1 rec2 rec3
do
    echo "|$rec1|$rec2|$rec3|" >> ETD.md
done < <(tail -n +2 etd.csv)
rm etd.csv