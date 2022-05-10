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

# Load 'static' values

ontology_iri = 'http://openenergy-platform.org/ontology/oeo/OEO'

modules = ['oeo-shared',
           'oeo-physical',
           'oeo-social',
           'oeo-model']


src_path = path.Path(__file__).parent.parent.parent.absolute()
script_path = path.Path(__file__).parent.parent.absolute()

omn_path = src_path / 'ontology' / 'edits'              
csv_path = src_path / 'ontology' / 'exports'          
owl_path = src_path / 'ontology' / 'imports'
robot_path = script_path / 'btma' / 'robot.jar'

def extract_IDs(module : list) -> list:
    file = open(csv_path / (module + '.csv'))
    CSVreader = csv.reader(file)
    ids = []
    for row in CSVreader:
        t = row[0].split('_')
        if t[0] == ontology_iri: 
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

    # Load necessary IRIs of the different ontology-modules

    print('Loading ontologies...')
    ids : set = set([])
    for (i,module) in enumerate(modules):
        mod = ""
        mod = omn_path / "{m}.omn".format(m=module)
        exp = csv_path / "{m}.csv".format(m=module)
        sp.call('java -jar {jar} export --input {m} \
                                    --header "{c}" \
                                    --export {e}'.format(jar=robot_path,
                                                           m=mod, 
                                                           c=col, 
                                                           e=exp))
        tmp = extract_IDs(module)
        ids = ids.union(set(tmp))
        ids_per_module[i] = tmp

    ids = list(ids)

    # Create overview about IRIs and there belonging

    print('Finding belongings...')

    belonging = ids.copy()

    for (i,id) in enumerate(ids):
        for (j,module_ids) in enumerate(ids_per_module):
            if id in module_ids:
                belonging[i] = modules[j]
                break

    # Create the CSV template with the help of the overview

    print('Creating template...')
        
    belongs_to_module = list(zip(ids, belonging))

    csv_table = [["ID","belongs to module"],
                 ["ID","AI OEO:belongs_to_module"]]

    csv_table_per_module = (csv_table, csv_table, csv_table, csv_table)

    for (ids, belonging) in belongs_to_module:
        if belonging == module[0]:
            csv_table_per_module[0].append(['OEO:' + ids, ontology_iri + '/' + belonging])
        elif belonging == module[1]:
            csv_table_per_module[1].append(['OEO:' + ids, ontology_iri + '/' + belonging])
        elif belonging == module[2]:
            csv_table_per_module[2].append(['OEO:' + ids, ontology_iri + '/' + belonging])
        else:
            csv_table_per_module[3].append(['OEO:' + ids, ontology_iri + '/' + belonging])
        
    print('Creating ontologies...')

    for (i, csv_table) in enumerate(csv_table_per_module):
        f = open(script_path / 'btma' / "template.csv", 'w', newline='')

        writer = csv.writer(f)

        writer.writerows(csv_table)

        f.close()

        # Create OWL/XML with help of the CSV template
    
        sp.call('java -jar {jar} template --template {template} \
                                          --prefix "OEO: {iri}_" \
                                          --output {out}'.format(jar=robot_path,
                                                                 template=script_path / 'btma' / 'template.csv',
                                                                 iri=ontology_iri,
                                                                 out=csv_path / 'belongs-to-{m}-annotation.omn'.format(m=modules[i])))
    
        os.remove(script_path / 'btma' / "template.csv")

        sp.call('java -jar {jar} merge --input {out} \
                                       --input {inp} \
                                       --output {out}'.format(jar=robot_path,
                                                              out=omn_path / (modules[i] + '.omn'),
                                                              inp=csv_path / 'belongs-to-{m}-annotation.omn'.format(m=modules[i])))
    
    # MERGE .OMN with oeo-modules

    sh.rmtree(csv_path)

    print('Finished!')
    
if __name__ == '__main__':
    main()
