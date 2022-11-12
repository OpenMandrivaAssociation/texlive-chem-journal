Name:		texlive-chem-journal
Version:	15878
Release:	1
Summary:	Various BibTeX formats for journals in Chemistry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/chem-journal
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chem-journal.r15878.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Various BibTeX formats for journals in Chemistry, including
Reviews in Computational Chemistry, Journal of Physical
Chemistry, Journal of Computational Chemistry, and Physical
Chemistry Chemical Physics.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/chem-journal/jcc.bst
%{_texmfdistdir}/bibtex/bst/chem-journal/jpc.bst
%{_texmfdistdir}/bibtex/bst/chem-journal/pccp.bst
%{_texmfdistdir}/bibtex/bst/chem-journal/revcompchem.bst

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}
