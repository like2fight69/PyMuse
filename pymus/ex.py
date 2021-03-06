import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os
import vlc

#add file menu and open submenu
#addstop button
#test

#test
# list of tuples for each software, containing the software name, initial release, and main programming languages used
software_list = [
     ("Firefox", 2002,"length"),
    
]


#test
class FileChooserWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="FileChooser Example")

        box = Gtk.Box(spacing=6)
        self.add(box)

        button1 = Gtk.Button("Choose File")
        button1.connect("clicked", self.on_file_clicked)
        box.add(button1)

        button2 = Gtk.Button("Choose Folder")
        button2.connect("clicked", self.on_folder_clicked)
        box.add(button2)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            "Please choose a file",
            self,
            Gtk.FileChooserAction.OPEN,
            (
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN,
                Gtk.ResponseType.OK,
            ),
        )

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            #tree = TreeViewFilterWindow()
            #tree.connect("destroy", Gtk.main_quit)
            #tree.show_all()
            win.add_to_list(dialog.get_filename())
            
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_folder_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            "Please choose a folder",
            self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK),
        )
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()


#test
def on_open(self):
        dialog = Gtk.FileChooserDialog("Please choose a file", win,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

#        self.win.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            file_path = dialog.get_filename()
            print("Open clicked")
            print("File selected: " + file_path)
            #self.labelframe.set_label(os.path.basename(file_path))
            #self.editor.open_file(file_path)
            win.add_to_list(dialog.get_filename())

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()




#test
class TreeViewFilterWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Treeview Filter Demo")
        self.set_border_width(10)

        # Setting up the self.grid in which the elements are to be positionned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
#test
        mb = Gtk.MenuBar()

        filemenu = Gtk.Menu()
        filem = Gtk.MenuItem("File")
        filem.set_submenu(filemenu)
       
        open = Gtk.MenuItem("Open")
        open.connect("activate", on_open)
        filemenu.append(open)        



        exit = Gtk.MenuItem("Exit")
        exit.connect("activate", Gtk.main_quit)
        filemenu.append(exit)

        mb.append(filem)

        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        vbox.pack_start(self.grid, False, False, 0)
        self.add(vbox)

        self.connect("destroy", Gtk.main_quit)
#        self.show_all()
        



#test
       # self.add(self.grid)
        #test








        #test
        # Creating the ListStore model
        self.software_liststore = Gtk.ListStore(str,int,str)#str,int,str
        for software_ref in software_list:
            self.software_liststore.append(list(software_ref))
        self.current_filter_language = None

        # Creating the filter, feeding it with the liststore model
        self.language_filter = self.software_liststore.filter_new()
        # setting the filter function, note that we're not using the
        self.language_filter.set_visible_func(self.language_filter_func)

        # creating the treeview, making it use the filter as a model, and adding the columns
        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
        for i, column_title in enumerate(
            ["Song", "Release Year","Length"]
        ):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)
        #self.treeview.get_selection().set_select_function(self.on_tree_selection_changed())
        select = self.treeview.get_selection()
        select.connect("changed", self.selection_changed)
        # creating buttons to filter by programming language, and setting up their events
        self.buttons = list()
        for prog_language in ["Java", "C", "C++", "Python", "None"]:
            button = Gtk.Button(prog_language)
            self.buttons.append(button)
            button.connect("clicked", self.on_selection_button_clicked)

        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(
            self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1
        )
        #for i, button in enumerate(self.buttons[1:]):
            #self.grid.attach_next_to(
                #button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1
            #)
        self.scrollable_treelist.add(self.treeview)
       # self.add_to_list("hi")
        self.show_all()
        song_store = Gtk.ListStore(str)
    def add_to_list(self,fileName):
         # self.software_liststore = Gtk.ListStore(str, int, str,str)
          #software_list.append(fileName)
         # software_list[0] = fileName
            software_list = [ (fileName,2002,"hi"),]
            self.language_filter.refilter()

         # software_list[1] = 2002
         #song_store = gtk.ListStore(str)
            for software_ref in software_list:
                self.software_liststore.append(list(software_ref))
                #win.queue_draw() 
       #         while Gtk.events_pending():
        #          Gtk.main_iteration_do(False) 
               # self.language_filter = self.software_liststore.filter_new()
                #self.language_filter.refilter()


                print(software_ref)
              #  view = Gtk.TreeView.set_model(self)
         # printsoftware_list)
          #self.language_filter.refilter()
     
    def language_filter_func(self, model, iter, data):
        """Tests if the language in the row is the one in the filter"""
        if (
            self.current_filter_language is None
            or self.current_filter_language == "None"
        ):
            return True
        else:
            return model[iter][2] == self.current_filter_language

    def on_selection_button_clicked(self, widget):
        """Called on any of the button clicks"""
        # we set the current language filter to the button's label
        self.current_filter_language = widget.get_label()
        print("%s language selected!" % self.current_filter_language)
        #os.system("/home/tyler/python/pymusic/sample.mp3")
        #test
#        file = FileChooserWindow()
 #       file.connect("destroy", Gtk.main_quit)
  #      file.show_all()
        
        
        #test
        for row in software_list:
          print(row[0])
        # we update the filter, which updates in turn the view
        self.language_filter.refilter()
#test   
    def selection_changed(self,selection):
       model, treeiter = selection.get_selected()
       if treeiter is not None:
         print("You selected", model[treeiter][0])
          
         file = model[treeiter] [0]
        # os.system("mpg123 " + file)
         p = vlc.MediaPlayer(file)
         p.play()
#test
win = TreeViewFilterWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
#file = FileChooserWindow()
#file.connect("destroy", Gtk.main_quit)
#file.show_all()
#test

#test
#wind = FileChooserWindow()
#wind.add(wind)
Gtk.main()
