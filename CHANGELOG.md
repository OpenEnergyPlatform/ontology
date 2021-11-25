# Changelog
All notable changes to this project will be documented in this file.

The format is inspired from [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and the versioning aim to respect [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

Here is a template for new release sections

```
## [1.X.X] - 20XX-XX-XX

### Added
### Changed
### Removed

```

## [1.x.x] - 20XX-XX-XX

### Added
- energy transformation unit, energy transfer (#895)
- outage and subclasses, curtailment (#897)
- levy, tax, feed in tariff, market and capacity premium (#909)
- inflation rate, exchange rate, purchasing power parity, electricity price, system cost (#910)
- carbon capture, carbon storage, carbon capture and storage, direct air capture (#911)
- resolution and subclasses (#912)
- fee, due, remuneration, LCOE (#913)
- combined heat and power generation (CHP), CHP plant, CHP generating unit (#923)
- eurostat synonyms (#924)
- market revenue (#929)
- solid, liquid and gaseous combustion fuels; liquid and gaseous fossil fuels; solid, liquid and gaseous renewable fuels; gaseous biofuel; solid, liquid and gaseous synthetic fuel (#931)
- (specific) space requirement, km2, area per power unit, area value (#933)
- gross electricity generation, net electricity generation, electricity generation process (#932)
- power value (#935)
- GovReg sector division, MMR sector division and further CRF (2006) sector individuals (#941, #944)
- total emissions including/exluding LULUCF, international aviation, maritime navigation, multilateral operations and related sector individuals (#944)
- liquid air production (#945)
- decarbonisation pathway, emission constraint (#951)
- rotor diameter (#949)
- variable (production) cost (#953)
- energy use, non-energy use (#950)
- conventional (energy carrier disposition), fossil energy (#955) 

### Changed
- energy converting device / component, unit of measurement (#895)
- currency (#910)
- has resolution and subclasses (#912)
- reclassify of marine hydro energy classes (#921)
- list of contributors (#927)
- artificial object, nameplate capacity (#933)
- declared net capacity, nameplate capacity, power rating (#928)
- combustion fuel, solid fossil fuel, syngas (#931)
- CRF sector individuals: energy industry; fugitive emissions; industrial processes and product use; agriculture; LULUCF; waste (#941)
- European Union Emissions Trading System (#944)
- liquid air (#945)
- renewable energy (#955)
- PtL fuel (formerly: synthetic liquid fuel) (#957)

### Removed

## [1.7.0] - 2021-10-04

### Added
- power plant portfolio, dispatch assignment (#792)
- yield profile, demand trader, direct marketer, merit order, full load hours (#793)
- energy demand (#796)
- policy, policy instrument, transformative measure (#797, #853)
- markup, markdown (#800)
- syngas, hydrocarbon (#805)
- ocean/marine energy and water (flow) related classes including power generating units and powerplants (#806)
- cooperative programming (#808)
- mapping to ENVO (#810)
- power plant with electromotive generator (#810)
- waste thermal energy (#813)
- rotational energy (#817)
- models (#821)
- uncertainty approach, stochastic and deterministic (#824)
- has documentation quality (#825)
- email address (#827)
- has gross output, has net output (#838)
- has number (#840)
- economy, good, good role (#843)
- production (#845)
- guides, has bearer (#853)
- secondary energy production (#856)
- EU climate policy, European Union Emissions Trading System, effort sharing and subclasses, Annual Emission Allocation (#857)
- EU emission sector division and EU emission sector individuals (#857)
- renewable energy, renewable energy carrier disposition, natural / pumped hydro energy (#861)
- governs (#868)
- typical period and subclasses (#875)
- distribution (#876)
- objective variable (#878)
- metric ton (#879)
- target description (#881)
- scenario year, scenario horizon, meteorological year, weather time series, scenario time series (#882) 
- axioms of typical period and aggregation type (#883)

### Changed
- battery and subclasses (#801)
- geographic coordinate (#803)
- river (#806)
- air pollutant (#816)
- motor, electric motor, internal combustion engine (#817)
- is traded at (#842)
- commodity, commodity role (#843)
- producer, primary energy production and subclasses (#845, #860)
- covers energy carrier, covers sector (#852)
- model descriptor, model factsheet OEO:00000277 (#854)
- origin, renewable, some portion of matter classes, renewable energy carrier, renewable fuel (#861)
- good, project, study, energy carrier (disposition) (#869)
- domains and ranges for some object properties added (#871)
- axioms of hydro energy (incl. subclasses), wind energy, study, study report and model calculation (#871)
- hydrogen turbine (#877)
- has objective (#878)

### Removed
- molten state battery (#801)
- duplicate model factsheet OEO:00020031 (#854)

## [1.6.1] - 2021-07-07

### Changed
- commodity (#789)

## [1.6.0] - 2021-07-01

### Added
- trade, market participant (#745)
- reservoir (#755)
- contract (#756)
- hydro power unit, hydro powerplant and subclasses, pump (#758, #768)
- river (#760)
- analysis scope (#764)
- fluid (#769)
- grid-bound heating (#770)
- delivery time (point), sender, receiver, bid, award, provider, service (#778)
- planned / unplanned availability, fraction value, block size, delivery interval, power plant operator, conventional trader (#779)
- RE-share (#780)
- emission market exchange (#781)
- hydrogen fuel cell, natural gas turbine, energy related axioms (#782)

### Changed
- trader (#745)
- has typical computation time (#751)
- powerplant and power generating unit subclasses (#752)
- dammed water -> dam; pumped water (#755)
- objective function (#757)
- water turbine (#758)
- portion of matter (#759)
- energy-related input and output relations (#766)
- derived and district heat(ing), solar thermal energy (#770)
- spelling convention: British labels with American synonyms (#772)
- usage of alternative term (#774)

### Removed
- hydroelectric dam energy transformation and run-off-river energy transformation (#758)

## [1.5.0] - 2021-05-03

### Added
- thorium and plutonium (#708)
- has information input / output (#716)
- has typical computation time / hardware (#723)
- quality control flag (#724)
- goal description (#729)
- heat transfer (#733)
- heat exchanger (#734)
- geothermal heat transfer, rock (#739)
- emission certificate (#740)
- natural / artificial ambient thermal energy, ambient thermal energy transfer (#742)
- energy market exchange (#748)
- public and private funders (#246)


### Changed
- has physical output, has constraint (#716)
- gross inland energy consumption, primary energy consumption (#719)
- covers energy carrier (#722)
- photon, wind energy, solar energy (#732)
- geothermal energy (#739)
- ambient thermal energy (#742)
- has origin, renewable, anthropogenic (#742)
- wind energy converting unit uses wind rotor (#754)

### Removed
- has numerical input / output (#716)
- computation time (#723)

## [1.4.0] - 2021-03-02

### Added
- monetary price and currency (#331)
- market exchange (#341)
- trader (#377)
- price request and marginal cost (#376)
- cost (#268)
- commodity (#339)
- emission value, greenhouse gas emission value, carbon dioxide equivalent quantity (#651)
- disjointness axiom for (has origin some natural gas) and (has origin some anthropogenic) (#658)
- radiative energy (#665)
- solar energy transformation and subclasses (#672, #701)
- potential energy (#670)
- photon (#674)
- abbreviations GDP and GVA (#676)
- renewable energy carrier (equivalent class) (#684)
- global warming potential (#683)
- steam-electric process (#691)
- volumetric flow rate value (#693)
- emission quantity value (#697)
- nuclear fission, nuclear energy transformation (#698)
- solar chemical energy transformation (#735)

### Changed
- relations to energy transformation (#646)
- has global warming potential (#651, #683)
- definition of battery electric vehicle and fuel cell electric vehicle (#655)
- energy (#656 and #665)
- solar energy (#672)
- fix def of secondary energy carrier (#678)
- restructure hydro energy classes in dev meeting (#682)
- license from string to IRI format (#686)
- definition of water (#689)
- emission value (#697)
- nuclear (binding) energy (#698)
- bioethanol (#704)
- has input / has physical input (#702)

### Removed
- delete hydroelectricity class (#682)

## [1.3.0] - 2020-12-18

### Added
- industrial process (#589)
- energy conversion efficiency and energy conversion performance (#591)
- fuel-powered electricity generation (#592)
- further IPCC sector individuals (#595)
- sector division and sector individuals of Bundes-Klimaschutzgesetz (#595)
- radiation (#600)
- subclasses of energy unit (#608)
- flow / stock potential and subclasses (#607)
- kinetic energy (#609)
- aggregation types (#610)
- subclasses of consumption and energy amount value (#613)
- areal energy / power density classes, solar-related subclasses and corresponding unit classes (#615)
- primary, secondary and final energy carrier (disposition) (#633)

### Changed
- powerplant (#594)
- relations has part and part of (#599)
- heat, renamed to thermal energy (#609)
- replace iao-annotation-module and iao-minimal-module with OBO metadata ontology, restructure iao-module (#616)
- defs of relations has contributer, has resolution and covers (#626)
- energy carrier disposition (#627)
- comment on waste fuel (#631)
- energy transformation has input/output energy (#690)

## [1.2.0] - 2020-10-30

### Added
- sensitivity analysis (#550)
- has contributor (#530)
- sponsor (#557)
- economic value and gross domestic product (#559)
- time step, time series, etc (#538)
- has member and member of (#562)
- gross value added (#563)
- validation and subclasses (#565)
- chemical reaction and subclasses (#568)
- demand (#569)
- consumption (#569)
- time stamp and time stamp alignment (#570)
- model descriptor and subclasses (#577)
- further sector individuals (#578)
- emission factor (#581)
- spatial regions (#585)

### Changed
- move subclasses of has participant (#530)
- licence (#561)
- ipcc_year_guidelines to CRF sectors (IPCC year) (#578)
- factsheet subclasses (#584)

### Removed
- software maintenance (#566)

## [1.1.0] - 2020-09-01

### Added
- vehicle and subclasses and vehicle related energy converting devices and energy storage objects (#431, #435)
- natural gas relation to methane (#431)
- ethanol (#445)
- factsheet-covers-relationships (#440)
- oeo-shared module (#450)
- object property definitions (#478)
- energy and supply system (#493)
- primary energy production and subclasses (#498)
- study and study report (#497)
- exogeneous, endogeneous data (#482)
- hub height, length value and has quantity value (#505)
- transport and subclasses (#517)
- annotation property unique individual identifier (#523)
- sector individuals (#523)
- output and input data (#536)

### Changed
- harmonise 'definition' annotation property (#529)
- move object properties to oeo-shared (#472)
- definition of sector and sector subclasses (#477, #484)
- definition of sector (#477)
- object property conforms_to renamed to is_defined_by (#480)
- model calculation (#504)
- electrical energy definition (#524)
- assumption (#525)
- update original release date and teams in `README` (#535)
- unit (#537)

### Removed
- unused object properties (#452)

## [1.0.0] - 2020-06-11

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
- energy producers (#370)
- energy transformation (#77)
- synthetic fuels and respective energy converting devices (#411)
- process attribute (#386)


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
- change power definition (#79)
- change quantity to quantity value (#386)
- grid, link, node, grid component (#36, #231)
- electricity as alternative term for electrical energy (#621)

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
- remove energy production and subclasses (#77)
- quantity subclasses (#368)
