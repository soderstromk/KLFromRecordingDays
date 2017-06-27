from tkinter import *
import pymysql
import os

# ParseSAPRecorderWavs
# This program takes *.wav file recordings produced over several days by Sound Analysis Pro 2011 and organizes them
# into folders by recording day. It also renames them to the format used by KLFromDays to generate KL distances from
# Sound Analysis Pro 2011 MySQL tables of acoustic features by syllable

# The GUI interface class object
class ParseGUI:
    def __init__(self, master, Database):
        frame = Frame(master,width=50)
        frame.pack(side=TOP)

        topframe = Frame(master)
        topframe.pack(side=TOP)

        #Allow user to select the directory with the Sound Analysis Recorder 2011 *.wav file output
        # Sound Analysis Recorder 2011 is accessed via the "Live Analysis" feature in SAP 2011
        self.SourceLabel = Label(topframe,text='Directory with files to parse')
        self.SourceLabel.pack(side=TOP)

        self.SourceDir = StringVar()
        sourcepath = os.path.normpath("c:/sap/")
        self.SourceDir.set(sourcepath)

        self.SourceInput = Entry(topframe,width=40)
        self.SourceInput["textvariable"]= self.SourceDir
        self.SourceInput.pack(side=TOP, padx=5)

        self.SourceButton = Button(topframe,text='Change Source Directory',command=self.ChangeSource)
        self.SourceButton.pack(side=TOP, pady=(5,10))

        # *.wav files can either be copied or renamed and moved to the destination directory
        # The move feature saves disk space that can be important with experiments covering weeks
        self.CopyDontMove = IntVar()
        self.CopyFileButton = Checkbutton(topframe, text='Copy instead of move', variable=self.CopyDontMove).pack(
            side=TOP, padx=5, pady=5)

        # Destination directory is selected
        self.DestinationLabel = Label(topframe, text='Directory to place parsed files')
        self.DestinationLabel.pack(side=TOP)

        self.DestinationDir = StringVar()
        destinationpath = ""
        self.DestinationDir.set(destinationpath)

        self.DestinationInput = Entry(topframe, width=40)
        self.DestinationInput["textvariable"] = self.DestinationDir
        self.DestinationInput.pack(side=TOP, padx=5)

        self.DestinationButton = Button(topframe, text='Change Destination Directory', command=self.ChangeDestination)
        self.DestinationButton.pack(side=TOP, pady=(1, 10))

        #Controls

        self.RunButton = Button(topframe, text='Parse Files', command=self.ParseFiles)
        self.RunButton.pack(side=BOTTOM,anchor=E, pady=(1, 5),padx=(1, 5))
        self.StatusLabel = Label(topframe, text='Running...', justify=RIGHT, fg="red")

    # Runs if user selects a new source directory
    def ChangeSource(self):
        from tkinter import filedialog
        sourcepath = filedialog.askdirectory()
        self.SourceInput.delete(0, END)
        self.SourceInput.insert(0, sourcepath)

    # Runs if user selects a new destination directory
    def ChangeDestination(self):
        from tkinter import filedialog
        destinationpath = filedialog.askdirectory()
        self.DestinationInput.delete(0, END)
        self.DestinationInput.insert(0, destinationpath)

    # Main function
    def ParseFiles(self):

        # Call function that returns a list of *.wav file names in the Source directory
        WavFileList = self.GetWavFiles()

        # Label updates user on progress
        # With lots of files the program can take several minutes
        window.StatusLabel.pack(side=BOTTOM)

        # No *.wav files were found in the Source directory
        if not WavFileList:
            from tkinter import messagebox
            messagebox.showinfo("No Files", "No *.wav files found")
            window.StatusLabel.config(text='No *.wav files found')
            window.StatusLabel.update()
            return

        # NewNameList function returns a dictionary of new filenames and their directories keyed by original filenames and a list of destination directory names:
        # dict{oldfilename: (newfilename, DirText)}, DirNames[]
        # New filenames are in the format: *-##-#####.wav, where * = animal ID, ## = recording day, ##### = *.wav file number
        # The KL distance software depends upon this file format to process the syllable table that will be produced from these *.wav files

        NewNameDict, DirNames = self.NewNameList(WavFileList)

        if NewNameDict and DirNames:
            if self.DestinationDir.get() == "" or self.DestinationDir.get() == self.SourceDir.get(): #No destination directory entered so use the source directory
                if self.CopyDontMove.get() == 0: #Move don't rename
                    os.chdir(self.SourceDir.get())
                    CurrentDir = os.getcwd()
                    #Function
                    self.CreateDayDirectories(DirNames)
                    window.StatusLabel.config(text='Moving (this may take a while...)')
                    window.StatusLabel.update()
                    for WavFile in WavFileList:
                        os.rename(CurrentDir + '/' + WavFile, CurrentDir + '/' + NewNameDict[WavFile][1] + '/' + NewNameDict[WavFile][0])
                    window.StatusLabel.config(text='Done')
                    window.StatusLabel.update()
                else: # Copy *.wav files, don't move them
                    from shutil import copyfile
                    os.chdir(self.SourceDir.get())
                    CurrentDir = os.getcwd()
                    self.CreateDayDirectories(DirNames)
                    window.StatusLabel.config(text='Copying files (this may take a while...)')
                    window.StatusLabel.update()
                    for WavFile in WavFileList:
                        copyfile(str(self.SourceDir.get()) + '/' + WavFile,
                                 CurrentDir + '/' + NewNameDict[WavFile][1] + '/' + NewNameDict[WavFile][0])
                    window.StatusLabel.config(text='Done')
                    window.StatusLabel.update()

            else: # Copy files to destination directory
                if self.CopyDontMove.get() == 0:  # Move them don't rename
                    os.chdir(self.DestinationDir.get())
                    CurrentDir = os.getcwd()
                    self.CreateDayDirectories(DirNames)
                    window.StatusLabel.config(text='Moving files (this may take a while...)')
                    window.StatusLabel.update()
                    for WavFile in WavFileList:
                        os.rename(str(self.SourceDir.get()) + '/' + WavFile,
                                  CurrentDir + '/' + NewNameDict[WavFile][1] + '/' + NewNameDict[WavFile][0])
                    window.StatusLabel.config(text='Done')
                    window.StatusLabel.update()
                else:
                    from shutil import copyfile
                    os.chdir(self.DestinationDir.get())
                    CurrentDir = os.getcwd()
                    self.CreateDayDirectories(DirNames)
                    window.StatusLabel.config(text='Copying files (this may take a while...)')
                    window.StatusLabel.update()
                    for WavFile in WavFileList:
                        copyfile(str(self.SourceDir.get()) + '/' + WavFile,
                                  CurrentDir + '/' + NewNameDict[WavFile][1] + '/' + NewNameDict[WavFile][0])
                    window.StatusLabel.config(text='Done')
                    window.StatusLabel.update()
        else:
            window.StatusLabel.config(text='No *.wav in SAP format...')
            window.StatusLabel.update()
            return

    # Creates subdirectories for each recording day
    def CreateDayDirectories(self,DirNames):
        # In these cases use the source directory for output
        if self.DestinationDir.get() == '' or self.DestinationDir.get() == self.SourceDir.get():
            for DirName in DirNames:
                NewDir = self.SourceDir.get() + '/' + DirName
                os.makedirs(NewDir,exist_ok=True)
        # In this case a destination directory was provided by the user
        else:
            for DirName in DirNames:
                NewDir = self.DestinationDir.get() + '/' + DirName
                os.makedirs(NewDir, exist_ok=True)

    # Makes a list of *.wav files that are in the directory
    def GetWavFiles(self):
        WavFileList = []
        for file in os.listdir(os.path.normpath(self.SourceDir.get())):
            if file.endswith(".wav"):
                WavFileList.append(file)
        return WavFileList

    # Creates a list of file names in the updated file format: *-##-#####.wav, where * = animal ID, ## = recording day, ##### = *.wav file number
    # The updated format is derived from the SAP 2011 recorder
    def NewNameList(self,list):
        from datetime import date
        from operator import itemgetter
        OldNewDict ={}
        DayList =[]
        DirNames =[]
        dashpositions = []

        #Takes a SAP 2011 recorder *.wav file name and extracts information
        for oldname in list:
            dashpositions.clear()
            for i in range(0,len(oldname)):
                if oldname[i] == '_':
                    # Find where in the SAP file name dashes are that separate ID, recording date and serial number info
                    dashpositions.append(i)
            if len(dashpositions) == 4:
                BirdID = oldname[:dashpositions[0]]
                Month = self.GetMonth(oldname[dashpositions[0]+1:dashpositions[1]])
                Day = int(oldname[dashpositions[1]+1:dashpositions[2]])
                Year = int(oldname[dashpositions[2]+1:dashpositions[3]])
                RecordingDate = date(Year,Month,Day)
                SerNum = int(oldname[dashpositions[3]+1:-4])
                DayList.append([oldname,BirdID,Month,Day,Year,RecordingDate,SerNum])

            # The list passed must not have been of SAP 2011 Recorder *.wav files
            if not DayList:
                return None, None

        # Sort DayList by Recording Date
        DayList = sorted(DayList, key = lambda x: x[5])

        # Determine range of recording days
        FirstDay = DayList[0][5] # Tuple date = date(Year,Month,Day)
        LastDay = DayList[len(DayList)-1][5] # Tuple date = date(Year,Month,Day)
        DeltaDays = LastDay - FirstDay # Tuple date = date(Year,Month,Day)
        NumberOfDays = DeltaDays.days + 1

        # Make a list of directory names, one for each day
        for i in range(NumberOfDays):
            DirNames.append(DayList[0][1] + '_' + self.GetDayText(i+1))

        OldDay = DayList[0][5]  # first day
        FileNumber = 1

        for ParsedDay in DayList:
            CurrentDay = ParsedDay[5]
            DeltaCurrentDay = CurrentDay - FirstDay
            NumberOfDays = DeltaCurrentDay.days + 1
            if CurrentDay != OldDay:
                OldDay = CurrentDay
                FileNumber = 1
            # GetFileText function returns the file number in ##### format with '0' appended to fill five digits
            FileText = self.GetFileText(FileNumber)
            # GetDayText function returns the recording day in ## format with '0' appended left of days < 10
            DayText = self.GetDayText(NumberOfDays)
            # Creates the new file name
            NewName = ParsedDay[1] + '-' + DayText + '-' + FileText + ".wav"
            # Stores the new file name and the name of the directory it will be stored in
            OldNewDict[ParsedDay[0]] = [NewName,(ParsedDay[1]+ '_' + DayText)] #New name of file, Directory it belongs in
            FileNumber = FileNumber + 1

        # All is well
        if len(DirNames) > 0:
            return OldNewDict, DirNames
        # Catch problem with SAP file format
        else:
            window.StatusLabel.config(text='No *.wav files in SAP format found!')
            window.StatusLabel.update()
            return None, None

        # Library of month numbers keyed by text
    def GetMonth(self,TextMonth):
        Months = {'January': 1,'February': 2,'March': 3,'April': 4,'May': 5,'June':6,'July':7,'August':8,
                  'September':9,'October':10,'November':11,'December':12}
        return Months[TextMonth]

    # GetFileText function returns the file number in ##### format with '0' appended to fill five digits
    def GetFileText(self,FileNumber):
        FileText = str(FileNumber)
        for i in range(5-len(str(FileNumber))):
            FileText = "0" + FileText
        return FileText

    # GetDayText function returns the recording day in ## format with '0' appended left of days < 10
    def GetDayText(self,DayNumber):
        if DayNumber < 10:
            DayText = "0" + str(DayNumber)
        else:
            DayText = str(DayNumber)
        return DayText

# Tkinter GUI
root = Tk()
root.title("ParseSAPRecorderWavs")

# Create GUI window
window = ParseGUI(root, Database='sap')

# Infinite loop
root.mainloop()