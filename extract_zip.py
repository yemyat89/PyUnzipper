import sys
import os
import zipfile
import glob
import shutil

def _cleanUpFirst(filename):
    path = os.path.split(filename)[0]
    ald_extracted = os.path.splitext(filename)[0]
    if os.path.exists(ald_extracted):
        print 'File (%s) exists. Overriding it.' % ald_extracted
        shutil.rmtree(ald_extracted)

def _unzipDirectory(zipfilePath, dest_dir=None):    
    newpath, fname = os.path.split(zipfilePath)
    if dest_dir:
        newpath = dest_dir
    else:
        if not newpath:
            newpath = './'
    newpath = os.path.join(newpath, os.path.splitext(fname)[0])
    
    with zipfile.ZipFile(zipfilePath) as zfile:
        zfile.extractall(newpath)
    
    return newpath
        

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


def extract(zfile, dest_dir=None, delete_zip=False):
    try:
        croot = _unzipDirectory(zfile, dest_dir=dest_dir)
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
        print 'Usage: python do_unzip.py ZIPFILE_NAME [DESTINATION]'
        sys.exit(1)

    # Remove if there is already a directory with same name as zip file

    filename = sys.argv[1]
    
    if len(sys.argv) > 2:
        target = sys.argv[2]
        if not os.path.exists(target):
            print 'ERROR: Target path %s does not exist.' % target
            sys.exit(1)
        tgclean = os.path.join(target, os.path.split(filename)[1])
        _cleanUpFirst(tgclean)
    else:
        target = None
        _cleanUpFirst(filename)
    
    # Do the extraction

    extract(filename, dest_dir=target)
    
    sys.exit(0)
