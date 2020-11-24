MKDIR_P = mkdir -p
VERSION:= $(shell cat VERSION)
OURCEDIR := src
BUILDDIR := build
VERSIONDIR := $(BUILDDIR)/oeo/$(VERSION)
ONTOLOGY_SOURCE := src/ontology
OWL_FILES := $(shell find $(ONTOLOGY_SOURCE)/* -type f -name "*.owl")
OMN_FILES := $(shell find $(ONTOLOGY_SOURCE)/* -type f -name "*.omn")

OWL_COPY := $(OWL_FILES:$(ONTOLOGY_SOURCE)/%.owl=$(VERSIONDIR)/%.owl)
OMN_COPY :=	$(OMN_FILES:$(ONTOLOGY_SOURCE)/%.omn=$(VERSIONDIR)/%.omn)
OMN_TRANSLATE := $(OMN_FILES:$(ONTOLOGY_SOURCE)/%.omn=$(VERSIONDIR)/%.owl) 


RM=/bin/rm

$(VERSIONDIR)/%.owl: $(ONTOLOGY_SOURCE)/%.omn
	robot convert --input $< --output $@ --format owl
	sed -i -E "s/(http:\/\/openenergy-platform\.org\/ontology\/oeo\/releases\/(v[0-9]+\.[0-9]+\.[0-9]+)\/([A-z-]+)\.)omn/\1owl/m" $@

$(VERSIONDIR)/%.owl: $(ONTOLOGY_SOURCE)/%.owl
	cp -a $< $@

$(VERSIONDIR)/%.omn: $(ONTOLOGY_SOURCE)/%.omn
	cp -a $< $@
	

.PHONY: all clean

all: directories $(OMN_TRANSLATE) $(OWL_COPY) $(OMN_COPY)

clean:
	- $(RM) $(OMN_TRANSLATE) $(OWL_COPY) $(OMN_COPY)

directories: ${VERSIONDIR}/imports ${VERSIONDIR}/edits

${VERSIONDIR}/imports:
	${MKDIR_P} ${VERSIONDIR}/imports

${VERSIONDIR}/edits:
	${MKDIR_P} ${VERSIONDIR}/edits