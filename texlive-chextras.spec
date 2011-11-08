# revision 20044
# category Package
# catalog-ctan /macros/latex/contrib/chextras
# catalog-date 2010-10-10 14:40:20 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-chextras
Version:	1.0
Release:	1
Summary:	A companion package for the Swiss typesetter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chextras
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chextras.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chextras.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chextras.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package simplifies the preparation of Swiss documents and
letters by setting up linguistic and common packages. While
linked to the chletter document class, it is not tied to it and
may be used as a general purpose package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
