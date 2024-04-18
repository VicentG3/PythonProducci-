import os
import shutil

def categoritzar_arxiu(nom_arxiu):
    extensio = nom_arxiu.split(".")[-1].lower()
    imatges_extensio = ["jpg", "jpeg", "png", "gif"]
    documents_extensio = ["pdf", "doc", "docx", "txt"]
    
    if extensio in imatges_extensio:
        return "imatges"
    elif extensio in documents_extensio:
        return "documents"
    else:
        return "altres"

def moure_arxiu(origen, desti):
    try:
        shutil.move(origen, desti)
        print(f"Arxiu mogut: {origen} -> {desti}")
    except Exception as e:
        print(f"Error en moure l'arxiu {origen}: {str(e)}")

def main():
    directori_actual = os.getcwd()
    
    imatges_dir = os.path.join(directori_actual, "Imatges")
    documents_dir = os.path.join(directori_actual, "Documents")
    altres_dir = os.path.join(directori_actual, "Altres")
    
    for directori in [imatges_dir, documents_dir, altres_dir]:
        try:
            if not os.path.exists(directori):
                os.makedirs(directori)
                print(f"Creat directori: {directori}")
        except Exception as e:
            print(f"Error en crear el directori {directori}: {str(e)}")
    
    arxius = os.listdir(directori_actual)
    
    for arxiu in arxius:
        if os.path.isfile(arxiu):
            categoria = categoritzar_arxiu(arxiu)
            if categoria == "imatges":
                moure_arxiu(arxiu, os.path.join(imatges_dir, arxiu))
                print(f"Arxiu classificat com a imatge: {arxiu}")
            elif categoria == "documents":
                moure_arxiu(arxiu, os.path.join(documents_dir, arxiu))
                print(f"Arxiu classificat com a document: {arxiu}")
            else:
                moure_arxiu(arxiu, os.path.join(altres_dir, arxiu))
                print(f"Arxiu classificat com a altre: {arxiu}")
    
    print("Procés de categorització completat amb èxit.")

if __name__ == "__main__":
    main()