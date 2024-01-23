Name:		texlive-libertinust1math
Version:	69440
Release:	1
Summary:	A Type 1 font and LaTeX support for Libertinus Math
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libertinust1math
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinust1math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinust1math.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a Type1 version of Libertinus Math, with a
number of additions and changes, plus LaTeX support files that
allow it to serve as a math accompaniment to Libertine under
LaTeX. In addition, with option sansmath, it can function as a
standalone math font with sans serif Roman and Greek letters.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/libertinust1math
%{_texmfdistdir}/fonts/vf/public/libertinust1math
%{_texmfdistdir}/fonts/type1/public/libertinust1math
%{_texmfdistdir}/fonts/tfm/public/libertinust1math
%{_texmfdistdir}/fonts/map/dvips/libertinust1math
%{_texmfdistdir}/fonts/enc/dvips/libertinust1math
%{_texmfdistdir}/fonts/afm/public/libertinust1math
%doc %{_texmfdistdir}/doc/fonts/libertinust1math

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
