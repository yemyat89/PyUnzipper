#PyUnzipper

This tool allows you to extract a ZIP file which may contain nested zips. It goes to each nested zip and do the extraction recursively. You can use it from command line or from your code. It is free to use. Just implemented to see how it behaves. There is a test module (test.py) that test with a ZIP file containing valid nested ZIPs and invaldi ZIP files. In such case, only the valid ones are extracted as expected.

##Usage

**From command line**

```
    python extract_zip.py [ZIP_FILE] (DESTINATION)
```

**Calling programmatically**

```
    from extract_zip import extractFiles
    extractFiles([ZIP_FILE], (DESTINATION))
```

##Example

Calling the script with provided sample file to extract inside `/tmp/extract`.

```
    python extract_zip.py sample_input/package_valid.zip /tmp/extract
```

The result is files being extracted as follows.

```
/tmp
/tmp/extract
/tmp/extract/package_valid
/tmp/extract/package_valid/package_valid
/tmp/extract/package_valid/package_valid/input
/tmp/extract/package_valid/package_valid/input/external
/tmp/extract/package_valid/package_valid/input/external/data.vmx
/tmp/extract/package_valid/package_valid/input/internal
/tmp/extract/package_valid/package_valid/path
/tmp/extract/package_valid/package_valid/path/abc
/tmp/extract/package_valid/package_valid/path/abc/abc
/tmp/extract/package_valid/package_valid/path/abc/abc/opaque
/tmp/extract/package_valid/package_valid/path/abc/abc/opaque/opaque
/tmp/extract/package_valid/package_valid/path/abc/abc/opaque/opaque/ghop
/tmp/extract/package_valid/package_valid/path/abc/abc/opaque/opaque/ghop/ghop
/tmp/extract/package_valid/package_valid/path/abc/abc/opaque/opaque/ghop/ghop/lma.txt
/tmp/extract/package_valid/package_valid/path/abc/abc/opaque/opaque/lkl.txt
/tmp/extract/package_valid/package_valid/path/abc/abc/opaque/opaque/nn.txt
```
