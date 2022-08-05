# NOMBRE (Roa, Luis):

# Lectura y visualización
def download_pubmed(k): 
    """
    Docstring download_pubmed
    k = Keyword1, palabra clave con la que se realizará la búsqueda
    """
    from Bio import Entrez 
    import re

    Entrez.email = "gualapuro.moises@gmail.com"
    handle = Entrez.esearch(db="pubmed", 
                            term="k[Title]",
                            usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    record["Count"]
    print (record)

    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                           rettype="medline", 
                           retmode="text", 
                           retstart=0,
    retmax=543, webenv=webenv, query_key=query_key)
    
    nombre= k+".txt"
    out_handle = open(nombre, "w")
    data = handle.read() 
    handle.close()
    out_handle.write(data) 
    out_handle.close()
    return 



def mapscience(       ):
    """
    Docstring map_science
    
    
    
    
    
    
    
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 

    