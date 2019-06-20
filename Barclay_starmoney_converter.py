# -*- coding: cp1252 -*-

import os # For iterating through directories
#import Tkinter, Tkconstants, tkFileDialog


class BarclayStarmoneyConverter:
        edit_consol_output = object
        def __init__(self, guiRoot, new_edit_consol_output):
                global edit_consol_output
                edit_consol_output = new_edit_consol_output

        # To print something on the consol in the gui
        def print_to_consol(self, strToPrint):
                print(strToPrint)

        def process_bc_line(self, line):
                line = line.split(',')
                print('#### (line):', (line))
                betrag = float((line[5]).replace('.', '')[1:]) + float(line[6][:-2])/100
                print('betrag:', betrag)
                print('line[6][-2]:', line[6][-2])
                if line[6][-2] == '-':
                        betrag = (-1) * betrag
                else:
                        betrag = 1 * betrag
                betrag = round(betrag, 2)
                betrag = str(betrag).replace('.', ',')
                return "\";\"\";\"\";\"\";" + line[3] + ";\"" + line[1][1:-1] + "\";\"" + line[0][1:-1] + "\";\"\";\"\";\"\";\"\";\"\";\"\"" + betrag + "\";\" EUR\"\";\"" + line[2][1:-1] + "\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\"\";\n"


        # Coverts and analyses one file
        def convert_and_analyse_one_file(self, input_file_name, destPath, is_first):
                output_file_name = destPath + '\\' + "barclays_to_starmoney.txt"
                self.print_to_consol('output_file_name: ' + str(output_file_name))
                #output_file_name = input_file_name.split('.')[0]+"_processed.csv"
                # open a file for writing
                output = open(output_file_name, 'a')
                # create the csv writer object # lineterminator = '\n' is necessarry for windows
                if is_first:
                        columns_line = "\"Bestätigt\";\"Umsatz getätigt von\";\"Kartentyp\";\"Belegdatum\";\"Buchungsdatum\";\"Betrag\";\"Transaktion/\";\"Beschreibung\";\"Beschreibung\";\"Beschreibung\";\"Beschreibung\";\"Beschreibung\";\"Beschreibung\";\"Beschreibung\";\"Abgerechnet\";\"Kategorie/Unterkategorie\";\"Kostenstelle\";\"Steuersatz\";\"Steuerbetrag\"\n"
                        output.write(columns_line)
                with open(input_file_name) as fp:
                   line = fp.readline()
                   cnt = 1
                   while line:
                       line = fp.readline()
                       cnt += 1
                       if cnt > 12:
                               if len(line) > 10:
                                       print("Line {}: {}".format(cnt, line.strip()))
                                       output.write(self.process_bc_line(line))


        def convert_and_analyse_directory(self, srcPath, destPath):
                is_first = True
                for subdir, dirs, files in os.walk(srcPath):
                        for file in files:
                                #path_for_single_file = file # Was
                                path_for_single_file = os.path.join(subdir, file)
                                #print('path_for_single_file: ' + str(path_for_single_file))
                                self.convert_and_analyse_one_file(path_for_single_file, destPath, is_first)
                                is_first = False
                                self.print_to_consol('_________________________________________________________')
                        break # Without the break it would also scan the subdirs

### For Tests without GUI
#xmlCsvConf = XmlCsvConf()
#xmlCsvConf.convert_and_analyse_directory('C:\Users\Julian\Desktop\Uni\Mexiko Drone 2017 und KML CSV\kml_to_csv_tool\KMLs_which_caused_NAs')
