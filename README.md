<a href="https://openenergy-platform.org/"><img align="right" width="200" height="200" src="https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4" alt="OpenEnergyPlatform"></a>

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/OpenEnergyPlatform/ontology)

# Open Energy Family - Open Energy Ontology (OEO)

Developing a common ontology for the domain of energy system analysis.

## Introduction

The **Open Energy Ontology (OEO)** is a domain ontology of the energy system analysis context. It is developed as part of the [Open Energy Family](https://github.com/OpenEnergyPlatform). The OEO is published on GitHub under an open source license. The language used is the Manchester OWL Syntax, which was chosen because it is user-friendly for editing and viewing differences of edited files. The OEO is constantly being extended. The first version of the OEO has been released on June 11th 2020. A Steering Committee (OEO-SC) was created to accompany the development, increase awareness of the ontology and include it in current projects.

## Scope of this ontology

This domain ontology is a collaborative effort to represent the context of **energy system analysis** based on standard terminologies used by human experts in this field of research. It is designed to improve transparency and facilitate comparability and transferability of energy system modelling and scenario analysis. This ontology makes use of the Basic Formal Ontology ([BFO](https://github.com/OpenEnergyPlatform/ontology/wiki/BFO-Upper-Ontology-Classes)) and its principles. It re-uses several other ontologies as described in the [GitHub Wiki](https://github.com/OpenEnergyPlatform/ontology/wiki/use-of-external-ontologies).

## License / Copyright / Citation

This repository is licensed under `CC0 1.0 Universal (CC0 1.0) Public Domain Dedication`. <br>
For a scientific citation please see the [CITATION.cff](CITATION.cff). <br>

To cite a specific class of the ontology and its definition please use the following convention:
> 'class label' (FUll-URI) from the [Open Energy Ontology (OEO)](https://github.com/OpenEnergyPlatform/ontology)

Example:
> 'energy system' (https://openenergy-platform.org/ontology/oeo/OEO_00030024) from the [Open Energy Ontology (OEO)](https://github.com/OpenEnergyPlatform/ontology)


## Releases and installation

The latest version of the OEO can be accessed on the [Open Energy Platform](https://openenergy-platform.org/ontology/oeo) and the [Master Branch](https://github.com/OpenEnergyPlatform/ontology/tree/master). <br>
All released versions can be downloaded directly from the [GitGub Releases](https://github.com/OpenEnergyPlatform/ontology/releases/). <br>
The currently developed version is available on the default [dev Branch](https://github.com/OpenEnergyPlatform/ontology/).

The source code of the ontology is found in the folder `src/ontology/` <br>
The main file is `src/ontology/oeo.omn` <br>

All own modules are collected in the folder `src/ontology/edits/` <br>
The imported modules are under `src/ontology/imports/` <br>
We recommend to use the software [Protégé](https://protege.stanford.edu/) to open and edit the ontology. Additionally, an ontology viewer is available on the [Open Energy Platform](https://openenergy-platform.org/viewer/oeo/).


## Collaboration
This is an interdisciplinary open source project, help is always welcome. <br>
Everyone is invited to develop this repository with good intentions.

The development of the ontology happens mainly on [GitHub](https://github.com/OpenEnergyPlatform/ontology) and is supplemented by regular (online) developer meetings to review the progress and discuss more complicated topics. 

If you're new to GitHub or ontologies check out our ["How to participate"](https://github.com/OpenEnergyPlatform/ontology/wiki/Welcome!-How-to-participate) article for some first advice and helpful links.
The workflow is described in the [CONTRIBUTING.md](https://github.com/OpenEnergyPlatform/ontology/blob/dev/CONTRIBUTING.md) file. Please check it out before you start working on this project. Points that are not clear in the file can be discussed in a [GitHub Issue](https://github.com/OpenEnergyPlatform/ontology/issues/new/choose).
Please read the [GitHub Wiki](https://github.com/OpenEnergyPlatform/ontology/wiki) for more information about the ontology, its standards, its best practice principles and the BFO classification.
 
## Teams
Experts in ontology engineering, economy and energy-system modelling work together collaboratively.<br>
We combine domain knowledge with knowledge about how an ontology should be designed.

If you have a specific question about ontology design, energy system modelling or economy (in context of this ontology), you can [tag](https://github.com/OmahaGirlsWhoCode/OmahaGirlsWhoCode/wiki/How-to-tag-someone-in-a-pull-request) one of these teams (or persons) to notify its members that you need their feedback or help.

The OEO is organised in a general team and several [subteams](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-dev/teams):
 
- [@oeo-dev](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-dev)
    - All developers of the OEO

### Organisation

- [@oeo-community-manager](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-community-manager)
    - Contact point for personal and team related concerns
- [@oeo-concept-owner](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-concept-owner)
    - Strategic and long-term development and coordination of developers
- [@oeo-steering-committee](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-steering-committee)
    - Members of the [Steering Committee (OEO-SC)](https://openenergy-platform.org/ontology/oeo-steering-committee/)
- [@oeo-release-team](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-release-team)
    - Coordinates the periodic releases

### Domain Experts

- [@oeo-domain-expert-energy-modelling](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-domain-expert-energy-modelling)
    - Knowledge related to energy system modelling and simulation
- [@oeo-domain-expert-economy](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-domain-expert-economy)
    - Knowledge related to economic system, costs, monetary issues
- [@oeo-domain-expert-linked-open-data](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-domain-expert-linked-open-data)
    - Knowledge related to linked open data
- [@oeo-domain-expert-meteorology](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-domain-expert-meteorology)
    - Knowledge related to meteorology and weather

### Ontology experts

- [@oeo-general-expert-formal-ontology](https://github.com/orgs/OpenEnergyPlatform/teams/oeo-general-expert-formal-ontology)
    - Knowledge related to formal ontology expertise and BFO
