<!--
SPDX-FileCopyrightText: Open Energy Ontology (OEO) <https://github.com/OpenEnergyPlatform/ontology/>
SPDX-License-Identifier: CC0-1.0 OR MIT
-->

<a href="https://openenergyplatform.org/"><img align="right" width="200" height="200" src="https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4" alt="OpenEnergyPlatform"></a>

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-green.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/mit)
[![REUSE](https://api.reuse.software/badge/github.com/OpenEnergyPlatform/ontology)](https://api.reuse.software/info/github.com/OpenEnergyPlatform/ontology)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/OpenEnergyPlatform/ontology)
![Coverage Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/areleu/6d00affa9fbc89c79684d62091d96551/raw/open_energy_ontology__heads_feature-1419-competency-question-coverage-report.json)

# Open Energy Family - Open Energy Ontology (OEO)

Developing a common ontology for the domain of energy system analysis.

## Introduction

The **Open Energy Ontology (OEO)** is a domain ontology of the energy system analysis context. It is developed as part of the [Open Energy Family](https://github.com/OpenEnergyPlatform). The OEO is published on GitHub under an open source license. The language used is the Manchester OWL Syntax, which was chosen because it is user-friendly for editing and viewing differences of edited files. The OEO is constantly being extended. The first version of the OEO has been released on June 11th 2020. A Steering Committee (OEO-SC) was created to accompany the development, increase awareness of the ontology and include it in current projects.

## Scope of this ontology

This domain ontology is a collaborative effort to represent the context of **energy system analysis** based on standard terminologies used by human experts in this field of research. It is designed to improve transparency and facilitate comparability and transferability of energy system modelling and scenario analysis. This ontology makes use of the Basic Formal Ontology ([BFO](https://github.com/OpenEnergyPlatform/ontology/wiki/BFO-Upper-Ontology-Classes)) and its principles. It re-uses several other ontologies as described in the [GitHub Wiki](https://github.com/OpenEnergyPlatform/ontology/wiki/use-of-external-ontologies).

## License / Copyright

This repository is **dual-licensed** under [Creative Commons Zero v1.0 Universal (CC0-1.0)](https://creativecommons.org/publicdomain/zero/1.0/legalcode) or [MIT License (MIT)](https://opensource.org/license/mit). <br>
You can choose between one of them if you use this work. <br>

## Citation

For **scientific citation** of this ontology, please refer to the [CITATION.cff](CITATION.cff) file. <br>
If you cite this work in a publication, please reference the following article: <br>
Booshehri, Meisam, et al. "Introducing the Open Energy Ontology: Enhancing data interpretation and interfacing in energy systems analysis."
Energy and AI 5 (2021): 100074. [10.1016/j.egyai.2021.100074](http://dx.doi.org/10.1016/j.egyai.2021.100074)

To cite a specific class of the ontology and its definition please use the following convention:
> 'class label' (FUll-URI) from the [Open Energy Ontology (OEO)](https://github.com/OpenEnergyPlatform/ontology)

Example:
> 'energy system' (https://openenergyplatform.org/ontology/oeo/OEO_00030024) from the [Open Energy Ontology (OEO)](https://github.com/OpenEnergyPlatform/ontology)


## Releases and installation

The latest version of the OEO can be accessed on the [Open Energy Platform](https://openenergyplatform.org/ontology/oeo) and the [Master Branch](https://github.com/OpenEnergyPlatform/ontology/tree/master). <br>
All released versions can be downloaded directly from the [GitHub Releases](https://github.com/OpenEnergyPlatform/ontology/releases/). <br>
The currently developed version is available on the default [dev Branch](https://github.com/OpenEnergyPlatform/ontology/).

The source code of the ontology is found in the folder `src/ontology/` <br>
The main file is `src/ontology/oeo.omn` <br>

All own modules are collected in the folder `src/ontology/edits/` <br>
The following diagram illustrates the modular file structure of the OEO. It depicts the import and file hierarchy from external imports (right) to the main file oeo.omn (left).
![grafik](https://github.com/user-attachments/assets/13e25c6e-aa15-4be5-9b81-df58fc097e48)


The imported modules are under `src/ontology/imports/` <br>
To get an overview of the existing modules, take a look at the following wiki article: [GitHub Wiki](https://github.com/OpenEnergyPlatform/ontology/wiki/Modules-of-the-OEO)
We recommend to use the software [Protégé](https://protege.stanford.edu/) to open and edit the ontology. Additionally, an ontology viewer is available on the [Open Energy Platform](https://openenergyplatform.org/viewer/oeo/).


## Collaboration
This is an interdisciplinary open source project, help is always welcome. <br>
Everyone with good intentions is invited to develop this repository.

The development of the ontology happens mainly on [GitHub](https://github.com/OpenEnergyPlatform/ontology) and is supplemented by regular (online) [developer meetings](https://github.com/OpenEnergyPlatform/ontology/wiki/oeo-dev-meeting-plan) to review the progress and discuss more complicated topics. <br>
If you would like to participate in meetings you can become a team member. Use the [OEP contact form](https://openenergyplatform.org/contact/) and [add yourself as a contributor](https://github.com/OpenEnergyPlatform/ontology/wiki/Add-yourself-as-a-contributor) after approval.
<br><br>
If you're new to GitHub or ontologies check out our ["How to participate"](https://github.com/OpenEnergyPlatform/ontology/wiki/Welcome!-How-to-participate) article for some first advice and helpful links. You may also use the [Open Energy Academy course](https://openenergyplatform.github.io/academy/courses/05_ontology/#how-to-become-an-oeo-developer) to get used to the necessary tools and background information.
<br>
The workflow is described in the [CONTRIBUTING.md](https://github.com/OpenEnergyPlatform/ontology/blob/dev/CONTRIBUTING.md) file. Please check it out before you start working on this project. Points that are not clear in the file can be discussed in a [GitHub Issue](https://github.com/OpenEnergyPlatform/ontology/issues/new/choose).
Please read the [GitHub Wiki](https://github.com/OpenEnergyPlatform/ontology/wiki) for more information about the ontology, its standards, its best practice principles and the BFO classification.
<br><br>
Wiki articles that you would be most helpful to a beginner are:
- [How to Participate](https://github.com/OpenEnergyPlatform/ontology/wiki/Welcome!-How-to-participate)
- [Best Practice Principles](https://github.com/OpenEnergyPlatform/ontology/wiki/Best-Practice-Principles) including subsections
- [BFO Upper Ontology](https://github.com/OpenEnergyPlatform/ontology/wiki/BFO-Upper-Ontology-Classes) including subsections
- [Explanation on Mass Nouns](https://github.com/OpenEnergyPlatform/ontology/wiki/Explanation-on-mass-nouns)
- [Handeling Ambiguous Terms](https://github.com/OpenEnergyPlatform/ontology/wiki/Handling-ambiguous-terms)
- [Use Protégé to Change the Ontology](https://github.com/OpenEnergyPlatform/ontology/wiki/How-to-use-prot%C3%A9g%C3%A9-to-change-the-ontology)
- [Term Tracker Annotation](https://github.com/OpenEnergyPlatform/ontology/wiki/Term-Tracker-Annotation)
<br>

... as well as the [CONTRIBUTING.md](https://github.com/OpenEnergyPlatform/ontology/blob/dev/CONTRIBUTING.md)

 
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
    - Members of the [Steering Committee (OEO-SC)](https://openenergyplatform.org/ontology/oeo-steering-committee/)
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
