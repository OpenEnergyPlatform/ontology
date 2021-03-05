
import logging
import rdflib
import time
from rdflib.namespace import *

def findConcept(ontologyPath, term):
    g = rdflib.Graph()
    g.parse (ontologyPath, format='turtle')
    variable1= "".join(["\"", term.lower() , "\""])
    query= ' '.join(['select distinct ?s where { ?s rdfs:label ', variable1,"} LIMIT 1"])
    result = g.query(query)
    for row in result:
        return row[0]



from rdflib import Graph, Literal, RDF, URIRef, RDFS, OWL
from rdflib.namespace import *
import os
import fnmatch

OEO = Namespace("http://openenergy-platform.org/ontology/oeo/")
OEO_KG =Namespace("http://openenergy-platform.org/thing/")
dbp = Namespace("http://dbpedia.org/resource/")
dbo = Namespace("http://dbpedia.org/ontology/")
schema = Namespace("https://schema.org/")
obo= Namespace("http://purl.obolibrary.org/obo/") 
npg= Namespace("http://ns.nature.com/terms/")
wikidata= Namespace("https://www.wikidata.org/wiki/")
SIO= Namespace("http://semanticscience.org/resource/")
owl= Namespace("http://www.w3.org/2002/07/owl#")
rdfs= Namespace("http://www.w3.org/2000/01/rdf-schema#")


# create a Graph
g = Graph()


#--------------------- find the input files ---------------
def loop_directory(directory: str, fileList:list, pattern:str):       
        for filename in os.listdir(directory):
            if fnmatch.fnmatch(filename, pattern):
                fileList.append(filename)

#----------------------------------------------------------                

def formStudyReport(g,title, studyReportIns, subtitle,abstract,study_report_url,Year_of_publication):
    studyReportIns = URIRef("http://openenergy-platform.org/thing/"+title[0:35].rstrip().replace("-","_").replace("%","").replace("Ö","Oe").replace("ö","oe").replace("ü","ue").replace("ä","ae").replace(".", "").replace(" ","_"))
    g.add((studyReportIns, RDF.type, OEO.OEO_00020012)) # study report
    g.add((studyReportIns, DC.title, Literal(title)))
    if subtitle!=None:
        g.add((studyReportIns, dbo.subtitle, Literal(subtitle)))
    if abstract!=None:
        g.add((studyReportIns, dbo.abstract, Literal(abstract)))
    if study_report_url!=None:
        g.add((studyReportIns, schema.url, Literal(study_report_url)))
    if Year_of_publication!=None:
        g.add((studyReportIns, npg.publicationYear, Literal(Year_of_publication, datatype=XSD.integer)))
    
    return studyReportIns

#---------------------------------------------------------------------------------------

