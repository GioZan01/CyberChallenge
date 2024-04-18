FROM nixos/nix
RUN nix-channel --update
RUN nix-env -iA nixpkgs.python39 nixpkgs.gnumake nixpkgs.gcc nixpkgs.pkg-config nixpkgs.jemalloc nixpkgs.cmake nixpkgs.openssl nixpkgs.libpqxx
COPY ./ /app
RUN nix-env -f /app/default.nix -i
EXPOSE 18080
CMD biomarkt
