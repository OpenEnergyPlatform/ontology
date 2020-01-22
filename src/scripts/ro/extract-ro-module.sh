curl -L http://purl.obolibrary.org/obo/ro.owl > ro.owl

robot merge --input ro.owl extract --method MIREOT --lower-terms ro-extract.txt --intermediates all annotate --ontology-iri http://open-energy-ontology.org/ontology/imports/ro-module.owl --version-iri http://open-energy-ontology.org/ontology/imports/ro-module.owl --annotation rdfs:comment "This file contains externally imported content from the Relations Ontology (RO) for import into the Open Energy Ontology (OEO). It is automatically extracted using ROBOT from the term list ro-terms.txt." --output ../../ontology/imports/ro-module.owl

