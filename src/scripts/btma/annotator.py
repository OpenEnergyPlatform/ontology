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

def extract_belongings(ids : set, ids_per_module) -> list[list]:
    """
    Extracts the belonging of each ID

    Args:
        `ids (set)`: set of IDs
        `ids_per_module (_type_)`: partition of `ids` in modules

    Returns:
        `list[list]`: list of IDs per modules
    """
    belongings : list[list] = []

    for (i,id) in enumerate(ids):
        belongings.append([])
        for (j,module_ids) in enumerate(ids_per_module):
            if id in module_ids:
                belongings[i].append(modules[j])
                
    return belongings

def extract_prefixes(onto : io.TextIOWrapper) -> list:
    """
    Extracts Prefixes of the ontology `onto`.

    Args:
        `onto (io.TextIOWrapper)`: Ontology in OMN format

    Returns:
        `list`: the prefixes used in `onto`
    """
    prefixes = []
    lines = onto.readlines()
    
    for line in lines:
        if line.startswith('Prefix:'):
            prefixes.append(line[8:-1])             #* <- Abhängig vom Prefix
        else:
            break
        
    return prefixes
    
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
                ids.append((row[0], row[1]))
    return ids

def serialize_prefixes(prefixes : list) -> str:
    """
    Serialize the prefixes for `'--add-prefix'` in the `robot` command
    
    Args:
        `prefixes (list)`: list of IRIs

    Returns:
        ``str`: Concatenated '--add-prefix IRI' for each IRI
    """
    prefix_str = ""
    
    for prefix in prefixes:
            prefix_ = ""
            for c in prefix:
                if c != '<' and c != '>':
                    prefix_ += c

            prefix_str += '--add-prefix \"{p}\" '.format(p=prefix_)

    return prefix_str

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

    prefixes = []
    oeo = open(src_path / 'ontology' / 'oeo.omn')
    prefixes = extract_prefixes(oeo)

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

    old_ids_per_module = [_,_,_,_]
    try:
        for i, module in enumerate(modules):
            old_ids_per_module[i] = extract_IDs_Types(db_path / (module + '.csv'))
    except:
        pass
    
    changed = old_ids_per_module != ids_per_module
    #* edit omn if and only if omn was changed
    if changed:
        #* Create the CSV template with the help of an 'overview'                            
        
        belongings : list[list] = extract_belongings(ids, ids_per_module)
        
        types = extract_types(ids)
        
        belongs_to_module = list(zip(ids, types, belongings))
        
        csv_table = [["ID", "Entity Type", "OEO:00260001"],
                     ["ID", "TYPE", "AI OEO:00260001"]]
        
        csv_table_per_module = {'oeo-shared' : csv_table, 
                                'oeo-physical' : [a for a in csv_table], 
                                'oeo-social' : [a for a in csv_table], 
                                'oeo-model' : [a for a in csv_table]}

        #* Adds only one belonging to an entity
        #* regarding to following rule:
        #* First: Shared; Second: Physical; Third: Model; Fourth: Social
        #* Using Dictionaries instead of lists <dict>[<string>] instead of <list>[<int>] for better maintenance 
        for ids, type_, belonging in belongs_to_module:
            if 'oeo-shared' in belonging:
                csv_table_per_module['oeo-shared'].append([ids, 'owl:' + type_, ontology_iri + '/oeo-shared'])
            elif 'oeo-physical' in belonging:
                csv_table_per_module['oeo-physical'].append([ids, 'owl:' + type_, ontology_iri + '/oeo-physical'])
            elif 'oeo-model' in belonging:
                csv_table_per_module['oeo-model'].append([ids, 'owl:' + type_, ontology_iri + '/oeo-model'])
            elif 'oeo-social' in belonging:
                csv_table_per_module['oeo-social'].append([ids, 'owl:' + type_, ontology_iri + '/oeo-social'])
                        
        add_prefixes = serialize_prefixes(prefixes[1:])
                
        for module in csv_table_per_module:
            
            with open(script_path / 'btma' / 'template.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(csv_table_per_module[module])

            #* Create OMN with help of the CSV template
            
            sp.call('java -jar {jar} template --template {template} \
                                              --add-prefix \"OEO: {iri}\" \
                                              --add-prefix \"owl: http://www.w3.org/2002/07/owl#\" \
                                              --output {out}'.format(jar=robot_path,
                                                                     template=script_path / 'btma' / 'template.csv',
                                                                     iri=ontology_iri + '/OEO_',
                                                                     out=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=module)), shell=True)
        
        #* MERGE OMN files with the oeo modules
        
        for module in csv_table_per_module:
            #TODO: Valid Call
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
            #TODO: Test Call
            sp.call('java -jar {jar} merge --input {out} \
                                           --input {inp} \
                                           --add-prefix \"OEO: {iri}\" \
                                           {pre} \
                                           --output {out_} \
                                           --include-annotations true'.format(jar=robot_path,
                                                                              out=omn_path / (module + '.omn'),
                                                                              out_=omn_path / (module + '-new.omn'),
                                                                              inp=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=module),
                                                                              pre=add_prefixes[:-1],
                                                                              iri=ontology_iri + '/OEO_'), shell=True)
                
        reset_btma()
        
    else:
        sh.rmtree(csv_path)
        
    running = False    

#* Script start here
#* Load 'static' values

ontology_iri = 'http://openenergy-platform.org/ontology/oeo'

changed = False
running = True
modules = ['oeo-shared',
           'oeo-physical',
           'oeo-social',
           'oeo-model']

#* src_path = path.Path('src').absolute()            #<- For development use this in your IDE instead of 'find_root_dir'
src_path = find_root_dir('src')
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