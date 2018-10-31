# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/chem-journal
# catalog-date 2007-01-01 10:31:54 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-chem-journal
Version:	20180303
Release:	2
Summary:	Various BibTeX formats for journals in Chemistry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/chem-journal
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chem-journal.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070101-2
+ Revision: 750145
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070101-1
+ Revision: 718043
- texlive-chem-journal
- texlive-chem-journal
- texlive-chem-journal
- texlive-chem-journal
- texlive-chem-journal

