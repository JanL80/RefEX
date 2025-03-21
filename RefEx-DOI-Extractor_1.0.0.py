import csv
import requests
import time
import re


print(r'''
                        ______      __ _______   __                          
                        | ___ \    / _|  ___\ \ / /                          
                        | |_/ /___| |_| |__  \ V /                          
                        |    // _ \  _|  __| /   \                           
                        | |\ \  __/ | | |___/ /^\ \                          
                        \_| \_\___|_| \____/\/   \/                                                                              
     ______ _____ _____      _____     _                  _                  
     |  _  \  _  |_   _|    |  ___|   | |                | |                 
     | | | | | | | | |______| |____  _| |_ _ __ __ _  ___| |_ ___  _ __      
     | | | | | | | | |______|  __\ \/ / __| '__/ _` |/ __| __/ _ \| '__|     
     | |/ /\ \_/ /_| |_     | |___>  <| |_| | | (_| | (__| || (_) | |        
     |___/  \___/ \___/     \____/_/\_\\__|_|  \__,_|\___|\__\___/|_|        
                                                                             
              --------------------------------------------                      
                                                                             
                              Kondinski Group                                
                                                                             
                                                                             
                    Author     :    Jan Leodolter
                    Version    :    1.0.0 (alpha)                                                      
                    Date       :    21.03.2025                                                  


              --------------------------------------------                      


    CrossRef:   Crossref. (n.d.). REST API. Retrieved April 27, 2025, 
                from https://api.crossref.org/


    Instructions:
    
        + The given CSV file needs to have two columns:
            1. one column that contains continuous numbering
            2. a second column that contains the references
          (the first row will be ignored, as it is usually a header)
          Make sure that the CSV file uses semicolons as delimiters
        
        + Before using this script, the current working directory should 
          be changed to where the input is located 
          (the full path can also be given)
      
        + After processing is complete, a new CSV file will be written that 
          contains the initial numbering as well as the found DOIs
      
        + Since the code uses an online API (CrossRef), an internet 
          connection is required

                                                                             
''')


time.sleep(1)


def get_doi_from_crossref(reference_text):
    
    ### Constructs the API endpoint
    ### We use 'query.bibliographic=' to search across typical citation fields.
    
    
    base_url = "https://api.crossref.org/works"
    params = {
        "query.bibliographic": reference_text,                                          ### Search in bibliographic fields
        "rows": 1                                                                       ### Return only 1 top match
    }
    
    headers = {
        "User-Agent": "YourAppName/1.0 (mailto:your_email@example.com)"                 ### Currently just dummy-entry; enter information here
    }

    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=30)
        response.raise_for_status()                                                     ### Raise HTTPError if the response was unsuccessful
        data = response.json()
        items = data.get("message", {}).get("items", [])
        
        if items:
            return items[0].get("DOI", "")
        else:
            return ""
    except Exception as e:
        print(f"Error querying CrossRef for reference: {reference_text}")
        print(e)
        return ""





def main(input_csv_path, output_csv_path):
    
    ### Reads references from input_csv_path (two columns: index, reference_text).
    ### Uses the CrossRef API to find DOIs, then writes output to output_csv_path.
    
    
    results = []

    with open(input_csv_path, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=';')
        
        next(reader, None)                                                              ### skips header row

        for row in reader:
            if len(row) < 2:                                                            ### Skip rows that don't have at least 2 columns
                continue
            
            ref_index = row[0]
            input_reference_text = row[1]
            reference_text = re.sub(r'^\s*\d{1,3}[.\)]\s*', '', input_reference_text)
            doi = get_doi_from_crossref(reference_text)                                 ### Get the DOI from CrossRef
            
            print(f"Ref #{ref_index}: DOI = {doi}")                                     ### Print progress (optional)

            results.append([ref_index, reference_text, doi])                            ### Append to results
            
            time.sleep(0)                                                               ### Sleeping between requests

    with open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerow(["Index", "Reference-Text", "DOI"])
        writer.writerows(results)





if __name__ == "__main__":
    input_csv = input("Enter the path for the input CSV file: ")
    output_csv = input("Enter the path for the output CSV file: ")
    print("\n")
    main(input_csv, output_csv)
    print("\nDone! Writing output...")




