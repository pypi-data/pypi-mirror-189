{ pkgs }: {
    deps = [
        pkgs.twine
        pkgs.python39Full
        pkgs.cargo
        pkgs.rustc
        pkgs.cowsay
    ];
}