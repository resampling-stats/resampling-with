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

clean_cmd = 'rm -rf _quarto-*.yml *_cache/ .quarto/ notebooks/*'

w.rule('svg2x', 'inkscape --export-area-drawing -o $out --export-dpi=300 $in')
w.rule('compile-config', f'{clean_cmd}; ../scripts/set_version.py --output=_quarto-$lang.yml $lang')
w.rule('quarto-render', 'quarto render $in --no-clean --to $format --profile $lang')
w.rule('quarto-render-project', 'quarto render --to $format --profile $lang')
w.rule('copy', 'cp $in $out')
w.rule('cleanup', clean_cmd)
w.rule('print-help', 'echo -ne "$$(cat .ninja-usage)"')
w.rule('check-bibliography', 'biber --tool $in')

# --- SVG diagrams ---
diagrams = glob('diagrams/*.svg') + glob('images/*.svg')
image_formats = ('png', 'pdf')
built_diagrams = {
    fmt: [replace_ext(d, f'.{fmt}') for d in diagrams]
    for fmt in image_formats
}
for fmt in image_formats:
    for (diagram, built_diagram) in zip(diagrams, built_diagrams[fmt]):
        w.build(built_diagram, 'svg2x', diagram)

data_files = glob('data/*')

# --- Configure language ---
for lang in languages:
    w.build(
        f'_quarto-{lang}.yml',
        'compile-config',
        # Should contain the following, but then the r/python language rules conflict
        # See https://github.com/quarto-dev/quarto-cli/issues/5954
        # implicit_outputs=['_variables.yml'],
        implicit=['_quarto.yml.template', 'text_variables.yml'],
        variables={'lang': lang}
    )

# --- Build HTML
quarto_conf = yaml.load(open('_quarto.yml.template'), Loader=yaml.FullLoader)
Rmd_chapters = quarto_conf['book']['chapters']

for lang in languages:
    for data_file in data_files:
        w.build(f'../{lang}-book/notebooks/{data_file}', 'copy', data_file)

    for fmt in ('html', 'pdf'):
        # HTML builds use PNG images; PDF builds use PDF images
        image_fmt = {
            'html': 'png',
            'pdf': 'pdf'
        }[fmt]

        # Individual chapters
        output_files = [f'../{lang}-book/{replace_ext(ch, f".{fmt}")}' for ch in Rmd_chapters]
        for (infile, outfile) in zip(Rmd_chapters, output_files):
            w.build(
                outfile,
                'quarto-render',
                infile,
                implicit=[f'_quarto-{lang}.yml', 'simon_refs.bib'] + built_diagrams[image_fmt],
                variables={'lang': lang, 'format': fmt}
            )

        # Book builds, e.g. `python-book` and `python-book-pdf`
        target_postfix = '' if (fmt == 'html') else '-pdf'

        w.build(
            f'{lang}-book{target_postfix}',
            'quarto-render-project',
            "",
            implicit=[f'_quarto-{lang}.yml', 'simon_refs.bib'] + built_diagrams[image_fmt],
            variables={'lang': lang, 'format': fmt}
        )

w.build('bibcheck', 'check-bibliography', 'simon_refs.bib')
w.build('clean', 'cleanup')
w.build('help', 'print-help')

w.default('help')
