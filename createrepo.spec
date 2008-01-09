Summary:	Creates a common metadata repository
Summary(pl.UTF-8):	Tworzenie wspólnego repozytorium metadanych
Name:		createrepo
Version:	0.9.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/createrepo/download/%{name}-%{version}.tar.gz
# Source0-md5:	2a903c9f33c8a56dbfb89c2875d9978d
#Patch0:	%{name}-missingok.patch
URL:		http://linux.duke.edu/metadata/
BuildRequires:	python-devel > 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python
Requires:	python-libxml2
Requires:	python-rpm
Requires:	yum >= 3.2.7
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
#%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
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
%attr(755,root,root) %{_bindir}/modifyrepo
%dir %{_datadir}/%{name}
# note that these DO NEED executable bit set!
%attr(755,root,root) %{_datadir}/%{name}/genpkgmetadata.py*
%attr(755,root,root) %{_datadir}/%{name}/modifyrepo.py*
%dir %{py_sitedir}/createrepo
%{py_sitedir}/createrepo/*.py[co]
%{_mandir}/man1/modifyrepo.1*
%{_mandir}/man8/createrepo.8*
