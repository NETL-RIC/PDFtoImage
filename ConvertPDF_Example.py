#import modules
from pdf2image import convert_from_path
import os

#input paths where files will be converted
pdfpath = r"E:\_NLP\snorkel\ImageRec\EDX\InputPDF"
outputfolder = r"E:\_NLP\snorkel\ImageRec\EDX\pdfImages"

#read all files and subfoders from input folder
folder = os.walk(pdfpath)

#loop through each file
for path, dir, file in folder:
    for f in file:
        #filter PDF files
        if f.endswith(".pdf"):
            #create file path for found pfd file
            filepath =os.path.join(path,f)
            #print(filepath)
            #try to convert pdf file to image
            try:
                #convert pages at 400 pixels and (none) preserve aspect ratio
                pages = convert_from_path(filepath, 400, None)
                #loop through pages append page number and save a jpg 
                for x, page in enumerate(pages):
                    page.save(outputfolder+"\\"+str(x)+os.path.splitext(f)[0]+'.jpg', 'JPEG')
            #if error print error
            except:
                print("Error with ", filepath)
                continue
