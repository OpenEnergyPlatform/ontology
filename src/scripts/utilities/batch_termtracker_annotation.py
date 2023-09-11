# %% Requires py-horned-owl: https://github.com/jannahastings/py-horned-owl
import pyhornedowl
import subprocess as sp
import os
# %%
# Adjust to your system needs!
ROBOT_PATH = "C:/Software/robot/robot.jar"
TMP_DIR = os.path.join(os.getcwd(), "tmp")
if not os.path.exists("src"):
    SRC_DIR =  os.path.abspath( os.path.join(os.getcwd(), "../.."))
else:
    SRC_DIR = "src"
if not os.path.exists(TMP_DIR):
    os.mkdir(TMP_DIR)

# %%
def convert(input_file, output_file, output_format="owx"):
    CONVERT_TIMESTRING = 'java -jar {jar} convert --input {input_file} \
                                                --output {output_file} \
                                                --format {format}'.format(jar=ROBOT_PATH,
                                                                        input_file=input_file,
                                                                        output_file=output_file,
                                                                        format=output_format)
    sp.call(CONVERT_TIMESTRING)
# %%
temporary_file = os.path.join(TMP_DIR, "oeo-physical.owx")
original_file = os.path.join(SRC_DIR,"ontology/edits/oeo-physical.omn")
convert(original_file, temporary_file, output_format="owx")

added_item_to_tracker = """moved to oeo-shared
https://github.com/OpenEnergyPlatform/ontology/pull/956
add axiom to social cost of carbon
pull request: https://github.com/OpenEnergyPlatform/ontology/pull/1034"""
# %%
onto = pyhornedowl.open_ontology(temporary_file)
# %%
TERMTRACKER = "http://purl.obolibrary.org/obo/IAO_0000233"
ELECTRICAL_ENERGY_SHARE="http://openenergy-platform.org/ontology/oeo/OEO_00020254"
# %%
term_tracker_axion = onto.get_annotation(ELECTRICAL_ENERGY_SHARE, TERMTRACKER)
onto.remove_axiom(['AnnotationAssertion', ELECTRICAL_ENERGY_SHARE, TERMTRACKER])
# %%
