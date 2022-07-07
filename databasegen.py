"""Database generator."""
import json
import os


def save_json(file, j):
    """Save dict as .json."""
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(j, f, indent=4, ensure_ascii=False)


def get_ext(file):
    """Get file extension."""
    return file.split('.')[-1]


def get_base(file):
    """Get file name with no extension."""
    return '.'.join(file.split('.')[:-1])


def get_uassets_rec(root_path):
    """Get uasset files."""
    paths = [os.path.join(root_path, p) for p in os.listdir(root_path)]
    dirs = [p for p in paths if os.path.isdir(p)]
    rec_uassets = []
    for d in dirs:
        rec_uassets += get_uassets_rec(d)
    files = [p for p in paths if os.path.isfile(p)]
    uassets = [f for f in files if get_ext(f) == 'uasset']
    return rec_uassets + uassets


PREFIX = {
    'T': 'Texture2D',
    'M': 'Material',
    'SK': 'SkeletalMesh',
    'SM': 'StaticMesh',
}

if __name__ == '__main__':
    json_file = 'database.json'
    uassets = get_uassets_rec('.')
    uassets = [p.split(os.sep) for p in uassets]
    uassets = [(p[1], os.path.join(*p[1:]), get_base(p[-1])) for p in uassets]
    samples = []
    for (version, path, base), i in zip(uassets, range(len(uassets))):
        pref = base.split('_')[0]
        asset_type = PREFIX.get(pref, 'Others')
        if asset_type == 'SkeletalMesh':
            suf = base.split('_')[-1]
            if suf in ['PhysicsAsset', 'Skeleton']:
                asset_type = suf
        samples.append({
            'file': path,
            'version': version,
            'class': asset_type
        })

    save_json(json_file, {'samples': samples})
