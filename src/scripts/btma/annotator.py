"""
annotator.py

annotate automatically 
for every class in all oeo-modules
to which module this class belongs

@author: alexander stage    
"""

#* Imports
import io
import pathlib as path
import csv
import subprocess as sp
import os
import shutil as sh
import sys, time, threading

#* Define used methods

def find_root_dir(dirname : str) -> path.Path:
    """
    Finds the parent directory named `dirname` of the current directory.

    Args:
        `dirname (str)`: name of the current file directory

    Returns:
        `path.Path`: parent path of the directory with the name `dirname` in this project
    """
    return __find_root_dir(path.Path('.').absolute(), dirname)

def __find_root_dir(cur_path : path.Path, dirname : str) -> path.Path:
    if cur_path.name == dirname:
        return cur_path
    else:
        return __find_root_dir(cur_path.parent, dirname)

#* Create overview about IRIs and there belonging

def extract_belongings(ids : set, ids_per_module) -> list:
    """
    Extracts the belonging of each ID

    Args:
        `ids (set)`: set of IDs
        `ids_per_module (_type_)`: partition of `ids` in modules

    Returns:
        `list`: list of IDs per modules
    """
    belongings : list = []

    for (i,id) in enumerate(ids):
        belongings.append([])
        for (j,module_ids) in enumerate(ids_per_module):
            if id in module_ids:
                belongings[i].append(modules[j])
                
    return belongings

def extract_types(ids) -> list:
    """
    Assigns each ID to its type.

    Args:
        `ids`: list of IDs

    Returns:
        `list`: list of the types of each ID
    """
    types = []
    for i, elem in enumerate(ids):
            types.append(elem[1])
            ids[i] = elem[0]
    return types


def extract_IDs_Types(path : path.Path) -> list:
    """
    Extract ID and Type of each entity.

    Args:
        `path (path.Path)`: The path of a CSV-file with IDs and Types in the first and second column

    Returns:
        `list`: List of Tuples e.g. [(<ID_1>,<Type_1>),...,(<ID_N>,<Type_N>)]
    """
    ids = []
    with open(path) as file:
        CSVreader = csv.reader(file)
        for row in CSVreader:
            if row[0].startswith('OEO'):
                id = row[0]
                typ = row[1]
                if typ == 'Class':
                    typ = typ.lower()
                ids.append((id, typ))
    return ids


def reset_btma():
    """
    Reset the project at the end of the script.
    """
    os.remove(script_path / 'btma' / "template.csv")
    try:
        sh.rmtree(db_path)
    except:
        pass
    os.rename(csv_path, db_path)
    sh.rmtree(exp_path)


def __loadingAnimation(process):
    while running:
        chars = '/—\|' 
        for char in chars:
            sys.stdout.write('\r'+'Running annotator... '+char)
            time.sleep(.1)
            sys.stdout.flush()
    if not changed:
        sys.stdout.write('\r'+'Annotations are already up to date.\n')
    sys.stdout.write('\r'+'Finished!                    ')


def main():
    global running
    global changed
    
    try:
        os.mkdir(csv_path)
    except:
        pass

    col = 'ID|Type'                           
    _ = None
    ids_per_module = [_,_,_,_]

    #* Load necessary IRIs of the different ontology-modules

    ids : set = set([])
    for (i,module) in enumerate(modules):
        mod = omn_path / "{m}.omn".format(m=module)
        exp = csv_path / "{m}.csv".format(m=module)
        
        sp.call('java -jar {jar} export --input {m} \
                                        --prefix "OEO: {iri}" \
                                        --header "{c}" \
                                        --export {e}'.format(jar=robot_path,
                                                             m=mod, 
                                                             iri=ontology_iri + '/OEO_', 
                                                             c=col, 
                                                             e=exp), shell=True)
        
        tmp = extract_IDs_Types(csv_path / (module + '.csv'))
        ids = ids.union(set(tmp))
        ids_per_module[i] = tmp

    ids = list(ids)

    #* Compare new data with database

