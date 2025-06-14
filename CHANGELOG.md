<!--
SPDX-FileCopyrightText: Open Energy Ontology (OEO) <https://github.com/OpenEnergyPlatform/ontology/>
SPDX-License-Identifier: CC0-1.0 OR MIT
-->

# Changelog
All notable changes to this project will be documented in this file. <br>
For each version, important additions, changes and removals are listed here.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/),
and the versioning adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [2.X.X] - 20XX-XX-XX

### Added
- multi-criteria decision analysis (#2091)

### Changed

### Removed


## [2.8.0] - 2025-05-28

### Added
- has scenario year value (#2045)
- WHG, BWaldG (#2006)
- biosphere reserve role, protected landscape area role, water protection area role, floodplain role, forest role (#2006)
- biosphere reserve, protected landscape area, water protection area, floodplain, forest (#2006)
- arable land, arable land with poor soil quality, arable land with high soil quality, arable land role, arable land with poor soil quality role, arable land with high soil quality role (#2041)
- wind power density (#2067)
- electricity transmission function, electricity distribution function (#2043)
- grid component role (#2054)
- CCO import: prescribes, prescribed by, designates, designated by, describes, described by, represents, represented by (#2074)
- quarter-hourly, every minute, every ten minutes (#2087)

### Changed
- changed base IRI to https://openenergyplatform.org/
- vehicle operational mode (bug fix) (#2046)
- demand, efficiency value, final energy consumption value, process climate neutrality, material climate neutrality, primary energy consumption value, net electricity generation, climate neutrality criterion (#2063)
- grid component (#2054)
- has uuid (#2077)
- electricity grid, energy transfer function (#2073)
- energetic conversion process, energy transfer (bug fix) (#2061)

### Removed
- has creation date, has report title (#2079)

## [2.7.0] - 2025-03-06

### Added
- conceptual model (#1976)
- model uncertainty location (#1990)
- legislation, ROG, BNatSchG, protected area role, Fauna Flora Habitat role, Bird Sanctuary role, Fauna Flora Habitat, Bird Sanctuary (#1991)
- imports from stato: cutoff, lower confdence limit, upper confdence limit, statistic, measure of dispersion, confidence interval (#2002)
- import from CCO event ontology: Change, Effect, Stasis and subclasses, has occurent part, occurrent part of and subproperties (#2016)
- has iri, has study descriptor tag, has uuid, has scenario type, has publication date, has report title, has doi, has reference, based on sector division, has creation date, covers technology (#2020)
- add dual licensing CC0-1.0 OR MIT (#2021)
- add REUSE license check and copyright info (#2021)
- import from MENO ontology: energetic conversion process, energy decrease, energy increase, quality transfer + subclasses, quality transformation + subclasses(#2022)

### Changed
- technical model implementation, conceptual model, model system boundary, input data/exogenous data, output data (#1990)
- protected area, conditionally reserved region role, priority region role, suitable region role (#1991)
- apply socio-economic constraints for assessment of potential, net capacity factor (#1995)
- cost, delivery cost, fixed cost, investment cost, levelised cost of electricity, social cost of emission, system cost, variable cost (#1999)
- has model(#2001)
- feasible potential determination method, techno-economic potential determination method, wind characteristics determination method, wind farm area determination method, wind potential determination method (#2005)
- model, models (#2007)
- uncertainty of a model, model, model system boundary (#2012)
- solid (#2019)


## [2.6.0] - 2024-12-06

### Added
- has aggregation type, has time stamp alignment (#1944)
- study descriptor (#1950)
- file oeo-tasks (#1940)
- action specification for techno-economic potential, calculate economic potential, calculate levelised cost of energy, determine capital expenditures, determine discount and interest rate, determine operational expenditures, determine wind turbine lifetime (#1940, #1964)
- action specification for the feasible potential, apply constraints for assessment of potential, calculate feasible potential (#1940)
- action specification for the technical wind potential, account for wake losses, calculate technical potential, determine annual energy yield, determine capacity density, determine capacity factor, place turbines within area, select appropriate turbine types (#1940, #1966)
- action specification for wind characteristics, air density adjustment, data preparation, wind power density calculation, wind speed calculation, wind speed frequency analysis, wind variability identification (#1940, #1964, #1966)
- action specification for wind farm development area, determine development area, determine geographical potential, improve spatial resolution, prepare exclusion criteria datasets, run multi-criteria decision analysis, select exclusion criteria (#1940, #1964)
- determined feasible potential, determined techno-economic potential, determined wind characteristics, determined wind farm area, determined wind potential (#1940)
- uncertainty of a model, nature of uncertainty, level of uncertainty, location of uncertainty role, ambiguous uncertainty, epistemological uncertainty, ontological uncertainty, shallow uncertainty, medium uncertainty, deep uncertainty, recognised ignorance, has uncertainty nature, has uncertainty location, has uncertainty level (#1829)
- feasible potential determination process, techno-economic potential determination process, wind characteristics determination process, wind farm area determination process, wind potential determination process (#1940, #1966)
- feasible potential determination method, techno-economic potential determination method, wind characteristics determination method, wind farm area determination method, wind potential determination method (#1940, #1966)
- model system boundary (#1977)
- technical model implementation(#1978)
- gaseous (#1980)

### Changed
- energy amount value / energy value (#1941)
- rework contributing and readme file (#1937, #1946)
- time stamp (#1944)
- supply grid, transport network, critical infrastructure (#1947)
- areal solar energy density (#1983)


## [2.5.0] - 2024-09-24

### Added
- German alternative labels (#1883, #1895)
- English language tags to existing alternative labels (#1883, #1895)
- GAMS programming language (#1889)
- oeo:unit, oeo:physical unit (#1892)
- oekg annotation (#1897)
- kilowatt, megawatt (#1900)
- monetary price (new entity) (#1902)
- amount (#1905)
- economic instrument function, education instrument function, information instrument function, regulatory instrument function, voluntary agreement instrument function (#1906)
- product (#1912)
- term tracker annotation (#1913)
- licence provider, licensee, has licence provider, permits (#1925)

### Changed
- gams -> General Algebraic Modeling System (#1889)
- uo:unit (#1892)
- train, regionalisation (#1899)
- add annotation: climate neutrality criterion, negative emission, study report due to legislation, decarbonisation pathway, re-share, flexibility, energy conversion efficiency, resilience, life cycle assessment, co2 emissions, ghg emissions, acceptance, sufficiency, energy demand, electrical energy share, regionalsation, gross electricity generation, electricity/gas/heating grid, sector coupling, model coupling, scenario projection comparison, model intercomparison study, policies and measures  (#1897)
- monetary value (formerly: monetary price) and subclasses (#1902)
- size (#1905)
- economic instrument, education instrument, information instrument, regulatory instrument, voluntary agreement instrument (#1906)
- is traded at, trades (#1912)
- replace term tracker item with term tracker annotation (#1922, #1923)
- replace has bearer with characteristic of (#1928)

### Obsoletion
- economic value, has economic value, economic value (#1931)
- has bearer (#1928)


## [2.4.0] - 2024-07-01

### Added
- subsector, has subsector, subsector of (#1788)
- manufacturing technology, manufacturing plant, manufactured commodity (#1840)
- German alternative labels (#1862, #1868)
- Matlab programming language (#1869)
- SKOS annotations: skos:closeMatch, skos:exactMatch, skos:relatedMatch (#1874)

### Changed
- electricity sector, industry sector, CRF sector (IPCC 2006) individuals (#1788)
- industrial process -> manufacturing process, industrial material -> manufactured material (#1840)
- electricity import/export value (#1864)
- C++, Fortran, Java, Matlab, PHP, Python, R, Ruby, VBA (#1869)
- ENVO mappings (#1879)
- emission factor value (#1880)

### Removed
- emission value (#1880)


## [2.3.0] - 2024-05-21

### Added
- methanol (#1827)
- has prefix (#1835)
- imported 'characteristic of' and subclasses from RO (#1838)
- quantity (#1839)
- model coupling, sector coupling, sector coupling technology (#1842)
- system robustness, robust system scenario, statistically robust, statistically robust scenario (#1843)
- emission value, greenhouse gas emission value, CO2 emission value, emission factor value (#1846)
- size (#1851)
- (de)commissioning start, (de)commissioning end (#1853)
- German alternative labels to about 40 classes (#1854)

### Changed
- has documentation quality (#1834)
- megawatt-hour, gigawatt-hour, terawatt-hour, petawatt-hour (#1845)
- energy consumption value, final energy consumption value, primary energy consumption value, gross inland energy consumption value, gross national electricity consumption value (#1841)
- emission factor, emission rate, greenhouse gas emission rate, CO2 emission rate, carbon dioxide equivalent quantity value (#1846)
- area value (#1851)
- has bearer, has characteristic, characteristic of, role of, model role (#1852)
- time stamp (#1853)


## [2.2.0] - 2024-03-04

### Added
- economic instrument, voluntary agreement, voluntary agreement instrument, regulatory instrument, information instrument, education instrument (#1786)
- priority region role, priority region, conditionally reserved region role, conditionally reserved region, suitable region role, suitable region, priority region with effect of suitable region, spatial planning policy (#1791)
- missing value reason, notation key (#1795)
- non-energy use technology (#1803)
- BSI-KritisV sector division, BSI-KritisV energy sector, BSI-KritisV transport sector, critical infrastructure role, critical infrastructure (#1809)
- has unit numerator, has unit denominator and subproperties (#1816)
- compressor, compressor station and subclasses (#1818)
- new units and prefixes from UO (#1820)
- has associated axiom(sparql), shortcut relations for has information input/output, covers energy carrier, covers technology, covers sector (#2023)

### Changed
- energy transfer function, energy transformation function and subclasses (#1785)
- effort sharing, feed-in tariff, levy, market premium (#1786)
- policy instrument (#1791)
- region of relevance (#1791)
- MMR sector division, EU emission sector division (#1797)
- German energy balance sector division (#1798)
- non-energy use (#1803)
- API -> application programming interface; GUI -> graphical user interface (#1810)
- forecasting model calculation (#1799)
- uo-extracted.owl (#1820)


## [2.1.0] - 2023-12-05

### Added
- resilience, power system resilience, power system (#1744)
- service product role, service product (#1748)
- region of relevance, study subregion role, study region role, interacting region role, considered region role (#1749)
- import from IAO: time stamped measurement datum, action specification, data format specification, objective specification, study design, software application, software library, software method, software module, software script, document part, journal article, version number, cartesian spatial coordinate datum, one dimensional cartesian spatial coordinate datum, two dimensional cartesian spatial coordinate datum, three dimensional cartesian spatial coordinate datum, has time stamp (#1754)
- fuel blending quota, fuel quota blending value (#1763)
- study report due to legal obligation (#1777)
- market share and market share value (#1779)

### Changed
- subregion, study region, study subregion, interacting region, considered region (#1749)
- model factsheet (#1751)
- is connected to, has sink, has source (#1762)
- temperature, pressure (#1767)
- carbon capture and storage technology (#1768)
- power rating, power capacity (#1770)
- boiler (#1771)
- B7, E10 (#1774)
- data descriptor (#1775)
- target description, policy instrument, policy (#1778)


## [2.0.1] - 2023-10-26

### Changed
- unit, prefix, generically dependent continuant (#1741/#1742)


## [2.0.0] - 2023-10-25

### Major stuctural changes
For the version 2.0.0 we especially did some major structural changes on the OEO. Two new modules were introduced:
* The first one, oeo-sector, is a module on the same hierarchical level as the other content-related modules, i.e. oeo-physical, oeo-model and oeo-social. All sector-related entities were moved there from oeo-social.
* The second one, oeo-shared-axioms, is a module that imports the four content-related modules and contains all axioms that are introduced across modules.

This caused a lot of movement of entities, especially from oeo-shared. Many classes were moved back to their original module. This restructuring was done to foster the modularity, which makes the implementation easier and more error-prone. Yet, we had to break with the rule, that all axioms should live in the same module as their class of declaration. The full axiomatisation of a class is now only provided if the module oeo-shared-axioms is used. See also the wiki article on the [modules of the OEO](https://github.com/OpenEnergyPlatform/ontology/wiki/Modules-of-the-OEO).

Further, the import process for UO and OMO were updated. All scripts and tools not essential for the building routine moved to a [seperate repository](https://github.com/OpenEnergyPlatform/oeo-tools). And finally, english language labels were added to (english) definitions and labels, to allow other language extentions in the future.

### Content-related changes
We added a lot of classes that are relevant for the OEKG development, i.e. technologies (#1572) and descriptors for scenario studies (https://github.com/OpenEnergyPlatform/oekg/issues/19).

### Added
- heat generation technology, solar heat technology, geothermal heat technology (#1610)
- new files for new UO v2023-05-25 import process (#1633)
- recycling (#1638)
- regionalisation (#1639)
- sufficiency scenario (#1642)
- increase, decrease (#1644)
- new files for new OMO v2023-08-23 import process (#1646)
- power-to-fuel technology and subclasses (#1647)
- sufficiency scenario, sufficiency (#1642, #1648)
- new module oeo-shared-axioms.omn (#1649)
- acceptance (#1698)
- scenario projection comparison, model intercomparison study (#1711)
- flexibility, energy balancing (#1717)
- control area, bidding zone, bidding zone role (#1718)
- climate neutrality criterion, process climate neutrality, climate neutral process, material climate neutrality (#1722)
- blended liquid fuel, bioethanol, E10, B7 (#1723)
- new module oeo-sectors (#1724)
- mobility technology, electric mobility technology (#1727)
- energy storage object hierarchy, energy storage technology hierarchy (#1728)

### Changed
- energy transformation (#1625)
- waste role (#1638)
- economy, economic scenario, target driven scenario, explorative scenario, policy scenario (#1642)
- regionalisation (#1644)
- oeo.omn imports (#1649)
- model relabeled to numerical computer model, model, has contributor and subclasses (#1707)
- study (#1711)
- person, organisational role, organisation (#1716)
- energy balance -> energy balance data set (#1717) 
- state of matter (#1720)
- potential energy storage function (#1728)

### Removed
- import and annotation scripts removed from repo. New repo is https://github.com/OpenEnergyPlatform/oeo-tools (#1686)

### Deprecated
- belongs to module (#1732)


## [1.16.1] - 2023-08-01

### Changed
- Update module files after saving with Protégé 5.6.1(#1628)


## [1.16.0] - 2023-08-01

### Added
- boolean value (#1255)
- material transformation, fuel production (#1575)
- life cycle assessment (#1576)
- energy technology (#1591)
- power generation technology and 20 subclasses (#1601)
- policy scenario, reference role, reference scenario (#1614)
- greenhouse gas emission scenario, co2 emission scenario (#1615)
- population count, annual GDP growth (#1623)

### Changed
- boolean variable, true, false (#1255)
- reimplemented competency question tests in pytest (#1420)
- added commands to filter competency questions from the command line (#1420)
- added descriptive names to competency questions. and organized them in directories (#1420)
- production (#1575)
- technology (#1591)
- quantity value (#1606)
- trade (#1613)
- climate scenario, climate system, energy scenario, carbon dioxide, energy system, supply system, emission scenario (#1615)
- secondary energy production (#1619)
- hydro energy, solar energy, wind energy (#1620)
- gross domestic product (#1623)

### Removed
- old competency question bash script (#1420)


## [1.15.0] - 2023-05-31

### Added
- energy transfer function (#1515)
- mineral oil refining process, mineral oil product (#1531)
- propulsion/energy-to-motion (#1541)
- climate system (#1542)
- forecast (#1544)
- creative work licence (#1547)
- IAO extraction file iao-extracted.owl and extraction scripts extract-iao-module.sh, iao-w-hierarchy.txt (#1555)
- subsurface collector, downhole heat exchanger (#1557)
- nuclear, nuclear electric hydrogen, nuclear electrical energy, solar electric hydrogen, solar electrical energy (#1559)
- electrical energy share, renewable energy share value, electrical energy share value (#1561)
- has energy main/auxilary input, has energy main/waste output (#1564)

### Changed
- propulsion/traction (#1541)
- clean up oeo.omn and oeo-shared (#1546)
- has copyright license -> has licence; information content entity; data set, database, modelling software, software, document, software documentation, factsheet, report (#1547)
- common report format (#1558)
- RE-share -> renewable energy share (#1561)
- heat generation process, fuel-powered electricity generation (process), combined heat and power generation (CHP) (process), electricity generation process (#1562)
- policy instrument, guides (#1563)
- Fixed IAO import source to [v2022-11-07](https://raw.githubusercontent.com/information-artifact-ontology/ (#1555)
- update files: oeo-import-edits.owl, src/ontology/catalog-v001.xml and src/ontology/edits/catalog-v001.xml, oeo-shared (#1555)

### Removed
-  files and scripts from outdated import process: extract-iao-module.bat, imports/iao-module.owl, ro-module.owl (#1555)


## [1.14.0] - 2023-03-30

### Added
- CRF-based sector division, EU legislation sector division (#1462)
- Brent crude, Western Texas Intermediate (#1478)
- electricity cost (#1482)
- power-to-fuel system, power-to-fuel process, power-to-ammonia system, power-to-liquid process (#1483)
- energy storage level, energy storage content (#1486)
- compressed-air energy storage unit (#1499)
- added built ontology to the pipeline artifacts (#1475)

### Changed
- NC/BR sector division and sector individuals; KSG sector division;  EU sectors/divisions; EU climate policy (#1462)
- electricity grid (#1479)
- Updated RO import source to [v2023-02-22](https://raw.githubusercontent.com/oborel/obo-relations/v2023-02-22/ro.owl)
- air (#1499)
- storage capacity -> energy storage capacity (#1486)
- changed order in which the oeo-full files are compiled, owl now builds before omn (#1475)
- specifically dependent continuant, has bearer, energy, disposition, good role, demand (#1485)
- sector division (#1506)
- uses, is used by (#1508)
- update oeo.omn description (#1509)


## [1.13.0] - 2023-02-01

### Added
- oeo-import-edits as a unified file for custom extensions of imported concepts + properties (#1268)
- tank, fuel tank, volume (#1356)
- heat generating unit, heat plant, heat transfer unit, solar heat plant, solar heat unit (#1360)
- combustion-based heater, electrical heater, geothermal heat unit, geothermal heat plant (#1360)
- thermo-chemical heat storage object, chemical heat storage object, sorption heat storage object, adsorption, desorption (#1363)
- sensible heat storage object, sensible solid heat storage object, sensible fluid heat storage object (#1363)
- phase transition, evaporation, melting, latent heat storage object, latent fluid-gaseous heat storage object, latent solid-fluid heat storage object (#1363)
- filling station, hydrogen station, hydrogen transport (#1357)
- OEP user, qualitist, quantitist, apinist (#1383)
- sustainability criterion, material sustainability, process sustainability, process sustainability, sustainable process (#1385)
- vehicle-kilometre (#1388)
- electricity demand, fuel demand (#1389)
- based on (#1391)
- bidirectional vehicle charging station (#1393)
- charging (#1394)
- non-energy use, cold start, cooperative programming, distribution, (electricity) export/import, frequency control, request, service, chemical reaction (#1395)
- ton of oil equivalent, ton of coal equivalent, kilo ton of oil equivalent, kilo ton of coal equivalent, million ton of oil equivalent, million ton of coal equivalent (#1398)
- sustainable biofuel, non-sustainable biofuel (#1409)
- source category (#1428)
- scenario bundle (#1429)
- gas turbine process, combined cycle electricity generation, steam power unit (#1362)
- rotary heat exchanger, plate heat exchanger, boiler, tube collector, flat-plate collector (#1432)
- explorative and target driven scenario (#1459)
- utilisation value (#1435)
- amortisation time, economic life time (#1436)
- renewable power unit, renewable power plant (#1437)
- CRF sector individuals 2.A.2, 2.A.3, 2.A.4, 2.B.1 to 2.B.10, 2.C.2 to 2.C.7, 2.E.1 to 2.E.5, 2.F.1 to 2.F.6 and 2.G.1 to 2.G.4 (#1440)
- has spatial region (#1441)
- (renewable) electrolytic hydrogen, (fossil/abated) steam reforming hydrogen, renewable electrical energy (#1442)
- energy transformation function and subclasses (#1445)
- RED sector individuals (#1446)
- direct/diffuse solar radiation, non-scattered radiant flux density, (single/two axis) solar tracking, (single/two axis) solar tracked receiving surface (#1448)
- power-only generating unit (#1456)
- energy balance, energy balance collection, energy balance calculation method, energy balance sector division (#1463)

### Changed
- bearer of -> has characteristic (#1268)
- ro-module -> ro-extracted (#1268)
- power plant, power generating unit, combined heat and power plant, combined heat and power generating unit, solar thermal collector (#1360)
- internal combustion vehicle, plug-in hybrid electric vehicle, fuel cell electric vehicle, tank ship, gas turbine vehicle (#1356)
- gas turbine, gas power unit (#1362)
- model descriptor (#1387)
- passenger-kilometre, ton-kilometre (#1388)
- SMES -> superconducting magnetic energy storage (#1396)
- biofuel; competency questions Q1 and Q2 (#1409)
- global warming potential, binary file format, text file format, source code file format, generation time series, optimisation, simulation (#1410)
- has economic value, economic value of (#1422)
- solar thermal collector (#1432)
- net capacity factor (#1435)
- yield profile, geothermal power unit, marine current/tidal/wave energy converting unit, solar power unit, wind energy converting unit (#1437)
- CRF sector individual 2.C.1 (#1440)
- has study region, has considered region, has interacting region, has study region (#1441)
- synthetic hydrogen, fossil hydrogen (#1442)
- renewable_energy_directive_sectors -> Renewable Energy Directive sector division (#1446)
- radiation (#1447)
- german/eurostat energy balances -> German/Eurostat energy balance sector division; empirical/synthetic/test data set (#1463)
- replaced owl:equivalentClass with 'may be identical to' in annotation properties


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
- has study region, has study subregio, has considered region, has interacting region, has scenario year (#1347)
- equivalence subclasses for car and truck (#1345)
- refinery gas, petroleum coke (#1351)
- chemical/electrical/kinetic/potential energy storage function; underground fuel storage object (#1348)
- data center, sewage plant, industrial waste thermal energy, recovered heat, aerothermal energy (#1359)

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
- energy converting component, energy storage object, hardware, solar receiving object, vehicle, waste thermal energy (#1359)

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


## [1.9.0] - 2022-03-01

### Added
- memo item and CRF (2006) sector individuals relating to memo item; has information content entity (#967)
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
