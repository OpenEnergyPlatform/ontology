#!/bin/bash

COMMAND=$1
MERGED=$2
EXPECTED_RESULT=$3

INFERABLE="q1.omn q2.omn q3.omn q4.omn q5.omn q6.omn q7.omn q8.omn q9.omn q10.omn q11.omn q12.omn q13.omn q14.omn q15.omn q16.omn q17.omn q18.omn q23.omn q24.omn q26.omn q27.omn q28.omn q29.omn q30.omn q31.omn q32.omn q33.omn q34.omn q35.omn q36.omn q37.omn q38.omn q39.omn q40.omn q41.omn"
NON_INFERABLE="q19.omn q20.omn q21.omn q22.omn q25.omn"

PWD=$(pwd)

for file in $INFERABLE
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