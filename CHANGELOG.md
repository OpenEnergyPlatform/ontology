# Changelog
All notable changes to this project will be documented in this file.

The format is inspired from [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and the versioning aim to respect [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

Here is a template for new release sections

```
## [_._._] - 20XX-MM-DD

### Added
-
### Changed
-
### Removed
-
```
## [Unreleased]

### Added
- Concepts of biogenic, fossil, renewable and synthetic (#130)
- factsheet categories (#47)
- storage technologies (#47)
- `ObjectProperty` `has_normal_state_of_matter` (#39)
- add individuals `solid`, `liquid`, `gaseous`, `plasmatic` (#39)
- Add has_normal_state_of_matter value solid/liquid/gaseous/plasmatic to fuels (#39)
- object properties: 'has_disposition', 'has_role', 'has_function',
  'has_quality' (#51)
- issue templates (#92, #146) 
- ArtificialObject (#121) 
- classes for objects that apply to technologies like EnergyGenerator (#128)
- Grid class (#137)
- object properties to describe models (#109)
- RenewableEnergyCarrier (#206)
- ChemicalEnergy (#214)
- scenario subclasses (#344)
- state of matter defined classes (#354)

### Changed
- Restructured the repository to add a 'src' folder with an 'ontology' sub-folder with sub-folders for editable modules and import modules (#200)
- Split the ontology file into three modules: oeo-social,oeo-model and oeo-physical (#167)
- FluorinatedGreenhouseGas (#88) and GreenhouseGas (#234)
- agent and subclasses (#51)
- pollutant and subclasses (#51, #356)
- structure of the ontology (#47)
- change peat to solid and not gas (#39)
- StateOfMatter and subclasses (#45)
- improved workflow in `CONTRIBUTE.md` (#98)
- linked wiki and `CONTRIBUTE.md` in `README`(#113)
- add github team handle in `README` (#119)
- technology and subclasses (#128)
- rename CONTRIBUTE.md CONTRIBUTING.md (#144)
- individuals without types (#191)
- import unit-ontology (#215)
- import ro-ontology module replacing some of our relations (#216)
- replace InformationArtifact with information content entity from imported iao-ontology module (#223)
- unify -Energy and -Power classes (#225)
- ModelElement and subbclasses
- update issue templates 'workflow checklist' (#258)
- Generator (#273)
- EnergyStorage (#276)
- Turbine (#299)
- Change to use numeric identifiers for classes and individuals (#133)
- change origin individuals to classes (#321)
- modeling software (#345)
- change model def (#180)
- change energy class (#224)

### Removed
- `ObjectProperty` `has_stateofmatter` (#39)
- some superclasses of unsatisfiable classes and some that made the
  ontology inconsistent (#51)
- contact and subclasses (#101)
- subclasses of assumption (#102)
- time step, time series, time horizon (#327)
- type and subclasses (#325)
- cost and subclasses (#326)
- GeographicRegion and subclasses (#322)
- Validation and subclasses (#347)
- SoftwareElement (#348)
- unused object properties (#351)


