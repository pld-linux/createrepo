Summary:	Creates a common metadata repository
Summary(pl.UTF-8):	Tworzenie wspólnego repozytorium metadanych
Name:		createrepo
Version:	0.10.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://createrepo.baseurl.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	1f499e055d64f03127aea3ae84c9ef1a
Patch1:		rpm5-caps.patch
URL:		http://createrepo.baseurl.org/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	sed >= 4.0
Requires:	python
Requires:	python-deltarpm
Requires:	python-libxml2
Requires:	python-pylzma
Requires:	python-rpm
Requires:	yum >= 3.2.23
Requires:	yum-metadata-parser >= 1.1.1-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of utilities for generating a common metadata repository from a
directory of RPM packages and maintaining it.

%description -l pl.UTF-8
Zestaw narzędzi do generowania oraz utrzymywania wspólnego
repozytorium metadanych z katalogu pakietów RPM.

%package -n bash-completion-%{name}
Summary:	bash-completion for createrepo commands
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla poleceń createrepo
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-%{name}
bash-completion for createrepo commands.

%description -n bash-completion-%{name} -l pl.UTF-8
bashowe uzupełnianie nazw dla poleceń createrepo.

%prep
%setup -q
%patch1 -p1

%{__sed} -i -e '1s,#!.*python,#!%{__python},' modifyrepo.py

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	compdir=%{bash_compdir} \
	sysconfdir=%{_sysconfdir} \
	PKGDIR=%{py_sitescriptdir}/%{name} \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/createrepo
%attr(755,root,root) %{_bindir}/mergerepo
%attr(755,root,root) %{_bindir}/modifyrepo
%{_mandir}/man1/mergerepo.1*
%{_mandir}/man1/modifyrepo.1*
%{_mandir}/man8/createrepo.8*
%dir %{_datadir}/%{name}
# note that these DO NEED executable bit set!
%attr(755,root,root) %{_datadir}/%{name}/genpkgmetadata.py
%attr(755,root,root) %{_datadir}/%{name}/mergerepo.py
%attr(755,root,root) %{_datadir}/%{name}/modifyrepo.py
%attr(755,root,root) %{_datadir}/%{name}/worker.py
%{_datadir}/%{name}/*.py[co]
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{_datadir}/bash-completion/completions/createrepo
%{_datadir}/bash-completion/completions/genpkgmetadata.py
%{_datadir}/bash-completion/completions/mergerepo
%{_datadir}/bash-completion/completions/mergerepo.py
%{_datadir}/bash-completion/completions/modifyrepo
%{_datadir}/bash-completion/completions/modifyrepo.py
