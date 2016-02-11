import glob
glob.glob('*.whl')
with open('index.html', 'w') as f:
    f.write('<ol>\n')
    for wheel in glob.glob('*.whl'):
        f.write("<li><a href='{}'>{}</a></li>\n".format(wheel, wheel))
    f.write('</ol>')
