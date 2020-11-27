MKDIR_P = mkdir -p
VERSION:= $(shell cat VERSION)
VERSIONDIR := build/oeo/$(VERSION)
ONTOLOGY_SOURCE := src/ontology
OWL_FILES := $(shell find $(ONTOLOGY_SOURCE)/imports/* -type f -name "*.owl")
OMN_FILES := $(shell find $(ONTOLOGY_SOURCE)/edits/* -type f -name "*.omn")

OEP_BASE := http:\/\/openenergy-platform\.org\/ontology\/oeo

OWL_COPY := $(OWL_FILES:$(ONTOLOGY_SOURCE)/%.owl=$(VERSIONDIR)/%.owl)
OMN_COPY :=	$(OMN_FILES:$(ONTOLOGY_SOURCE)/edits/%.omn=$(VERSIONDIR)/modules/%.omn) $(VERSIONDIR)/oeo.omn
OMN_TRANSLATE := $(OMN_FILES:$(ONTOLOGY_SOURCE)/edits/%.omn=$(VERSIONDIR)/modules/%.owl) $(VERSIONDIR)/oeo.owl

RM=/bin/rm
ROBOT_PATH := build/robot.jar
ROBOT := java -jar $(ROBOT_PATH)


define replace_devs
	sed -i -E "s/$(OEP_BASE)\/dev\/([A-z/-\.]+)/$(OEP_BASE)\/releases\/$(VERSION)\/\1/m" $1
endef

define replace_oms
	sed -i -E "s/($(OEP_BASE)\/dev\/([A-z/-]+)\.)omn/\1owl/m" $1
endef

define translate_to_owl
	$(ROBOT) convert --input $2 --output $1 --format owl
	$(call replace_omns,$1)
	$(call replace_devs,$1)
endef

.PHONY: all clean base merge directories

.IGNORE: $(VERSIONDIR)/oeo-full.omn $(VERSIONDIR)/oeo-full.owl

all: base merge

base: | directories build/robot.jar $(OMN_TRANSLATE) $(OWL_COPY) $(OMN_COPY)

merge: | $(VERSIONDIR)/oeo-full.owl

clean:
	- $(RM) -r $(VERSIONDIR) $(ROBOT_PATH)

directories: ${VERSIONDIR}/imports ${VERSIONDIR}/modules

${VERSIONDIR}/imports:
	${MKDIR_P} ${VERSIONDIR}/imports

${VERSIONDIR}/modules:
	${MKDIR_P} ${VERSIONDIR}/modules

build/robot.jar: | build
	curl -L -o $@ https://github.com/ontodev/robot/releases/download/v1.4.1/robot.jar


$(VERSIONDIR)/%.owl: $(ONTOLOGY_SOURCE)/%.omn
	$(call translate_to_owl,$@,$<)

$(VERSIONDIR)/modules/%.owl: $(ONTOLOGY_SOURCE)/edits/%.omn
	$(call translate_to_owl,$@,$<)

$(VERSIONDIR)/%.owl: $(ONTOLOGY_SOURCE)/%.owl
	cp -a $< $@
	$(call replace_devs,$@)

$(VERSIONDIR)/modules/%.omn: $(ONTOLOGY_SOURCE)/edits/%.omn
	cp -a $< $@
	$(call replace_devs,$@)

$(VERSIONDIR)/%.omn: $(ONTOLOGY_SOURCE)/%.omn
	cp -a $< $@
	$(call replace_devs,$@)

$(VERSIONDIR)/oeo-full.omn : | base
	$(ROBOT) merge $(foreach f,$(OMN_COPY), --input $(f)) annotate --ontology-iri http://openenergy-platform.org/ontology/oeo/ --output $@

$(VERSIONDIR)/oeo-full.owl : $(VERSIONDIR)/oeo-full.omn
	$(call translate_to_owl,$@,$<)
	$(call replace_omns,$@)