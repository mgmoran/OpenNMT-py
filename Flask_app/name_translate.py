from __future__ import unicode_literals

from onmt.translate.translator import build_translator

import onmt.opts as opts
from onmt.utils.parse import ArgumentParser


def translate(src):
    parser = _get_parser()
    opt = parser.parse_args()

    translator = build_translator(opt, report_score=False)
    result = translator.translate(
        src=src,
        tgt=src,
        batch_size=opt.batch_size,
        batch_type=opt.batch_type,
        attn_debug=opt.attn_debug,
        align_debug=opt.align_debug
        )
    print(''.join(result[1][0][0].split(" ")))

def _get_parser():
    parser = ArgumentParser()
    opts.config_opts(parser)
    opts.translate_opts(parser)
    return parser

if __name__=='__main__':
    translate("src_file.txt")
