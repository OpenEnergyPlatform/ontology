# 8. Identifier and Naming Conventions

## Summary
Each entity in an ontology should contain an identifier (IRI/CURIE) and a label. The identifier is used to identify the entity anywhere it is cited/used. The label is used as its main name/title.

## Purpose
A consistent identifier format allows users to understand where a class term is defined, helps in creating interoperable ontologies, and aids in the development of software that uses the ontologies.

## Implementation
### Naming Conventions for Labels
- The annotation property `rdfs:label` MUST be used for the primary label for each entity.
- Primary labels SHOULD be as unambiguous as possible. Remember, your ontology may be used in a different context than that for which it was originally intended. Remember also of course that the label should be unambiguous without looking at parent terms.
- Each entity MUST have exactly one `rdfs:label` annotation.
- Labels MUST be unique within an ontology.
- Synonyms/alternative labels MAY be added, e.g. via the annotation property `IAO_0000118` (alternative term).
- Labels and synonyms SHOULD be written as if writing in plain English text:
    - Use spaces to separate words. Avoid extra spaces between words, or at the beginning or end of the label/synonym.
    - Only capitalize proper names (e.g. Parkinson's disease).
    - Do not use CamelCase.
    - do_not_use_underscores
- Abbreviations SHOULD be spelled out in the `rdfs:label` annotation. Abbreviations MAY be included as a separate property or synonym.
- Special characters (such as % or &) SHOULD NOT be used in the `rdfs:label` annotation. They MAY be included in synonyms.

### Naming Conventions for Identifiers
- Each entity MUST be given a unique IRI.
- Opaque identifiers SHOULD be used. This means that each IRI is an alpha-numeric identifier, in contrast to the natural language label. Tools like Ontology Lookup Services, Protégé etc. assist users with an automated translation to the human-readable label.

## Examples
### Labels and alternative labels/synonyms
Foundry-compliant annotation property usage for a "research and development grant" ontology entity:

- `rdfs:label` "research and development grant"
- `IAO_0000118` "research & development grant"
- `IAO_0000118` "R&D grant"

### Identifiers
- IRI: https://openenergyplatform.org/ontology/oeo/OEO_00360008 (energy balancing)
    - CURIE: [OEO:00360008](https://openenergyplatform.org/ontology/oeo/OEO_00360008)
- IRI: http://purl.obolibrary.org/obo/BFO_0000015 (process)
    - CURIE: [BFO:0000015](http://purl.obolibrary.org/obo/BFO_0000015)
