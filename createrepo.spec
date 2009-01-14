Summary:	Creates a common metadata repository
Summary(pl.UTF-8):	Tworzenie wspólnego repozytorium metadanych
Name:		createrepo
Version:	0.9.6
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/createrepo/download/%{name}-%{version}.tar.gz
# Source0-md5:	d8b11b3b38205fe351497c7e10ae5500
Patch0:		%{name}-typo.patch
URL:		http://linux.duke.edu/metadata/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq  python
Requires:	python-libxml2
Requires:	python-rpm
Requires:	yum >= 3.2.11-1
Requires:	yum-metadata-parser >= 1.1.1-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility will generate a common metadata repository from a
directory of RPM packages.

%description -l pl.UTF-8
To narzędzie tworzy wspólne repozytorium metadanych z katalogu
pakietów RPM.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,#!.*python,#!%{__python},' modifyrepo.py

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
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
%dir %{_datadir}/%{name}
# note that these DO NEED executable bit set!
%attr(755,root,root) %{_datadir}/%{name}/genpkgmetadata.py*
%attr(755,root,root) %{_datadir}/%{name}/mergerepo.py*
%attr(755,root,root) %{_datadir}/%{name}/modifyrepo.py*
%dir %{py_sitescriptdir}/createrepo
%{py_sitescriptdir}/createrepo/*.py[co]
%{_mandir}/man1/mergerepo.1*
%{_mandir}/man1/modifyrepo.1*
%{_mandir}/man8/createrepo.8*
