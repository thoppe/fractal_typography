import os, shutil, glob
import subprocess

levels = 5
os.system('mkdir -p pdf')

args = {
    "f_source_tex" : os.path.join('source.tex'),
    "f_table_tex"  : os.path.join('table.tex'),
    "f_source_pdf" : os.path.join('pdf','source.pdf'),
    "f_table_pdf"  : os.path.join('pdf','table.pdf'),
}

def copy_over(fin, level=1, crop=False):
    fout = os.path.join(os.path.dirname(fin),
                        'level_{:03d}.pdf'.format(level))
    shutil.copyfile(fin,fout)
    shutil.move(fin,args["f_source_pdf"])
        
    if crop:
        run_pdfcrop()


def run_pdfcrop():
    cmd = ('pdfcrop -hires '
            '{f_source_pdf} '
           '{f_source_pdf} ').format(**args)
    os.system(cmd)

def run_tex(source):
    cmd = ('pdflatex '
           '-interaction=batchmode '
           '-output-directory=pdf '
           '{source} '
           '1>/dev/null  '
           ).format(source=source)
    os.system(cmd)


# Build the source
print ("Building level {}".format(1))
run_tex(args["f_source_tex"])
copy_over(args["f_source_pdf"],1)

# Build all the copies
for n in range(2, levels+1):
    print ("Building level {}".format(n))
    run_tex(args["f_table_tex"])
    copy_over(args["f_table_pdf"],n)

# Remove the extra files (source, logs and aux files)
def remove_glob(FILES):
    for f in FILES:
        os.remove(f)
        
remove_glob(glob.glob("pdf/source*"))
remove_glob(glob.glob("pdf/*.log"))
remove_glob(glob.glob("pdf/*.aux"))


