%global tl_name libertinust1math
%global tl_revision 77682
%global tl_version 2.0.6

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A Type 1 font and LaTeX support for Libertinus Math
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/libertinust1math
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinust1math.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinust1math.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides a Type1 version of Libertinus Math, with a number
of additions and changes, plus LaTeX support files that allow it to
serve as a math accompaniment to Libertine under LaTeX. In addition,
with option sansmath, it can function as a standalone math font with
sans serif Roman and Greek letters.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from libertinust1math:
Map libertinust1math.map
TL_DROPIN_EOF
