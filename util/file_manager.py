import pandas as pd

class CSVFileManager:
  """
  Gestiona la lectura y escritura de ficheros CSV.
  Argumentos:
    Ruta del fichero CSV con el que queremos trabajar (path)
  """
  def __init__(self, path: str):
    self.path = path

  def read(self) -> str:
    """Lee CSV y devuelve su contenido como DataFrame"""
    return pd.read_csv(self.path)  
  
  def write(self, dataFrame : pd.DataFrame):
    """Escribe los datos de dataFrame al final de un CSV, sin incluir la cabecera """
    dataFrame.to_csv(self.path, mode = "a", index = False, header = False)
