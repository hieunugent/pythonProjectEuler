def shorted_equivalent_path(path: str)-> str:
    if not path:
        raise ValueError('Empty string is not a valid path')
    path_names = []
    if path[0] =='/':
        path_names.append('/')
    for token in (token for token in path.split('/'))