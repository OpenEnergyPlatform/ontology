"""
annotator.py

annotate automatically 
for every class in all oeo-modules
to which module this class belongs

@author: alexander stage    
"""

# Imports

import pathlib as path
import csv
import subprocess as sp
import os
import shutil as sh
import sys, time, threading
#import panda as pn
#import numpy as np

# Load 'static' values

ontology_iri = 'http://openenergy-platform.org/ontology/oeo'

modules = ['oeo-shared',
           'oeo-physical',
           'oeo-social',
           'oeo-model']

def find_root_dir(dirname : str):
    return find_root_dir_(path.Path('.').absolute(), dirname)

def find_root_dir_(cur_path : path.Path, dirname : str):
    if cur_path.name == dirname:
        return cur_path
    else:
        return find_root_dir_(cur_path.parent, dirname)
    
src_path = find_root_dir('src')

changes_exists = False
running = True

# src_path = path.Path('src').absolute()            <- use in IDE
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

def extract_IDs_Types(path) -> list:
    ids = []
    with open(path) as file:
        CSVreader = csv.reader(file)
        for row in CSVreader:
            if row[0].startswith('OEO'): 
                ids.append((row[0], row[1]))
    return ids

def main():
    global running
    global changes_exists
    try:
        os.mkdir(csv_path)
    except:
        pass

    col = 'ID|Type'                           
    _ = None
    ids_per_module = [_,_,_,_]

    prefixes = []
    
    oeo = open(src_path / 'ontology' / 'oeo.omn')

    lines = oeo.readlines()
    
    for line in lines:
        if line.startswith('Prefix:'):
            prefixes.append(line[8:-1])             #* Abhängig vom Prefix
        else:
            break
        

    # Load necessary IRIs of the different ontology-modules

    ids : set = set([])
    for (i,module) in enumerate(modules):
        mod = omn_path / "{m}.omn".format(m=module)
        exp = csv_path / "{m}.csv".format(m=module)
        
        sp.call('java -jar {jar} export --input {m} \
                                        --prefix "OEO: http://openenergy-platform.org/ontology/oeo/OEO_" \
                                        --header "{c}" \
                                        --export {e}'.format(jar=robot_path,
                                                             m=mod, 
                                                             c=col, 
                                                             e=exp), shell=True)
        
        tmp = extract_IDs_Types(csv_path / (module + '.csv'))
        ids = ids.union(set(tmp))
        ids_per_module[i] = tmp

    ids = list(ids)

    # Compare new data with database

    old_ids_per_module = [_,_,_,_]
    try:
        for i, module in enumerate(modules):
            old_ids_per_module[i] = extract_IDs_Types(db_path / (module + '.csv'))
    except:
        pass
    
    changes_exists = old_ids_per_module != ids_per_module
    if changes_exists:

        # Create overview about IRIs and there belonging
        
        """
        #! Check if duplicates exists in ids
        for i, x in enumerate(ids):
            for j, y in enumerate(ids):
                if i != j and x == y:
                    print("1:" + str(x))
        
        #! Check if duplicates exists in the seperate lists in ids_per_module
        for li in ids_per_module:
            for i, x in enumerate(li):
                for j, y in enumerate(li):
                    if i != j and x == y:
                        print("2:" + str(x))                                           
        
        """
        
        belonging = []

        for (i,id) in enumerate(ids):
            belonging.append([])
            for (j,module_ids) in enumerate(ids_per_module):
                if id in module_ids:
                    belonging[i].append(modules[j])

        # Create the CSV template with the help of the overview
        
        types = []
        
        for i, elem in enumerate(ids):
            types.append(elem[1])
            ids[i] = elem[0]
        
        belongs_to_module = list(zip(ids, types, belonging))
        
        csv_table = [["ID", "Entity Type", "OEO:00260001"],
                     ["ID", "TYPE", "AI OEO:00260001"]]

        csv_table_per_module = {'oeo-shared' : csv_table, 
                                'oeo-physical' : [a for a in csv_table], 
                                'oeo-social' : [a for a in csv_table], 
                                'oeo-model' : [a for a in csv_table]}

        # Add only one belonging to an entity
        # regarding to following rule:
        # IF in shared THEN annotate as shared ELSE annotate as the first in the list
        # Using Dictionaries instead of lists <dict>[<string>] instead of <list>[<int>] for better maintenance 
        #?DOMAIN EXPERTS: is another rule needed then priority
        for ids, type_, belonging in belongs_to_module:
            if 'oeo-shared' in belonging:
                csv_table_per_module['oeo-shared'].append([ids, 'owl:' + type_, ontology_iri + '/oeo-shared'])
            elif 'oeo-physical' in belonging:
                csv_table_per_module['oeo-physical'].append([ids, 'owl:' + type_, ontology_iri + '/oeo-physical'])
            elif 'oeo-social' in belonging:
                csv_table_per_module['oeo-social'].append([ids, 'owl:' + type_, ontology_iri + '/oeo-social'])
            elif 'oeo-model' in belonging:
                csv_table_per_module['oeo-model'].append([ids, 'owl:' + type_, ontology_iri + '/oeo-model'])
                
        prefix_adder = ""

        for prefix in prefixes[1:]:
            prefix_ = ""
            for c in prefix:
                if c != '<' and c != '>':
                    prefix_ += c
            prefix_adder += '--add-prefix \"{p}\" '.format(p=prefix_)
                
        for module in csv_table_per_module:
            f = open(script_path / 'btma' / "template.csv", 'w', newline='')

            writer = csv.writer(f)

            writer.writerows(csv_table_per_module[module])

            f.close()

            # Create OMN with help of the CSV template
            
            sp.call('java -jar {jar} template --template {template} \
                                              --add-prefix \"OEO: {iri}OEO_\" \
                                              --add-prefix \"owl: http://www.w3.org/2002/07/owl#\" \
                                              --output {out}'.format(jar=robot_path,
                                                                     template=script_path / 'btma' / 'template.csv',
                                                                     iri=ontology_iri + '/',
                                                                     pre=prefix_adder[-1],
                                                                     out=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=module)), shell=True)
        
        # MERGE OMN files with the oeo modules
        
        for module in csv_table_per_module:
            # Valid Call
            """
            sp.call('java -jar {jar} merge --input {out} \
                                           --input {inp} \
                                           --add-prefix \"OEO: {iri}OEO_\" \
                                           {pre} \
                                           --output {out} \
                                           --include-annotations true'.format(jar=robot_path,
                                                                              out=omn_path / (module + '.omn'),
                                                                              inp=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=module),
                                                                              pre=prefix_adder[:-1],
                                                                              iri=ontology_iri + '/'), shell=True)
            """
            # Test Call
            sp.call('java -jar {jar} merge --input {out} \
                                           --input {inp} \
                                           --add-prefix \"OEO: {iri}OEO_\" \
                                           {pre} \
                                           --output {out_} \
                                           --include-annotations true'.format(jar=robot_path,
                                                                              out=omn_path / (module + '.omn'),
                                                                              out_=omn_path / (module + '-new.omn'),
                                                                              inp=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=module),
                                                                              pre=prefix_adder[:-1],
                                                                              iri=ontology_iri + '/'), shell=True)
            
        os.remove(script_path / 'btma' / "template.csv")
    
        try:
            sh.rmtree(db_path)
        except:
            pass

        os.rename(csv_path, db_path)
        
        sh.rmtree(exp_path)

    else:
        sh.rmtree(csv_path)
        
    running = False    

def loadingAnimation(process):
    #global running
    while running:
        chars = '/—\|' 
        for char in chars:
            sys.stdout.write('\r'+'Running annotator... '+char)
            time.sleep(.1)
            sys.stdout.flush()
    #sys.stdout.flush()
    if not changes_exists:
        sys.stdout.write('\r'+'Annotations are already up to date.\n')
    sys.stdout.write('\r'+'Finished!                    ')
            
if __name__ == '__main__':
    loading_process = threading.Thread(target=main)
    loading_process.start()

    loadingAnimation(loading_process)
    loading_process.join()