# 6. Ontology Scope

## Summary
The scope of an ontology is the extent of the domain or subject matter it intends to cover. The ontology must have a clearly specified scope and content that adheres to that scope.

## Purpose
A well-defined scope allows to decide whether a requested term should be part of an ontology or be reused from another ontology. A fairly narrow scope supports orthogonality and prevents overlaps between ontologies (duplication of terms). From the user perspective, it facilitates searches for specific content, and enables quick selection of ontologies of interest.

## Implementation
- The scope SHOULD be defined fairly narrow. 
- The domain (scope) covered by the ontology MUST be clearly stated. 
    - The statement SHOULD be brief, free of jargon and written in a way that people outside the domain are able to understand it.
- The content of the ontology SHOULD stay within the confines of the stated scope. 
- Required terms that are out of scope SHOULD be imported from the appropriate ontology, unless no such ontology exists and there is an immediate need for an out-of-scope term (or set thereof). We encourage the ontology maintainers to create a shareable file with such terms so that the community can access, reuse, edit, and add these new terms as new ontologies with the intended scope are developed.
Out-of-scope terms should be placed within a separate module that can be imported/exported as a single unit. Generic terms must be maintained with community needs in mind. 

## Examples
Examples how to describe and document the scope of an ontology:

- Write a short abstract about the scope
- Provide a list of sample competency questions

Example how to collect generic scope-independent terms:

- OBO creates the [COB ontology](https://github.com/OBOFoundry/COB) to provide a reusable resource for terms that are too broad for a specific domain ontology
