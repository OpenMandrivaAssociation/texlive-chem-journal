%global tl_name chem-journal
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Various BibTeX formats for journals in Chemistry
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/chem-journal
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chem-journal.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Various BibTeX formats for journals in Chemistry, including Reviews in
Computational Chemistry, Journal of Physical Chemistry, Journal of
Computational Chemistry, and Physical Chemistry Chemical Physics.

