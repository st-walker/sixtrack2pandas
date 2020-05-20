import pandas as pd
import os.path
import fnmatch

FLUKA_IMPACTS_COLUMNS = ["icoll",
                         "c_rotation", 
                         "s", # m
                         "x", # mm
                         "xp", # mrad
                         "y", # mm
                         "yp", # mrad
                         "nabs", # number of absorbed particles
                         "np",
                         "turn"]

COLL_SUMMARY_COLUMNS =  ["icoll",
                         "collname",
                         "nimp",
                         "nabs",
                         "imp_av",
                         "imp_sig",
                         "length"]

APERTURE_LOSSES_COLUMNS = ["turn",
                           "block",
                           "bezid",
                           "bez",
                           "slos",
                           "partid",
                           "x",
                           "xp",
                           "y",
                           "yp",
                           "etot",
                           "dE",
                           "dT",
                           "A_atom",
                           "Z_atom"]

APERTURE_LOSSES_DTYPES = {"turn": int,
                          "block": int,
                          "bezid": int,
                          "bez": str,
                          "slos": float,
                          "partid": int,
                          "x": float,
                          "xp": float,
                          "y": float,
                          "yp": float,
                          "etot": float,
                          "dE": float,
                          "dT": float,
                          "A_atom": int,
                          "Z_atom": int}

def _get_files(path, filename):
    matches  = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, filename):
            matches.append(os.path.join(root, filename))     
    return matches
    # if os.path.isdir(path):
    #     files = glob2.glob("path/**/{}".format(filename))

    # return files

def load_fluka_impacts(filein, dropna=True):
    if os.path.isdir(filein):
        files = _get_files(filein, "FLUKA_impacts.dat")
    else:
        files = [filein]
    # from IPython import embed; embed()
    df = pd.concat((pd.read_csv(filein,
                                header=None,
                                names=FLUKA_IMPACTS_COLUMNS,
                                # dtype=SURVIVAL_DTYPES,
                                comment="#",
                                delim_whitespace=True) for filein in files))
    if dropna:
        df = df.dropna()
    return df

def load_coll_summary(filein, dropna=True):
    files = _get_files(filein, "coll_summary.dat")
    
    df = pd.concat((pd.read_csv(f,
                                header=None,
                                names=COLL_SUMMARY_COLUMNS,
                                # dtype=SURVIVAL_DTYPES,
                                skiprows=1,
                                comment="#",
                                delim_whitespace=True)
                   for f in files))
    # from IPython import embed; embed()

    if dropna:
        df = df.dropna()
    return df

def load_aperture_losses(filein, dropna=True):
    if os.path.isdir(filein):
        files = _get_files(filein, "aperture_losses.dat")
    else:
        files = [filein]

    df = pd.concat((pd.read_csv(filein,
                     header=None,
                     skiprows=1,
                     names=APERTURE_LOSSES_COLUMNS,
                     # dtypes=APERTURE_LOSSES_DTYPES,
                     comment="#",
                     delim_whitespace=True) for filein in files))
    if dropna:
        df = df.dropna()
    return df

        
    # df = pd.read_csv(filein,
    #                  header=None,
    #                  skiprows=1,
    #                  names=APERTURE_LOSSES_COLUMNS,
    #                  # dtypes=APERTURE_LOSSES_DTYPES,
    #                  comment="#",
    #                  delim_whitespace=True)

    # if dropna:
    #     df = df.dropna()
    # return df
                     

