# Download current UO release
curl -L https://raw.githubusercontent.com/bio-ontology-research-group/unit-ontology/master/uo.owl > uo-full-download.owl
# Extract the terms we want with hierarchy
robot merge --input uo-full-download.owl extract --method MIREOT --lower-terms uo-w-hierarchy.txt --intermediates all --output uo-module-temp.owl
# add xmlns:obo="http://purl.obolibrary.org/obo/"
sed -i 's/xmlns:owl/xmlns:obo="http:\/\/purl.obolibrary.org\/obo\/"\
     xmlns:owl/' uo-module-temp.owl
# Replace "<rdfs:comment>" with "obo:IAO_0000115" 
sed -i 's/<rdfs:comment>/<obo:IAO_0000115>/g' uo-module-temp.owl
# Replace "<rdfs:comment>" with "</obo:IAO_0000115>"
sed -i 's/<\/rdfs:comment>/<\/obo:IAO_0000115>/g' uo-module-temp.owl
# Annotates the output with a commentary to the origin of the content
robot annotate --input uo-module-temp.owl --annotation rdfs:comment "This file contains externally imported content from the Unit Ontology (UO) for import into the Open Energy Ontology (OEO). It is automatically extracted using ROBOT." --output ../../ontology/imports/uo-extracted.owl
# Annotates each axiom with the ontology IRI, using prov:wasDerivedFrom
robot annotate --input ../../ontology/imports/uo-extracted.owl --annotate-derived-from true --annotate-defined-by true --output ../../ontology/imports/uo-extracted.owl
# add 'definition' label to IAO_0000115
sed -i "33s/.*/        <rdfs:label>definition<\/rdfs:label>/" ../../ontology/imports/uo-extracted.owl
# Annotate with new ontology information
robot annotate --input ../../ontology/imports/uo-extracted.owl  --ontology-iri http://openenergy-platform.org/ontology/imports/uo-extracted.owl --version-iri http://openenergy-platform.org/ontology/imports/uo-extracted.owl --output ../../ontology/imports/uo-extracted.owl

rm uo-full-download.owl
rm uo-module-temp.owl
