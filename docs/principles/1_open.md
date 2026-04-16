# 1. Openness
## Summary
The ontology must be openly available to be used by all without any constraints other than <br>
(a) its origin must be acknowledged, and <br>
(b) it is not to be altered and subsequently redistributed in altered form under the original name or with the same identifiers.

## Purpose
ENERO Foundry ontologies are resources intended for reuse and interoperability among energy-related domains and communities. An explicitly stated copyright license clearly stating the acceptable use reduces legal risks for users and promotes use and reuse. Therefore, the ontologies must be available to all without any constraint on their use or redistribution.

## Implementation
- ENERO Foundry ontologies MUST
    - be released under a **public domain** mark or **permissive open license**
    - have an [OSI approved](https://opensource.org/licenses) or [open definition approved](https://opendefinition.org/licenses/api/) open license
- ENERO Foundry ontologies MAY use one of the following suitable open licenses:
    - Public domain under [Creative Commons CC0 1.0 Universal (CC0-1.0)](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en) or equivalent.
    - A permissive software license under [MIT License (MIT)](https://opensource.org/license/mit) or [BSD 3-Clause "New" or "Revised" License (BSD-3-Clause)](https://opensource.org/license/BSD-3-Clause) or equivalent.
    - The **dual license** “CC0 1.0 OR MIT” or equivalent. (We encourage this option, as it reflects the dual nature of ontologies as both databases and software.)
- ENERO Foundry ontologies MAY but SHOULD NOT use the [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/legalcode.en) (see [discussion](https://opensource.stackexchange.com/questions/9242/why-does-creative-commons-recommend-not-using-cc-by-licenses-for-software)).
- The license MUST be clearly stated using the `dcterms:license` annotation property (http://purl.org/dc/terms/license) followed by the URL representing the license (e.g. https://creativecommons.org/publicdomain/zero/1.0/legalcode.en) in the ontology file of any publicly released OWL version of the ontology.
- Any ENERO Foundry ontology reusing individual terms from another ontology SHOULD
    - reuse the original terms' IRI, and
    - use an `IAO:imported from` annotation (http://purl.obolibrary.org/obo/IAO_0000412) on each imported term to link back to the group (i.e. ontology) maintaining it, where more information would be available about the license include any annotations for term or definition editors from the original ontology.

## Examples
- An [OWL example](https://oboacademy.github.io/obook/reference/formatting-license/) displaying the proper inclusion of a license in an ontology file.
- Example usage of the `dcterms:license` annotation property with the MIT license URL: <br>
`<dcterms:license rdf:datatype="&xsd;anyURI">[http://opensource.org/licenses/MIT</dcterms:license](http://opensource.org/licenses/MIT%3c/dcterms:license)>`
