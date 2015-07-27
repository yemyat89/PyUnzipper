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
    extractFiles([ZIP_FILE])
```
