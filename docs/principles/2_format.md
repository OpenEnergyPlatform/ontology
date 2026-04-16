# 2. Common Format

## Summary
The ontology is made available in a common formal language in an accepted concrete syntax.

## Purpose
The purpose of this principle is to allow the maximum number of people to access and reuse an ontology.

## Implementation
- ENERO Foundry ontologies MUST be provided in at least one OWL product
- Developers are free to use whatever combination of technologies and formats is appropriate for development. However, the official OWL PURL for the ontology MUST resolve to a syntactically valid OWL file using the [RDF-XML](https://www.w3.org/TR/rdf-syntax-grammar/) syntax.
- Developers MAY produce ontologies in other formats, e.g.:
    - Common Logic  
    - OWL or OWL2 concrete syntax
    - OWL2-XML                               
    - OWL2-Manchester Syntax          
    - Turtle
- The filename for the ontology SHOULD be the ontology prefix.

## Examples
- The [Open Energy Ontology](https://openenergyplatform.org/ontology/) is maintained as omn-Format. It is automatically converted to OWL and is available in both OWL2-Manchester Syntax (oeo.omn) and OWL (oeo-full.owl). The ontology's prefix "oeo" is used in the filenames.
- The [ChEBI ontology](https://www.ebi.ac.uk/chebi/) is maintained in a relational database using a custom schema, but makes an OBO-Format file available that is automatically converted to OWL. It is available in both OBO and OWL via the OBO Foundry.

## Counter-Examples
An ontology that is ONLY in Frames format, OWL/XML, or OWL Manchester Syntax.
