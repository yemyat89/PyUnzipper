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


def extractFiles(zipfile_name, destination_dir=None):
    
    # zipfile valid path?
    
    if not os.path.exists(zipfile_name):
        print 'Zip file %s not found.' % zipfile_name
        return None

    # directory exists

    path = os.path.split(zipfile_name)[0]
    if destination_dir is not None:
        path = destination_dir
    
    fn = os.path.split(zipfile_name)[1]
    fn = os.path.splitext(fn)[0]

    newpath = os.path.join(path, fn)
    if os.path.exists(newpath):
        print 'Directory %s exists.' % newpath
        return None
    
    return extract(zipfile_name, destination_dir, delete_zip=False)


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print 'Usage: python do_unzip.py ZIPFILE_NAME [DESTINATION]'
        sys.exit(1)

    # Remove if there is already a directory with same name as zip file

    filename = sys.argv[1]
    
    if len(sys.argv) > 2:
        target = sys.argv[2]
    else:
        target = None
    
    # Do the extraction

    extractFiles(filename, destination_dir=target)
    
    sys.exit(0)
