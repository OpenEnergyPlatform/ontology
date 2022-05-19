MKDIR_P = mkdir -p
VERSION:= $(shell cat VERSION)
VERSIONDIR := build/oeo/$(VERSION)
ONTOLOGY_SOURCE := src/ontology

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

UNION_FILE := $(shell mktemp).omn

define replace_devs
	sed -i -E "s/$(OEP_BASE)\/dev\/([a-zA-Z/\.\-]+)/$(OEP_BASE)\/releases\/$(VERSION)\/\1/m" $1
endef

define replace_oms
	sed -i -E "s/($(OEP_BASE)\/dev\/([a-zA-Z/\-]+)\.)omn/\1owl/m" $1
endef

define translate_to_owl
	$(ROBOT) convert --input $2 --output $1 --format owl
	$(call replace_omns,$1)
	$(call replace_devs,$1)
endef

.PHONY: all clean base merge directories

all: base merge

base: | directories $(VERSIONDIR)/catalog-v001.xml build/robot.jar $(OMN_TRANSLATE) $(OWL_COPY) $(OMN_COPY)

merge: | $(VERSIONDIR)/oeo-full.owl

clean:
	- $(RM) -r $(VERSIONDIR) $(ROBOT_PATH)

directories: ${VERSIONDIR}/imports ${VERSIONDIR}/modules

${VERSIONDIR}/imports:
	${MKDIR_P} ${VERSIONDIR}/imports

${VERSIONDIR}/modules:
	${MKDIR_P} ${VERSIONDIR}/modules

$(VERSIONDIR)/catalog-v001.xml: src/ontology/catalog-v001.xml
	cp $< $@
	$(call replace_devs,$@)
	sed -i -E "s/edits\//modules\//m" $@

build/robot.jar: | build
	curl -L -o $@ https://github.com/ontodev/robot/releases/latest/download/robot.jar
	
$(VERSIONDIR)/%.owl: $(ONTOLOGY_SOURCE)/%.omn
	$(call translate_to_owl,$@,$<)

$(VERSIONDIR)/modules/%.owl: $(ONTOLOGY_SOURCE)/edits/%.omn
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

$(VERSIONDIR)/oeo-full.omn : | base
	$(ROBOT) merge --catalog $(VERSIONDIR)/catalog-v001.xml $(foreach f, $(VERSIONDIR)/oeo.omn $(OMN_COPY) $(OWL_COPY), --input $(f)) annotate --ontology-iri http://openenergy-platform.org/ontology/oeo/ --output $(UNION_FILE)
	$(ROBOT) reason --create-new-ontology true --catalog $(VERSIONDIR)/catalog-v001.xml --input $(UNION_FILE) annotate --ontology-iri http://openenergy-platform.org/ontology/oeo/ --output $@

$(VERSIONDIR)/oeo-full.owl : $(VERSIONDIR)/oeo-full.omn
	$(call translate_to_owl,$@,$<)
	$(call replace_omns,$@)
