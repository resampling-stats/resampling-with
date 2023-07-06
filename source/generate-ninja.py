"""
See

  https://github.com/ninja-build/ninja/blob/master/misc/ninja_syntax.py

for the Writer API. This is truly minimal, and you could just as well
output these with "print" statements.

Ninja variables are listed a https://ninja-build.org/manual.html#ref_rule

"""

from glob import glob
import os
import yaml

from ninja import Writer


w = Writer(open('build.ninja', 'w'), width=120)

languages = ('python', 'r')


def replace_ext(fn, new_ext):
    return os.path.splitext(fn)[0] + new_ext

w.rule('svg2png', 'inkscape --export-area-drawing -o $out --export-dpi=300 $in')
w.rule('compile-config', '../scripts/set_version.py --output=_quarto-$lang.yml $lang')
w.rule('quarto', 'quarto render $in --to $format --profile $lang')
w.rule('cleanup', 'rm -rf *_cache/ .quarto/ notebooks/*')
w.rule('print-help', 'echo -ne "$$(cat .ninja-usage)"')
w.rule('check-bibliography', 'biber --tool $in')

# --- SVG diagrams ---
diagrams = glob('diagrams/*.svg') + glob('images/*.svg')
built_diagrams = [replace_ext(d, '.png') for d in diagrams]
for (diagram, built_diagram) in zip(diagrams, built_diagrams):
    w.build(built_diagram, 'svg2png', diagram)

# --- Configure language ---
for lang in languages:
    w.build(
        f'_quarto-{lang}.yml',
        'compile-config',
        # Should contain the following, but then the r/python language rules conflict
        # See https://github.com/quarto-dev/quarto-cli/issues/5954
        # implicit_outputs=['_variables.yml'],
        implicit=['_quarto.yml.template', 'text_variables.yml'] + built_diagrams,
        variables={'lang': lang}
    )

# --- Build HTML
quarto_conf = yaml.load(open('_quarto.yml.template'), Loader=yaml.FullLoader)
Rmd_chapters = quarto_conf['book']['chapters']

for lang in languages:
    # Individual chapters
    output_files = [f'../{lang}-book/{replace_ext(ch, ".html")}' for ch in Rmd_chapters]
    for (infile, outfile) in zip(Rmd_chapters, output_files):
        w.build(
            outfile,
            'quarto',
            infile,
            implicit=[f'_quarto-{lang}.yml', 'simon_refs.bib'],
            variables={'lang': lang, 'format': 'html'}
        )

    # Book
    w.build(
        f'{lang}-book',
        'phony',
        output_files
    )

w.build('bibcheck', 'check-bibliography', 'simon_refs.bib')
w.build('clean', 'cleanup')
w.build('help', 'print-help')

w.default('help')