def formStudy(g , study_id, studyIns, studyReportIns, funding_institution, energy_carriers, sectors, study_region, interacting_region, scenario_IDs, scenario_names, scenario_abbreviations, scenario_abstracts ):
    studyIns = URIRef("http://openenergy-platform.org/thing/" + study_id)
    g.add((studyIns, RDF.type, OEO.OEO_00020011)) # study
    g.add((studyReportIns, obo.IAO_0000136, studyIns)) # is about

    for f in funding_institution:
        #print(f)
        temp=f.lstrip().rstrip().replace(" ", "_").replace("-","_").replace("Ö","Oe").replace("ü","ue").replace("ä","ae").replace(".", "")
        fInst= URIRef("http://openenergy-platform.org/thing/" + temp.lstrip().rstrip())
        g.add((fInst, FOAF.name, Literal(f.lstrip().rstrip())))
        g.add((studyIns, OEO.OEO_00000509, fInst))#has funding source
    
    for ec in energy_carriers:
        conceptID= findConcept('oboRobot/oeoMerged.ttl',ec)
        if (conceptID != None):
            g.add((studyIns, OEO.OEO_00000523, conceptID))#study covers_energycarrier
            #print(ec+ ":"+ str(findConcept('oboRobot/oeoMerged.ttl',ec)))
    
    ## create analysis scope as an individual of the type OWL:Thing
    analysisScopeIns = URIRef("http://openenergy-platform.org/thing/" + study_id+ "_analysis_scope")
    g.add((analysisScopeIns, RDF.type, RDFS.Class)) # analysis scope
    g.add ((analysisScopeIns, RDFS.label, Literal("analysis scope of a specific study")))
    #g.add((analysisScopeIns, RDF.type, OWL.Thing)) # analysis scope
    
    # add study region (OEO_00020032) to the analysis scope
    studyRegionIns = URIRef("http://openenergy-platform.org/thing/" + study_id+ "_study_region")
    g.add((studyRegionIns, RDF.type, OEO.OEO_00020032)) # study region instance(OEO_00020032)
    g.add((studyRegionIns, RDFS.label, Literal(study_region))) 
    
    
    # add interacting region to the analysis scope
    interactingRegionIns = URIRef("http://openenergy-platform.org/thing/" + study_id+ "_interacting_region")
    g.add((interactingRegionIns, RDF.type, OEO.OEO_00020036)) # interacting region instance(OEO_00020036)
    g.add((interactingRegionIns, RDFS.comment, Literal(interacting_region))) 
    
    
    # the analysis scope covers (OEO_00000522) both the study region and the interacting region
    g.add((analysisScopeIns, OEO.OEO_00000522, studyRegionIns)) 
    g.add((analysisScopeIns, OEO.OEO_00000522, interactingRegionIns)) 
    
    
    # add sectors to the analysis scope
    for sec in sectors:
        g.add((analysisScopeIns, OEO.OEO_00000505, URIRef("http://openenergy-platform.org/ontology/oeo/" + sec ))) # analysis scope covers sector(OEO_00000505)
   
    
    for (q,w,e,r) in zip(scenario_IDs, scenario_names, scenario_abbreviations, scenario_abstracts):  
        #q2= q.replace("Ö","Oe").replace("ö","oe").replace("ü","ue").replace("ä","ae").replace(".", "").replace(" ","_")
        scenarioIns = URIRef("http://openenergy-platform.org/thing/" + q) # OEO_00000364
        g.add((scenarioIns, RDF.type, OEO.OEO_00000364))
        g.add((scenarioIns, FOAF.name, Literal(w)))
        g.add((scenarioIns, dbo.abbreviation, Literal(e)))
        g.add((scenarioIns, dbo.abstract, Literal(r)))
        #g.add((studyIns, obo.BFO_0000051, scenarioIns)) # study has part (= BFO_0000051) some scenario
        g.add((studyIns, obo.RO_0000057, scenarioIns)) # study has participant (= RO_0000057) some scenario
        g.add((analysisScopeIns, OEO.OEO_00000504, scenarioIns)) # analysis scope is defined by scenario
    
    return studyIns

#---------------------------------------------------------------------------------------

def formInstitutions(g , affiliantions, authors_list, studyReportIns):
    institutions=affiliantions.split(",")
    #print(institutions)
    for (x,y) in zip(institutions, authors_list):
        #print(x, y)
        m=x.lstrip().rstrip().replace(" ", "_").replace("-","_").replace("Ö","Oe").replace("ü","ue").replace("ä","ae").replace(".", "")
        inst= URIRef("http://openenergy-platform.org/thing/" + m.lstrip().rstrip())
        g.add((inst, FOAF.name, Literal(x.lstrip().rstrip())))
        # Create an RDF URI node to use as the subject for multiple triples
        p=y.lstrip().rstrip().replace(" ", "_").replace("-","_").replace("Ö","Oe").replace("ö","oe").replace("ü","ue").replace("Ü","Ue").replace("ä","ae").replace("Ä","Ae").replace(".", "")
        donna = URIRef("http://openenergy-platform.org/thing/"+ p)
        g.add((donna, RDF.type, FOAF.Person))
        g.add((donna, FOAF.givenName, Literal(y.split()[0])))
        g.add((donna, FOAF.familyName, Literal(y.split()[-1])))
        if (len(y.split())==3):
            g.add((donna, SIO.SIO_001317, Literal(y.split()[1])))# middle name
        g.add((donna, schema.affiliation, inst))
        g.add((donna, obo.RO_0000087, OEO.OEO_00000064)) # has_role author
        g.add((studyReportIns, OEO.OEO_00000506, donna)) # has_author
        
##-------------------------------------------------------------------------------------


