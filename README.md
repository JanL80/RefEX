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


