%global tl_name chextras
%global tl_revision 27118

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	A companion package for the Swiss typesetter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chextras
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chextras.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chextras.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chextras.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package simplifies the preparation of Swiss documents and letters by
setting up linguistic and common packages. While it is a useful addition
to the chletter document class, it is not tied to it and may be used as
a general purpose package.

