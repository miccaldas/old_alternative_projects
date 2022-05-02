"""Write file that will set pygment settings for a note"""
import os
import subprocess


def write_setting():
    """Write pygments settings in another file"""

    path_directory = "/home/mic/old-html/posts_notes_md/"
    pyfile_directory = "/home/mic/python/paste_pygments/python_config_files/"
    paths = []
    pyfiles = []
    for filename in os.listdir(path_directory):
        print(f"filename is {filename}")
        path = os.path.join(path_directory, filename)
        print(f"path is {path}")
        paths.append(path)
        print(f"paths is {paths}")
        pyfile = pyfile_directory + filename[:-3] + ".py"
        print(f"pyfile is {pyfile}")
        pyfiles.append(pyfile)
        print(f"pyfiles is {pyfiles}")

    for pyfile in pyfiles:
        cmd = "touch " + pyfile
        print(f"cmd is {cmd}")
        subprocess.run(cmd, shell=True)

    for pyfile in pyfiles:
        with open(pyfile, "w") as f:
            f.write("import os\n")
            f.write("from pygments import highlight\n")
            f.write("from pygments.lexers import get_lexer_by_name\n")
            f.write("from pygments.formatters import HtmlFormatter\n")
            f.write("\n")
            f.write("path_directory = '/home/mic/old-html/posts_notes_md'\n")
            f.write("pyfile_directory = '/home/mic/python/paste_pygments/python_config_files'\n")
            f.write("for filename in os.listdir(path_directory):\n")
            f.write("    print(os.path.join(path_directory, filename))\n")
            f.write("pyfile_directory = '/home/mic/python/paste_pygments/python_config_files'\n")
            f.write("path = os.path.join(path_directory, filename)\n")

    path_names = []
    pyfile_names = []
    path_dirname = "/home/mic/old-html/posts_notes_md"
    pyfile_dirname = "/home/mic/python/paste_pygments/python_config_files"
    path_files = os.listdir(path_dirname)
    pyfile_files = os.listdir(pyfile_dirname)
    for file in path_files:
        path_name = file[:-3]
        path_names.append(path_name)
    print(f"path_names is {path_names}")
    for file in pyfile_files:
        pyfile_name = file[:-3]
        pyfile_names.append(pyfile_name)
    print(f"pyfile is {pyfile_names}")
    common = set(path_names).intersection(pyfile_names)
    print(f"common is {common}")
    for i in common:
        path = path_directory + i + ".md"
        pyfile = pyfile_directory + i + ".py"
        input_file = open(path, "r+")
        note_content = input_file.readlines()
        output_file = open(pyfile, "a")
        output_file.write('code = """')
        for line in note_content:
            output_file.write(line)
        output_file.write('"""')

    for pyfile in pyfiles:
        with open(pyfile, "a") as f:
            f.write("\n")
            f.write("pyfile = pyfile_directory + '/' + filename[:-3] + '.py'\n")
            f.write("lexer = get_lexer_by_name('python', stripall=True)\n")
            f.write("formatter = HtmlFormatter(linenos=True, full=True, style='zenburn')\n")
            f.write("f = open(pyfile[:-3] + '.html', 'w')\n")
            f.write("highlight(code, lexer, formatter, outfile=f)\n")


if __name__ == "__main__":
    write_setting()
