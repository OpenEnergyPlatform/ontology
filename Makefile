MKDIR_P = mkdir -p
VERSION:= $(shell cat VERSION)
VERSIONDIR := build/oeo/$(VERSION)
ONTOLOGY_SOURCE := src/ontology
OWL_FILES := $(shell find $(ONTOLOGY_SOURCE)/imports/* -type f -name "*.owl")
OMN_FILES := $(shell find $(ONTOLOGY_SOURCE)/edits/* -type f -name "*.omn")

OWL_COPY := $(OWL_FILES:$(ONTOLOGY_SOURCE)/%.owl=$(VERSIONDIR)/%.owl)
OMN_COPY :=	$(OMN_FILES:$(ONTOLOGY_SOURCE)/edits/%.omn=$(VERSIONDIR)/modules/%.omn) $(VERSIONDIR)/oeo.omn
OMN_TRANSLATE := $(OMN_FILES:$(ONTOLOGY_SOURCE)/edits/%.omn=$(VERSIONDIR)/modules/%.owl) $(VERSIONDIR)/oeo.omn

RM=/bin/rm

$(VERSIONDIR)/oeo.owl: $(ONTOLOGY_SOURCE)/oeo.omn
	$(ROBOT) convert --input $< --output $@ --format owl
	sed -i -E "s/(http:\/\/openenergy-platform\.org\/ontology\/oeo\/releases\/(v[0-9]+\.[0-9]+\.[0-9]+)\/([A-z-]+)\.)omn/\1owl/m" $@

$(VERSIONDIR)/modules/%.owl: $(ONTOLOGY_SOURCE)/edits/%.omn
	$(ROBOT) convert --input $< --output $@ --format owl
	sed -i -E "s/(http:\/\/openenergy-platform\.org\/ontology\/oeo\/releases\/(v[0-9]+\.[0-9]+\.[0-9]+)\/([A-z-]+)\.)omn/\1owl/m" $@

$(VERSIONDIR)/%.owl: $(ONTOLOGY_SOURCE)/%.owl
	cp -a $< $@

$(VERSIONDIR)/modules/%.omn: $(ONTOLOGY_SOURCE)/edits/%.omn
	cp -a $< $@

$(VERSIONDIR)/%.omn: $(ONTOLOGY_SOURCE)/%.omn
	cp -a $< $@


.PHONY: all clean

all: directories build/robot.jar $(OMN_TRANSLATE) $(OWL_COPY) $(OMN_COPY)

clean:
	- $(RM) -r $(VERSIONDIR) $(ROBOT_PATH)

directories: ${VERSIONDIR}/imports ${VERSIONDIR}/modules

${VERSIONDIR}/imports:
	${MKDIR_P} ${VERSIONDIR}/imports

${VERSIONDIR}/modules:
	${MKDIR_P} ${VERSIONDIR}/modules

build/robot.jar: | build
	curl -L -o $@ https://github.com/ontodev/robot/releases/download/v1.4.1/robot.jar

ROBOT_PATH := build/robot.jar
ROBOT := java -jar $(ROBOT_PATH)