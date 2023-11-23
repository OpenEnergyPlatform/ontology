
.. figure:: https://user-images.githubusercontent.com/14353512/185425447-85dbcde9-f3a2-4f06-a2db-0dee43af2f5f.png
    :align: left
    :target: https://github.com/rl-institut/super-repo/
    :alt: Repo logo

==========
ontology
==========


.. image:: https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4
   :align: right
   :width: 200
   :height: 200
   :alt: OpenEnergyPlatform
   :target: https://openenergy-platform.org/


.. image:: https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg
   :target: http://creativecommons.org/publicdomain/zero/1.0/

.. image:: https://img.shields.io/github/v/release/OpenEnergyPlatform/ontology

.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/areleu/6d00affa9fbc89c79684d62091d96551/raw/open_energy_ontology__heads_feature-1419-competency-question-coverage-report.json

.. list-table::
   :widths: auto

   * - License
     - |badge_license|
   * - Documentation
     - |badge_documentation|
   * - Publication
     -
   * - Development
     - |badge_issue_open| |badge_issue_closes| |badge_pr_open| |badge_pr_closes|
   * - Community
     - |badge_contributing| |badge_contributors| |badge_repo_counts|

.. contents::
    :depth: 2
    :local:
    :backlinks: top

Open Energy Family - Open Energy Ontology (OEO)
================================================

Developing a common ontology for the domain of energy system analysis.

Introduction
================================================

The **Open Energy Ontology (OEO)** is a domain ontology of the energy system analysis context. It is developed as part of the `Open Energy Family <https://github.com/OpenEnergyPlatform>`_. The OEO is published on GitHub under an open source license. The language used is the Manchester OWL Syntax, which was chosen because it is user-friendly for editing and viewing differences of edited files. The OEO is constantly being extended. The first version of the OEO was released on June 11th 2020. A Steering Committee (OEO-SC) was created to accompany the development, increase awareness of the ontology and include it in current projects.

Scope of this ontology
================================================

This domain ontology is a collaborative effort to represent the context of **energy system analysis** based on standard terminologies used by human experts in this field of research. It is designed to improve transparency and facilitate comparability and transferability of energy system modelling and scenario analysis. This ontology makes use of the Basic Formal Ontology (`BFO <https://github.com/OpenEnergyPlatform/ontology/wiki/BFO-Upper-Ontology-Classes>`_) and its principles. It re-uses several other ontologies as described in the `GitHub Wiki <https://github.com/OpenEnergyPlatform/ontology/wiki/use-of-external-ontologies>`_.

License / Copyright / Citation
================================================

This repository is licensed under `CC0 1.0 Universal (CC0 1.0) Public Domain Dedication <http://creativecommons.org/publicdomain/zero/1.0/>`_.
For a scientific citation please see the `CITATION.cff <CITATION.cff>`_ file.

To cite a specific class of the ontology and its definition please use the following convention:
> 'class label' (Full-URI) from the `Open Energy Ontology (OEO) <https://github.com/OpenEnergyPlatform/ontology>`_

Example:
> 'energy system' (`https://openenergy-platform.org/ontology/oeo/OEO_00030024 <https://openenergy-platform.org/ontology/oeo/OEO_00030024>`_) from the `Open Energy Ontology (OEO) <https://github.com/OpenEnergyPlatform/ontology>`_

Releases and installation
================================================

The latest version of the OEO can be accessed on the `Open Energy Platform <https://openenergy-platform.org/ontology/oeo>`_ and the `Master Branch <https://github.com/OpenEnergyPlatform/ontology/tree/master>`_.
All released versions can be downloaded directly from the `GitGub Releases <https://github.com/OpenEnergyPlatform/ontology/releases/>`_.
The currently developed version is available on the default `dev Branch <https://github.com/OpenEnergyPlatform/ontology/>`_.

The source code of the ontology is found in the folder `src/ontology/`.
The main file is `src/ontology/oeo.omn`.

All own modules are collected in the folder `src/ontology/edits/`.
The following diagram illustrates the modular file structure of the OEO. It depicts the import and file hierarchy from external imports (right) to the main file oeo.omn (left).

.. image:: https://user-images.githubusercontent.com/38690039/275459325-1c6eb63d-287a-45b5-a107-839c8c09bfe0.png
   :alt: Structure of the OEO

