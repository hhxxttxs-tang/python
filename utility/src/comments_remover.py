# ref:
#   https://gist.github.com/ChunMinChang/88bfa5842396c1fbbc5b
#   http://nerdfever.com/remove-all-comments-from-c-and-c-source-code/

from __future__ import print_function
import sys, re, os

# for Python 2.7
def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " "  # note: a space and not an empty string
        else:
            return s

    pattern_rule = r"""
           /\*              ##  Start of /* ... */ comment
           [^*]*\*+         ##  Non-* followed by 1-or-more *'s
           (                ##
             [^/*][^*]*\*+  ##
           )*               ##  0-or-more things which don't start with /
                            ##    but do end with '*'
           /                ##  End of /* ... */ comment
    """
    pattern = re.compile(pattern_rule, re.VERBOSE|re.MULTILINE|re.DOTALL)

    r1 = re.sub(pattern, replacer, text,1)
    return r1




def NoComment(infile, outfile):
    root, ext = os.path.splitext(infile)

    valid = [".cpp"]

    if ext.lower() in valid:

        inf = open(infile, "r")

        dirty = inf.read()
        clean = comment_remover(dirty)

        inf.close()

        outf = open(outfile, "wb")  # 'b' avoids 0d 0d 0a line endings in Windows
        outf.write(clean)
        outf.close()

        print("Comments removed:", infile, ">>>", outfile)

    else:

        print("Did nothing:     ", infile)

if __name__ == "__main__":

    for root, folders, fns in os.walk("/Users/ezhou/Google Drive/algorithm/java_solution_NoComments/"):

        for fn in fns:
            filePath = os.path.join(root, fn)
            print(filePath)
            # NoComment(filePath, filePath)