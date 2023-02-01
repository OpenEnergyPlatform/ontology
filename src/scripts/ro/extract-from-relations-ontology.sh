# Download the RO
curl -L http://purl.obolibrary.org/obo/ro.owl > ro-full-download.owl
# Extract the terms we want with hierarchy
robot merge --input ro-full-download.owl extract --method MIREOT --lower-terms ro-extract-w-hierarchy.txt --intermediates all --output ro-extracted-w-hierarchy.owl
# Extract the terms we want without hierarchy
robot merge --input ro-full-download.owl extract --method MIREOT --lower-terms ro-extract-n-hierarchy.txt --upper-term owl:topObjectProperty --intermediates none --output ro-extracted-n-hierarchy.owl
# Create Extracted module
robot merge --input ro-extracted-w-hierarchy.owl --input ro-extracted-n-hierarchy.owl annotate --ontology-iri http://openenergy-platform.org/ontology/oeo/imports/ro-extracted.owl --version-iri http://openenergy-platform.org/ontology/oeo/dev/imports/ro-extracted.owl --annotation rdfs:comment "This file contains externally imported content from the Relations Ontology (RO) for import into the Open Energy Ontology (OEO). It is automatically extracted using ROBOT from the list of selected terms (ro-extract-w-hierarchy.txt, ro-extract-n-hierarchy.txt) located in the OEO-repository." --output ../../ontology/imports/ro-extracted.owl
# Remove inSubset axioms
robot remove --input ../../ontology/imports/ro-extracted.owl --term oboInOwl:inSubset --output ../../ontology/imports/ro-extracted.owl
# Remove subclass axioms from BFO classes
robot remove --input ../../ontology/imports/ro-extracted.owl --term BFO:0000002 --select "self descendants" --select "<http://purl.obolibrary.org/obo/BFO_*>"   --axioms subclass --signature true --exclude-term BFO:0000040 --preserve-structure false --output ../../ontology/imports/ro-extracted.owl
# Remove annotations from BFO classes
# This is kaputt, makes the annotations appear twice. 
# robot remove --input ../../ontology/imports/ro-extracted.owl --term BFO:0000002 --term BFO:0000004 --term BFO:0000040 --select "self"  --exclude-term RO:0002577 --exclude-term BFO:0000050 --axioms annotation --signature true --preserve-structure false --output ../../ontology/imports/ro-extracted.owl

rm ro-full-download.owl
rm ro-extracted-w-hierarchy.owl
rm ro-extracted-n-hierarchy.owl