The imported modules are under `src/ontology/imports/`.
To get an overview of the existing modules, take a look at the following wiki article: `GitHub Wiki <https://github.com/OpenEnergyPlatform/ontology/wiki/Modules-of-the-OEO>`_
We recommend to use the software `Protégé <https://protege.stanford.edu/>`_ to open and edit the ontology. Additionally, an ontology viewer is available on the `Open Energy Platform <https://openenergy-platform.org/viewer/oeo/>`_.

Collaboration
================================================

This is an interdisciplinary open source project, help is always welcome.
Everyone is invited to develop this repository with good intentions.

The development of the ontology happens mainly on `GitHub <https://github.com/OpenEnergyPlatform/ontology>`_ and is supplemented by regular (online) developer meetings to review the progress and discuss more complicated topics.

If you're new to GitHub or ontologies check out our `"How to participate" <https://github.com/OpenEnergyPlatform/ontology/wiki/Welcome!-How-to-participate>`_ article for some first advice and helpful links.
The workflow is described in the `CONTRIBUTING.md <https://github.com/OpenEnergyPlatform/ontology/blob/dev/CONTRIBUTING.md>`_ file. Please check it out before you start working on this project. Points that are not clear in the file can be discussed in a `GitHub Issue <https://github.com/OpenEnergyPlatform/ontology/issues/new/choose>`_.
Please read the `GitHub Wiki <https://github.com/OpenEnergyPlatform/ontology/wiki>`_ for more information about the ontology, its standards, its best practice principles and the BFO classification.

Teams
================================================

Experts in ontology engineering, economy and energy-system modelling work together collaboratively.
We combine domain knowledge with knowledge about how an ontology should be designed.

If you have a specific question about ontology design, energy system modelling or economy (in context of this ontology), you can `tag <https://github.com/OmahaGirlsWhoCode/OmahaGirlsWhoCode/wiki/How-to-tag-someone-in-a-pull-request>`_ one of these teams (or persons) to notify its members that you need their feedback or help.

The OEO is organised in a general team and several `subteams <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-dev/teams>`_:

- `@oeo-dev <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-dev>`
    - All developers of the OEO

### Organisation

- `@oeo-community-manager <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-community-manager>`
    - Contact point for personal and team related concerns
- `@oeo-concept-owner <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-concept-owner>`
    - Strategic and long-term development and coordination of developers
- `@oeo-steering-committee <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-steering-committee>`
    - Members of the Steering Committee (OEO-SC)
- `@oeo-release-team <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-release-team>`
    - Coordinates the periodic releases

### Domain Experts

- `@oeo-domain-expert-energy-modelling <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-domain-expert-energy-modelling>`
    - Knowledge related to energy system modelling and simulation
- `@oeo-domain-expert-economy <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-domain-expert-economy>`
    - Knowledge related to economic system, costs, monetary issues
- `@oeo-domain-expert-linked-open-data <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-domain-expert-linked-open-data>`
    - Knowledge related to linked open data
- `@oeo-domain-expert-meteorology <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-domain-expert-meteorology>`
    - Knowledge related to meteorology and weather

### Ontology experts

- `@oeo-general-expert-formal-ontology <https://github.com/orgs/OpenEnergyPlatform/teams/oeo-general-expert-formal-ontology>`
    - Knowledge related to formal ontology expertise and BFO


.. |badge_license| image:: https://img.shields.io/github/license/OpenEnergyPlatform/ontology
    :target: LICENSE.txt
    :alt: License

.. |badge_documentation| image::
    :target:
    :alt: Documentation

.. |badge_contributing| image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
    :alt: contributions

.. |badge_repo_counts| image:: http://hits.dwyl.com/OpenEnergyPlatform/ontology.svg
    :alt: counter

.. |badge_contributors| image:: https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square
    :alt: contributors

.. |badge_issue_open| image:: https://img.shields.io/github/issues-raw/OpenEnergyPlatform/ontology
    :alt: open issues

.. |badge_issue_closes| image:: https://img.shields.io/github/issues-closed-raw/OpenEnergyPlatform/ontology
    :alt: closes issues

.. |badge_pr_open| image:: https://img.shields.io/github/issues-pr-raw/OpenEnergyPlatform/ontology
    :alt: closes issues

.. |badge_pr_closes| image:: https://img.shields.io/github/issues-pr-closed-raw/OpenEnergyPlatform/ontology
    :alt: closes issues
