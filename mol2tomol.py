import sys
sys.path.append('/opt/homebrew/Cellar/pymol/2.4.0_2/libexec/lib/python3.9/site-packages/')
import pymol
from tqdm import tqdm

def main(mol2list, savedir):
    mol2files = open(mol2list, "r")

    for path in tqdm(mol2files):
        path_to_readfile = path.replace('\n','')
        fname = path_to_readfile.split("/")[-1]
        path_to_writefile = check_slash(savedir) + fname[:-4] + "mol"

        pymol.cmd.load(path_to_readfile)
        pymol.cmd.save(path_to_writefile)
        pymol.cmd.remove('all')

    mol2files.close()

def check_slash(dname):
    if dname[-1]=='/':
        return dname + '/'
    else:
        return dname

if __name__ == '__main__':
    argv = sys.argv
    if len(argv)==3:
        main(argv[1], argv[2])
    else:
        print("Please input:")
        print("         $ python mol2tomol.py path-to-list.txt path-to-savedirectory")