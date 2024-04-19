import glob2 as glob

from matdata.util.parsers import json2movelet

def read_all_movelets(path_name, name='movelets'):
    count = 0
    path_to_file = glob.glob(os.path.join(path_name, '**', 'moveletsOnTrain.json'), recursive=True)

    movelets = []
    for file_name in path_to_file:
        aux_mov = read_movelets(file_name, name, count)
        movelets = movelets + aux_mov
        count = len(movelets)

    return movelets
    
def read_movelets(file_name, name='movelets', count=0):
    with open(file_name) as f:
        return json2movelet(f, name, count)
    return []