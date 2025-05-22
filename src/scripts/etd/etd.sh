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
    export  --header "LABEL|ID|definition" \
            --prefix "OEO: https://openenergyplatform.org/ontology/oeo/OEO_" \
            --sort "LABEL" \
            --export "$ETD_PATH""etd.xlsx"
python3 etd.py
rm etd.xlsx