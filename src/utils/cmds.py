from src.utils import operations, files


def form_prokka_cmd(newname, inpath, outpath):
    name, ext = newname.split(".")

    args = list()
    args.append(("--cpus", "2"))
    args.append(("--outdir", files.joinpath(outpath, name)))
    args.append(("--prefix", name))
    return operations.format_cmd("prokka", args, files.joinpath(inpath, newname))


def form_roary_cmd(inpath, outpath, ident_min, threads):
    args = list()
    args.append(("-p", threads))
    args.append(("-i", ident_min))
    args.append(("-f", files.joinpath(outpath, "roary")))
    return operations.format_cmd("roary", args, files.joinpath(inpath, "*.gff"))
