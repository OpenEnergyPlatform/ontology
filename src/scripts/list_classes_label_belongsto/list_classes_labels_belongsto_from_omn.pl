#/usr/bin/perl
# short script to extract classes and individuals from an .omn file 
# The script reads a file referenced in the open statement below and scanns the file line by line for class, belongs to and labels. 
# As the script uses a very simple apprach, the list may not be complete. 
# written by Carsten Hoyer-Klick carsten.hoyer-klick@dlr.de 
# Licencse: MIT
# Usage: replace the file name in the open statement, run the script from the command line. 
# output can be saved to a file with:is list_classes_labels_belongsto_from_omn.pl >file.csv
use strict; 
my $inline_out; # read line in the outer loop
my $inline_in;  # read line in the inner loop. 
my $class; # contains "Class:" or individual in the split statement
my $classid; # contains the OEO Key from the split statement. 
my $belongsto; #contains the OEO Key OEO_000040001  in the split statement
my $oeomodule; #contains the information which module the current class belongs to. 
my $rdfs; # contains the "rdfs:label" part in the split statement
my $label; # contains the label of the class. 
open(IN,"C:\\data\\LOD-GEOSS\\LOD-GEOSS Ontology\\ontology\\src\\ontology\\edits\\oeo-shared.omn");
while ($inline_out = <IN>)
{
	if ($inline_out =~ /Class:/)   # scan the file line by line until Class apprears for the first time. 
     {
		chomp($inline_out); # remove CRLF/LF depending on operating system .
		($class,$classid) = split(/\:/,$inline_out); # split line by the : 
		while ($inline_in = <IN>) # inner loop. 
		{
			chomp($inline_in); # remove CRLF / LF
			if ($inline_in =~ /OEO_00040001/)  # OEO Class for "belongs to"
			{
				($belongsto,$oeomodule) = split(" ",$inline_in);
				$oeomodule =~ s/\"//g; # remove " from string
				$oeomodule =~ s/\,//g; # remove , from string
			}
			if ($inline_in =~ /Class:/) # new class, set $classid to new value. 
			{
	    		($class,$classid) = split(/\:/,$inline_in);
     		}
			if ($inline_in =~ /Individual:/) # new individual, set $classid to new value
			{
	    		($class,$classid) = split(/\:/,$inline_in);
			}
			if ($inline_in =~  /rdfs:label/) # label in line 
			{
				($rdfs,$label) = split(/\"/,$inline_in);
				$label =~ s/\"//g; # remove " in string. 
				# if label is dected in input line, information on Calls, belongs to and label should be complete, 
			    # information can now be printed. 
				print "$classid, $label, $oeomodule \n"; 
			}
		}
     }
}
close(IN); 
