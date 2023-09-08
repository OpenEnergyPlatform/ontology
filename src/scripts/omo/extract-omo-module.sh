# Download the OMO release from 2023-08-23
curl -L http://purl.obolibrary.org/obo/omo/releases/2023-08-23/omo.owl > omo-full-download.owl
# Extract the terms we want with hierarchy
robot merge --input omo-full-download.owl extract --method MIREOT --lower-terms omo-w-hierarchy.txt --intermediates all --output omo-module-temp.owl
# add xmlns:obo="http://purl.obolibrary.org/obo/"
#sed -i 's/xmlns:owl/xmlns:obo="http:\/\/purl.obolibrary.org\/obo\/"\
#     xmlns:owl/' omo-module-temp.owl
# Annotates the output with a commentary to the origin of the content
robot annotate --input omo-module-temp.owl --annotation rdfs:comment "This file contains externally imported content from the OBO Metadata Ontology (OMO) for import into the Open Energy Ontology (OEO). It is automatically extracted using ROBOT." --output ../../ontology/imports/omo-extracted.owl
# Annotates each axiom with the ontology IRI, using prov:wasDerivedFrom
robot annotate --input ../../ontology/imports/omo-extracted.owl --annotate-derived-from true --annotate-defined-by true --output ../../ontology/imports/omo-extracted.owl
# Annotate with new ontology information
robot annotate --input ../../ontology/imports/omo-extracted.owl  --ontology-iri http://openenergy-platform.org/ontology/imports/omo-extracted.owl --version-iri http://openenergy-platform.org/ontology/imports/omo-extracted.owl --output ../../ontology/imports/omo-extracted.owl

rm omo-full-download.owl
rm omo-module-temp.owl
