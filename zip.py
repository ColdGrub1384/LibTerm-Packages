import sys
import zipfile
import os

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except (ImportError, AttributeError):
    compression = zipfile.ZIP_STORED

modes = {
    zipfile.ZIP_DEFLATED: 'deflated',
    zipfile.ZIP_STORED: 'stored',
}

def zip_dir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def zip_file(path, ziph):
    mode_name = modes[compression]
    ziph.write(path, compress_type=compression)

try:
    if os.path.isfile(sys.argv[1]):
        if not (os.path.isfile(sys.argv[1] + ".zip")):
            try:
                with zipfile.ZipFile(sys.argv[1] + ".zip", 'w') as zip_ref:
                    zip_file(sys.argv[1], zip_ref)
            except Exception as e:
                print("Terminated with exception " + str(e))
        else:
            print(sys.argv[1] + ".zip" + " is already existing!" +
                  "Please delete it to continue!")
    elif os.path.isdir(sys.argv[1]):
        if not (os.path.isfile(sys.argv[1] + ".zip")):
            try:
                with zipfile.ZipFile(sys.argv[1] + ".zip", 'w') as zip_ref:
                    zip_dir(sys.argv[1], zip_ref)
            except Exception as e:
                print("Terminated with exception " + str(e))
        else:
            print(sys.argv[1] + ".zip" + " is already existing!" +
                  "Please delete it to continue!")
    else:
        print("File wasn't found!")
except IndexError:
    print("Usage: zip <zip_file>")
