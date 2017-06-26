# KLFromRecordingDays
Calculates KL distances by day from multiday Sound Analysis Pro 2011 (SAP2011) MySQL tables

Runs on 64-bit Windows.

Install SAP2011 prior to KLFromRecordingDays. Get SAP2011 from: http://soundanalysispro.com/. Download the "syll_Example.sql" file within this GitHub directory. This file creates a SAP2011 syllable table that will allow you to test the KLFromRecordingDays software.

To install the sample syllable table, through the SAP2011 Data Managment feature click the Backup and restore data button, then the Restore Table button, navagate to your download folder and and select "syll_Example.sql". This will add a table named syll_pi73v to SAP2011's database. This table contains measures of acoustic features derived from syllables uttered by a zebra finch over the course of several days.

KLFromRecordingDays is contained within a self-installing package: KLFromRecordingDays-1.1-amd64.msi. To comply with GitHub file size restrictions the self-installer is split into six 7-Zip archives: KLFromRecordingDays-1.1-amd64.7z.001 - 006. These archive files are in the \cx_Freeze\KLFromRecordingDays subdirectory.

If you have not already, download 7-Zip from: http://www.7-zip.org/ and install it.

Create a folder and download all six archive files. Right click KLFromRecordingDays-1.1-amd64.7z.001, select 7-Zip -> Extract Files...

The archive files are combined into the installer: KLFromRecordingDays-1.1-amd64.msi.

Double-click the installer and follow the instructions. 

A KLFromRecordingDays folder is created. Within this folder is KLFromRecordingDays.exe. Double click this file to run the program.

It will access the SAP2011 database where the syll_pi73v table was imported. Select this table and day(s) you wish to use as a template. Days 1-3 were pretreatment recording days. Days 4-9 were drug treatment days. On day 10 an HVC microlesion was done. Days 11-20 were recovery days. Note that this my SQL table contains acoustic feature data from over a quarter million syllables. Depending upon the speed of the computer, processing may take several minutes to over an hour. Progress is indicated by red text at the bottom of the GUI. The features of the software are described in detail in the manuscript.

KL distances between acoustic features of syllables produced on the day(s) selected as a template will be calculated for all other days as targets and stored in an Excel spreadsheet. This spreadsheet is stored in the "Directory to Store Results" indicated in the user interface (default is "c:\sap\kl_results". KL distance measures for 13 acoustic features are presented by target recording day. The daily means across all acoustic features are calculated as well as the total number of syllables produced on that day.






