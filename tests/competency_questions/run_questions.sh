#!/bin/bash

COMMAND=$1
MERGED=$2
EXPECTED_RESULT=$3

INFER="q2.omn q3.omn q4.omn q5.omn q6.omn q7.omn q8.omn q9.omn q10.omn q11.omn q12.omn q13.omn q14.omn q15.omn q16.omn q17.omn q18.omn q19.omn q20.omn q21.omn q22.omn q23.omn q24.omn q25.omn q26.omn q27.omn q28.omn q30.omn q31.omn q32.omn q33.omn q34.omn q35.omn q36.omn q37.omn q38.omn q39.omn q40.omn q41.omn q51.omn "
NON_INFERABLE_BUT_SHOULD="q42.omn q43.omn q44.omn q46.omn q47.omn q48.omn q49.omn q50.omn"
DONT_INFER="q1.omn q29.omn q45.omn"

if [ "$EXPECTED_RESULT" = "true" ]
then
    LIST=$INFER
else
    LIST=$DONT_INFER
fi

PWD=$(pwd)

for file in $LIST
do
    echo "Infer $file"
    FULLCOMMAND="$COMMAND --premise=file:$MERGED --conclusion=file:$PWD/tests/competency_questions/$file -E"
    echo "$FULLCOMMAND"
    RESULT=$($FULLCOMMAND)
    if [ "$RESULT" != "$EXPECTED_RESULT" ]
    then
        echo "Inference failed for $file"
        echo "Output: $RESULT"
        exit 1
    fi
done