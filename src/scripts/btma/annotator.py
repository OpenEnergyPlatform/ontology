"""
annotator.py

annotate automatically 
for every class in all oeo-modules
to which module this class belongs

@author: alexander stage    
"""

# Imports

import timeit as tt
import pathlib as path
import csv
import subprocess as sp
import os
import shutil as sh
#import panda as pn
#import numpy as np

# Load 'static' values

ontology_iri = 'http://openenergy-platform.org/ontology/oeo'

modules = ['oeo-shared',
           'oeo-physical',
           'oeo-social',
           'oeo-model']


src_path = path.Path(__file__).parent.parent.parent.absolute()
script_path = src_path / 'scripts'

omn_path = src_path / 'ontology' / 'edits'
btma_path = script_path / 'btma'
csv_path = btma_path / 'data'
db_path = btma_path / 'database'
exp_path = btma_path / 'exports'
onto_path = src_path / 'ontology'
owl_path = onto_path / 'imports'
robot_path = btma_path / 'robot.jar'
pre_path = btma_path / 'prefixes'

def export_prefixes():
    pass

def extract_IDs(path) -> list:
    file = open(path)
    CSVreader = csv.reader(file)
    ids = []
    for row in CSVreader:
        t = row[0].split('_')
        if t[0] == ontology_iri + '/OEO': 
            ids.append(t[1])
    return ids

def main():
    try:
        os.mkdir(csv_path)
    except:
        pass

    col = 'ID'                           
    _ = None
    ids_per_module = [_,_,_,_]

    prefixes = []
    
    oeo = open(src_path / 'ontology' / 'oeo.omn')

    lines = oeo.readlines()
    
    for line in lines:
        if line.startswith('Prefix:'):
            prefixes.append(line[8:-1])
        else:
            break
        

    # Load necessary IRIs of the different ontology-modules

    print('Loading ontologies...')
    ids : set = set([])
    for (i,module) in enumerate(modules):
        mod = omn_path / "{m}.omn".format(m=module)
        exp = csv_path / "{m}.csv".format(m=module)
        
        sp.call('java -jar {jar} export --input {m} \
                                        --header "{c}" \
                                        --export {e}'.format(jar=robot_path,
                                                             m=mod, 
                                                             c=col, 
                                                             e=exp))
        
        tmp = extract_IDs(csv_path / (module + '.csv'))
        ids = ids.union(set(tmp))
        ids_per_module[i] = tmp

    ids = list(ids)

    # Compare new data with database

    old_ids_per_module = [_,_,_,_]
    try:
        for i, module in enumerate(modules):
            old_ids_per_module[i] = extract_IDs(db_path / (module + '.csv'))
    except:
        pass
        
    if old_ids_per_module != ids_per_module:

        # Create overview about IRIs and there belonging

        print('Finding belongings...')

        belonging = []

        for (i,id) in enumerate(ids):
            belonging.append([])
            for (j,module_ids) in enumerate(ids_per_module):
                if id in module_ids:
                    belonging[i].append(modules[j])

        # Create the CSV template with the help of the overview

        print('Creating template...')
        
        belongs_to_module = list(zip(ids, belonging))

        csv_table = [["ID","belongs to module"],
                     ["ID","AI OEO:belongs_to_module"]]

        csv_table_per_module = (csv_table, csv_table, csv_table, csv_table)

        # Add only one belonging to an entity
        # regarding to following rule:
        # IF in shared THEN annotate as shared ELSE annotate as the first in the list
        #TODO: May use Dictionaries instead of lists <dict>[<string>] instead of <list>[<int>]   
        #?DOMAIN EXPERTS: is another needed then priority
        for (ids, belonging) in belongs_to_module:
            if 'oeo-shared' in belonging:
                csv_table_per_module[0].append(['OEO:' + ids, ontology_iri + '/oeo-shared'])
            elif 'oeo-physical' in belonging:
                csv_table_per_module[1].append(['OEO:' + ids, ontology_iri + '/oeo-physical'])
            elif 'oeo-social' in belonging:
                csv_table_per_module[2].append(['OEO:' + ids, ontology_iri + '/oeo-social'])
            elif 'oeo-model' in belonging:
                csv_table_per_module[3].append(['OEO:' + ids, ontology_iri + '/oeo-model'])
        
        print('Loading prefixes...')
        
        start = tt.timeit()

        prefix_adder = ""

        for prefix in prefixes[1:]:
            prefix_ = ""
            for c in prefix:
                if c != '<' and c != '>':
                    prefix_ += c
            prefix_adder += '--add-prefix \"{p}\" '.format(p=prefix_)

        end = tt.timeit()
        
        #!
        print(end - start)
        
        print('Creating ontologies...')
        
        for (i, csv_table) in enumerate(csv_table_per_module):
            f = open(script_path / 'btma' / "template.csv", 'w', newline='')

            writer = csv.writer(f)

            writer.writerows(csv_table)

            f.close()

            # Create OWL/XML with help of the CSV template
            
            sp.call('java -jar {jar} template --template {template} \
                                              --add-prefix \"OEO: {iri}OEO_\" \
                                              --output {out}'.format(jar=robot_path,
                                                                     template=script_path / 'btma' / 'template.csv',
                                                                     iri=ontology_iri + '/',
                                                                     pre=prefix_adder[-1],
                                                                     out=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=modules[i])))
        # MERGE OMN files with the oeo modules
        
        for i in range(len(csv_table_per_module)):
            # Valid Call
            """
            sp.call('java -jar {jar} merge --input {out} \
                                           --input {inp} \
                                           --add-prefix \"OEO: {iri}OEO_\" \
                                           {pre} \
                                           --output {out} \
                                           --include-annotations true'.format(jar=robot_path,
                                                                              out=omn_path / (modules[i] + '.omn'),
                                                                              inp=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=modules[i]),
                                                                              pre=prefix_adder[:-1],
                                                                              iri=ontology_iri + '/'))
            """
            # Test Call
            sp.call('java -jar {jar} merge --input {out} \
                                           --input {inp} \
                                           --add-prefix \"OEO: {iri}OEO_\" \
                                           {pre} \
                                           --output {out_} \
                                           --include-annotations true'.format(jar=robot_path,
                                                                              out=omn_path / (modules[i] + '.omn'),
                                                                              out_=omn_path / (modules[i] + '-new.omn'),
                                                                              inp=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=modules[i]),
                                                                              pre=prefix_adder[:-1],
                                                                              iri=ontology_iri + '/'))
            
        os.remove(script_path / 'btma' / "template.csv")
    
        try:
            sh.rmtree(db_path)
        except:
            pass

        os.rename(csv_path, db_path)
        
        sh.rmtree(exp_path)

    else:
        print('Annotations are up to date.')
        
        sh.rmtree(csv_path)

    print('Finished!')
    
if __name__ == '__main__':
    main()
