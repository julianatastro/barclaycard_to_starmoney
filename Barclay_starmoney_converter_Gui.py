# -*- coding: cp1252 -*-

from tkinter import *
import tkinter, tkinter.constants, tkinter.filedialog
from tkinter import messagebox
from Barclay_starmoney_converter import BarclayStarmoneyConverter
import os # For iterating through directories
import webbrowser


class Converter_Gui:
    conv_instance = object
    guiRoot = object
    edit_kml_path = object
    edit_dest_path = object
    edit_consol_output = object

    
    def __init__(self, new_guiRoot, new_conv_instance, new_edit_consol_output):
        global guiRoot
        guiRoot = new_guiRoot
        global conv_instance
        conv_instance = new_conv_instance
        global edit_kml_path
        edit_kml_path = Text(guiRoot, height=1, width=120)
        global edit_dest_path
        edit_dest_path = Text(guiRoot, height=1, width=120)
        global edit_consol_output
        edit_consol_output = new_edit_consol_output
        setup_gui()
                 
def callback_select_src():
    path = tkinter.filedialog.askdirectory()
    global edit_kml_path
    edit_kml_path.delete('@0,0', END)
    edit_kml_path.insert(END, path)
    mainloop()
    print(path)

def callback_select_dest():
    path = tkinter.filedialog.askdirectory()
    global edit_dest_path
    edit_dest_path.delete('@0,0', END)
    edit_dest_path.insert(END, path)
    mainloop()
    print(path)

def callback_start():
    #xmlCsvConf.print_to_consol('TEST')
    srcPath = edit_kml_path.get("@0,0",END)
    srcPath = srcPath[:-1].replace("/", "\\")
    destPath = edit_dest_path.get("@0,0",END)
    destPath = destPath[:-1].replace("/", "\\")
    conv_instance.convert_and_analyse_directory(srcPath, destPath)

def callback_help():
    webbrowser.open_new(r"https://github.com/julianatastro/barclaycard_to_starmoney")

def setup_gui():
        guiRoot.title("Barclays Umsaetze zu Starmoney Kreditkartenumsaetze Converter")
        label_up3 = Label(guiRoot, height=1, width=150)
        label_up3.pack()
        button_help = Button(guiRoot, text='Hilfe', width=25, command=callback_help)
        button_help.pack()
        label_up = Label(guiRoot, height=1, width=150)
        label_up.pack()
        edit_kml_path.insert(END, 'Quellordner (muss CSV-Dateien enthalten)')
        edit_kml_path.pack()
        button_select_folder = Button(guiRoot, text='Quellordner auswaehlen', width=25, command=callback_select_src)
        button_select_folder.pack()
        label_up2 = Label(guiRoot, height=1, width=150)
        label_up2.pack()
        edit_dest_path.insert(END, 'Zielordner für TXT-Datei')
        edit_dest_path.pack()
        button_select_folder = Button(guiRoot, text='Zielordner auswaehlen', width=25, command=callback_select_dest)
        button_select_folder.pack()
        label_center_up = Label(guiRoot, height=2, width=120)
        label_center_up.pack()
        button_run = Button(guiRoot, text='Start', width=25, command = callback_start)
        button_run.pack()
        label_center = Label(guiRoot, height=3, width=120)
        label_center.pack()       
        edit_consol_output.insert(END, 'Meldungen')
        edit_consol_outputScroll = Scrollbar(guiRoot)
        edit_consol_outputScroll.pack(side=RIGHT, fill=Y)
        edit_consol_output.pack()
        edit_consol_outputScroll.config(command=edit_consol_output.yview)
        edit_consol_output.config(yscrollcommand=edit_consol_outputScroll.set)
        label_down = Label(guiRoot, height=1, width=150)
        label_down.pack()
        guiRoot.mainloop()

guiRoot = Tk()
edit_consol_output = Text(guiRoot, height=25, width=120)
barclayStarmoneyConverter = BarclayStarmoneyConverter(guiRoot, edit_consol_output)
cGui = Converter_Gui(guiRoot, barclayStarmoneyConverter, edit_consol_output)
