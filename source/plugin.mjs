import { fileError, liftChildren, NotebookCell } from 'myst-common';
import { remove } from 'unist-util-remove';

const MODE = 'python';

const R_VARS = {
  lang: 'R',
  np_or_r: 'R',
  other_lang: 'Python',
  cell: 'chunk',
  nb_app: 'RStudio',
  nb_fmt: 'RMarkdown',
  run_key: 'Ctl/Cmd-Shift-Enter',
  array: 'vector',
  an_array: 'a vector',
  true: '`TRUE`',
  false: '`FALSE`',
  sample: '`sample`',
  bincount: '`tabulate`',
  sum: '`sum`',
};
const PYTHON_VARS = {
  lang: 'Python',
  np_or_r: 'NumPy',
  other_lang: 'R',
  cell: 'cell',
  nb_app: 'Jupyter',
  nb_fmt: 'Jupyter',
  run_key: 'Shift-Enter',
  array: 'array',
  an_array: 'an array',
  true: [{ type: 'inlineCode', value: 'True' }],
  false: [{ type: 'inlineCode', value: 'False' }],
  sample: [{ type: 'inlineCode', value: 'rnd.choice' }],
  bincount: [{ type: 'inlineCode', value: 'np.bincount' }],
  sum: [{ type: 'inlineCode', value: 'np.sum' }],
};

/**
 * Create a documentation section for a directive
 *
 * @type {import('myst-common').RoleSpec}
 */
const varShortCode = {
  name: 'var',
  body: {
    type: String,
    required: true,
  },
  run(data, vfile) {
    const replacement = PYTHON_VARS[data.body];
    if (!replacement) {
      fileError(vfile, `shortcode: "var", unknown replacement "${data.body}"`, { node: data.node });
      return;
    }
    if (typeof replacement === 'string') {
      return [{ type: 'text', value: replacement }];
    }
    return replacement;
  },
};

/**
 * Create a documentation section for a directive
 *
 * @type {import('myst-common').RoleSpec}
 */
const spanRole = {
  name: 'span',
  body: {
    type: String,
    required: true,
  },
  run(data, vfile) {
    if (data.node.options?.class !== MODE) return [];
    return [{ type: 'span', children: data.node.children[0].children }];
  },
};

const langBlock = {
  name: 'lang-block',
  alias: ['python', 'r'],
  body: {
    type: String,
    required: true,
  },
  run(data, vfile) {
    const name = data.name;
    if (name !== MODE) return [];
    const code = {
      type: 'code',
      lang: data.name,
      executable: true,
      value: data.body ?? '',
    };
    const output = {
      type: 'output',
      data: [],
    };
    const block = {
      type: 'block',
      kind: NotebookCell.code,
      children: [code, output],
      data: {},
    };
    return [block];
  },
};

/**
 * Create a documentation section for a directive
 *
 * @type {import('myst-common').TransformSpec}
 */
const divTransform = {
  name: 'Hide Divs',
  stage: 'document',
  plugin: (opts, utils) => (mdast) => {
    const divs = utils.selectAll('div', mdast);
    divs.map((div) => {
      if (div.class === MODE) {
        div.type = '__lift__';
      } else {
        div.type = '__remove__';
      }
    });
    remove(mdast, '__remove__');
    liftChildren(mdast, '__lift__');
    return mdast;
  },
};

/**
 * @type {import('myst-common').MystPlugin}
 */
const plugin = {
  name: 'Short Code Plugins',
  author: 'Rowan Cockett',
  license: 'MIT',
  directives: [langBlock],
  roles: [varShortCode, spanRole],
  transforms: [divTransform],
};

export default plugin;
