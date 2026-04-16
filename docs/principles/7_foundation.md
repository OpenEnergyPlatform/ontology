# 7. Foundational Ontology

## Summary
We require either the use of BFO as a foundational ontology or a mapping to BFO's main structure.

## Purpose
Use of a foundational ontology provides the basis for ontological consistency and facilitates semantic interoperability. BFO is the preferred foundational ontology in the ENERO Foundry, since it is already widely used in OBO and IOF.

## Implementation

- ENERO Foundry ontologies MUST 
    - EITHER use [BFO](https://basic-formal-ontology.org/) as foundational ontology
    - OR provide a mapping to BFOs main structure
- Version BFO 2020 ([ISO/IEC 21838-2:202](https://www.iso.org/standard/74572.html)) SHOULD be used. However, if ontologies have chosen to use BFO 2.0 it is also compliant to this principle.
- ENERO Foundry ontologies SHOULD make use of existing mid-level / core ontologies like CCO or IAO
    - BFO 2020: https://standards.iso.org/iso-iec/21838/-2/ed-1/en/
    - BFO 2.0: https://ncorwiki.buffalo.edu/index.php/Basic_Formal_Ontology_2.0
    - CCO: https://www.ontologyrepository.com/
    - IAO: https://github.com/information-artifact-ontology/IAO
    - MENO: https://github.com/stap-m/midlevel-energy-ontology
    - SKOS: https://www.w3.org/2004/02/skos/

### Examples
- An example for a BFO mapping can be found here: [https://github.com/BFO-Mappings/PROV-to-BFO](https://github.com/BFO-Mappings/PROV-to-BFO)
