"""To be able to format HTML code inside PHP files is impossible, unless the html
   code is contained in  a html file. As I'm using html inside PHP files,
   I can't use it directly. To solve this, this script will change file
   extensions from php to html, open the files to run the formatter, and finally,
   convert them back to php."""

import inspect
import os
import shutil
import subprocess
import sys
from pathlib import Path

import fire
import isort
from loguru import logger

subprocess.run(["isort", __file__])

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


class PhpFormatter:
    """By default all files in a directory with a given extension will be converted.
    However, if a list of files is given as arguments to a command, that will be
    used instead. We'll first identify the files with the php extension, then
    we'll change their extensions to html, open the files, write a comment and
    leave. Finally we'll change them back to php extensions, with a 'new' prefix."""

    @logger.catch
    def create_html_folder(self):
        """It will be used to house the newly created files."""

        dir = os.getcwd()
        path = dir + "/" + "html"
        os.mkdir(path)

    @logger.catch
    def available_php_files(self):
        """Looks inside the current directory for files with a '.php' extension,
        appends them to a list. Returns said list."""

        self.php_file_list = []
        files = os.listdir(os.curdir)
        for file in files:
            if ".php" in file:
                self.php_file_list.append(file)
        return self.php_file_list

    @logger.catch
    def create_files(self, *files):
        """If the module is started without command line arguments, the module will
        use the former method's list to process, otherwise, the file list given
        in command line arguments are the target. The files will be copied to a
        different directory. Afterwards we'll replace their extensions for html
        ones."""

        flist = self.available_php_files()
        if files:
            ficheiros = files
        else:
            ficheiros = flist

            for file in ficheiros:
                if ".php" in file:
                    src = "./" + file
                    self.dst = "html/"
                    shutil.copy(src, self.dst)
                    self.new_dir = os.listdir(self.dst)
                    for file in self.new_dir:
                        infilename = os.path.join(self.dst, file)
                        newfile = infilename.replace(".php", ".html")
                        os.rename(infilename, newfile)

    @logger.catch
    def open_write_comment(self):
        """We change directory to the one that houses the changed names files,
        We run a while loop that loops only once. It is there just to start
        the for loop beneath him. For each file ib the directory, and only
        once, we run a inner function that appends a message to the bottom
        of the file. The objective is to trigger the autoformatter, that
        runs everytime the file is saved."""

        os.chdir(self.dst)
        self.curdir = os.getcwd()
        sourcelst = []
        for file in os.listdir(self.curdir):
            source = self.curdir + "/" + file
            sourcelst.append(source)

        def runs(file):
            cmd = "tidy -m " + file + " -f tidy_errors.txt"
            subprocess.run(cmd, shell=True)
            with open(file, "a") as f:
                f.write("<!--This file was automatically formatted.-->")

        run_once = 0
        while run_once < 1:
            for file in sourcelst:
                runs(file)
                run_once += 1

        self.signed_files = []
        for source in sourcelst:
            self.signed_files.append(source)

    @logger.catch
    def new_php(self):
        """Gets all the html files, copies to the original folder, and
        turns them back to php, but now with the code formatted."""

        for file in self.signed_files:
            src = file
            new = os.path.dirname(__file__)
            shutil.copy(src, new)

        for file in os.listdir(new):
            if ".html" in file:
                infilename = os.path.join(new, file)
                newfile = infilename.replace(".html", ".php")
                os.rename(infilename, newfile)

    @logger.catch
    def main(self):
        """Main method. It functions as the interface that runs, chooses and
        controls all the other methods."""

        self.create_html_folder()
        self.available_php_files()
        self.create_files()
        self.open_write_comment()
        self.new_php()
        self.new_php


if __name__ == "__main__":
    fire.Fire(PhpFormatter)


# format.available_php_files()
# format.create_files()
# format.open_write_comment()
# format.new_php()
