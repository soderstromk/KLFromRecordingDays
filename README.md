# KLFromRecordingDays
Calculates KL distances by day from multiday Sound Analysis Pro 2011 (SAP2011) MySQL tables

Runs on 64-bit Windows.

Install SAP2011 prior to KLFromRecordingDays. Get SAP2011 from: http://soundanalysispro.com/. 

A sample syllable table "syll_Example.sql" created by SAP2011 is contained in two 7-Zip archive files in the \cx_Freeze\KLFromRecordingDays subdirectory. The example syllable table had to be split into two archive files (Syll_Example.7z.001 and .002) to comply with GitHub file size restrictions. 

Download the two example syllable table archive files to an empty folder. If you have not already, download 7-Zip from: http://www.7-zip.org/ and install it. Right click Syll_Example.7z.001, select 7-Zip -> Extract Files. The two archive files will be combined into "syll_Example.sql" that will allow you to test the KLFromRecordingDays software. 

To install the sample syllable table, using the SAP2011 Data Managment feature click the "Backup and restore data" button, then the "Restore Table" button, navagate to your download folder and and select "syll_Example.sql". This will add a table named syll_pi27 to SAP2011's database. This table contains measures of acoustic features derived from syllables uttered by a zebra finch over the course of 20 days.

KLFromRecordingDays is contained within a self-installing package: KLFromRecordingDays-1.1-amd64.msi. This self-installer also had to be  split, and into six 7-Zip archives: KLFromRecordingDays-1.1-amd64.7z.001 - 006. These archive files are in the \cx_Freeze\KLFromRecordingDays subdirectory.

Create a new folder and download all six archive files. Right click KLFromRecordingDays-1.1-amd64.7z.001, select 7-Zip -> Extract Files.

The archive files are combined into the installer: KLFromRecordingDays-1.1-amd64.msi.

Double-click the installer and follow the instructions. 

A KLFromRecordingDays folder is created. Within this folder is KLFromRecordingDays.exe. Double click this file to run the program.

It will access the SAP2011 database that you previously restored the syll_pi27 table to. This table can now be used to test the software. Select this table and day(s) you wish to use as a template. Days 1-3 were pretreatment recording days and so are recommeded for selection to use as the template. Days not selected as part of the template will be used as targets and KL distances between them and the template days calculated. Days 4-9 were drug treatment days. On day 10 a microlesion of a vocal motor brain region was made. Days 11-20 were recovery days. Note that this mySQL table contains acoustic feature data from over half a million syllables. Depending upon the speed of the computer, processing may take several minutes to over an hour. Progress is indicated by red text at the bottom of the GUI. The features of the software are described in detail in the manuscript.

Daily mean KL distances between acoustic features of syllables produced on the day(s) selected as a template will be calculated for all other days as targets and stored as an Excel spreadsheet named by the subject ID (in the case of the test table this is pi27), days used as template and number of target days. This spreadsheet is stored in the "Directory to Store Results" indicated in the user interface (default is "c:\sap\kl_results"). KL distance measures for 13 acoustic features are presented by target recording day. The daily mean KL distances across all acoustic features are calculated as well as the total number of syllables produced on that day.

Excel data can be used for graphical and statistical analyses to evaluate effects of manipulations to alter vocal phonology.






