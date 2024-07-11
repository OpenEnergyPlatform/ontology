MKDIR_P = mkdir -p
VERSION:= $(shell cat VERSION)
VERSIONDIR := build/oeo/$(VERSION)
ONTOLOGY_SOURCE := src/ontology
IMPORTS := $(ONTOLOGY_SOURCE)/imports
subst_paths =	${subst $(ONTOLOGY_SOURCE),$(VERSIONDIR),${patsubst $(ONTOLOGY_SOURCE)/edits/%,$(ONTOLOGY_SOURCE)/modules/%,$(1)}}

OWL_FILES := $(call subst_paths,$(shell find $(ONTOLOGY_SOURCE)/* -type f -name "*.owl"))
OMN_FILES := $(call subst_paths,$(shell find $(ONTOLOGY_SOURCE)/* -type f -name "*.omn"))

OEP_BASE := http:\/\/openenergy-platform\.org\/ontology\/oeo

OWL_COPY := $(OWL_FILES)

OMN_COPY :=	$(OMN_FILES)

OMN_TRANSLATE := ${patsubst %.omn,%.owl,$(OMN_FILES)}

RM=/bin/rm
ROBOT_PATH := build/robot.jar
ROBOT := java -jar $(ROBOT_PATH)



define replace_devs
	sed -i -E "s/$(OEP_BASE)\/dev\/([a-zA-Z/\.\-]+)/$(OEP_BASE)\/releases\/$(VERSION)\/\1/m" $1
endef

define replace_oms
	sed -i -E "s/($(OEP_BASE)\/dev\/([a-zA-Z/\-]+)\.)omn/\1owl/m" $1
	sed -i -E "s/($(OEP_BASE)\/releases\/$(VERSION)\/([a-zA-Z/\-]+)\.)omn/\1owl/m" $1
endef

define replace_owls
	sed -i -E "s/($(OEP_BASE)\/dev\/([a-zA-Z/\-]+)\.)owl/\1omn/m" $1
	sed -i -E "s/($(OEP_BASE)\/releases\/$(VERSION)\/([a-zA-Z/\-]+)\.)owl/\1omn/m" $1
endef

define translate_to_owl
	$(ROBOT) convert --catalog $(VERSIONDIR)/catalog-v001.xml --input $2 --output $1 --format owl
	$(call replace_omns,$1)
	$(call replace_devs,$1)
endef

define translate_to_omn
	$(ROBOT) convert --catalog $(VERSIONDIR)/catalog-v001.xml --input $2 --output $1 --format omn
	$(call replace_owls,$1)
	$(call replace_devs,$1)
endef

.PHONY: all clean base merge directories

all: base merge closure

imports: directories $(IMPORTS)/ro-extracted.owl $(IMPORTS)/iao-extracted.owl $(IMPORTS)/uo-extracted.owl

base: | directories $(VERSIONDIR)/catalog-v001.xml build/robot.jar $(OWL_COPY) $(OMN_COPY) $(OMN_TRANSLATE)

merge: | $(VERSIONDIR)/oeo-full.omn

closure: | $(VERSIONDIR)/oeo-closure.owl

clean:
	- $(RM) -r $(VERSIONDIR) $(ROBOT_PATH)

clean-imports:
	- $(RM) -r $(IMPORTS)/*.owl

directories: ${VERSIONDIR}/imports ${VERSIONDIR}/modules

$(IMPORTS)/iao-extracted.owl: $(ROBOT_PATH)
	bash oeo-tools/oeo-imports/iao/extract-iao-module.sh

$(IMPORTS)/ro-extracted.owl: $(ROBOT_PATH)
	bash oeo-tools/oeo-imports/ro/extract-from-relations-ontology.sh

$(IMPORTS)/uo-extracted.owl: $(ROBOT_PATH)
	bash oeo-tools/oeo-imports/uo/extract-uo-module.sh

${VERSIONDIR}/imports:
	${MKDIR_P} ${VERSIONDIR}/imports

${VERSIONDIR}/modules:
	${MKDIR_P} ${VERSIONDIR}/modules

$(VERSIONDIR)/catalog-v001.xml: src/ontology/catalog-v001.xml
	cp $< $@
	$(call replace_devs,$@)
	sed -i -E "s/edits\//modules\//m" $@

build/robot.jar: | build
	curl -L -o $@ https://github.com/ontodev/robot/releases/download/v1.9.2/robot.jar


$(VERSIONDIR)/%.owl: $(VERSIONDIR)/%.omn
	$(call translate_to_owl,$@,$<)

$(VERSIONDIR)/modules/%.owl: $(VERSIONDIR)/edits/%.omn
	$(call translate_to_owl,$@,$<)

$(VERSIONDIR)/%.owl: $(ONTOLOGY_SOURCE)/%.owl
	cp -a $< $@
	$(call replace_devs,$@)

$(VERSIONDIR)/modules/%.owl: $(ONTOLOGY_SOURCE)/edits/%.owl
	cp -a $< $@
	$(call replace_devs,$@)

$(VERSIONDIR)/modules/%.omn: $(ONTOLOGY_SOURCE)/edits/%.omn
	cp -a $< $@
	$(call replace_devs,$@)

$(VERSIONDIR)/%.omn: $(ONTOLOGY_SOURCE)/%.omn
	cp -a $< $@
	$(call replace_devs,$@)

$(VERSIONDIR)/oeo-full.owl : | base
	$(ROBOT) merge --catalog $(VERSIONDIR)/catalog-v001.xml $(foreach f, $(VERSIONDIR)/oeo.owl $(OMN_COPY) $(OWL_COPY), --input $(f)) annotate --ontology-iri http://openenergy-platform.org/ontology/oeo/ --output $@
	$(call replace_oms,$@)

$(VERSIONDIR)/oeo-full.omn : $(VERSIONDIR)/oeo-full.owl
	$(call translate_to_omn,$@,$<)
	$(call replace_owls,$@)

$(VERSIONDIR)/oeo-closure.owl : $(VERSIONDIR)/oeo-full.owl
	$(ROBOT) reason --input $< --reasoner hermit --catalog $(VERSIONDIR)/catalog-v001.xml --axiom-generators "SubClass EquivalentClass DataPropertyCharacteristic EquivalentDataProperties SubDataProperty ClassAssertion EquivalentObjectProperty InverseObjectProperties ObjectPropertyCharacteristic SubObjectProperty ObjectPropertyRange ObjectPropertyDomain" --include-indirect true annotate --ontology-iri http://openenergy-platform.org/ontology/oeo/ --output $@
	$(ROBOT) merge --catalog $(VERSIONDIR)/catalog-v001.xml --input $< --input $@ annotate --ontology-iri http://openenergy-platform.org/ontology/oeo/ --output $@
