import logging
import os
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List, Union

logger = logging.getLogger("build-with-docker")


def main(cli_args: List[str]):
    logging.basicConfig(level=logging.DEBUG)

    parser = ArgumentParser()
    parser.add_argument("--image", type=str, required=True)
    parser.add_argument("--no-docker-interactive", action="store_true", default=False)
    parser.add_argument("--no-docker-tty", action="store_true", default=False)
    parser.add_argument("--project", type=str)
    parser.add_argument("--packaged-src", type=str, help="source code packaged in a JSON file")
    parser.add_argument("--contract", type=str)
    parser.add_argument("--output", type=str, default=Path(os.getcwd()) / "output")
    # Providing this parameter
    #   (a) *might* (should, but it doesn't) speed up (subsequent) builds, but
    #   (b) *might* (with a *very low* probability) break build determinism.
    # As of November 2022, both (a) and (b) are still open points.
    parser.add_argument("--cargo-target-dir", type=str)
    parser.add_argument("--no-wasm-opt", action="store_true", default=False, help="do not optimize wasm files after the build (default: %(default)s)")

    parsed_args = parser.parse_args(cli_args)
    image = parsed_args.image
    docker_interactive = not parsed_args.no_docker_interactive
    docker_tty = not parsed_args.no_docker_tty
    project_path = Path(parsed_args.project).expanduser().resolve() if parsed_args.project else None
    packaged_src_path = Path(parsed_args.packaged_src).expanduser().resolve() if parsed_args.packaged_src else None
    contract_path = parsed_args.contract
    output_path = Path(parsed_args.output).expanduser().resolve()
    cargo_target_dir = Path(parsed_args.cargo_target_dir).expanduser().resolve() if parsed_args.cargo_target_dir else None
    no_wasm_opt = parsed_args.no_wasm_opt

    output_path.mkdir(parents=True, exist_ok=True)

    return_code = run_docker(
        image,
        docker_interactive,
        docker_tty,
        project_path,
        packaged_src_path,
        contract_path,
        output_path,
        cargo_target_dir,
        no_wasm_opt
    )

    return return_code


def run_docker(
    image: str,
    docker_interactive: bool,
    docker_tty: bool,
    project_path: Union[Path, None],
    packaged_src_path: Union[Path, None],
    contract_path: str,
    output_path: Path,
    cargo_target_dir: Union[Path, None],
    no_wasm_opt: bool
):
    docker_mount_args: List[str] = ["--volume", f"{output_path}:/output"]

    if project_path:
        docker_mount_args.extend(["--volume", f"{project_path}:/project"])

    if packaged_src_path:
        docker_mount_args.extend(["--volume", f"{packaged_src_path}:/packaged-src.json"])

    if cargo_target_dir:
        docker_mount_args += ["--volume", f"{cargo_target_dir}:/rust/cargo-target-dir"]

    docker_args = ["docker", "run"]

    if docker_interactive:
        docker_args += ["--interactive"]
    if docker_tty:
        docker_args += ["--tty"]

    docker_args += docker_mount_args
    docker_args += ["--user", f"{str(os.getuid())}:{str(os.getgid())}"]
    docker_args += ["--rm", image]

    entrypoint_args: List[str] = []

    if project_path:
        entrypoint_args.extend(["--project", "project"])

    if packaged_src_path:
        entrypoint_args.extend(["--packaged-src", "packaged-src.json"])

    if no_wasm_opt:
        entrypoint_args.append("--no-wasm-opt")

    if contract_path:
        entrypoint_args.extend(["--contract", contract_path])

    args = docker_args + entrypoint_args
    logger.info(f"Running docker: {args}")

    result = subprocess.run(args)
    return result.returncode


if __name__ == "__main__":
    return_code = main(sys.argv[1:])
    exit(return_code)
