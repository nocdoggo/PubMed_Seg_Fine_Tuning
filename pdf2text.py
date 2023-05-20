!pip install PyMuPDF

import fitz
import re


def extract_tuples_from_pdf(file_path):  #extract every blocks of pdf in tuple form, storing in a list
    
    #initialize the list
    tuples_list = []
    
    #open the pdf file with fitz
    with fitz.open(file_path) as doc:
        
        #get through pages
        for page in doc:
            
            #extract the blocks in a page
            blocks = page.get_text("blocks")
            
            #append block to list
            for block in blocks:
                tuples_list.append(block)
                
    return tuples_list
  

def find_abstract_blocks(tuples_list):  #select the tuples containing "Abstract\n", storing to a list
    
    #initialize the list
    abstract_blocks = []
    
    #create re
    pattern = re.compile(r"Abstract\n", re.IGNORECASE)
    
    #get through the list
    for tpl in tuples_list:
        
        #check if tpl[4], which is the text part, contains "Abstract\n"
        if re.search(pattern, tpl[4]):
            
            #append block to list
            abstract_blocks.append(tpl)
    
    return abstract_blocks
  
  
def find_abstract_blocks_with_next(tuples_list):
    abstract_blocks = []
    pattern = re.compile(r"Abstract\n", re.IGNORECASE)

    for i in range(len(tuples_list)-1):
        tpl = tuples_list[i]
        next_tpl = tuples_list[i+1]

        # Check if the text part of the current tuple contains "Abstract\n"
        if re.search(pattern, tpl[4]):
            # Append the text part of the next tuple to the abstract_blocks list
            abstract_blocks.append(next_tpl[4])

    return abstract_blocks
  
  
def find_conclusion_blocks_with_next(tuples_list):
    conclusion_blocks = []
    pattern = re.compile(r"Conclusion\n", re.IGNORECASE)

    for i in range(len(tuples_list)-1):
        tpl = tuples_list[i]
        next_tpl = tuples_list[i+1]

        # Check if the text part of the current tuple contains "Conclusion\n"
        if re.search(pattern, tpl[4]):
            # Append the text part of the next tuple to the conclusion_blocks list
            conclusion_blocks.append(next_tpl[4])

    return conclusion_blocks
  
  
def main():
    path_file = "/path/to/pdf-file"
    tuples_list = extract_tuples_from_pdf(path_file)
    text_blocks = find_abstract_blocks_with_next(tuples_list)
    for text in text_blocks:
        print(text)

if __name__ == "__main__":
    main()

  
