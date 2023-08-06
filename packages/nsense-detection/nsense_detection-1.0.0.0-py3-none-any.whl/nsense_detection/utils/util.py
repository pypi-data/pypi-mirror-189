
import os
import sys
from logging import DEBUG
import logging as logger  

#logger.info('Start!')

def check_file_existance(filename):
    if os.path.isfile(filename):
        return True
    else:
        logger.error(f'{filename} not found')
        sys.exit()

def get_savepath(arg_path, src_path, prefix='', post_fix='_res', ext=None):
    """Get savepath
    NOTE: we may have better option...
    TODO: args.save_dir & args.save_path ?
    Parameters
    ----------
    arg_path : str
        argument parser's savepath
    src_path : str
        the path of source path
    prefix : str, default is ''
    postfix : str, default is '_res'
    ext : str, default is None
        if you need to specify the extension, use this argument
        the argument has to start with '.' like '.png' or '.jpg'
    Returns
    -------
    new_path : str
    """

    if '.' in arg_path:
        # 1. args.savepath is actually the image path
        arg_base, arg_ext = os.path.splitext(arg_path)
        new_ext = arg_ext if ext is None else ext
        new_path = arg_base + new_ext
    else:
        # 2. args.savepath is save directory path
        src_base, src_ext = os.path.splitext(os.path.basename(src_path))
        new_ext = src_ext if ext is None else ext
        new_path = os.path.join(
            arg_path, prefix + src_base + post_fix + new_ext
        )
    return new_path