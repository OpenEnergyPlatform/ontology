# Note: For consistent results run with ROBOT v1.91 or higher
# Download the IAO release from 2022-11-07
curl -L https://raw.githubusercontent.com/information-artifact-ontology/IAO/v2022-11-07/iao.owl > iao-full-download.owl
# Extract the terms we want with hierarchy, This removes the domain of IAO_0000136
robot merge --input iao-full-download.owl extract --method MIREOT --lower-terms iao-w-hierarchy.txt --intermediates all --output iao-module-temp.owl
# Remove subclass axioms from BFO classes
robot remove --input iao-module-temp.owl --term BFO:0000001 --select "self descendants" --select "<http://purl.obolibrary.org/obo/BFO_*>"   --axioms subclass --axioms annotation --signature true --exclude-term BFO:0000031 --preserve-structure false --output iao-module-temp.owl
# Extract domain of IAO_0000136
robot merge --input iao-full-download.owl filter --term http://purl.obolibrary.org/obo/IAO_0000136 --term rdfs:domain --term http://purl.obolibrary.org/obo/IAO_0000030 --select self  --axioms all --signature false   --output iao-extracted-domain.owl
# Extracted module
robot merge  --input iao-module-temp.owl --input iao-extracted-domain.owl --output ../../ontology/imports/iao-extracted.owl
# Remove subproperty axioms
robot remove --input  ../../ontology/imports/iao-extracted.owl --axioms subproperty --output  ../../ontology/imports/iao-extracted.owl
# Annotates the output with a commentary to the origin of the content
robot annotate --input ../../ontology/imports/iao-extracted.owl --annotation rdfs:comment "This file contains externally imported content from the Information Artifact Ontology (IAO) for import into the Open Energy Ontology (OEO). It is automatically extracted using ROBOT." --output ../../ontology/imports/iao-extracted.owl
# Annotates each axiom with the ontology IRI, using prov:wasDerivedFrom
robot annotate --input ../../ontology/imports/iao-extracted.owl --annotate-derived-from true --annotate-defined-by true --output ../../ontology/imports/iao-extracted.owl
# Annotate with new ontology information
robot annotate --input ../../ontology/imports/iao-extracted.owl  --ontology-iri http://openenergy-platform.org/ontology/oeo/imports/iao-extracted.owl --version-iri http://openenergy-platform.org/ontology/oeo/dev/imports/iao-extracted.owl --output ../../ontology/imports/iao-extracted.owl
rm iao-full-download.owl
rm iao-extracted-domain.owl
rm iao-module-temp.owl