Name:		texlive-chextras
Version:	27118
Release:	2
Summary:	A companion package for the Swiss typesetter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chextras
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chextras.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chextras.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chextras.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package simplifies the preparation of Swiss documents and
letters by setting up linguistic and common packages. While it
is a useful addition to the chletter document class, it is not
tied to it and may be used as a general purpose package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chextras/chextras.sty
%{_texmfdistdir}/tex/latex/chextras/eu1lmros.fd
%{_texmfdistdir}/tex/latex/chextras/eu1lmssos.fd
%{_texmfdistdir}/tex/latex/chextras/eu1lmttos.fd
%{_texmfdistdir}/tex/latex/chextras/eu1lmvttos.fd
%{_texmfdistdir}/tex/latex/chextras/t1lmros.fd
%{_texmfdistdir}/tex/latex/chextras/t1lmssos.fd
%{_texmfdistdir}/tex/latex/chextras/t1lmttos.fd
%{_texmfdistdir}/tex/latex/chextras/t1lmvttos.fd
%doc %{_texmfdistdir}/doc/latex/chextras/README
%doc %{_texmfdistdir}/doc/latex/chextras/chextras.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chextras/chextras.dtx
%doc %{_texmfdistdir}/source/latex/chextras/chextras.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
