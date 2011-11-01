Name:		texlive-chem-journal
Version:	20070101
Release:	1
Summary:	Various BibTeX formats for journals in Chemistry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/chem-journal
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chem-journal.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Various BibTeX formats for journals in Chemistry, including
Reviews in Computational Chemistry, Journal of Physical
Chemistry, Journal of Computational Chemistry, and Physical
Chemistry Chemical Physics.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/chem-journal/jcc.bst
%{_texmfdistdir}/bibtex/bst/chem-journal/jpc.bst
%{_texmfdistdir}/bibtex/bst/chem-journal/pccp.bst
%{_texmfdistdir}/bibtex/bst/chem-journal/revcompchem.bst

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}
