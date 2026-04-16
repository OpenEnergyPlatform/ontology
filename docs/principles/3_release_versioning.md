# 3. Release and Versioning

## Summary
A versioning and release workflow is mandatory.
It must document changes made, the date of publication, and the version number.
The workflow itself should also be documented and publicly accessible.

## Purpose
Ontologies change throughout their lifecycle, and users need to be aware when and
what changes have occurred. Since ontology changes are typically made incrementally
and infrequently, versioning provides the mechanism to distinguish between states of
an ontology over time. Publication ensures that new versions are findable and
accessible to all users and downstream systems.

## Implementation

### Release
ENERO Foundry ontologies MUST be made available with a stable and persistent identifier (IRI).<br>
The published IRI of an ontology MUST remain stable across versions.

Ontologies SHOULD be made available in a repository on a version control platform (e.g. GitHub, GitLab).

Ontologies SHOULD be made available in an ontology repository or terminology service (e.g. TIB TS, technoportal).<br>
This is recommended for discoverability within the broader ontology community.

### Versioning
ENERO Foundry ontologies MUST use a versioning workflow that publishes new ontology versions and documents:
- Changes made in each version (e.g. as a CHANGELOG.md)
- Date of version publication
- Version number

Developers MAY use either a semantic versioning format (SemVer) or a calendar versioning format (CalVer). 
ENERO Foundry recommends using SemVer. 
Guidance on the differences between these two formats can be found at [glinteco](https://glinteco.com/en/post/understanding-semver-vs-calver-making-the-right-choice-for-your-project/)
Ontologies MUST have the license annotation properties:
- The annotation `owl:versionInfo` to identify the version number.
- The annotation `owl:versionIRI` identify the versioned resource.

The versioning workflow for each ontology SHOULD be documented and publicly available.

### Publication Frequency
No fixed release schedule is mandated, as the appropriate frequency will vary
depending on the covered domain, the stage of development, and available resources.
However, ontology developers SHOULD:
- Communicate the expected maintenance status and release cadence in the
  ontology's documentation.
- Signal clearly if an ontology is in active development or maintenance-only mode.

Publication frequency is considered an indicator of active maintenance and is
implicitly linked to the **Collaboration and Responsiveness** principle: long
periods without releases or communication may indicate that an ontology is
outdated or no longer supported.
