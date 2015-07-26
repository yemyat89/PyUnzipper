import sys
import os
import zipfile
import glob
import shutil

def _cleanUpFirst(filename):
    path = os.path.split(filename)[0]
    ald_extracted = os.path.join(path, os.path.splitext(filename)[0])
    
    if os.path.exists(ald_extracted):
        print 'File (%s) exists. Overriding it.' % ald_extracted
        shutil.rmtree(ald_extracted)

def _unzipDirectory(zipfilePath):    
    newpath, fname = os.path.split(zipfilePath)
    if not newpath:
        newpath = './%s' % newpath
    
    with zipfile.ZipFile(zipfilePath) as zfile:
        zfile.extractall(newpath)

    return os.path.join(newpath, os.path.splitext(fname)[0])
        

def _getallzipsInside(d):
    zips = []
    for f in glob.glob('%s/*' % d):
        if os.path.isfile(f):
            if os.path.splitext(f)[1] == '.zip':
                zips.append(f)
        elif os.path.isdir(f):
            zips.extend(_getallzipsInside(f))
        else:
            print 'What is this type!'
    return zips


def extract(zfile, delete_zip=False):
    
    try:
        croot = _unzipDirectory(zfile)
        internal_zips = _getallzipsInside(croot)
        for izipfile in internal_zips:
            extract(izipfile, delete_zip=True)
    except IOError:
        print 'ERROR: File (%s) not found.' % zfile
    except zipfile.BadZipfile:
        print 'ERROR: File (%s) is not a zip file' % zfile
    finally:
        if delete_zip and os.path.exists(zfile):
            os.remove(zfile)


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print 'Usage: python do_unzip.py [ZIPFILE_NAME]'
        sys.exit(1)

    # Remove if there is already a directory with same name as zip file

    filename = sys.argv[1]
    _cleanUpFirst(filename)
    
    # Do the extraction

    extract(filename)
    
    sys.exit(0)
