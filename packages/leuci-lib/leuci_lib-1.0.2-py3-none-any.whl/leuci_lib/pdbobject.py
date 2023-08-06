"""
RSA 4/2/23


"""

import os
from os.path import exists
import urllib.request
from Bio.PDB.MMCIFParser import MMCIFParser        
from Bio.PDB.MMCIF2Dict import MMCIF2Dict


class PdbObject(object):
    def __init__(self, pdb_code, location="", delete=True):
        # PUBLIC INTERFACE
        self.pdb_code = pdb_code        
        self.ebi_link = f"https://www.ebi.ac.uk/pdbe/entry/pdb/{pdb_code}"
        self.pdb_link = f"https://www.ebi.ac.uk/pdbe/entry-files/download/{pdb_code}.cif"
        self.resolution = ""
        # PRIVATE INTERFACE
        self._location = location
        self._delete = delete
        self._filepath = f"{location}{pdb_code}.cif"

        self._fetch_pdbdata()
        self._fetch_maplink()
        self._fetch_mapdata()

    #################################################
    ############ PRIVATE INTERFACE ##################
    #################################################
    def _fetch_pdbdata(self):        
        if not exists(self._filepath):
            urllib.request.urlretrieve(self.pdb_link, self._filepath)                
        structure = MMCIFParser().get_structure(self.pdb_code, self._filepath)
        self._mmcif_dict = MMCIF2Dict(self._filepath)
        self.resolution = structure.header["resolution"]
        if self._delete and exists(self._filepath):
            os.remove(self._filepath)  # tidy up

    def _fetch_maplink(self):
        ccp4_link = ""
        em_link = ""

    def _fetch_mapdata(self):
        ccp4_link = ""
        em_link = ""
