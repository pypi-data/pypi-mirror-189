from itertools import zip_longest
from pathlib import Path
from sys import stdout
from typing import Dict, List

import typer

from nef_pipelines.lib.nef_lib import (
    molecular_system_from_entry,
    molecular_system_from_entry_or_exit,
    read_entry_from_file_or_stdin_or_exit_error,
)
from nef_pipelines.lib.sequence_lib import (
    frame_to_chains,
    get_chain_starts,
    sequence_from_frame,
)
from nef_pipelines.lib.structures import SequenceResidue
from nef_pipelines.lib.util import (
    STDIN,
    exit_error,
    parse_comma_separated_options,
    smart_open,
)
from nef_pipelines.transcoders.fasta.exporters.sequence import STDOUT
from nef_pipelines.transcoders.nmrview import export_app

app = typer.Typer()


@export_app.command()
def sequences(
    file_name_template: str = typer.Option(
        "%s.seq",
        "-t",
        "--template",
        help="the template for the filename to export to %s will get replaced by the name of the chain or a filename if"
        "set with the sequence_text-names option",
        metavar="<sequence-sequence_text.seq>",
    ),
    input: Path = typer.Option(
        STDIN, "-i", "--in", help="sequence_text to read input from [- is stdin]"
    ),
    output_to_stdout: bool = typer.Option(
        False, "-o", "--out", help="write the files to stdout for debugging"
    ),
    file_names: List[str] = typer.Option(
        None,
        "--file-names",
        help="alternative filenames to export to, can be a comma "
        "separated list of filenames. Repeated calls add "
        "more filenames.",
    ),
    chain_selectors: List[str] = typer.Argument(
        None,
        help="the names of the chains to export, can be a comma separated"
        " list of chains. Repeated calls add more chains. The default"
        " is to write all chains",
        metavar="<chains>",
    ),
):

    chain_selectors = parse_comma_separated_options(chain_selectors)

    file_names = parse_comma_separated_options(file_names)

    entry = read_entry_from_file_or_stdin_or_exit_error(input)

    molecular_system_frame = molecular_system_from_entry_or_exit(entry)

    chain_codes = frame_to_chains(molecular_system_frame)

    _exit_if_chain_selector_not_in_chain_codes(chain_codes, chain_selectors)

    chain_selectors = chain_selectors or chain_codes

    _exit_if_more_file_names_than_chains(chain_selectors, file_names)

    pipe(entry, output_to_stdout, file_name_template, file_names, chain_selectors)


def pipe(entry, output_to_stdout, file_name_template, file_names, chain_selectors):

    chains_to_filenames = _build_chains_to_filenames(
        chain_selectors, file_names, file_name_template
    )

    chain_sequences = _nmrview_sequences_from_entry(entry, chain_selectors)

    chains_to_output_file_names = _chains_to_output_filenames(
        chains_to_filenames, output_to_stdout
    )

    file_banners, final_banner = _make_file_name_banners(chains_to_filenames)

    for chain_code, sequence_text in chain_sequences.items():

        output_file_name = chains_to_output_file_names[chain_code]

        with smart_open(output_file_name) as file_pointer:

            if output_to_stdout:
                print(file_banners[chain_code], file=file_pointer)

            print(sequence_text, file=file_pointer)
    if output_to_stdout:
        print(final_banner)
    elif not stdout.isatty():
        print(entry)


def _make_file_name_banners(chains_to_filenames):
    same_width_names = _make_chain_code_to_names_same_width_names(chains_to_filenames)

    file_banners = {
        chain_code: f"------------- {same_width_names[chain_code]} -------------"
        for chain_code, file_name in chains_to_filenames.items()
    }
    banner_lengths = [len(banner) for banner in file_banners.values()]
    max_banner_width = max(banner_lengths)

    final_banner = "-" * max_banner_width

    return file_banners, final_banner


def _chains_to_output_filenames(chains_to_filenames, output_to_stdout):
    return {
        chain: STDOUT if output_to_stdout else file_name
        for chain, file_name in chains_to_filenames.items()
    }


def _exit_if_chain_selector_not_in_chain_codes(chain_codes, chain_selectors):
    for chain_selector in chain_selectors:
        if chain_selector not in chain_codes:
            msg = f"""\
                the chain code {chain_selector} is not in the molecular systems chain codes
                chain selectors:  {', '.join(chain_selectors)}
                chain codes: {', '.join(chain_codes)}
            """
        exit_error(msg)


def _exit_if_more_file_names_than_chains(chain_selectors, file_names):
    if len(file_names) > len(chain_selectors):
        msg = f"""\
            there are more file names than chains !

            chains = {','.join(chain_selectors)} [{len(chain_selectors)}]
            file names: {''.join(file_names)} [{len(file_names)}]
        """

        exit_error(msg)


def _nef_to_nmrview_sequences(
    residues: List[SequenceResidue], chain_codes: List[str]
) -> Dict[str, List[str]]:

    chain_starts = get_chain_starts(residues)

    residues_by_chain = {
        chain_code: [
            residue for residue in residues if residue.chain_code == chain_code
        ]
        for chain_code in chain_codes
    }
    residue_sequences = {
        chain_code: [residue.residue_name for residue in residues_by_chain[chain_code]]
        for chain_code in chain_codes
    }
    result = {}
    for chain_code, residue_sequence in residue_sequences.items():
        chain_start = chain_starts[chain_code]

        sequence_lines = []
        for i, residue in enumerate(residue_sequence):

            residue = residue.lower()

            if i == 0:
                if chain_start != 1:
                    line = f"{residue} {chain_start}"
            else:
                line = residue

            sequence_lines.append(line)

        result[chain_code] = "\n".join(sequence_lines)

    return result


def _nmrview_sequences_from_entry(entry, chain_codes):

    molecular_system_frame = molecular_system_from_entry(entry)

    residues = sequence_from_frame(molecular_system_frame)

    return _nef_to_nmrview_sequences(residues, chain_codes)


def _make_chain_code_to_names_same_width_names(names: Dict[str, str]) -> Dict[str, str]:
    max_length = -1
    for name in names.values():
        name_len = len(name)
        max_length = max(name_len, max_length)

    return {chain_code: name.center(max_length) for chain_code, name in names.items()}


def _open_for_writing_or_exit(file_name):
    try:
        result = open(file_name, "w")
    except Exception as e:
        msg = f"failed to open {file_name} for writing because {e}"

        exit_error(msg, e)

    return result


def _build_chains_to_filenames(
    chain_selectors: str, file_names: str, file_name_template: str
) -> Dict[str, str]:

    return {
        chain_selector: file_name or file_name_template % chain_selector
        for chain_selector, file_name in zip_longest(chain_selectors, file_names)
    }