cwd = os.getcwd()
fileList=list()
loop_directory(cwd, fileList, 'in*.txt')
#print(fileList)
#----------- reading new information ------
for file in fileList:
    f = open(file, "r")

    study_id=None
    title=None
    subtitle=None
    authors_list=None
    affiliantions=None
    funding_institution=None
    study_report_url=None
    Year_of_publication=None
    abstract=None

    studyIns=None
    studyReportIns=None


    #f = open("inputPszV.txt", "r")
    for aline in f:
        values = aline.split("=")
        if(values[0]=='study'):
            study_id=values[1].lstrip().rstrip()
        elif (values[0]=='title'):
            title=values[1].lstrip().rstrip()
        elif(values[0]=='subtitle'):
            subtitle=values[1].lstrip().rstrip()
        elif(values[0]=='authors_list'):
            authors_list=values[1].lstrip().rstrip().split(",")
        elif(values[0]=='affiliantions'):
            affiliantions=values[1].lstrip().rstrip()
        elif(values[0]=='funding_institution'):
            funding_institution=values[1].lstrip().rstrip().split(",")
        elif(values[0]=='study_report_url'):
            study_report_url=values[1].lstrip().rstrip()
        elif(values[0]=='Year_of_publication'):
            Year_of_publication=values[1].lstrip().rstrip()
        elif(values[0]=='abstract'):
            abstract=values[1].lstrip().rstrip()
        elif(values[0]=='energy_carriers'):
            energy_carriers=values[1].lstrip().rstrip().split(",")
        elif(values[0]=='sectors'):
            sectors=values[1].lstrip().rstrip().split(",")
        elif(values[0]=='study_region'):
            study_region=values[1].lstrip().rstrip()
        elif(values[0]=='interacting_region'):
            interacting_region=values[1].lstrip().rstrip()
        elif(values[0]=='scenario_IDs'):
            scenario_IDs=values[1].lstrip().rstrip().split(",")
        elif(values[0]=='scenario_names'):
            scenario_names=values[1].lstrip().rstrip().split(",")
        elif(values[0]=='scenario_abbreviations'):
            scenario_abbreviations=values[1].lstrip().rstrip().split(",")
        elif(values[0]=='scenario_abstracts'):
            scenario_abstracts=values[1].lstrip().rstrip().split("###")
            #print(scenario_abstracts)
            
        


    #f.close()

    #---------------- study report-------------

    studyReportIns= formStudyReport(g,title, studyReportIns, subtitle,abstract,study_report_url,Year_of_publication)

    #print(studyReportIns)
    #--------------- study --------------------

    studyIns= formStudy(g , study_id, studyIns, studyReportIns, funding_institution, energy_carriers, sectors, study_region, interacting_region, scenario_IDs, scenario_names, scenario_abbreviations, scenario_abstracts)
    #print(studyIns)
    #-------- institutions --------------------

    formInstitutions(g , affiliantions, authors_list, studyReportIns)



    # ----------------------------Bind the FOAF namespace to a prefix for more readable output
    g.bind("foaf", FOAF)
    g.bind("OEO", OEO)
    g.bind("OEO_KG", OEO_KG)
    g.bind("dbp", dbp)
    g.bind("schema", schema)
    g.bind("obo", obo)
    g.bind("dc", DC)
    g.bind("dbo", dbo)
    g.bind("npg", npg)
    g.bind("SIO", SIO)
    g.bind("owl", owl)
    g.bind("rdfs", rdfs)
    # -------------------------------print all the data in the Notation3 format
    #print("--- print all the data in the Notation3 format ---")
    #print(g.serialize(format='n3').decode("utf-8"))
    g.serialize(destination=file.replace("input", "").replace(".txt","")+'-KG.ttl', format='turtle')


cwd = os.getcwd()
outList=list()
loop_directory(cwd, outList, '*KG.ttl')
print(outList)





g0 = Graph()
g0.parse(outList[0], format="turtle")

g1 = Graph()
g1.parse(outList[1], format="turtle")

graph = g0 + g1

graph.serialize("KG.ttl", format="turtle")

g2=Graph()

for kg in outList:
    g2.parse("KG.ttl", format="turtle")
    g3=Graph()
    g3.parse(kg, format="turtle")
    graph = g2 + g3
    graph.serialize("KG.ttl", format="turtle")




