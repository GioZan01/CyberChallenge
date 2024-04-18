with import <nixpkgs> {};
let
    pkgs = import (builtins.fetchTarball {
        url = "https://github.com/NixOS/nixpkgs/archive/9e27e2e6bbc1e72f73fff75f669b7be53d0bba62.tar.gz";
    }) {};

    boost169 = pkgs.python38Packages.boost;
in
let crow = stdenv.mkDerivation rec {
      name = "crow";
      src = fetchFromGitHub {
        owner = "ipkn";
        repo = "crow";
        rev = "49edf898a5b9a39a0d69072cc2434c4f23692908";
        sha256 = "1qkyjc9yc2ak960wkcwp5kvxm4m4xqw0dvknsc9n292xcjlnga5v";
      };
      buildInputs = [ python39 ];
      buildPhase = ''
        cd amalgamate
        python merge_all.py '../include'
      '';
      installPhase = ''
        mkdir -p $out/include/crow
        cp crow_all.h $out/include/crow/crow.h
      '';
      meta = {
        description = "crow header file";
      };
    };
in
stdenv.mkDerivation rec {
  name = "biomarkt";
  src = ./.;
  buildInputs = [ boost169 gnumake gcc jemalloc openssl crow libpqxx ];
  dontUseCmakeConfigure = true;
  installPhase = ''
    mkdir -p $out/bin $out/share/${name}/
    cp -r static/ $out/share/${name}/static/
    cp -r templates/ $out/share/${name}/templates/
    cp ${name} $out/bin
  '';
  meta = {
    description = "E-Commerce Website";
  };
}
