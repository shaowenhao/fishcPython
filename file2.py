Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pathlib import Path
>>> p = path();
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    p = path();
NameError: name 'path' is not defined
>>> p = path(cwd);
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    p = path(cwd);
NameError: name 'path' is not defined
>>> p = Path();
>>> Path.cwd();
WindowsPath('D:/dev_tool/Python')
>>> p = Path.cwd()
>>> n = p / "FishC"
>>> n
WindowsPath('D:/dev_tool/Python/FishC')
>>> n.mkdir(parents=True,exist_ok=True)
>>> n =  p / "FishC/A/B/C"
>>> n.mkdir(parents=True,exist_ok=True)
>>> n = n / "FishC.txt"
>>> 
>>> f = n.open("w")
>>> f.write("2022 09 25 learn")
16
>>> f.close()
>>> [x for x in p.iterdir if x.is_file()]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    [x for x in p.iterdir if x.is_file()]
TypeError: 'method' object is not iterable
>>> [x for x in p.iterdir() if x.is_file()]
[WindowsPath('D:/dev_tool/Python/FishC.txt'), WindowsPath('D:/dev_tool/Python/LICENSE.txt'), WindowsPath('D:/dev_tool/Python/NEWS.txt'), WindowsPath('D:/dev_tool/Python/python.exe'), WindowsPath('D:/dev_tool/Python/python3.dll'), WindowsPath('D:/dev_tool/Python/python39.dll'), WindowsPath('D:/dev_tool/Python/pythonw.exe'), WindowsPath('D:/dev_tool/Python/vcruntime140.dll'), WindowsPath('D:/dev_tool/Python/vcruntime140_1.dll')]
>>> 
>>> ps = [x for x in p.iterdir() if x.is_file()]
>>> for each in ps:
	print(each)

	
