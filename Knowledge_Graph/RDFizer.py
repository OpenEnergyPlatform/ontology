#!/usr/bin/env python
# coding: utf-8

# In[49]:


from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import *
import os
import fnmatch

OEO = Namespace("https://openenergy-platform.org/ontology/oeo/")
OEO_KG =Namespace("https://openenergy-platform.org/thing/")
dbp = Namespace("http://dbpedia.org/resource/")
dbo = Namespace("http://dbpedia.org/ontology/")
schema = Namespace("https://schema.org/")
obo= Namespace("http://purl.obolibrary.org/obo/") 
npg= Namespace("http://ns.nature.com/terms/")
wikidata= Namespace("https://www.wikidata.org/wiki/")
SIO= Namespace("http://semanticscience.org/resource/")


# create a Graph
g = Graph()


#--------------------- find the input files ---------------
def loop_directory(directory: str, fileList:list, pattern:str):       
        for filename in os.listdir(directory):
            if fnmatch.fnmatch(filename, pattern):
                fileList.append(filename)

#----------------------------------------------------------                

def formStudyReport(g,title, studyReportIns, subtitle,abstract,study_report_url,Year_of_publication):
    studyReportIns = URIRef("https://openenergy-platform.org/thing/"+title.rstrip().replace("-","_").replace("Ö","Oe").replace(".", "").replace(" ","_"))
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

def formStudy(g , study_id, studyIns, studyReportIns, funding_institution):
    studyIns = URIRef("https://openenergy-platform.org/thing/" + study_id)
    g.add((studyIns, RDF.type, OEO.OEO_00020011)) # study
    g.add((studyReportIns, obo.IAO_0000136, studyIns)) # is about

    for f in funding_institution:
        #print(f)
        temp=f.lstrip().rstrip().replace(" ", "_").replace("-","_").replace("Ö","Oe").replace(".", "")
        fInst= URIRef("https://openenergy-platform.org/thing/" + temp.lstrip().rstrip())
        g.add((fInst, FOAF.name, Literal(f.lstrip().rstrip())))
        g.add((studyIns, OEO.OEO_00000509, fInst))#has funding source
    
    return studyIns

#---------------------------------------------------------------------------------------

def formInstitutions(g , affiliantions, authors_list, studyReportIns):
    institutions=affiliantions.split(",")
    #print(institutions)
    for (x,y) in zip(institutions, authors_list):
        #print(x, y)
        m=x.lstrip().rstrip().replace(" ", "_").replace("-","_").replace("Ö","Oe").replace(".", "")
        inst= URIRef("https://openenergy-platform.org/thing/" + m.lstrip().rstrip())
        g.add((inst, FOAF.name, Literal(x.lstrip().rstrip())))
        # Create an RDF URI node to use as the subject for multiple triples
        donna = URIRef("https://openenergy-platform.org/thing/"+ y.replace(" ", "_"))
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



    #f.close()

    #---------------- study report-------------

    studyReportIns= formStudyReport(g,title, studyReportIns, subtitle,abstract,study_report_url,Year_of_publication)

    #print(studyReportIns)
    #--------------- study --------------------

    studyIns= formStudy(g , study_id, studyIns, studyReportIns, funding_institution)
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

    # -------------------------------print all the data in the Notation3 format
    #print("--- print all the data in the Notation3 format ---")
    #print(g.serialize(format='n3').decode("utf-8"))
    g.serialize(destination=file.replace("input", "").replace(".txt","")+'-KG.ttl', format='turtle')


cwd = os.getcwd()
outList=list()
loop_directory(cwd, outList, '*KG.ttl')
#print(outList)





g0 = Graph()
g0.parse(outList[0], format="turtle")

g1 = Graph()
g1.parse(outList[1], format="turtle")

graph = g0 + g1

graph.serialize("file1.ttl", format="turtle")

g2=Graph()

for kg in outList:
    g2.parse("file1.ttl", format="turtle")
    g3=Graph()
    g3.parse(kg, format="turtle")
    graph = g2 + g3
    graph.serialize("KG.ttl", format="turtle")
