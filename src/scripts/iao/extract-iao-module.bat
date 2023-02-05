robot ^
merge ^ Rem Merging from the...
    --input iao.owl ^ 
extract ^ Rem ...chosen axioms...
    --method MIREOT ^ 
    --branch-from-term "http://purl.obolibrary.org/obo/IAO_0000030" ^ 
annotate ^ Rem ...annotated with the certain references...
    --ontology-iri http://open-energy-ontology.org/ontology/imports/iao-module.owl ^
    --version-iri http://open-energy-ontology.org/ontology/imports/iao-module.owl ^
    --annotation rdfs:comment "This file contains externally imported content from the Information Artifact Ontology (IAO) for import into the Open Energy Ontology (OEO). It is automatically extracted using ROBOT." ^
    --annotate-derived-from true ^ Rem ...into the iao-module.owl
    --output ../../ontology/imports/iao-module.owl 