D:\dev_tool\Python\FishC.txt
D:\dev_tool\Python\LICENSE.txt
D:\dev_tool\Python\NEWS.txt
D:\dev_tool\Python\python.exe
D:\dev_tool\Python\python3.dll
D:\dev_tool\Python\python39.dll
D:\dev_tool\Python\pythonw.exe
D:\dev_tool\Python\vcruntime140.dll
D:\dev_tool\Python\vcruntime140_1.dll
>>> 
>>> n
WindowsPath('D:/dev_tool/Python/FishC/A/B/C/FishC.txt')
>>> n.rename("NewFishC.txt")
WindowsPath('NewFishC.txt')
>>> n.mkdir(parents=True,exist_ok=True)
>>> 
>>> f = n.open("w")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    f = n.open("w")
  File "D:\dev_tool\Python\lib\pathlib.py", line 1252, in open
    return io.open(self, mode, buffering, encoding, errors, newline,
  File "D:\dev_tool\Python\lib\pathlib.py", line 1120, in _opener
    return self._accessor.open(self, flags, mode)
PermissionError: [Errno 13] Permission denied: 'D:\\dev_tool\\Python\\FishC\\A\\B\\C\\FishC.txt'
>>> f = n.open("w")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    f = n.open("w")
  File "D:\dev_tool\Python\lib\pathlib.py", line 1252, in open
    return io.open(self, mode, buffering, encoding, errors, newline,
  File "D:\dev_tool\Python\lib\pathlib.py", line 1120, in _opener
    return self._accessor.open(self, flags, mode)
PermissionError: [Errno 13] Permission denied: 'D:\\dev_tool\\Python\\FishC\\A\\B\\C\\FishC.txt'
>>> File "D:\dev_tool\Python\lib\pathlib.py", line 1120, in _opener
KeyboardInterrupt
>>> 
>>> n =  p / "FishC/A/B/C"
>>> n.open(w)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    n.open(w)
NameError: name 'w' is not defined
>>> f = n.open("w")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    f = n.open("w")
  File "D:\dev_tool\Python\lib\pathlib.py", line 1252, in open
    return io.open(self, mode, buffering, encoding, errors, newline,
  File "D:\dev_tool\Python\lib\pathlib.py", line 1120, in _opener
    return self._accessor.open(self, flags, mode)
PermissionError: [Errno 13] Permission denied: 'D:\\dev_tool\\Python\\FishC\\A\\B\\C'
>>> n
WindowsPath('D:/dev_tool/Python/FishC/A/B/C')
>>> n = n / "FishC.txt"
>>> f = n.open("w")
>>> f.wtite("hello")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    f.wtite("hello")
AttributeError: '_io.TextIOWrapper' object has no attribute 'wtite'
>>> f.write("hello")
5
>>> f.close()
>>> 
>>> n.rename("NreFishC.txt")
WindowsPath('NreFishC.txt')
>>> """改名字 附带移动"""
'改名字 附带移动'
>>> 
>>> """replace()"""
'replace()'
>>> 
>>> m =  Path("NewFishC.txt")
>>> m
WindowsPath('NewFishC.txt')
>>> n
WindowsPath('D:/dev_tool/Python/FishC/A/B/C/FishC.txt')
>>> m.replace(n)
WindowsPath('D:/dev_tool/Python/FishC/A/B/C/FishC.txt')
>>> 
>>> """rmdir() unlink()删除文件夹，删除文件"""
'rmdir() unlink()删除文件夹，删除文件'
>>> 
>>> n
WindowsPath('D:/dev_tool/Python/FishC/A/B/C/FishC.txt')
>>> n.parent.rmdir()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    n.parent.rmdir()
  File "D:\dev_tool\Python\lib\pathlib.py", line 1363, in rmdir
    self._accessor.rmdir(self)
OSError: [WinError 145] The directory is not empty: 'D:\\dev_tool\\Python\\FishC\\A\\B\\C'
>>> """目录不是空的"""
'目录不是空的'
>>> n.unlink()
>>> n.parent.rmdir()
>>> 
>>> """glob() 功能强大的查找功能"""
'glob() 功能强大的查找功能'
>>> 
>>> p = Path('.')
>>> p.glob("*.txt")
<generator object Path.glob at 0x000001849C33E040>
>>> list(p.glob("*.txt"))
[WindowsPath('FishC.txt'), WindowsPath('LICENSE.txt'), WindowsPath('NEWS.txt'), WindowsPath('NreFishC.txt')]
>>> 
>>> list(p.glob("*/*.py"))
[WindowsPath('Lib/abc.py'), WindowsPath('Lib/aifc.py'), WindowsPath('Lib/antigravity.py'), WindowsPath('Lib/argparse.py'), WindowsPath('Lib/ast.py'), WindowsPath('Lib/asynchat.py'), WindowsPath('Lib/asyncore.py'), WindowsPath('Lib/base64.py'), WindowsPath('Lib/bdb.py'), WindowsPath('Lib/binhex.py'), WindowsPath('Lib/bisect.py'), WindowsPath('Lib/bz2.py'), WindowsPath('Lib/calendar.py'), WindowsPath('Lib/cgi.py'), WindowsPath('Lib/cgitb.py'), WindowsPath('Lib/chunk.py'), WindowsPath('Lib/cmd.py'), WindowsPath('Lib/code.py'), WindowsPath('Lib/codecs.py'), WindowsPath('Lib/codeop.py'), WindowsPath('Lib/colorsys.py'), WindowsPath('Lib/compileall.py'), WindowsPath('Lib/configparser.py'), WindowsPath('Lib/contextlib.py'), WindowsPath('Lib/contextvars.py'), WindowsPath('Lib/copy.py'), WindowsPath('Lib/copyreg.py'), WindowsPath('Lib/cProfile.py'), WindowsPath('Lib/crypt.py'), WindowsPath('Lib/csv.py'), WindowsPath('Lib/dataclasses.py'), WindowsPath('Lib/datetime.py'), WindowsPath('Lib/decimal.py'), WindowsPath('Lib/difflib.py'), WindowsPath('Lib/dis.py'), WindowsPath('Lib/doctest.py'), WindowsPath('Lib/enum.py'), WindowsPath('Lib/filecmp.py'), WindowsPath('Lib/fileinput.py'), WindowsPath('Lib/fnmatch.py'), WindowsPath('Lib/formatter.py'), WindowsPath('Lib/fractions.py'), WindowsPath('Lib/ftplib.py'), WindowsPath('Lib/functools.py'), WindowsPath('Lib/genericpath.py'), WindowsPath('Lib/getopt.py'), WindowsPath('Lib/getpass.py'), WindowsPath('Lib/gettext.py'), WindowsPath('Lib/glob.py'), WindowsPath('Lib/graphlib.py'), WindowsPath('Lib/gzip.py'), WindowsPath('Lib/hashlib.py'), WindowsPath('Lib/heapq.py'), WindowsPath('Lib/hmac.py'), WindowsPath('Lib/imaplib.py'), WindowsPath('Lib/imghdr.py'), WindowsPath('Lib/imp.py'), WindowsPath('Lib/inspect.py'), WindowsPath('Lib/io.py'), WindowsPath('Lib/ipaddress.py'), WindowsPath('Lib/keyword.py'), WindowsPath('Lib/linecache.py'), WindowsPath('Lib/locale.py'), WindowsPath('Lib/lzma.py'), WindowsPath('Lib/mailbox.py'), WindowsPath('Lib/mailcap.py'), WindowsPath('Lib/mimetypes.py'), WindowsPath('Lib/modulefinder.py'), WindowsPath('Lib/netrc.py'), WindowsPath('Lib/nntplib.py'), WindowsPath('Lib/ntpath.py'), WindowsPath('Lib/nturl2path.py'), WindowsPath('Lib/numbers.py'), WindowsPath('Lib/opcode.py'), WindowsPath('Lib/operator.py'), WindowsPath('Lib/optparse.py'), WindowsPath('Lib/os.py'), WindowsPath('Lib/pathlib.py'), WindowsPath('Lib/pdb.py'), WindowsPath('Lib/pickle.py'), WindowsPath('Lib/pickletools.py'), WindowsPath('Lib/pipes.py'), WindowsPath('Lib/pkgutil.py'), WindowsPath('Lib/platform.py'), WindowsPath('Lib/plistlib.py'), WindowsPath('Lib/poplib.py'), WindowsPath('Lib/posixpath.py'), WindowsPath('Lib/pprint.py'), WindowsPath('Lib/profile.py'), WindowsPath('Lib/pstats.py'), WindowsPath('Lib/pty.py'), WindowsPath('Lib/pyclbr.py'), WindowsPath('Lib/pydoc.py'), WindowsPath('Lib/py_compile.py'), WindowsPath('Lib/queue.py'), WindowsPath('Lib/quopri.py'), WindowsPath('Lib/random.py'), WindowsPath('Lib/re.py'), WindowsPath('Lib/reprlib.py'), WindowsPath('Lib/rlcompleter.py'), WindowsPath('Lib/runpy.py'), WindowsPath('Lib/sched.py'), WindowsPath('Lib/secrets.py'), WindowsPath('Lib/selectors.py'), WindowsPath('Lib/shelve.py'), WindowsPath('Lib/shlex.py'), WindowsPath('Lib/shutil.py'), WindowsPath('Lib/signal.py'), WindowsPath('Lib/site.py'), WindowsPath('Lib/smtpd.py'), WindowsPath('Lib/smtplib.py'), WindowsPath('Lib/sndhdr.py'), WindowsPath('Lib/socket.py'), WindowsPath('Lib/socketserver.py'), WindowsPath('Lib/sre_compile.py'), WindowsPath('Lib/sre_constants.py'), WindowsPath('Lib/sre_parse.py'), WindowsPath('Lib/ssl.py'), WindowsPath('Lib/stat.py'), WindowsPath('Lib/statistics.py'), WindowsPath('Lib/string.py'), WindowsPath('Lib/stringprep.py'), WindowsPath('Lib/struct.py'), WindowsPath('Lib/subprocess.py'), WindowsPath('Lib/sunau.py'), WindowsPath('Lib/symbol.py'), WindowsPath('Lib/symtable.py'), WindowsPath('Lib/sysconfig.py'), WindowsPath('Lib/tabnanny.py'), WindowsPath('Lib/tarfile.py'), WindowsPath('Lib/telnetlib.py'), WindowsPath('Lib/tempfile.py'), WindowsPath('Lib/textwrap.py'), WindowsPath('Lib/this.py'), WindowsPath('Lib/threading.py'), WindowsPath('Lib/timeit.py'), WindowsPath('Lib/token.py'), WindowsPath('Lib/tokenize.py'), WindowsPath('Lib/trace.py'), WindowsPath('Lib/traceback.py'), WindowsPath('Lib/tracemalloc.py'), WindowsPath('Lib/tty.py'), WindowsPath('Lib/turtle.py'), WindowsPath('Lib/types.py'), WindowsPath('Lib/typing.py'), WindowsPath('Lib/uu.py'), WindowsPath('Lib/uuid.py'), WindowsPath('Lib/warnings.py'), WindowsPath('Lib/wave.py'), WindowsPath('Lib/weakref.py'), WindowsPath('Lib/webbrowser.py'), WindowsPath('Lib/xdrlib.py'), WindowsPath('Lib/zipapp.py'), WindowsPath('Lib/zipfile.py'), WindowsPath('Lib/zipimport.py'), WindowsPath('Lib/_aix_support.py'), WindowsPath('Lib/_bootlocale.py'), WindowsPath('Lib/_bootsubprocess.py'), WindowsPath('Lib/_collections_abc.py'), WindowsPath('Lib/_compat_pickle.py'), WindowsPath('Lib/_compression.py'), WindowsPath('Lib/_markupbase.py'), WindowsPath('Lib/_osx_support.py'), WindowsPath('Lib/_pydecimal.py'), WindowsPath('Lib/_pyio.py'), WindowsPath('Lib/_py_abc.py'), WindowsPath('Lib/_sitebuiltins.py'), WindowsPath('Lib/_strptime.py'), WindowsPath('Lib/_threading_local.py'), WindowsPath('Lib/_weakrefset.py'), WindowsPath('Lib/__future__.py'), WindowsPath('Lib/__phello__.foo.py')]
>>> 

>>> """如果希望 递归"""
'如果希望 递归'
>>> list(p.glob("**/*.py"))

>>> 