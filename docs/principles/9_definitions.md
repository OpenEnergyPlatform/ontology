# 9. Textual Definitions

## Summary
Definitions are required for ontology classes, preferably in [Aristotelian format](https://doi.org/10.7551/mitpress/9780262527811.003.0004). No two entities can have the same definition, and no entity can have multiple definitions.

## Purpose
ENERO Foundry ontologies are intended to provide a consensus view of a domain (to the extent possible) and the notions and terms used therein. As such they should be able to be used as a glossary for their domain.

Each entity provides a human-readable understanding about what is a member of the associated class. The textual definitions are, optimally, in concordance with associated machine-readable logical definitions.

Ultimately, humans will decide whether the notion or terms represented in an ontology are appropriate for their use. Therefore, an understanding (by humans) of a notion or term, its intent, and potential interpretations is required.

## Implementation
* All classes MUST and all relations SHOULD have a textual definition.
* Each definition MUST be unique.
* Each definition MUST be annotated with either `IAO:0000115` or `skos:definition` (consistent throughout the ontology).
* Each entity MUST NOT have more than one textual definition (annotated with `IAO:0000115` or `skos:definition`).
* Textual definitions SHOULD be given in [Aristotelian format](https://doi.org/10.7551/mitpress/9780262527811.003.0004).
