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

ontology_iri = 'http://openenergy-platform.org/ontology/oeo'

modules = ['oeo-shared',
           'oeo-physical',
           'oeo-social',
           'oeo-model']


src_path = path.Path(__file__).parent.parent.parent.absolute()
script_path = src_path / 'scripts'

omn_path = src_path / 'ontology' / 'edits'              
csv_path = script_path / 'btma' / 'data'          
db_path = script_path / 'btma' / 'database'
exp_path = script_path / 'btma' / 'exports'
owl_path = src_path / 'ontology' / 'imports'
robot_path = script_path / 'btma' / 'robot.jar'
pre_path = script_path / 'btma' / 'prefixes'

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
            if belonging == modules[0]:
                csv_table_per_module[0].append(['OEO:' + ids, ontology_iri + '/' + belonging])
            elif belonging == modules[1]:
                csv_table_per_module[1].append(['OEO:' + ids, ontology_iri + '/' + belonging])
            elif belonging == modules[2]:
                csv_table_per_module[2].append(['OEO:' + ids, ontology_iri + '/' + belonging])
            else:
                csv_table_per_module[3].append(['OEO:' + ids, ontology_iri + '/' + belonging])
                
        print('Creating ontologies...')

        prefix_adder = ""

        #! Error occurs if you include OEO Prefix as empty Prefix -> "Could not load prefix '' for <ontology_iri<"
        for prefix in prefixes[1:]:
            prefix_ = ""
            for c in prefix:
                if c != '<' and c != '>':
                    prefix_ += c
            prefix_adder += '--add-prefix \"{p}\" '.format(p=prefix_)

        for (i, csv_table) in enumerate(csv_table_per_module):
            f = open(script_path / 'btma' / "template.csv", 'w', newline='')

            writer = csv.writer(f)

            writer.writerows(csv_table)

            f.close()

            # Create OWL/XML with help of the CSV template
            
            sp.call('java -jar {jar} template --template {template} \
                                              --add-prefix \"OEO: {iri}OEO_\" \
                                              {pre} \
                                              --output {out}'.format(jar=robot_path,
                                                                     template=script_path / 'btma' / 'template.csv',
                                                                     iri=ontology_iri + '/',
                                                                     pre=prefix_adder[-1],
                                                                     out=exp_path / 'belongs-to-{m}-annotation.omn'.format(m=modules[i])))

            
            #! ontology Prefix as 'oeo:' instead of ':'
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
            
            # sp.call
        os.remove(script_path / 'btma' / "template.csv")
    
        # MERGE .OMN with oeo-modules
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
