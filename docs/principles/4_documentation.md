# 4. Ontology Documentation

## Summary
These principles provide a collection of required and recommended documentation about the ontology and its items.
Parts of the documentation should be embedded within the ontology ('in situ'), other parts could be located outside the ontology ('external'). The documentation considers both the overall ontology and the documentation per notion, i.e. of single ontology item.

## Purpose
Documentation can serve multiple purposes: It can allow a potential user to easily ascertain whether the ontology is of value to their domain of effort. It can aid developers in correcting, modifying, or extending the ontology. It can serve as a criterion for assessing its quality.

## Implementation
### In situ documentation on the overall ontology
Each ontology MUST document the following information within the ontology:

- Scope (see also principle on [scope](6_scope.md))
- Assumptions (if any)
- Copyright/License (see also principle on [openness](1_open.md))
- Version (see also principle on [versioning](5_version.md))
- Creator(s)
- Maintainer(s) contact information (see also principle on [responsiveness](10_collaboration.md))
- Location of external ontology documentation 

### In situ documentation per notion
Each ontology MUST document the following information within the ontology:

- a unique label (see also principle on [naming conventions](7_naming.md))
- a natural language definition (see also principle on [textual definitions](8_definitions.md))
- additional sources used in the creation of particular notions or terms

### External documentation on the overall ontology
Each ontology MUST document the following information, potentially outside the ontology:

- Details about the ontology’s raison d’etre, requirements, its coverage or context, or assumptions
- Any additional sources (e.g., standards) used in the creation of the ontology
- Instructions for submitting change requests
- User guides

Each ontology SHOULD document the following information, potentially outside the ontology:

- Use cases or user stories
- Published papers, project websites, repositories
- Diagrams or examples of use of the ontology
- Competency questions or queries (in a query language)
- Processes or tools used in the development of the ontology
- Which reasoner is recommended
- Recommendation: indicate which documentation is developer-specific or user-specific
- Recommendation: publish external documentation with permanent identifiers

### Usage of AI
Based on the [principle about the usage of AI](11_ai_usage.md), the support of AI methods and tools in the ontology development process MUST be documented.
