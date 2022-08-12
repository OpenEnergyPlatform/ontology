curl -L http://purl.obolibrary.org/obo/ro.owl > ro-full-download.owl

robot merge --input ro-full-download.owl extract --method MIREOT --lower-terms ro-extracted-w-hierarchy.txt --intermediates all --output ro-extracted-w-hierarchy.owl

robot merge --input ro-full-download.owl extract --method MIREOT --lower-terms ro-extracted-n-hierarchy.txt --upper-term owl:topObjectProperty --intermediates none --output ro-extracted-n-hierarchy.owl

robot merge --input ro-extracted-w-hierarchy.owl --input ro-extracted-n-hierarchy.owl annotate --ontology-iri http://openenergy-platform.org/ontology/oeo/imports/ro-module.owl --version-iri http://openenergy-platform.org/ontology/oeo/dev/imports/ro-module.owl --annotation rdfs:comment "This file contains externally imported content from the Relations Ontology (RO) for import into the Open Energy Ontology (OEO). It is automatically extracted using ROBOT from the term list ro-terms.txt." --output ../../ontology/imports/ro-extracted.owl

robot remove --input ro-extracted.owl --term oboInOwl:inSubset --output ro-extracted.owl


rm ro-full-download.owl
rm ro-extracted-w-hierarchy.owl
rm ro-extracted-n-hierarchy.owl