#    old_ids_per_module = [_,_,_,_]
#    try:
#        for i, module in enumerate(modules):
#            old_ids_per_module[i] = extract_IDs_Types(db_path / (module + '.csv'))
#    except:
#        pass
#
#    changed = old_ids_per_module != ids_per_module
    #* edit omn if and only if omn was changed
    if changed:
        #* Create the CSV template with the help of an 'overview'
        
        belongings : list[list] = extract_belongings(ids, ids_per_module)
        
        types = extract_types(ids)
        
        belongs_to_module = list(zip(ids, types, belongings))
        
        csv_table = [["ID", "Entity Type", "OEO:00269001"],
                     ["ID", "TYPE SPLIT=|", "A OEO:00269001"]]
        
        csv_table_per_module = {'oeo-shared' : csv_table,
                                'oeo-physical' : [a for a in csv_table], 
                                'oeo-social' : [a for a in csv_table], 
                                'oeo-model' : [a for a in csv_table]}

        #* Adds only one belonging to an entity
        #* regarding to following rule:
        #* First: Shared; Second: Physical; Third: Model; Fourth: Social
        #* Using Dictionaries instead of lists <dict>[<string>] instead of <list>[<int>] for better maintenance 
        for ids, type_, belonging in belongs_to_module:
            #print(ids,type_,belonging)
            if 'oeo-shared' in belonging:
                csv_table_per_module['oeo-shared'].append([ids, type_, ontology_iri + '/oeo-shared'])
            elif 'oeo-physical' in belonging:
                csv_table_per_module['oeo-physical'].append([ids, type_, ontology_iri + '/oeo-physical'])
            elif 'oeo-model' in belonging:
                csv_table_per_module['oeo-model'].append([ids, type_, ontology_iri + '/oeo-model'])
            elif 'oeo-social' in belonging:
                csv_table_per_module['oeo-social'].append([ids, type_, ontology_iri + '/oeo-social'])

        for module in csv_table_per_module:
            
            with open(script_path / 'btma' / 'template.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(csv_table_per_module[module])

            #* Create OMN with help of the CSV template
            callstring = 'java -jar {jar} template --template {template} \
                                              --prefix \"OEO: {iri}\" \
                                              --input {inp} \
                                              --force true --errors "errors.csv" \
                                              --output {out}'.format(jar=robot_path,
                                                                     template=script_path / 'btma' / 'template.csv',
                                                                     iri=ontology_iri + '/OEO_',
                                                                     inp=omn_path / (module + '.omn'),
                                                                     out=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=module))
            sp.call(callstring, shell=True)
        
        #* MERGE OMN files with the oeo modules
        
        for module in csv_table_per_module:

            sp.call('java -jar {jar} merge --input {out} \
                                           --input {inp} \
                                           --output {out} \
                                           --collapse-import-closure false \
                                           --include-annotations true'.format(jar=robot_path,
                                                                              out=omn_path / (module + '.omn'),
                                                                              inp=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=module)),
                    shell=True)
            sp.call(callstring, shell=True)
                
        reset_btma()
        
#    else:
#        sh.rmtree(csv_path)
        
    running = False    

#* Script start here
#* Load 'static' values

ontology_iri = 'http://openenergy-platform.org/ontology/oeo'

changed = True
running = True
modules = ['oeo-shared',
           'oeo-physical',
           'oeo-social',
           'oeo-model']

src_path = path.Path('/Users/hastingj/Work/Onto/open-energy-ontology/src').absolute()            #<- For development use this in your IDE instead of 'find_root_dir'
#src_path = find_root_dir('src')
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
            
if __name__ == '__main__':
    loading_process = threading.Thread(target=main)
    loading_process.start()

    __loadingAnimation(loading_process)
    loading_process.join()