# Changelog
All notable changes to this project will be documented in this file.

The format is inspired from [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and the versioning aims to respect [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.X.X] - 20XX-XX-XX

### Added
- tank, fuel tank, volume (#1356)

### Changed
- internal combustion vehicle, plug-in hybrid electric vehicle, fuel cell electric vehicle, tank ship, gas turbine vehicle (#1356)

### Removed


## [1.12.0] - 2022-11-02

### Added
- github: template for pull requests (#1162)
- steam reforming process (#1251)
- emission price, CO2 price, CO2 emission, CO2 emission value, carbon tax value (#1253)
- fuel cost (#1260)
- transport performance value, transport performance unit, passenger-kilometre, ton-kilometre (#1289)
- gas vehicles, gas engines, more gas fuels, compressed gas fuel role (#1290, #1305)
- motorised vehicle, aircraft and subclasses, land vehicle and subclasses, watercraft and subclasses (#1293)
- conventional energy (#1295)
- transport network, transport network component, transport hubs, and subclasses (#1297)
- subclasses for energy transfer, fuel transport and subclass, axiom for fuel, axiom for freight transport (#1299)
- primary energy consumption calculation method and subclasses (#1306)
- vehicle charging station (#1312)
- vehicle operational mode (#1314)
- gas turbine vehicle, jet fuel vehicle, jet fuel gas turbine (#1315)
- fuel supply system (#1316)
- NC/BR sector division; NC/BR sector individuals (#1317)
- is sector of, sectoral energy consumption, sectoral emission (#1321)
- data file format, and subclasses (#1326)
- mineral oil, mineral oil product, mineral oil refinery, mineral oil refining, mineral oil refining sector (#1331)
- international transport sector (#1334)
- equivalence subclasses for car and truck (#1345)
- refinery gas, petroleum coke (#1351)
- chemical/electrical/kinetic/potential energy storage function; underground fuel storage object (#1348)
- data center, sewage plant, industrial waste thermal energy, recovered heat, aerothermal energy (#1265)

### Changed
- github: update the description of the readme file (#1292)
- energy transformation (#1251)
- added annotations for which modules classes and individuals belong to (#1252)
- emission certificate price (#1253)
- power generating unit (#1259)
- equipment cost, variable cost, property cost, delivery cost, fixed cost (#1260)
- heat exchanger (#1263)
- program parameter (#1274)
- electrical heat pump (#1282)
- internal combustion engine (#1285)
- analysis scope (#1286)
- diesel fuel, diesel fuel role, diesel engine, diesel vehicle (#1288, #1315)
- internal combustion vehicle (#1293, #1315)
- scenario (#1296)
- heat transfer (#1299)
- bottom up, hybrid, top down (#1302)
- primary energy consumption, gross inland energy consumption (#1306)
- transport (#1309)
- has bearer axioms to OEO-defined realizable entities (#1310)
- vehicle (#1314)
- electric vehicle and subclasses, plug-in hybrid vehicle, gasoline vehicle, e-bike (#1315)
- energy use (#1321)
- data format (#1326)
- crude oil; gas diesel oil, gasoline, kerosene, and subclasses; CRF sector (IPCC 2006): petroleum refining (#1331)
- CRF sector (IPCC 2006): international bunkers / international aviation / maritime bunkers; MMR sector: M.International aviation in the EU ETS (#1334)
- final energy consumption (#1340)
- fuel cell (#1341)
- realized in, greenhouse effect disposition, combustible energy carrier disposition (#1353)
- energy storage -> energy storage function; thermal energy storage function; energy storage object; storage unit (#1348)
- methanation gas storage -> power-to-methane system; power-to-liquid system; pumped water, pumped hydro storage power plant (#1348)
- energy converting component, energy storage object, hardware, solar receiving object, vehicle, waste thermal energy (#1265)

### Removed
- battery storage (#1348)
- csv and txt (#1371)

## [1.11.0] - 2022-07-04

### Added
- tangential proper part, surface, solar radiation receiving surface (#1209)
- combustion thermal energy transformation (#1210)
- measurement device (#1215)
- parameterisation, model calibration (#1216)
- scenario projection (#1217)
- import, export, electricity import, electricity export, electrical energy amount value, electricity import value, electricity export value, sirup (#1221)
- has institution -> has organisation (#1226)
- solar receiving object (#1228)
- passenger, passenger transport, energy service demand for passenger/ton-kilometre (#1234)

### Changed
- endogenous data, exogenous data (#1216)
- origin, portion of matter (#1218)
- pv cell -> photovoltaic cell (#1220)
- is energy participant of, has energy participant (#1221)
- has participant (#1225)
- photovoltaic cell, solar thermal collector (#1228)
- public transport, private transport, vehicle (#1234)
- power capacity (#1235)
- jet fuel (#1237)
- fuel-powered electricity generation (#1240)
- charcoal, synthetic fuel, gas diesel oil, manufactured coal based gas, syngas, gasoline, kerosene, steam, compressed air, pumped water (#1243)



## [1.10.1] - 2022-06-14

### Added
- nationally determined contribution (#1151)
- maximum value, power capacity (#1155)
- bioenergy (#1188)
- general class axiom for energy (#1186)
- fissile material entity (#1190, #1196)
- realized in (#1197)
- frequency control and subclasses primary control, secondary control, tertiary control (#1202)

### Changed
- marine wave energy transformation, marine tidal energy transformation, marine current energy transformation (#1137)
- has input, input of, has output, output of, participates in, has participant (#1138)
- capacity factor (#1144)
- power value, declared net capacity, nameplate capacity, power rating (#1155)
- software license (#1163)
- photon, energy (#1165)
- energy carrier (#1173)
- transformation, energy transformation, energy carrier disposition, fuel role (#1178)
- fossil (#1181)
- energy transformation (#1182)
- fuel (#1184)
- fossil energy (#1185)
- origin and subclasses, energy, portion of matter (#1192)
- KSG sector buildings (#1198)
- general class axiom "combustible things" (#1195)
- has institution (#1200)
- waste fuel, liquid biofuel, solid biofuel, fossil combustion fuel, renewable fuel, synthetic fuel, volatile organic compound (#1201)

### Removed

## [1.10.0] - 2022-05-09

### Added
- abbreviation (#1075)
- discount rate (#1077)
- protected area (#1078)
- energy service demand (#1080)
- industrial material, chemical substance, paper, cement, mineral, non-metallic mineral, metal, non-ferrous metal, steel, physical output of (#1082)
- import price, export price (#1083)
- personal living space (#1084)
- data / copyright / software license, has copyright license (#1090)
- slope, surface azimuth angle (#1112)
- potential (#1102)
- information input/output of (#1113)
- ramping, start-up speed, cold start (#1126)
- heat generation, combustion thermal energy transformation (#1130)
- study factsheet, OEP study factsheet, scenario study (#1131)
- CITATION.cff (#1134)
- propulsion, traction motor (#1135)
- causally downstream of or within, causally upstream of or within (#1136)

### Changed
- has bearer, bearer of, is defined by, process attribute of (#985)
- biofuel and biogenic waste fuel (subclasses); origins (#1048)
- license (#1063)
- is energy participant of and subrelations (#1057)
- starts, starts with, located in, location of, ends, ends with, part of, has part (#1086)
- acronym (#1075)
- space requirement (#1084)
- flow potential, stock potential (#1102)
- energy, has role (#1101)
- greenhouse gas emission (#1100)
- water (#1099)
- CRF sector (IPCC 2006): pipeline transport (#1122)
- energy system (#1123)
- trades / is traded at, good, good role (#1127)
- traction motor -> electric traction motor (#1135)

### Removed

## [1.9.0] - 2022-03-01 

### Added
- memo item and CRF (2006) sector individuals relating to memo item; has information content entity (#966)
- annual, monthly, weekly, daily, hourly (#972)
- mathematical expression (annotation property) (#990)
- energy consumption value, gross national electricity consumption (#997)
- forecast error (#1002)
- has energy participant, has energy input, has energy output (#1006)
- gas mixture (#1009)
- methodology (#1011)
- liquified natural gas (#1016)
- alternative term specific power to areal power density (#1018)
- domains and range for axioms from Relation Ontology (#1019)
- alternative term specific power to areal power density (#893)
- cost subclasses (#1022)
- (operational) life time, construction time, decommissioning time (#1026)
- gasoline/diesel fuel, gasoline/diesel fuel role, gasoline/diesel engine, gasoline/diesel vehicle (#1027)
- has economic value / economic value of, social cost of emission (#1034)

### Changed
- biofuel (#965)
- has quantity value, has global warming potential (#966)
- resolution, has resolution and subclasses (#972)
- origin (#976)
- gross inland energy consumption (#997)
- heat exchanger, heater, turbine, water electrolyser, steam reformer, motor, pump, power rating, nameplate capacity (#993)
- has state of matter, has normal state of matter (#1001)
- peat (#1003)
- produces, has gross output, has net output, axioms of various artificial objects (#1006)
- energy transformation and subclasses, energy transformation unit (#1010)
- air, biogas, biomethane, manufactured coal based gas, natural gas, syngas (#1009)
- study, methodical focus (#1011)
- energy demand sector (#1015)
- duration / time span (#1017)
- market participant, market exchange (#1019)
- crude oil, gas diesel oil, gasoline, kerosene, oil power unit (#1024)
- study, study report (#1025)
- biogasoline, biodiesel, (fossil) gasoline/diesel fuel (#1027)
- natural gas, coal, crude oil, peat, wood (#1033)
- editor note on gasoline-related classed (#1037)
- use has energy input / output for energy transformation and subclasses (#1041)
- has institution (#1042)
- axiom in marine current energy transformation (#1044)

### Removed
- cost in oeo-social (#977)
- organisation in oeo-social (#992)
- oil and petroleum products (#1024)

## [1.8.0] - 2021-12-01

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
- net capacity factor (#946)
- decarbonisation pathway, emission constraint (#951)
- rotor diameter (#949)
- energy use, non-energy use (#950)
- variable (production) cost (#953)
- power-to-gas process, power-to-methane process, methanation, oxygen, water electrolysis process (#954)
- biomass, biomethane (#952)
- variable (production) cost (#953)
- conventional (energy carrier disposition), fossil energy (#955) 
- carbon tax, social cost of carbon, carbon price (#956)
- synthetic ammonia, power-to-ammonia process (#959)
- renewable waste fuel, fossil waste fuel, renewable industrial waste fuel, fossil industrial waste fuel (#961)

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
- power-to-gas system, synthetic methane, synthetic hydrogen, fossil hydrogen (#954)
- biofuel, biogas, charcoal, wood (#952)
- renewable energy (#955)
- PtL fuel (formerly: synthetic liquid fuel) (#957)
- ammonia (#959)
- industrial waste fuel, municipal waste fuel, renewable municipal waste fuel, fossil municipal waste fuel (previously: non renewable municipal waste fuel) (#961)

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
