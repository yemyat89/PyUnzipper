import shutil
import os
import tempfile
import unittest
from extract_zip import extractFiles


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.zip_dir = os.path.join(tempfile.gettempdir(), 'test-ymt')
        os.mkdir(self.zip_dir)
        self.extract_dir = os.path.join(tempfile.gettempdir(), 'test-ymt-extract')
        os.mkdir(self.extract_dir)

    def tearDown(self):
        shutil.rmtree(self.zip_dir)
        shutil.rmtree(self.extract_dir)
        if os.path.exists('%s.zip' % self.zip_dir):
            os.remove('%s.zip' % self.zip_dir)
    
    def _createZip(self, temp_dir):

        # Create files in top level directory

        # - [temp_dir]/data1.txt
        # - [temp_dir]/data2.txt

        with open(os.path.join(temp_dir, 'data1.txt'), 'w') as f:
            f.write('')
        with open(os.path.join(temp_dir, 'data2.txt'), 'w') as f:
            f.write('')

        # Create sub nested zips
        
        # - [temp_dir]/a/b/<c.zip>/data7.txt
        # - [temp_dir]/a/b/<c.zip>/d/<e.zip>/data3.txt
        # - [temp_dir]/a/b/<c.zip>/d/<e.zip>/data4.txt
        # - [temp_dir]/a/b/<c.zip>/d/<f.zip>/data5.txt
        # - [temp_dir]/a/b/<c.zip>/d/<f.zip>/data6.txt
        # - [temp_dir]/a/b/<c.zip/d/<f.zip>/invalid_zip_1.zip
        # - [temp_dir]/a/b/<c.zip>/d/<f.zip>/invalid_zip_2.zip

        abcde = os.path.join(temp_dir, 'a', 'b', 'c', 'd', 'e')
        os.makedirs(abcde)

        with open(os.path.join(abcde, 'data3.txt'), 'w') as f:
            f.write('')
        with open(os.path.join(abcde, 'data4.txt'), 'w') as f:
            f.write('')
        shutil.make_archive(abcde, 'zip', abcde)
        shutil.rmtree(abcde)
        
        abcdf = os.path.join(temp_dir, 'a', 'b', 'c', 'd', 'f')
        os.makedirs(abcdf)
                
        with open(os.path.join(abcdf, 'data5.txt'), 'w') as f:
            f.write('')
        with open(os.path.join(abcdf, 'data6.txt'), 'w') as f:
            f.write('')
        with open(os.path.join(abcdf, 'invalid_zip_1.zip'), 'w') as f:
            f.write('')
        with open(os.path.join(abcdf, 'invalid_zip_2.zip'), 'w') as f:
            f.write('')
        shutil.make_archive(abcdf, 'zip', abcdf)
        shutil.rmtree(abcdf)

        abc = os.path.join(temp_dir, 'a', 'b', 'c')
        with open(os.path.join(abc, 'data7.txt'), 'w') as f:
            f.write('')
        shutil.make_archive(abc, 'zip', abc)
        shutil.rmtree(abc)

        shutil.make_archive(temp_dir, 'zip', temp_dir)


    def _verify(self, extract_dir):
        
        x = [
            (extract_dir, 'test-ymt', 'data1.txt'),
            (extract_dir, 'test-ymt', 'data2.txt'),
            (extract_dir, 'test-ymt', 'a/b/c/d/e/data3.txt'),
            (extract_dir, 'test-ymt', 'a/b/c/d/e/data4.txt'),
            (extract_dir, 'test-ymt', 'a/b/c/d/f/data5.txt'),
            (extract_dir, 'test-ymt', 'a/b/c/d/f/data6.txt'),
            (extract_dir, 'test-ymt', 'a/b/c/data7.txt'),
        ]

        p = os.path.join(*x[0])
        assert (os.path.exists(p) == True)


    def testExtract(self):
        self._createZip(self.zip_dir)
        extractFiles('%s.zip' % self.zip_dir, self.extract_dir)
        self._verify(self.extract_dir)

if __name__ == '__main__':
    unittest.main()

